from __future__ import division, print_function

import sys
if sys.version_info[0] < 3:  # Use range iterator for Python 2
    range = xrange
from functools import reduce

import operator
from itertools import combinations

import networkx as nx
import numpy as np

from datarray import DataArray

from numpy.testing import assert_almost_equal


def test_pearl_network():
    """ From Russell and Norvig, "Artificial Intelligence, A Modern Approach,"
    Section 15.1 originally from Pearl.

    "Consider the following situation. You have a new burglar alarm installed
    at home. It is fairly reliable at detecting a burglary, but also responds
    on occasion to minor earthquakes. You also have two neighbors, John and
    Mary, who have promised to call you at work when they hear the alarm. John
    always calls when he hears the alarm, but sometimes confuses the telephone
    ringing with the alarm and calls then, too. Mary on the other hand, likes
    rather loud music and sometimes misses the alarm altogether. Given the
    evidence of who has or has not called, we would like to estimate the
    probability of a burglary.

                    Burglary         Earthquake

                           \         /
                           _\|     |/_

                              Alarm

                            /     \  
                          |/_     _\|

                    Johncalls        Marycalls

    This test function uses four different algorithms to calculate 

        P(burglary | johncalls = 1, marycalls = 1) 

    In increasing order of sophistication: 
        1. Simple (calculate joint distribution and marginalize) 
        2. Elimination (strategically marginalize over one variable at a time) 
        3. Sum-product algorithm on factor graph 
        4. Junction tree algorithm
    """
    burglary = DataArray([.999,.001], axes=["burglary"])
    earthquake = DataArray([.998,.002], axes=["earthquake"])
    alarm = DataArray([ [[.05,.95], [.06,.94]],                      
                        [[.71,.29], [.999,.001]] ],
        ["burglary","earthquake","alarm"])

    johncalls = DataArray([[.10,.90],[.95,.05]],["alarm","johncalls"])
    marycalls = DataArray([[.30,.70],[.01,.99]],["alarm","marycalls"])

    cpts = [burglary, earthquake, alarm, johncalls, marycalls]

    evidence = {"johncalls":0, "marycalls":0}

    margs1,lik1 = calc_marginals_simple(cpts,evidence)
    p_burglary,lik2 = digraph_eliminate(cpts,evidence,["burglary"])
    margs3,lik3 = calc_marginals_sumproduct(cpts,evidence)

    # TODO: This version is disabled until I can dig up the reference to figure
    # out how it works. -jt
    # margs4,lik4 = calc_marginals_jtree(cpts,evidence)

    # Check that all four calculations give the same p(burglary) and
    # likelihood, up to numerical error
    for (marg,lik) in \
            [(p_burglary, lik2), (margs3["burglary"], lik3)]: # , (margs4["burglary"],lik4)]:
        assert_almost_equal(marg,margs1["burglary"])
        assert_almost_equal(lik,lik1)
    
    print("p(burglary) = %s" % margs1["burglary"].__array__())
    print("likelihood of observations = %.3f" % lik1)
    
####### DataArray utilities ################

def match_shape(x,yshape,axes):
    """
    Creates a view v on x with the same number of dimensions as y.
    The axes of x are copied into the axes of v specified by the axes argument.
    
    Example
    ---------
    >>> x = np.arange(3)
    >>> match_shape(x,(2,3,2),(1,))
    array([[[0, 0],
            [1, 1],
            [2, 2]],
    <BLANKLINE>
           [[0, 0],
            [1, 1],
            [2, 2]]])

    """
    if isinstance(axes,int): axes = [axes]
    assert len(x.shape) == len(axes)
    assert all(xsize == yshape[yax] for xsize,yax in zip(x.shape,axes))
    strides = np.zeros(len(yshape), dtype=np.intp)
    for yax,xstride in zip(axes,x.strides):
        strides[yax] = xstride
    return np.ndarray.__new__(np.ndarray, strides=strides, shape=yshape, buffer=x, dtype=x.dtype)
   
def multiply_potentials(*DAs):
    """
    Multiply DataArrays in the way that we multiply functions, 
    e.g. h(i,j,k,l) = f(i,j,k) g(k,l)
    
    Parameters
    -------------
    DA1,DA2,... : DataArrays with variable names as axis labels
    
    Returns
    ---------
    product
    
    example
    ---------
    >>> f_of_a = DataArray([1, 2],"a")
    >>> g_of_b = DataArray([1,-1],"b")
    >>> multiply_potentials(f_of_a, g_of_b)
    DataArray([[ 1, -1],
           [ 2, -2]])
    ('a', 'b')
    >>> multiply_potentials(f_of_a, f_of_a)
    DataArray([1, 4])
    ('a',)

    
    """
    if len(DAs) == 0: return 1
    
    full_names, full_shape = [],[]
    for axis,size in zip(_sum(list(DA.axes) for DA in DAs), _sum(DA.shape for DA in DAs)):
        if axis.name not in full_names:
            full_names.append(axis.name)
            full_shape.append(size)

    return DataArray(
            _prod(match_shape(DA.copy(), full_shape, 
                [full_names.index(axis.name) for axis in DA.axes]) for DA in DAs), 
        axes=full_names)

def sum_over_axes(DA, axis_names):
    Out = DA
    for axname in axis_names:
        Out = Out.sum(axis=axname)
    return Out

def set_slices(DA,**axes2inds):
    """
    return a copy of DataArray DA, where several slices are taken along named axes,
    specified by keys ax1=ind1, ax2=ind2, etc.
    """
    Out = DA
    for (ax,ind) in axes2inds.items():
        Out = Out.axis[ax][ind:(ind+1)]
    return Out
    
def sum_over_other_axes(DA, kept_axis_name):
    "sum all axes of DataArray DA except for ax"
    return sum_over_axes(DA, 
            [axname for axname in DA.names if axname != kept_axis_name])

def _sum(seq): return reduce(operator.add, seq)
def _prod(seq): return reduce(operator.mul, seq)

####### Simple marginalization #############
    
def calc_marginals_simple(cpts,evidence):
    """
    Calculate the marginal probabilities the simple simple way. Calculate joint
    distribution of all variables and then marginalize. This algorithm becomes
    inefficient when there are a lot of variables, and the joint distribution
    becomes high-dimensional.
    
    Parameters
    -----------
    cpts : a list of DataArray. Gives conditional probability of variable with axis=-1
    evidence : a dictionary of variable -> value
        
    Returns
    --------
    marginals : dictionary of variable -> prob_table
    likelihood : likelihood of observations in the model
    """
    joint_dist = multiply_potentials(*cpts)
    joint_dist = joint_dist.axes.johncalls[evidence['johncalls']].axes.marycalls[evidence['marycalls']]
    return (dict((ax.name, normalize(sum_over_other_axes(joint_dist, ax.name))) 
                for ax in joint_dist.axes),
            joint_dist.sum())


############# Elimination #############

def digraph_eliminate(cpts,evidence,query_list):
    """
    Use elimination algorithm to find joint distribution over variables in
    query_list, given evidence.
    
    Parameters
    ------------
    cpts : a list of DataArray with variable names for axis names
    evidence : a dictionary of observed variables (strings) -> values
    query_list : a list of variables (strings)
        
    Returns
    --------
    marginals : dictionary of variable -> prob_table
    likelihood : likelihood of observations in the model
    """
    
    # find the directed graphical model
    DG = cpts2digraph(cpts)
    # use postorder (leaves to root) from depth-first search as elimination order
    rvs = nx.dfs_postorder_nodes(DG)

    # modify elimination list so query nodes are at the end
    rvs_elim = [rv for rv in rvs if rv not in query_list] + query_list
    for rv in rvs_elim:
        # find potentials that reference that node
        pots_here = [cpt for cpt in cpts if rv in cpt.names]
        # remove them from cpts
        cpts = [cpt for cpt in cpts if rv not in cpt.names]
        # Find joint probability distribution of this variable and the ones coupled to it
        product_pot = multiply_potentials(*pots_here)
        # if node is in query set, we don't sum over it
        if rv not in query_list:
            # if node is in evidence set, take slice
            if rv in evidence: product_pot = product_pot.axes(rv)[evidence[rv]]
            # otherwise, sum over it
            else: product_pot = product_pot.sum(axis=rv)

        # add resulting product potential to cpts
        cpts.append(product_pot)

    assert len(cpts) == 1
    unnormed_prob = cpts[0]
    likelihood = unnormed_prob.sum()
    return unnormed_prob/likelihood, likelihood

def cpts2digraph(cpts):
    """
    Each cpt has axes a_1,a_2,...a_k and represents p(a_k | a_1,...a_{k-1}).
    Use cpts to construct directed graph corresponding to these conditional
    probability dists.
    """
    G = nx.DiGraph()
    for cpt in cpts:
        names = [ax.name for ax in cpt.axes]
        target = names[-1]
        G.add_edges_from((source, target) for source in names[:-1])
    return G

############# Sum-product #############

def calc_marginals_sumproduct(cpts,evidence):
    """
    Construct the factor graph. Then use the sum-product algorithm to calculate
    marginals for all variables.
    
    Parameters
    ------------
    cpts : a list of DataArray with variable names for axis labels
    evidence : a dictionary of observed variables (strings) -> values
    query_list : a list of variables (strings)
        
    Returns
    --------
    marginals : dictionary of variable -> prob_table
    likelihood : likelihood of observations in the model
    """
    
    # In this implementation, we use evidence by using an evidence potential,
    # which equals 1 at the observed value and zero everywhere else.
    # Alternatively, we could take slices of cpts. This is the strategy used in
    # the junction tree algorithm below.
    
    G,names2tables = make_factor_graph(cpts,evidence)
    messages = {}
    # (source,target) for edges in directed spanning tree resulting from depth
    # first search
    message_pairs = dfs_edges(G)
        
    # message passing inward from leaves (actually we don't need to send
    # messages up from some leaves because cpt is normalized)
    for (parent,child) in message_pairs:
        m = make_message(child,parent,G,messages,names2tables)
        messages[(child,parent)] = m
    
    # message passing outward from root
    for (parent,child) in reversed(message_pairs):
        m = make_message(parent,child,G,messages,names2tables)
        messages[(parent,child)] = m

    # calculate marginals
    marginals = {}
    for node in G.nodes():
        potential = multiply_potentials(*[messages[(src,node)] for src in G.neighbors(node)])
        marginals[node] = normalize(potential)
        
    return marginals, potential.sum()
        
def make_message(src,targ,G,messages,names2tables):
    """
    Collect messages coming to src from all nodes other than targ and multiply them.
    If targ is a factor node, this product is the message.
    If targ is a variable node, marginalize over all other variables
    """
    # collect messages incoming to src
    incoming_msgs = [messages[(neighb,src)] for neighb in G.neighbors(src) if neighb != targ]
    if isvar2factor(src,targ): return multiply_potentials(names2tables[src],*incoming_msgs)
    return sum_over_other_axes(multiply_potentials(names2tables[src],*incoming_msgs),targ)
        
def isvar2factor(src,targ):
    "True if target is a factor node."
    return isinstance(targ,tuple)
    
def make_factor_graph(cpts,evidence):
    G = nx.Graph()
    
    names2factors = dict((tuple(cpt.names), cpt) for cpt in cpts)
    G.add_nodes_from(names2factors.keys())
    for (name,factor) in names2factors.items():
        for axnames in factor.names:
            G.add_edge(name, axnames)
            
    names2factors.update(
        dict((name,
              DataArray(np.ones(size) if name not in evidence 
                        else one_hot(size,evidence[name]),[name]))
             for cpt in cpts 
             for (name,size) in zip(cpt.names,cpt.shape)))
            
    return G, names2factors

def one_hot(size,val):
    "out[val] = 1, out[i] = 0 for i != val"
    out = np.zeros(size)
    out[val] = 1
    return out

def dfs_edges(G):
    """
    (source,target) for edges in directed spanning tree resulting from depth
    first search
    """
    DG = nx.dfs_tree(G, source=None)
    return [(src,targ) for targ in nx.dfs_postorder_nodes(DG) for src in DG.predecessors(targ)]


############# Junction tree #############

## Applying the junction tree algorithm to a directed graphical model requires several steps
## 1. Moralize the directed graph.
## 2. Add edges to obtain a triangulated graph. It is hard to find the best triangulation
##    (i.e., the one that adds as few edges as possible), so we use a greedy heuristic "min fill"
## 3. Form a clique tree for triangulated graph. Assign potentials to cliques.
## 4. Apply the Hugin algorithm to the clique tree


def calc_marginals_jtree(potentials, evidence):
    """
    Use the hugin algorithm to find marginals and data likelihood.
    """
    JT, names2factors = make_jtree_from_factors(potentials)
    pots = hugin(JT, names2factors, evidence)

    # Each random variable appears in many cliques and separators. Each of these potentials is a
    # joint probability distribution, and they should give the same marginals.
    rv2marg = {}
    for pot in pots.values():
        for rv in pot.labels:
            if rv not in rv2marg:
                rv2marg[rv] = normalize(sum_over_other_axes(pot,rv))
    
    return rv2marg, pot.sum()

def hugin(JT,names2factors,evidence):
    
    # intialize potentials, taking slices to incorporate evidence
    potentials = dict([(name,use_evidence(factor,evidence)) 
                        for (name,factor) in names2factors.items()])
        
    message_pairs = dfs_edges(JT)
    # iterate over edges of clique tree
    for (pred,succ) in message_pairs:
        sep = tuple(set(pred).intersection(succ))
        sepname = (pred,succ)
        # update separator
        potentials[sepname] = sum_over_axes(potentials[succ],set(succ).difference(sep))
        # update predecessor clique
        potentials[pred] = multiply_potentials(potentials[pred],potentials[sepname])

    for (pred,succ) in reversed(message_pairs):
        sep = tuple(set(pred).intersection(succ))
        sepname = (pred,succ)
        # update separator
        oldsep = potentials[sepname]
        potentials[sepname] = sum_over_axes(potentials[pred],set(pred).difference(sep))
        # update successor clique
        potentials[succ] = multiply_potentials(potentials[succ],1/oldsep,potentials[sepname])            
        
    return potentials
        
def use_evidence(potential,ev_dict):
    "Take slices of potential at all variables appearing in ev_dict"
    obs_dict = dict((label,ev_dict[label]) for label in potential.labels if label in ev_dict)
    return set_slices(potential,**obs_dict) if len(obs_dict) > 0 else potential

def triangulate_min_fill(G):
    """
    Return graph with a triangulation of undirected graph G, using min fill.
    Min fill forms an elimination ordering on graph. Each step, we eliminate the node that
    requires us to add the fewest new edges. A graph resulting from elimination is always triangulated (why?)
    """
    G_elim = nx.Graph(G.edges())
    added_edges = []
    for _ in range(G.number_of_nodes()):
        nodes,degrees = zip(*G_elim.degree().items())
        min_deg_node = nodes[np.argmin(degrees)]
        new_edges = [(n1,n2) for (n1,n2) in
                combinations(G_elim.neighbors(min_deg_node),2) if not
                G_elim.has_edge(n1,n2)]
        added_edges.extend(new_edges)        
        G_elim.remove_node(min_deg_node)
        G_elim.add_edges_from(new_edges)
    
    return nx.Graph(G.edges() + added_edges)

def make_jtree_from_tri_graph(G):
    """returns JT graph"""
    
    # clique graph
    CG = nx.Graph()
    # maximal weight spanning tree of clique graph is guaranteed to be a junction tree
    # (i.e., it satisfies running intersection property)
    # where weight is the size of the intersection between adjacent cliques.
    CG.add_weighted_edges_from((tuple(c1),tuple(c2),-c1c2) 
                      for (c1,c2) in combinations(nx.find_cliques(G),2)
                      for c1c2 in [len(set(c1).intersection(set(c2)))] if c1c2 > 0)
    JT = nx.Graph(nx.mst(CG)) # Minimal weight spanning tree for CliqueGraph
    for src,targ in JT.edges():
        JT[src][targ]["sep"] = tuple(set(src).intersection(set(targ)))
        
    return JT

def make_jtree_from_factors(factors):
    """
    Make junction tree and assign factors to cliques.
    1. Moralize
    2. Triangulate
    3. Take MST of clique tree to get junction tree
    4. Assign potentials to cliques and multiply them to get clique potentials
    
    parameters
    -----------
    factors : list of DataArray
    
    returns
    --------
    JT : junction tree (directed graph), with nodes labeled by tuples, e.g. ("A","B","C")
    clique2pot : dictionary of cliques (i.e., node labels) -> DataArray
    """
    VarGraph = moral_graph_from_factors(factors)
    TriangulatedGraph = triangulate_min_fill(VarGraph)
    JT = make_jtree_from_tri_graph(TriangulatedGraph)
    clique2potlist = dict((node,[]) for node in JT.nodes())
    for factor in factors:
        varset = set(factor.labels)
        for clique in JT:
            if varset.issubset(set(clique)):
                clique2potlist[clique].append(factor)
                continue
    clique2pot = dict((clique,multiply_potentials(*potlist)) for (clique,potlist) in clique2potlist.items())
    # todo: make sure all cliques have a potential
    return JT,clique2pot
    
def moral_graph_from_factors(factors):
    G = nx.Graph()
    for factor in factors:
        for label1,label2 in combinations(factor.names, 2):
            G.add_edge(label1,label2)    
                    
    return G

def normalize(arr):
    return arr/arr.sum()

if __name__ == "__main__":
    test_pearl_network()
    #import doctest
    #doctest.testmod()
