import sys
import argparse
import os
import re
from collections import namedtuple

# For packaging harnessmaker to tstl package
import pkg_resources

############## GLOBAL VARIABLES #############
# These varaibles will be modified when needed

config = None
poolSet = {}
initSet = []
baseIndent = ""
poolPrefix = None
genCode = None
#############################################

def parse_args():
    """
    To parse command line arguments. Makes use of built-in python library argprase
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('tstl', metavar='filename', type=str, default=None,
                        help='Path to the .tstl file.')
    parser.add_argument('-o', '--output', type=str, default="sut.py",
                        help='Name of the file containing the generated harness code (default = sut.py)')
    parser.add_argument('-c', '--classname', type=str, default='sut',
                        help='Name of the class representing the SUT (default=sut)')
    parser.add_argument('-n', '--nocover', action='store_true',
                        help='Disable generating coverage collection support.')
    parser.add_argument('-r', '--coverreload', action='store_true',
                        help='Generate coverage for module reload behavior.')
    parser.add_argument('-i', '--coverinit', action='store_true',
                        help='Generate coverage for SUT initialization behavior.')

    # Useful to print internal variables iteratively
    parser.add_argument('--debug', dest='debug', action='store_true', help='Toggle debug mode on')
    parser.add_argument('--no-debug', dest='debug', action='store_false')
    parser.set_defaults(debug=False)
    parsed_args = parser.parse_args(sys.argv[1:])
    return (parsed_args, parser)


def make_config(pargs, parser):
    """
    Process the raw arguments, returning a namedtuple object holding the
    entire configuration, if everything parses correctly.
    Example:
    Config(output='sut.py', classname='sut', nocover=False, tstl='yourfile.tstl',
           debug=False, coverreload=False, coverinit=False)
    """
    pdict = pargs.__dict__
    if pargs.tstl is None:
        parser.print_help()
        raise ValueError('The .tstl file is not specified.')
    elif not os.path.exists(pargs.tstl):
        parser.print_help()
        raise ValueError('Cannot locate the .tstl file at path={}'.format(pargs.output))
    
    if pargs.output is None:
        parser.print_help()
        raise ValueError('The output file is not specified.')
    
    # create a namedtuple object for fast attribute lookup
    key_list = pdict.keys()
    arg_list = [pdict[k] for k in key_list]
    Config = namedtuple('Config', key_list)
    nt_config = Config(*arg_list)
    return nt_config   
    

def parse_import_line(line):
    """
    Parses an import line in the raw python code.
    Input --> Output (Example)
    :
    :    "from math import sqrt" --> ['sqrt']
    :
    """
    raw = line.split('import ')
    assert len(raw) == 2, 'import statement error in line --> {}'.format(line)
    # import X
    # from X import Y
    # from X import Y,Z
    # from X import Y as Z
    # import X as Y, A as B
    raw = raw[1]
    # check for multiple imports
    subimports = [raw]
    if ', ' in raw:
        subimports = raw.split(', ')
    assert len(subimports) > 0
    # check for aliasing
    mod_names = []
    for si in subimports:
        name = None
        if 'as' in si:
            ts = si.split(' as ')
            assert len(ts) == 2, 'Parse error on "as" during import of {}'.format(name)
            name = ts[1].rstrip()  # remove the trailing newline or whitespace if any
        else:
            name = si.rstrip()
        mod_names.append(name)
    assert len(mod_names) > 0
    return mod_names


def expandPool(original):
    """
    Expand pool references
    """
    newVersion = []
    for c in original:
        for p in poolSet:
            if poolSet[p] == 1:
                pexpr = p + " [0]"
            else:
                pexpr = p + " [%[0.." + str(poolSet[p]-1) + "]%]"
            c = c.replace(p, pexpr)
        newVersion.append(c)
    return newVersion


def expandRange(original):
    """
    Expand all range expressions
    """
    current = original
    anyChanged = True
    while anyChanged:
        anyChanged = False
        newVersion = []
        for c in current:
            if "%[" in c:
                anyChanged = True
                lpos = c.find("%[")
                dotpos = c.find("..",lpos)
                endpos = c.find("]%",dotpos)
                low = int(c[lpos+2:dotpos])
                high = int(c[dotpos+2:endpos])
                rexp = c[lpos:endpos+2]
                for x in xrange(low,high+1):
                    newVersion.append(c.replace(rexp, str(x), 1))
            else:
                newVersion.append(c)
        current = newVersion

    for index, line in enumerate(newVersion):
        for refPool in re.findall("%([^%,]*)\s*,\s*(\d+)%", line):
            # it finds e.g., ('LIST', '2') if you have   ~%LIST,2%   in your .tstl file
            poolName, refIndex = refPool
            # if you had 
            # ~%LIST% = ~%LIST% + [%INT%, %INT%]
            # in your .tstl file, and in this particular line they were expanded to e.g., 
            # ~%LIST% [2] = ~%LIST% [3] + [%INT% [0], %INT% [0]]
            # then poolOccurences will be ['2', '3']
            poolOccurences = re.findall("%"+poolName+"%\s*\[(\d+)\]", line)
            
            # refIndex is 2, so the actual pool used for the secons %LIST% is poolOccurences[1]
            actualPoolUsed = poolOccurences[int(refIndex)-1]
            # replace   ~%LIST,2%    with    self.p_LIST[3]
            
            line = re.sub("~?%("+poolName+")\s*,\s*("+refIndex+")%", poolPrefix+"\\1["+actualPoolUsed+"]", line)
            newVersion[index] = line

    return newVersion


actCount = 0
def genAct():
    global actCount
    s = "act" + str(actCount)
    actCount += 1
    return s

guardCount = 0
def genGuard():
    global guardCount
    s = "guard" + str(guardCount)
    guardCount += 1
    return s


def genInitialization():
    """
    Generate initialization from configuration, poolSet
    """
    for p in poolSet:
        s = baseIndent
        s += poolPrefix + p.replace("%","") + " = {}"
        genCode.append(s + "\n")
        s = baseIndent
        s += poolPrefix + p.replace("%","") + "_used = {}"
        genCode.append(s + "\n")
        for x in xrange(0,poolSet[p]+1):
            s = baseIndent
            s += poolPrefix + p.replace("%","") + "[" + str(x) + "] = None"
            genCode.append(s + "\n")    
            s = baseIndent
            s += poolPrefix + p.replace("%","") + "_used[" + str(x) + "] = True"
            genCode.append(s + "\n")
    if (not config.nocover) and config.coverinit:
        genCode.append(baseIndent + "if self.__collectCov: self.__cov.start()\n")
    for i in initSet:
        s = baseIndent
        s += i
        genCode.append(s)
    if (not config.nocover) and config.coverinit:
        genCode.append(baseIndent + "if self.__collectCov: self.__cov.stop()\n")        
        genCode.append(baseIndent + "if self.__collectCov: self.__updateCov()\n")


def main():

    global config;
    global poolSet;
    global initSet;
    global baseIndent;
    global poolPrefix;
    global genCode;

    baseIndent = "    "
    
    parsed_args, parser = parse_args()
    config = make_config(parsed_args, parser)
    print('Generating harness core using config={}'.format(config))

    if config.debug:
        from pprint import pprint

    # sut.py (default)
    outf = open(config.output,'w')

    # Handle raw python, imports
    outf.write("import copy\n")
    outf.write("import traceback\n")
    outf.write("import re\n")
    outf.write("import sys\n")

    if not config.nocover:
        outf.write("import coverage\n")

    code = []
    import_modules = []             # We will call reload on these during restart
    inside_literal_block = False    # To check whether we are inside raw python code
    
    inside_function = False         # Are we inside a function def, so need to consider PRE?
    function_code = []
    anyPre = False

    with open(config.tstl, 'r') as fp:
        for l in fp:
            if l[-1] != "\n":
                l += "\n"

            if l[0] == "#":
                continue # COMMENT

            if re.match("<@", l):
                #XXX: Any line with <@ will be ignored
                inside_literal_block = True
                continue

            if re.match("@>", l):
                inside_literal_block = False
                continue

            if inside_literal_block or l[0] == "@":
                if l[0] == "@":
                    l = l[1:]
                if re.match("import ", l):
                    outf.write(l[:])
                    # import, so set up reloading
                    module_names = parse_import_line(l)
                    import_modules += module_names

                if re.match("def guarded", l):
                    if function_code != []:
                        if anyPRE:
                            outf.write(baseIndent + "__pre = {}\n")
                        for fl in function_code:
                            outf.write(fl)                    
                    # guarded function, append the speculation argument and continue
                    outf.write(l.replace("):",", SPECULATIVE_CALL = False):"))
                    inside_function = True
                    anyPRE = False
                    function_code = []
                elif l.find("def ") == 0:
                    if function_code != []:
                        if anyPRE:
                            outf.write(baseIndent + "__pre = {}\n")
                        for fl in function_code:
                            outf.write(fl)
                    outf.write(l)
                    inside_function = True
                    anyPRE = False
                    function_code = []
                elif inside_function:
                    if l.find("%COMMIT%") != -1:
                    
                        # commit point in a guarded function definition
                        outf.write(l.replace("%COMMIT%","if SPECULATIVE_CALL: return True"))
                    m = re.match(r".*PRE%\((\S+)\)%.*",l)
                    while m:
                        anyPRE = True
                        pre_expr = m.groups()[0]
                        spre_expr = "'''" + pre_expr + "'''"
                        l = l.replace("PRE%(" + pre_expr + ")%", "__pre[" + spre_expr + "]", 1)
                        function_code = [(baseIndent + "__pre[" + spre_expr + "] = " + pre_expr + "\n")] + function_code
                        m = re.match(r".*PRE%\((\S+)\)%.*",l)
                    function_code.append(l)                    
                else:
                    outf.write(l)
            elif l[0] == "*":       # include action multiple times
                spos = l.find(" ")
                times = int(l[1:spos])
                for n in xrange(0,times):
                    code.append(l[spos:])
            else:
                code.append(l)
    if function_code != []:
        if anyPRE:
            outf.write(baseIndent + "__pre = {}\n")
        for fl in function_code:
            outf.write(fl)       
                
    assert len(code) > 0, 'No non-comment lines found in .tstl file'

    # Build up the pool, initialization values

    poolPrefix = "self.p_"

    sourceSet = []

    initSet = []
    propSet = []
    refSet = []
    compareSet = []
    featureSet = []
    logSet = []
    referenceMap = {}

    # Parse the code to process the "tag lines"
    newCode = []
    for c in code:
        cs = c.split()
        if cs == []:
            continue
        elif cs[0] == "init:":
            initSet.append(c.replace("init: ",""))
        elif cs[0] == "log:":
            logSet.append(c.replace("log: ",""))
        elif cs[0] == "property:":
            propSet.append(c.replace("property: ",""))
        elif cs[0] == "pool:":
            poolSet[cs[1]] = int(cs[2])
            if (len(cs)>3) and (cs[3] == "REF"):
                refSet.append(cs[1])
                poolSet[cs[1]+"_REF"] = int(cs[2])
        elif cs[0] == "reference:":
            baseRefSplit = c.split("reference: ")[1]
            rs = baseRefSplit.split(" ==> ")
            refLeft = rs[0]
            refRight = rs[1][:-1]
            leftMeth = re.match(r"METHOD\((\S+)\)", refLeft)
            if leftMeth:
                method = leftMeth.groups()[0]
                refLeft = r"(\S+)\."+ method + "\(\)"
            leftCall = re.match(r"CALL\((\S+)\)", refLeft)
            if leftCall:
                function = leftCall.groups()[0]
                refLeft = function + r"\((\S+)\)"
            rightCall = re.match(r"CALL\((\S+)\)", refRight)
            if rightCall:
                function = rightCall.groups()[0]
                refRight = function+r"(\1)"
            rightMeth = re.match(r"METHOD\((\S+)\)", refRight)
            if rightMeth:
                method = rightMeth.groups()[0]
                refRight = r"\1." + method + "()"
            referenceMap[refLeft] = refRight
        elif cs[0] == "feature:":
            featureSet.append(cs[1])
        elif cs[0] == "compare:":
            compareSet.append(cs[1])        
        elif cs[0] == "source:":
            sourceSet.append(cs[1])
        else:
            if cs[0] == "expect:":
                baseExpectSplit = c.split("expect: ")[1]
                c = baseExpectSplit
            newCode.append(c)
    code = newCode

    if config.debug:
        print("-------- :code: --------")
        pprint(code)
        print("------------------------")

    # ------------------------------------------ #
    code = expandPool(code)
    propSet = expandPool(propSet)
    initSet = expandPool(initSet)
    logSet = expandPool(logSet)

    if config.debug:
        print(":code: after expandPool(code)")
        pprint(code)
        print("------------------------")

    code = expandRange(code)
    propSet = expandRange(propSet)
    initSet = expandRange(initSet)
    logSet = expandRange(logSet)

    if config.debug:
        print(":code: after expandRange(code)")
        pprint(code)
        print("------------------------")

    # Finally go ahead and directly reference pools in preds and initalizers
    newProps = []
    for c in propSet:
        newProps.append((c,[]))
    propSet = newProps

    for p in poolSet:
        newProps = []
        for (c,u) in propSet:
            uses = u
            found = c.find(p)
            while (found != -1):
                use = c[found:c.find("]", found)+1]
                use = use.replace(p + " ", poolPrefix + p.replace("%",""))
                uses.append(use)
                found = c.find(p,found+1)
            newProps.append((c.replace(p + " ", poolPrefix + p.replace("%","")),uses))
        propSet = newProps

    for p in poolSet:
        newInits = []
        for c in initSet:
            newInits.append(c.replace(p + " ", poolPrefix + p.replace("%","")))
        initSet = newInits

    for p in poolSet:
        newLogs = []
        for c in logSet:
            newLogs.append(c.replace(p + " ", poolPrefix + p.replace("%","")))
        logSet = newLogs

    # ------------------------------------------ #
    newLogs = []
    for l in logSet:
        refl = l
        for p in poolSet:
            if p in refSet:
                pRaw = poolPrefix + p.replace("%","")
                refl = l.replace(pRaw,pRaw+"_REF")
        if refl != l:        
            for base in referenceMap:
                if re.match(r"^[a-zA-Z_0-9]+$", refl):  # base is not a regex; treat it like a function name
                    refl = re.sub(r'\b'+base+r'\b',referenceMap[base],refl)
                else:   # base is a regex; treat it like one
                    refl = re.sub(base,referenceMap[base],refl)
        newLogs.append(l)        
        if refl != l:
            newLogs.append(refl)
    logSet = newLogs

    # Now generate the action and guard code

    outf.write("class " + config.classname + "(object):\n")

    genCode = []

    # ------------------------------------------ #
    actDefs = []

    for corig in code:
        act = genAct()
        guard = genGuard()

        guardCode = "True"
        guardConds = []

        changes = []

        okExcepts = ""
        if corig[0] == "{":
            c = corig[corig.find("}")+1:]
            while c[0] == " ":
                c = c[1:]
            for e in corig[1:corig.find("}")].split(","):
                okExcepts += e + ","
            okExcepts = okExcepts[:-1]
        else:
            c = corig

        newC = c
        eqPos = c.find(":=")
        if eqPos == -1:
            eqPos = 0
            
        lhsUse = []
        rhsUse = []

        for p in poolSet:
            newC = newC.replace(p + " ", poolPrefix + p.replace("%",""))
            newC = newC.replace(p, poolPrefix + p.replace("%",""))
            plhs = []
            prhs = []
            found = c.find(p)
            while (found != -1):
                use = c[found:c.find("]", found)+1]
                twiddle = (found > 0) and (c[found-1]=='~')
                if (found >= eqPos):
                    prhs.append((use,twiddle))
                else:
                    plhs.append(use)
                found = c.find(p,found+1)
            for assign in plhs:
                g = assign
                g = g.replace("%","")
                g = poolPrefix + g
                g = g.replace(" ","")
                gval = g
                g = g.replace("[", "_used[")
                gguard = "((" + g + ") or (" + gval + " == None))"
                guardConds.append(gguard)
                changes.append(g + "=False")
            for (used,twiddle) in prhs:
                g = used
                g = g.replace("%","")
                g = poolPrefix + g
                g = g.replace(" ","")
                if (not twiddle):
                    changes.append(g.replace("[","_used[") + "=True")
                g += " != None"
                guardConds.append(g)

        newC = newC.replace(":=","=")
        newC = newC.replace("~"+poolPrefix,poolPrefix)

        if newC.find(" -> ") > -1:
            inlineGuardSplit = newC.split(" -> ")
            guardConds.append(inlineGuardSplit[0])
            newC = inlineGuardSplit[1]

        postCode = None
        if newC.find(" => ") > -1:
            postCodeSplit = newC.split(" => ")
            newC = postCodeSplit[0] + "\n"
            postCode = postCodeSplit[1].rstrip('\n')        

        preSet = []
        if postCode:
            m = re.match(r".*PRE%\((\S+)\)%.*",postCode)
            while m:
                pre_expr = m.groups()[0]
                spre_expr = "'''" + pre_expr + "'''"
                postCode = postCode.replace("PRE%(" + pre_expr + ")%", "__pre[" + spre_expr + "]", 1)
                if preSet == []:
                    preSet.append("__pre = {}\n")
                preSet.append("__pre[" + spre_expr + "] = " + pre_expr + "\n")
                m = re.match(r".*PRE%\((\S+)\)%.*",postCode)
            
        expectCode = None
        if newC.find(" ==> ") > -1:
            codeExpectkSplit = newC.split(" ==> ")
            newC = codeExpectkSplit[0] + "\n"
            expectCode = codeExpectkSplit[1].rstrip('\n')

        refC = newC
        for p in poolSet:
            if p in refSet:
                pRaw = poolPrefix + p.replace("%","")
                refC = refC.replace(pRaw,pRaw+"_REF")

        for base in referenceMap:
            if re.match(r"^[a-zA-Z_0-9]+$", refC):  # base is not a regex; treat it like a function name
                refC = re.sub(r'\b'+base+r'\b',referenceMap[base],refC)
            else:   # base is a regex; treat it like one
                refC = re.sub(base,referenceMap[base],refC)

        comparing = False
        for comp in compareSet:
            if re.match(".*" + comp + ".*", newC):
                if refC != newC:
                    newC = "__result = " + newC
                    refC = "__result_REF = " + refC
                    comparing = True

        beforeSig = afterSig = checkSig = ""
        if expectCode:
            beforeSig = re.sub('([^\(]+)\(', "\\1_before(", expectCode, count=1)
            afterSig = re.sub('([^\(]+)\(', "\\1_after(", expectCode, count=1)
            checkSig = re.sub('([^\(]+)\(', "\\1_check(__before_res, __after_res, ", expectCode, count=1)

        genCode.append("def " + act + "(self):\n")
        if logSet != []:
            genCode.append(baseIndent + "self.log()\n")
        if preSet != []:
            for p in preSet:
                genCode.append(baseIndent + p)
        if not config.nocover:
            genCode.append(baseIndent + "if self.__collectCov:\n")
            genCode.append(baseIndent + baseIndent + "self.__cov.start()\n")

            genCode.append(baseIndent + "try:\n")
            genCode.append(baseIndent + baseIndent + "test_before_each()\n")
            genCode.append(baseIndent + "except:\n")
            genCode.append(baseIndent + baseIndent + "pass\n")

            genCode.append(baseIndent + "try:\n")
            if expectCode:
                genCode.append(baseIndent + baseIndent + "__before_res = " + beforeSig + "\n")
            genCode.append(baseIndent + baseIndent + newC + "\n")
            if expectCode:
                genCode.append(baseIndent + baseIndent + "__after_res = " + afterSig + "\n")
                genCode.append(baseIndent + baseIndent + "__check_res = " + checkSig + "\n")
                genCode.append(baseIndent + baseIndent + "assert __check_res == True, \" check of (%s) for before and after values (%s) and (%s) failed\" % (\"" + expectCode + "\", __before_res, __after_res)\n")

            if okExcepts != "":
                genCode.append(baseIndent + "except (" + okExcepts + "):\n")
                genCode.append(baseIndent + baseIndent + "pass\n")

            genCode.append(baseIndent + "finally:\n")
            genCode.append(baseIndent + baseIndent + "try:\n")
            genCode.append(baseIndent + baseIndent + baseIndent + "test_after_each()\n")
            genCode.append(baseIndent + baseIndent + "except:\n")
            genCode.append(baseIndent + baseIndent + baseIndent + "pass\n")
            genCode.append(baseIndent + baseIndent + "if self.__collectCov:\n")
            genCode.append(baseIndent + baseIndent + baseIndent + "self.__cov.stop()\n")
            genCode.append(baseIndent + baseIndent + baseIndent + "self.__updateCov()\n")
        else:
            genCode.append(baseIndent + newC + "\n")
        if refC != newC:
            genCode.append(baseIndent + refC + "\n")
            if comparing:
                genCode.append(baseIndent + "assert __result == __result_REF, \" (%s) == (%s) \" % (__result, __result_REF)\n")
            if postCode:
                genCode.append(baseIndent + "assert " + postCode + "\n")
        for ch in changes:
            genCode.append(baseIndent + ch + "\n")

        for g in guardConds:
            guardCode += " and (" + g + ")"

        if newC.find("guarded") == 0:
            guardCode += " and (" + newC.replace(")\n",",True))")

        genCode.append("def " + guard + "(self):\n")
        genCode.append(baseIndent + "return " + guardCode + "\n")

        genCode.append("\n")

        d = "self.__actions.append(("
        d += "'''" + newC[:-1] +" ''',"
        d += "self." + guard + ","
        d += "self." + act + "))\n"
        actDefs.append(d)
        d = "self.__names[" + "'''" + newC[:-1] + " '''] = ("
        d += "'''" + newC[:-1] + " ''',"
        d += "self." + guard + ","
        d += "self." + act + ")\n"
        actDefs.append(d)


    # ------------------------------------------ #
    genCode.append("def __init__(self):\n")
    genCode.append(baseIndent + "try:\n")
    genCode.append(baseIndent + baseIndent + "test_before_all()\n")
    genCode.append(baseIndent + "except:\n")
    genCode.append(baseIndent + baseIndent + "pass\n")
    genCode.append(baseIndent + "self.__modules = []\n")
    for s in sourceSet:
        genCode.append(baseIndent + 'self.__modules.append(r"' + s + '")\n')
    genCode.append(baseIndent + "self.__features = []\n")
    for f in featureSet:
        genCode.append(baseIndent + 'self.__features.append(r"' + f + '")\n')

    if not config.nocover:
        covc = baseIndent + "self.__cov = coverage.coverage(branch=True, source=["
        for s in sourceSet:
            covc += '"' + s + '",'
        if len(sourceSet) > 0:
            covc = covc[:-1]
        genCode.append(covc + "])\n")
        genCode.append(baseIndent + "self.__collectCov = True\n")
        genCode.append(baseIndent + "self.__allBranches = set()\n")
        genCode.append(baseIndent + "self.__allStatements = set()\n")
        genCode.append(baseIndent + "self.__newBranches = set()\n")
        genCode.append(baseIndent + "self.__newStatements = set()\n")
        genCode.append(baseIndent + "self.__currBranches = set()\n")
        genCode.append(baseIndent + "self.__currStatements = set()\n")
        genCode.append(baseIndent + "self.__newCurrBranches = set()\n")
        genCode.append(baseIndent + "self.__newCurrStatements = set()\n")

    genInitialization()
        
    genCode.append(baseIndent + "self.__actions = []\n")
    genCode.append(baseIndent + "self.__names = {}\n")
    genCode.append(baseIndent + "self.__failure = None\n")
    genCode.append(baseIndent + "self.__log = None\n")
    genCode.append(baseIndent + "self.__logAction = self.logPrint\n")
    for d in actDefs:
        genCode.append(baseIndent + d + "\n")

    genCode.append(baseIndent + "self.__actions_backup = list(self.__actions)\n")

    genCode.append("def restart(self):\n")
    if not config.nocover:
        genCode.append(baseIndent + "self.__currBranches = set()\n")
        genCode.append(baseIndent + "self.__currStatements = set()\n")
        genCode.append(baseIndent + "self.__newCurrBranches = set()\n")
        genCode.append(baseIndent + "self.__newCurrStatements = set()\n")
        if config.coverreload:
            genCode.append(baseIndent + "if self.__collectCov: self.__cov.start()\n")
    for l in import_modules:
        s = baseIndent + 'reload({})\n'.format(l)
        genCode.append(s)
    if (not config.nocover) and config.coverreload:
        genCode.append(baseIndent + "if self.__collectCov: self.__cov.stop()\n")        
        genCode.append(baseIndent + "if self.__collectCov: self.__updateCov()\n")
    genInitialization()

    genCode.append("def log(self):\n")
    if logSet != []:
        genCode.append(baseIndent + "if self.__log == None:\n")
        genCode.append(baseIndent + baseIndent + "return\n")
        for l in logSet:
            ls = l.split()
            try:
                level = int(ls[0])
                lcode = l[l.find(ls[1]):]
            except ValueError:
                level = 0
                lcode = l
            genCode.append(baseIndent + "if (self.__log == 'All') or (self.__log >= " + str(level) + "):\n")
            genCode.append(baseIndent + baseIndent + "try:\n")
            genCode.append(baseIndent + baseIndent + baseIndent + "self.__logAction(" + '"""' + lcode[:-1] + '""",' + lcode[:-1] + ")\n")
            genCode.append(baseIndent + baseIndent + "except:\n")
            genCode.append(baseIndent + baseIndent + baseIndent + "pass\n")
            
    else:
        genCode.append(baseIndent + "pass\n")
        
    genCode.append("def state(self):\n")
    st = baseIndent + "return [ "
    for p in poolSet:
        st += "copy.deepcopy(" + poolPrefix + p.replace("%","") + "),"
        st += "copy.deepcopy(" + poolPrefix + p.replace("%","") + "_used),"
    st = st[:-1]
    genCode.append(st + "]\n")

    genCode.append("def backtrack(self,old):\n")
    n = 0
    for p in poolSet:
        genCode.append(baseIndent + poolPrefix + p.replace("%","") + " = copy.deepcopy(old[" + str(n) + "])\n")
        n += 1
        genCode.append(baseIndent + poolPrefix + p.replace("%","") + "_used = copy.deepcopy(old[" + str(n) + "])\n")
        n += 1
    if len(poolSet) == 0:
        genCode.append(baseIndent + "pass\n")

    genCode.append("def check(self):\n")
    if propSet != []:
        genCode.append(baseIndent + "try:\n")
        if not config.nocover:
            genCode.append(baseIndent + baseIndent + "if self.__collectCov:\n")
            genCode.append(baseIndent + baseIndent + baseIndent + "self.__cov.start()\n")
        for (p, u) in propSet:
            if u != []:
                pr = baseIndent + baseIndent + "if True"
                for use in u:
                    pr += " and (" + use + " != None)"
                pr += ":\n"
                genCode.append(pr)
                
                genCode.append(baseIndent + baseIndent + baseIndent + "assert " + p + "\n")
            else:
                genCode.append (baseIndent + baseIndent + "assert " + p + "\n")
        genCode.append(baseIndent + "except:\n")
        genCode.append(baseIndent + baseIndent + "self.__failure = sys.exc_info()\n")
        genCode.append(baseIndent + baseIndent + "return False\n")
        if not config.nocover:
            genCode.append(baseIndent + "finally:\n")
            genCode.append(baseIndent + baseIndent + "if self.__collectCov:\n")
            genCode.append(baseIndent + baseIndent + baseIndent + "self.__cov.stop()\n")
            genCode.append(baseIndent + baseIndent + baseIndent + "self.__updateCov()\n")
    genCode.append(baseIndent + "return True\n")

    for c in genCode:
        outf.write(baseIndent + c.replace("True and (","("))

    ######################## REQUIRED FOR PACKAGING TSTL ##########################
    boilerplate = pkg_resources.resource_stream('src', 'static/boilerplate.py')
    boilerplate_cov = pkg_resources.resource_stream('src', 'static/boilerplate_cov.py')
    ###############################################################################

    for l in boilerplate:
        outf.write(baseIndent + l)

    if not config.nocover:
        for l in boilerplate_cov:
            outf.write(baseIndent + l)    

    outf.close()


if __name__ == '__main__':
    main()
