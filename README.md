TSTL: the Template Scripting Testing Language
===========================================

TSTL is a domain-specific language (DSL) and set of tools to support automated generation of tests for software.  This
implementation targets Python.  You define (in Python) a set of
components used to build up a test, and any properties you want to
hold for the tested system, and TSTL generates tests for your system.
TSTL supports test replay, test reduction, and code coverage analysis,
and includes push-button support for some sophisticated
test-generation methods.  In other words, TSTL is a _property-based
testing_ tool.

What is property based testing?  Property-based testing is testing that relies
not on developers specifying results for specific inputs or call sequences, but on more
general specification of behavior, combined with automatic generation of many
tests to make sure that the general specification holds.  For more on
property-based testing see:

- https://fsharpforfunandprofit.com/posts/property-based-testing/

- https://hypothesis.works/articles/what-is-property-based-testing/

- https://github.com/trailofbits/deepstate (a tool mixing symbolic
  analysis and fuzzing with property-based testing, for C and C++,
  with design somewhat informed by TSTL)

TSTL has been used to find and fix real faults in real code, including ESRI's ArcPy (http://desktop.arcgis.com/en/arcmap/latest/analyze/arcpy/what-is-arcpy-.htm), sortedcontainers (https://github.com/grantjenks/sorted_containers),
gmpy2 (https://github.com/aleaxit/gmpy), sympy (http://www.sympy.org/en/index.html), pyfakefs (https://github.com/jmcgeheeiv/pyfakefs),
Python itself (https://bugs.python.org/issue27870), the Solidity compiler (https://github.com/ethereum/solidity), a Solidity static analysis tool (https://github.com/crytic/slither), the Vyper compiler (e.g. https://github.com/ethereum/vyper/issues/1658), and even OS X.

Installation
------------

You can grab a recent tstl most easily using pip.  `pip install tstl` should work fine.  If you want something even more recent you can do:

    git clone https://github.com/agroce/tstl.git
    cd tstl
    python setup.py install

For code coverage, you will also need to install Ned Batchelder's `coverage.py` tool; `pip install coverage` is all that is needed.

TSTL in a Nutshell
------------------

To get an idea of how TSTL operates, let's try a toy example.  We will use TSTL to solve a simple "puzzle" to see if it is possible to generate the integer value 510 using only a few lines of Python code, using only a small set of operations (add 4, subtract 3, multiply by 3, and produce a power of two) starting from 0.

1.  Create a file called `nutshell.tstl` with the following content:

```
@import math

# A line beginning with an @ is just python code.

pool: <int> 5

# A pool is a set of values we'll produce and use in testing.
# We need some integers, and we'll let TSTL produce up to 5 of them.
# The name is a variable name, basically, but often will be like a
# type name, showing how the value is used.

<int> := 0
<int> += 4
<int> -= 3
<int> *= 3
{OverflowError} <int> := int(math.pow(2,<int>))

# These are actions, basically single lines of Python code.
# The big changes from normal Python are:
# 1. := is like Python assignment with =, but also tells TSTL this
# assignment _initializes_ a value.
# 2. <int> is a placeholder meaning _any_ int value in the pool.
# 3. {OverflowError} means that we want to ignore if this line of
# Python produces an uncaught OverflowError exception.

# A test in TSTL is a sequence of actions.  So, given the above, one
# test would be:
#
# int3 = 0
# int4 = 0
# int3 *= 3
# int4 += 4
# int3 = 0
# int2 = int(math.pow(2,int4))
# int2 -= 3

# As you can see, the actions can appear in any order, but every
# pool variable is first initialized by some := assignment.
# Similarly, TSTL may use pool variables in an arbitrary order;
# thus we never see int0 or int1 used, here, by chance.

# The size of the int pool determines how many different ints can
# appear in such a test.  You can think of it as TSTL's "working
# memory."  If you have a pool size of 1, and an action like
# foo(<int>,<int>) you'll always call foo with the same value for both
# parameters -- like foo(int0,int0).  You should always have a pool
# size at least as large as the number of times you use a pool in a
# single action.  More is often better, to give TSTL more ability to
# bring back in earlier computed values.

property: <int> != 510

# property: expresses an invariant of what we are testing.  If the
# boolean expression evaluates to False, the test has failed.
```

As in normal Python, `#` indicates a comment.  Comment lines are below
the TSTL code being described.

2. Type `tstl nutshell.tstl`.
3. Type `tstl_rt --normalize --output nutshell.test`.

This should, in a few seconds, find a way to violate the property
(produce the value 510), find a maximally-simple version of that
"failing test", and produce a file `nutshell.test` that contains the
test.  If we had omitted the `{OverflowError}` TSTL would either have
found a way to produce 510, or (less likely) would have found a way to
produce an overflow in the `pow` call:  either would be considered a failure.

4. Type `tstl_replay nutshell.test --verbose`.

This will replay the test you just created.

5. Comment out (using `#` as usual in Python code) the line `<int> -= 3`.  Now try running `tstl_rt`.

The core idea of TSTL is to define a set of possible steps in a test,
plus properties describing what can be considered a test failure, and
let TSTL find out if there exists a sequence of actions that will
produce a test failure.  The actions may be function or method calls,
or steps that assemble input data (for example, building up a string
to pass to a parser), or, really, anything you can do with Python.

Using TSTL
------------

TSTL installs a few standard tools: the TSTL compiler itself, `tstl`; a random test generator
`tstl_rt`; a tool for producing standalone tests, `tstl_standalone`;
a tool for replaying TSTL test files, `tstl_replay`; a tool for
delta-debugging and normalization of TSTL tests, `tstl_reduce`; and a tool for running a set of tests as a regression, `tstl_regress`.

You can do most of what you'll need with just the commands `tstl`, `tstl_rt`, `tstl_replay`, and `tstl_reduce`.

* `tstl <filename.tstl>` compiles a `.tstl` file into an `sut.py` interface for testing
* `tstl_rt` runs random testing on the `sut.py` in the current directory, and dumps any discovered faults into `.test` files
* `tstl_replay <filename.test>` runs a saved TSTL test, and tells you if it passes or fails; with `--verbose` it provides a fairly detailed trace of the test execution
* `tstl_reduce <filename.test> <newfilename.tstl>` takes `<filename.test>` runs reduction and normalization on it to produce a shorter, easier to understand test, and saves the output as `<newfilename.tstl>`.

All of these tools offer a large number of configuration options; `--help` will produce a list of supported options for all TSTL tools.


Extended Example
-----

The easiest way to understand TSTL may be to examine
examples/AVL/avlnew.tstl (https://github.com/agroce/tstl/blob/master/examples/AVL/avlnew.tstl), which is a simple example file in the latest
language format.

`avlnew.tstl` creates a pretty full-featured tester for an AVL tree class.  You can
write something very quick and fairly effective with just a few lines
of code, however:

    @import avl
    pool: <int> 3
	pool: <avl> 2
	
	property: <avl>.check_balanced()

	<int> := <[1..20]>
    <avl> := avl.AVLTree()
	
	<avl>.insert(<int>)
	<avl>.delete(<int>)
	<avl>.find(<int>)
    <avl>.display()	

This says that there are two kinds of "things" involved in our
AVL tree implementation testing:  `int` and `avl`.   We define, in
Python, how to create these things, and what we can do with
these things, and then TSTL produces sequences of actions, that is
_tests_, that match our definition.  TSTL also checks that all AVL trees, at all times, are
properly balanced.  If we wanted, as in `avlnew.tstl`, we could also
make sure that our AVL tree "acts like" a set --- when we insert
something, we can find that thing, and when we delete something, we
can no longer find it.

Note that we start with "raw Python" to import the avl module, the SUT.  While TSTL
supports using from, aliases, and wildcards in imports, you should always
import the module(s) under test with a simple import.  This allows TSTL to identify
the code to be tested and automatically provide coverage, static analysis-aided
testing methods, and proper module management.  Utility code in the standard library,
on the other hand, can be imported any way you wish.

If we test this (or `avlnew.tstl`) for 30 seconds, something like this will appear:

`~/tstl/examples/AVL$ tstl_rt --timeout 30`


    Random testing using config=Config(swarmSwitch=None, verbose=False, fastQuickAnalysis=False, failedLogging=None, maxtests=-1, greedyStutter=False, exploit=None, seed=None, generalize=False, localize=False, uncaught=False, speed='FAST', internal=False, normalize=False, highLowSwarm=None, replayable=False, essentials=False, quickTests=False, coverfile='coverage.out', uniqueValuesAnalysis=False, swarm=False, ignoreprops=False, total=False, swarmLength=None, noreassign=False, profile=False, full=False, multiple=False, relax=False, swarmP=0.5, stutter=None, running=False, compareFails=False, nocover=False, swarmProbs=None, gendepth=None, quickAnalysis=False, exploitCeiling=0.1, logging=None, html=None, keep=False, depth=100, throughput=False, timeout=30, output=None, markov=None, startExploit=0)
      12 [2:0]
    -- < 2 [1:0]
    ---- < 1 [0:0] L
    ---- > 5 [0:0] L
    -- > 13 [1:-1]
    ---- > 14 [0:0] L
    set([1, 2, 5, 12, 13, 14])
    ...
      11 [2:0]
    -- < 5 [1:0]
    ---- < 1 [0:0] L
    ---- > 9 [0:0] L
    -- > 14 [1:-1]
    ---- > 18 [0:0] L
    set([1, 5, 9, 11, 14, 18])
    STOPPING TEST DUE TO TIMEOUT, TERMINATED AT LENGTH 17
    STOPPING TESTING DUE TO TIMEOUT
    80.8306709265 PERCENT COVERED
    30.0417540073 TOTAL RUNTIME
    236 EXECUTED
    23517 TOTAL TEST OPERATIONS
    10.3524413109 TIME SPENT EXECUTING TEST OPERATIONS
    0.751145362854 TIME SPENT EVALUATING GUARDS AND CHOOSING ACTIONS
    18.4323685169 TIME SPENT CHECKING PROPERTIES
    28.7848098278 TOTAL TIME SPENT RUNNING SUT
    0.179262161255 TIME SPENT RESTARTING
    0.0 TIME SPENT REDUCING TEST CASES
    224 BRANCHES COVERED
    166 STATEMENTS COVERED

For many (but not all!) programs, a more powerful alternative to
simple random testing is to use swarm testing, which restricts the
actions in each individual test (e.g., insert but no delete, or find
but no inorder traversals) (see
http://agroce.github.io/issta12.pdf).

    ~/tstl/examples/AVL$ tstl_rt --timeout 30 --swarm
    Random testing using config=Config(swarmSwitch=None, verbose=False, fastQuickAnalysis=False, failedLogging=None, maxtests=-1, greedyStutter=False, exploit=None, seed=None, generalize=False, localize=False, uncaught=False, speed='FAST', internal=False, normalize=False, highLowSwarm=None, replayable=False, essentials=False, quickTests=False, coverfile='coverage.out', uniqueValuesAnalysis=False, swarm=True, ignoreprops=False, total=False, swarmLength=None, noreassign=False, profile=False, full=False, multiple=False, relax=False, swarmP=0.5, stutter=None, running=False, compareFails=False, nocover=False, swarmProbs=None, gendepth=None, quickAnalysis=False, exploitCeiling=0.1, logging=None, html=None, keep=False, depth=100, throughput=False, timeout=30, output=None, markov=None, startExploit=0)
      11 [2:0]
    -- < 7 [1:0]
    ...
    STOPPING TEST DUE TO TIMEOUT, TERMINATED AT LENGTH 94
    224 BRANCHES COVERED
    166 STATEMENTS COVERED

Here, the method is not very important; simple random testing does a
decent job covering the AVL tree code in just 60 seconds.  If we
introduce a bug by removing the `self.rebalance()` call on line 205 of
avl.py, either method will quickly report a failing test case,
automatically reduced.  By default, the random tester will run the test
in a verbose mode to show in more detail what happens during the execution
that causes a failure.
        
	~/tstl/examples/AVL$ tstl_rt --timeout 30
	Random testing using config=Config(swarmSwitch=None, verbose=False, fastQuickAnalysis=False, failedLogging=None, maxtests=-1, greedyStutter=False, exploit=None, seed=None, generalize=False, localize=False, uncaught=False, speed='FAST', uniqueValuesAnalysis=False, normalize=False, silentFail=False, noAlphaConvert=False, replayable=False, essentials=False, quickTests=False, coverfile='coverage.out', swarm=False, internal=False, total=False, progress=False, swarmLength=None, noreassign=False, profile=False, full=False, multiple=False, timedProgress=30, relax=False, swarmP=0.5, stutter=None, highLowSwarm=None, readQuick=False, verboseActions=False, running=False, ignoreProps=False, compareFails=False, nocover=False, swarmProbs=None, gendepth=None, quickAnalysis=False, exploitCeiling=0.1, computeFeatureStats=False, logging=None, html=None, keep=False, noExceptionMatch=False, depth=100, showActions=False, throughput=False, timeout=30, output='failure.26816.test', markov=None, startExploit=0)
	  11 [2:0]
	-- < 8 [1:0]
	---- < 4 [0:0] L
	---- > 9 [0:0] L
	-- > 18 [1:1]
	---- < 15 [0:0] L
	set([4, 8, 9, 11, 15, 18])
	PROPERLY VIOLATION
	ERROR: (<type 'exceptions.AssertionError'>, AssertionError(), <traceback object at 0x1032bf4d0>)
	TRACEBACK:
	  File "/Users/alex/tstl/examples/AVL/sut.py", line 7960, in check
	    assert self.p_avl[0].check_balanced()
	Original test has 98 steps
	REDUCING...
	Failed to reduce, increasing granularity to 4
	Reduced test length to 73
	Failed to reduce, increasing granularity to 4
	Reduced test length to 55
	Failed to reduce, increasing granularity to 4
	Reduced test length to 41
	Failed to reduce, increasing granularity to 4
	Reduced test length to 31
	Failed to reduce, increasing granularity to 4
	Reduced test length to 24
	Failed to reduce, increasing granularity to 4
	Failed to reduce, increasing granularity to 8
	Reduced test length to 20
	Failed to reduce, increasing granularity to 4
	Failed to reduce, increasing granularity to 8
	Reduced test length to 17
	Failed to reduce, increasing granularity to 4
	Failed to reduce, increasing granularity to 8
	Reduced test length to 14
	Failed to reduce, increasing granularity to 4
	Failed to reduce, increasing granularity to 8
	Reduced test length to 13
	Failed to reduce, increasing granularity to 4
	Failed to reduce, increasing granularity to 8
	Reduced test length to 11
	Failed to reduce, increasing granularity to 4
	Failed to reduce, increasing granularity to 8
	Failed to reduce, increasing granularity to 11
	Reduced test has 11 steps
	REDUCED IN 1.02356314659 SECONDS
	Alpha converting test...
	int0 = 1                                                                 # STEP 0
	avl0 = avl.AVLTree()                                                     # STEP 1
	avl0.insert(int0)                                                        # STEP 2
	int0 = 6                                                                 # STEP 3
	avl0.insert(int0)                                                        # STEP 4
	int0 = 8                                                                 # STEP 5
	avl0.insert(int0)                                                        # STEP 6
	int1 = 20                                                                # STEP 7
	avl0.insert(int1)                                                        # STEP 8
	int1 = 1                                                                 # STEP 9
	avl0.delete(int1)                                                       # STEP 10

	SAVING TEST AS failure.26816.test
	FINAL VERSION OF TEST, WITH LOGGED REPLAY:
	int0 = 1                                                                 # STEP 0
	ACTION: int0 = 1 
	int0 = None : <type 'NoneType'>
	=> int0 = 1 : <type 'int'>
	==================================================
	avl0 = avl.AVLTree()                                                     # STEP 1
	ACTION: avl0 = avl.AVLTree() 
	avl0 = None : <type 'NoneType'>
	avl_REF0 = None : <type 'NoneType'>
	=> avl0 = <avlbug2.AVLTree instance at 0x10311edd0> : <type 'instance'>
	REFERENCE ACTION: avl_REF0 = set()
	=> avl_REF0 = set([]) : <type 'set'>
	==================================================
	avl0.insert(int0)                                                        # STEP 2
	ACTION: avl0.insert(int0) 
	int0 = 1 : <type 'int'>
	avl0 = <avlbug2.AVLTree instance at 0x10311edd0> : <type 'instance'>
	avl_REF0 = set([]) : <type 'set'>
	REFERENCE ACTION: avl_REF0.add(int0)
	=> avl_REF0 = set([1]) : <type 'set'>
	==================================================
	int0 = 6                                                                 # STEP 3
	ACTION: int0 = 6 
	int0 = 1 : <type 'int'>
	=> int0 = 6 : <type 'int'>
	==================================================
	avl0.insert(int0)                                                        # STEP 4
	ACTION: avl0.insert(int0) 
	int0 = 6 : <type 'int'>
	avl0 = <avlbug2.AVLTree instance at 0x10311edd0> : <type 'instance'>
	avl_REF0 = set([1]) : <type 'set'>
	REFERENCE ACTION: avl_REF0.add(int0)
	=> avl_REF0 = set([1, 6]) : <type 'set'>
	==================================================
	int0 = 8                                                                 # STEP 5
	ACTION: int0 = 8 
	int0 = 6 : <type 'int'>
	=> int0 = 8 : <type 'int'>
	==================================================
	avl0.insert(int0)                                                        # STEP 6
	ACTION: avl0.insert(int0) 
	int0 = 8 : <type 'int'>
	avl0 = <avlbug2.AVLTree instance at 0x10311edd0> : <type 'instance'>
	avl_REF0 = set([1, 6]) : <type 'set'>
	REFERENCE ACTION: avl_REF0.add(int0)
	=> avl_REF0 = set([8, 1, 6]) : <type 'set'>
	==================================================
	int1 = 20                                                                # STEP 7
	ACTION: int1 = 20 
	int1 = None : <type 'NoneType'>
	=> int1 = 20 : <type 'int'>
	==================================================
	avl0.insert(int1)                                                        # STEP 8
	ACTION: avl0.insert(int1) 
	int1 = 20 : <type 'int'>
	avl0 = <avlbug2.AVLTree instance at 0x10311edd0> : <type 'instance'>
	avl_REF0 = set([8, 1, 6]) : <type 'set'>
	REFERENCE ACTION: avl_REF0.add(int1)
	=> avl_REF0 = set([8, 1, 20, 6]) : <type 'set'>
	==================================================
	int1 = 1                                                                 # STEP 9
	ACTION: int1 = 1 
	int1 = 20 : <type 'int'>
	=> int1 = 1 : <type 'int'>
	==================================================
	avl0.delete(int1)                                                       # STEP 10
	ACTION: avl0.delete(int1) 
	int1 = 1 : <type 'int'>
	avl0 = <avlbug2.AVLTree instance at 0x10311edd0> : <type 'instance'>
	avl_REF0 = set([8, 1, 20, 6]) : <type 'set'>
	REFERENCE ACTION: avl_REF0.discard(int1)
	=> avl_REF0 = set([8, 20, 6]) : <type 'set'>
	==================================================
	ERROR: (<type 'exceptions.AssertionError'>, AssertionError(), <traceback object at 0x10369c128>)
	TRACEBACK:
	  File "/Users/alex/tstl/examples/AVL/sut.py", line 7960, in check
	    assert self.p_avl[0].check_balanced()
	STOPPING TESTING DUE TO FAILED TEST
	79.552715655 PERCENT COVERED
	2.22598695755 TOTAL RUNTIME
	15 EXECUTED
	1498 TOTAL TEST OPERATIONS
	0.408244371414 TIME SPENT EXECUTING TEST OPERATIONS
	0.0258889198303 TIME SPENT EVALUATING GUARDS AND CHOOSING ACTIONS
	0.706946611404 TIME SPENT CHECKING PROPERTIES
	1.11519098282 TOTAL TIME SPENT RUNNING SUT
	0.00753235816956 TIME SPENT RESTARTING
	1.03021097183 TIME SPENT REDUCING TEST CASES
	220 BRANCHES COVERED
	164 STATEMENTS COVERED


Using `--output`, the failing test can be saved to a named file, and with the `standalone.py`
utility, converted into a completely standalone test case that does
not require TSTL itself.  Without `--output` the test is still saved, but the name is based on the process ID of `tstl_rt`.  In either case, you can easily re-run a saved test, even without converting to a standalone test, using `tstl_replay <testname>`, and reduce it using `tstl_reduce`.  The `--verbose` flag is useful for replay, since it will show you exactly what happens during a test.

    ~/tstl/examples/AVL$ tstl_rt --timeout 30 --output failure.test
    Random testing using config=Config(swarmSwitch=None, verbose=False, fastQuickAnalysis=False, failedLogging=None, maxtests=-1, greedyStutter=False, exploit=None, seed=None, generalize=False, localize=False, uncaught=False, speed='FAST', internal=False, normalize=False, highLowSwarm=None, replayable=False, essentials=False, quickTests=False, coverfile='coverage.out', uniqueValuesAnalysis=False, swarm=False, ignoreprops=False, total=False, swarmLength=None, noreassign=False, profile=False, full=False, multiple=False, relax=False, swarmP=0.5, stutter=None, running=False, compareFails=False, nocover=False, swarmProbs=None, gendepth=None, quickAnalysis=False, exploitCeiling=0.1, logging=None, html=None, keep=False, depth=100, throughput=False, timeout=30, output=None, markov=None, startExploit=0)
    ...
    ~/tstl/examples/AVL$ tstl_reduce failure.test failure_norm.test
    REDUCING...
    ...
    NORMALIZING...
    ...
    ~/tstl/examples/AVL$ tstl_replay failure_norm.test --verbose
    ...
    ~/tstl/examples/AVL$ tstl_standalone failure_norm.test failure.py
    ~/tstl/examples/AVL$ python failure.py
    Traceback (most recent call last):
      File "failure.py", line 98, in <module>
        check()
      File "failure.py", line 45, in check
        assert avl2.check_balanced()
    AssertionError

The final useful hint for getting started is that sometimes you may want to test something
(for example, a library implemented in C) where failing tests crash the Python interpreter.  This is possible,
but requires some effort.  First, run `tstl_rt` with the `--replayable` option.  This causes the generator to
keep a file, `currtest.test`, in the directory you are running testing in: this file holds the current test.  If the random tester crashes, this will include the action that caused the crash.  In a few rare cases, the behavior of past tests is also relevant to a crash (reloading the module does not really reset state of the system -- e.g., interacting with hardware).  For these cases, use `--total` and look at the file `fulltest.test`, which contains ALL actions ever performed by the random tester.

The `currtest.test` and `fulltest.test` files work just like normal TSTL files, and can be replayed with the replay utility or turned into standalone files.  However, for test reduction and normalization to work correctly, they must be reduced by passing the `--sandbox` argument to `tstl_reduce`.

What about tests that fail by entering an infinite loop?  The same technique as is used for crashes works.  However, you need to run `tstl_rt` with a time limit (using ulimit if you are on UNIX-like systems, for example).  The `tstl_reduce` utility provides a `--timeout` argument to handle such tests, but this only works on systems supporting ulimit, for now.  In very rare cases, you might have a test execution lock up because, for example, the failure causes a read from standard input.  If you hit this, contact me.

Finally, how do you integrate TSTL testing with more conventional approaches, e.g., pytest?  The file `test_tstl_regressions.py` in the examples directory shows one way.  If you add all your TSTL tests of interest to a `tstl_tests` directory under the directory where `sut.py` lives, you can make pytest run all your TSTL tests.  Perhaps more interestingly, this file also wraps a simple caller that forces 60 seconds of random testing to be executed by pytest, as a sanity check.  You can tweak the configuration of the random testing easily -- often, adding "--swarm" is a good idea.

Differential Testing and References
-----

The most important thing missing from the simplified version of the AVL harness above is the use of TSTL's powerful *differential testing* capabilities.

When a TSTL pool is defined as a "ref" pool, as in the full avlnew.tstl version, that means the pool will actually have *two* versions.  The first works just like a normal TSTL pool.  The second pool is a "copy" of the original pool, that is created by running the same Python code as the original version, with one key difference: some of the code will be automatically modified so that the "copy" can use a different underlying implementation.  In the avlnew.tstl file, the code necessary for using a reference is quite small:

```
pool: <avl> 3 OPAQUE REF

reference: avl.AVLTree ==> set
reference: insert ==> add
reference: delete ==> discard
reference: find ==> __contains__

reference: METHOD(inorder) ==> CALL(items)
reference: METHOD(display) ==> CALL(print)

compare: find
compare: inorder
```

The pool is marked as a "REF" pool (TSTL is not case sensitive for such designations).  The actual introduction of differential testing is accomplished largely by the "reference:" parts of the harness.  The first of these changes the call to the AVLTree constructor to a call to Python's built-in set implementation.  The next three change the methods for AVLTrees to the appropriate methods for sets.  The ones using METHOD and CALL transform methods of AVLTree into calls to functions on sets.  Finally the two "compare:" lines tell TSTL that the return values for the actions find and inorder and their reference equivalents should be compared for equality, and failure should result if the results don't match.

TSTL and Mutation Testing
-----
Using the
[universalmutator](https://github.com/agroce/universalmutator) tool,
you can easily investigate the power of your TSTL test harnesses to find
bugs.  For example, if we wanted to see how effective 10 seconds of
random testing using our AVL harness is, we could do this:

```
~/tstl/examples/AVL$ pip install universalmutator
~/tstl/examples/AVL$ tstl avlnew.tstl
Generating harness core using config=Config(tstl='avlnew.tstl', stats=False, checkFailureDeterminism=False, pylib=False, defaultReplay=False, forceRefExceptionMatch=False, enumerateEnabled=False, forceStrongRefExceptionMatch=False, classname='sut', version=False, noCover=False, debug=False, output='sut.py', noReload=False, ignoreAngles=False, coverReload=False, coverInit=False)
~/tstl/examples/AVL$ mkdir mutants
~/tstl/examples/AVL$ mutate avl.py --mutantDir mutants
*** UNIVERSALMUTATOR ***
MUTATING WITH RULES: universal.rules, python.rules
1497 MUTANTS GENERATED BY RULES
...
768 VALID MUTANTS
591 INVALID MUTANTS
138 REDUNDANT MUTANTS
~/tstl/examples/AVL$ analyze_mutants avl.py "tstl_rt --timeout 10" --mutantDir mutants
ANALYZING avl.py
COMMAND: ** ['tstl_rt --timeout 10'] **
#1: [0.0s 0.0% DONE]
  mutants/avl.mutant.89.py NOT KILLED
  RUNNING SCORE: 0.0
#2: [10.43s 0.13% DONE]
  mutants/avl.mutant.507.py KILLED IN 0.689107179642
  RUNNING SCORE: 0.5
#3: [11.12s 0.26% DONE]
  mutants/avl.mutant.312.py KILLED IN 2.01887583733
  RUNNING SCORE: 0.666666666667
#4: [13.14s 0.39% DONE]
  mutants/avl.mutant.165.py NOT KILLED
  RUNNING SCORE: 0.5
...
```

This reports the score for mutants that our testing doesn't even
cover, which may be of little interest if we only target part of an
API.  And, frankly, there are easier ways to see which code isn't covered
than using mutation testing!  So we may want to limit our analysis to
code actually covered by the AVL harness, using a generously large
timeout:

```
~/tstl/examples/AVL$ tstl_rt --timeout 120 --internal >& avlnew.lines
~/tstl/examples/AVL$ check_covered avl.py avlnew.lines coveredmutants.txt --tstl --mutantDir mutants
~/tstl/examples/AVL$ analyze_mutants avl.py "tstl_rt --timeout 10" --mutantDir mutants --fromFile coveredmutants.txt
ANALYZING avl.py
COMMAND: ** ['tstl_rt --timeout 10'] **
#1: [0.0s 0.0% DONE]
  mutants/avl.mutant.17.py KILLED IN 0.574796915054
  RUNNING SCORE: 1.0
#2: [0.58s 0.14% DONE]
  mutants/avl.mutant.186.py KILLED IN 0.581020116806
  RUNNING SCORE: 1.0
#3: [1.16s 0.28% DONE]
  mutants/avl.mutant.692.py NOT KILLED
  RUNNING SCORE: 0.666666666667
...
```

Hints for Better Testing
-----

Sometimes just doing `tstl_rt` or even `tstl_rt --swarm` isn't enough.  There are other options for improving testing.  A particularly powerful one in many cases is using the size of functions in terms of lines-of-code to guide testing.  To do this, you first let TSTL determine the sizes:

`tstl_rt --generateLOC sut.loc --timeout 120 --noCover`

(the `--noCover` is needed because LOC uses instrumentation that interacts badly with coverage instrumentation).

Then you use that generated file to guide testing:

`tstl_rt --biasLOC sut.loc`

It's also a good idea, for faster testing (since the power of random
testing is partly in generating huge numbers of tests every minute),
to turn off code coverage collection with `--noCover`.  This isn't so
great if you are looking to see if your tests cover your code well,
but for pedal-to-the-metal bug-hunting, it is often the way to go.

There are other things that can improve testing.  The `--profileProbs`
option gathers information on how often each action in the TSTL
harness has been taken during testing, and linearly biases random action
choice towards actions that have been taken fewer times.  This slows
down test generation substantially in most cases, but for many
programs (especially complex ones) it also dramatically improves code
coverage and fault detection, by exploring hard-to-hit actions, and
spending less time generating input data vs. running the SUT.  In
these cases the loss in test throughput produced by attempts to take
likely-disabled actions is much more than compensated
for by an improvement in test quality.  Because both rely on setting
action probabilities, `--profileProbs` and `--biasLOC` are
unfortunately not compatible.

For some programs, the structure of the harness file slows down test
generation, and the `--useDependencies` option can improve test throughput by
a factor of 2-10x.  However, for most programs this option slows down
test generation by roughly a factor of two.

Because the utility of these options varies so widely, it is best to
simply try them out.  For `--profileProbs` you should see a large
increase in code coverage if it is effective for your testing problem
(probably accompanied by a large drop in the number of tests generated),
and for `--useDependencies` you should see a large increase in the
number of tests/test operations performed.

You can also try a "genetic algorithms" approach guided by coverage, that exploits "high coverage" tests:

`tstl_rt --exploit 0.8 --Pmutate 0.5`

Adding `--reducePool` sometimes also improves the performance of this method.

You can tune the exploit and mutate parameters to see if they improve
results.  You can even combine lines-of-code bias or profile-based
probabilities with the `exploit` approach and/or swarm testing.  Unfortunately, using `--exploit` does mean you can't get away with `--noCover` to avoid the overhead of computing code coverage.

We're working on a way to get TSTL to perform experiments
automatically and advise you of the best configuration for testing a
given harness.

To get a set of very fast "regression tests" you can run `tstl_rt` for
a long time in a good configuration with the `--quickTests` option,
and generate a set of very short tests with high code coverage.

Fault Localization
-----

TSTL supports automated fault localization.  If you have a harness that finds
a bug, you might get some insight into the nature of that bug by
running something like:

`tstl-rt --localize --multiple`

This will run TSTL for an hour, generate a number of failing
test cases (if your bug can be found relatively easily in an hour),
and then report on the 20 most-likely-faulty statements and branches
in the code under test.   Some of this code may be involved in things
like printing assertion values, or error handling for the fault, but
there's a good chance you'll find the buggy code in the localization
results, in our experience.  In fact, a five minute run will suffice
for good localization, often, if five minutes is sufficient to find
your bug a few times.  Note that results are much worse if you have more than one bug!

A Swarm-Based Workflow
-----------
One way to use swarm testing effectively is to apply _directed swarm
testing_, an approach where data on how swarm interacts with code
coverage is used to boost coverage of rarely covered statements and
branches.

To do this, run your initial testing using `tstl_rt` (for an hour or more) with the options:

- `--swarm`
- `--saveSwarmCoverage <filename1>`
- `--fullCoverage <filename2>`

This will test your program, and produce two files of interest.
`<filename2>` will contain a simple text file with branches and
statements covered, ranked by the number of times they were covered.
This is basically a simplified version of the kind of output you may
be familiar with from `gcov` or other tools.  You can look at this
file, and identify interesting looking, but rarely-covered, code.

Then, take the identifier (the full string, including parenthesis) of
the interesting code and use the `tstl_directedswarm` tool like this:

`tstl_directedswarm <filename1> "<coverage target>" <probFile>`

(`<filename1>` is the file you produced in the original run of swarm
testing.)  This will try to figure out which actions help ("trigger")
and hinder ("suppress") coverage of
the target code, and produce a file (`probFile`) with probabilities for use in more
focused swarm testing.    If the tool doesn't identify any triggers or
suppressors, try running again with the `--confidence` option and a
number less than 0.95; the lower the confidence required, the more
likely you are to find triggers and suppressors, but the less likely
they are to be meaningful -- you can try slowly lowering until you get
some results.  Then run testing again, like this:

`tstl_rt --swarm --swarmProbs <probFile>`

You should usually be able to cover the rarely-covered code well this
way.  Since covering rarely covered code often
uncovers interesting new never-seen-before code, you may want to
repeat this process once you've explored the rarely-covered code from
your intial run.  You can, of course, store swarm
coverage and full coverage stats for the focused runs of TSTL, and
keep exploring.

A more systematic way to go about directed swarm testing is to try:

`tstl_analyzeswarm <filename1> <prefix> --cutoff 0.5`

to generate triggers and suppressors for ALL coverage targets hit
during a run, grouped into equivalence classes (targets with the same
set of triggers and suppressors) and ranked by the least-hit target in
each equivalence class.  The output will be stored in files beginning
with `<prefix>`:  a set of files named `<prefix>.N.probs` that can
used with `--swarmProbs`, and a single `.class` file, with all the targets,
triggers, suppressors, and minimum frequencies for classes, plus
pointers to the related probability files.  Just iterating through the generated
probability files for the classes for the rarest targets is a good way
to go about directed swarm testing.  The `0.5` above can be any
cutoff, above which targets hit by at least that fraction of tests are
considered well-tested and ignored.  Setting this as low as `0.01` can
work well, for initial runs producing a large number of tests.


TSTL and the American Fuzzy Lop (AFL) Fuzzer
---------

You can even use AFL (http://lcamtuf.coredump.cx/afl/) to generate
TSTL tests.  You need to install AFL itself and the `python-afl` pip
package (or grab the code from github at https://github.com/jwilk/python-afl).  Then you can fuzz using AFL in any directory with a compiled
TSTL harness:

`tstl_afl_fuzz --output <outputdir> --input <inputdir>`

This will use some (usually good) default settings to first have TSTL
generate some good starting tests for AFL to build on, then run AFL
for a day on the SUT.  A day may not be enough, so the same
`--timeout` parameter is supported as by the TSTL random tester.  You
can also use swarm testing by adding `--swarm`.  There are other, less
frequently used, options as well.  Failing tests generated by AFL will
be stored as `aflfail.<PID>.test` in the current directory.  One piece
of advice:  `<outputdir>` should probably be a ramdisk, unless you
want to really hammer your SSD (don't even think about doing this on
an actual hard drive).

You should also try the `--persist` option to `tstl_afl_fuzz`, which
will often improve fuzzing speed by a large margin, and
dramatically improve AFL results (since throughput is so critical); however, 
this is somewhat less well-tested than the non-persistent mode.  With
more testing, this will likely become the default setting, so you may
want to jump ahead of the curve, and only run non-persistent if
persistent mode seems to cause problems.

This is a powerful testing option, as it lets you use AFL's great
heuristics to fuzz things that are at best highly inconvenient with
just AFL.  You can set up complex TSTL properties, mix grammar
generation and API-call sequences, and do differential testing
TSTL-style, but use AFL's tuned input generation methods.  The main
drawback is that AFL really expects much faster executables than TSTL
is giving it, so you probably need to run for days to improve on what
TSTL can do in an hour, unless your SUT is unusual.  But it is
certainly an attractive option for week-long heavy-duty testing when
`tstl_rt` isn't finding any problems.

Note that if you don't use `tstl_afl_fuzz` but directly call
`py-afl-fuzz` you probably (except on Mac OS, where memory limiting
doesn't work anyway) need a large `-m` for TSTL to work.

 Under the hood, the`tstl_afl`command takes a file of bytes and interprets every N bytes (N
depends on how many actions your harness has) as the
index of a TSTL action (modulo the number of actions), using `sut.py`
as usual.  When `tstl_afl` detects a failure
it also produces a conventional TSTL test file under the name
`aflfail.<PID>.test`.  You can even use `--swarm` to interpret the first 4 bytes
as a seed to control swarm testing, thus allowing AFL to use swarm testing; this has the drawback that the
file will be interpreted incorrectly by other TSTL tools, unless you
pass them the `--aflswarm` option.  Most TSTL tools take an
`--afl` option that indicates tests to be read in are in AFL format,
and `--aflswarm` to indicate they are swarm tests.

`tstl_afl` is also useful for turning a single
AFL byte file into a normal TSTL test file, using the `--alwaysSave` option, which dumps a TSTL test file in the current directory, created from the byte-based input.

There are also tools for converting large numbers of files to and from AFL format.
`tstl_toafl` simply takes existing TSTL test files and
converts them to AFL byte inputs, and `tstl_fromafl` does the expected
opposite (and takes an argument indicating the files are in swarm format).    `tstl_aflcorpus` randomly generates inputs that trigger novel SUT
coverage to get AFL started, but it is usually easier to just generate quick tests with
`tstl_rt --quickTests` and convert those with `tstl_toafl`.
`tstl_aflcorpus` does allow using the AFL swarm format, however; just
run it with `--swarm`.  Because of the way the swarm format works, it
is unfortunately currently not possible to extract a swarm format test
from a standard TSTL test.

TSTL's "SmallCheck"
------------------

`tstl_smallcheck` is a special-purpose test generator that uses a
depth-first-search to exhaustively generate tests up to a provided
depth limit.  The tool outputs 
coverage-increasing tests, and stops if it encounters a failure.   This will seldom finish if the depth is more than 3 to
10 (at the most) steps, unless it hits a failure.  If you run out of
patience, you can interrupt the process with CTRL-C and the tool will
save the discovered tests.

One way to get deeper "exhaustive" testing
is to use the `--recursive` option to explore from coverage increasing
tests, repeatedly up to a limited number of times, using the same
depth as the original run (and a small initial depth).

If you want to collect all failing tests, not just stop at the first one,
you'll need to use the `--multiple` option.  Because of their small size and
the presumed desire for exhaustive exploration (you used this tool,
after all), this tool provides neither reduction nor normalization of
covering tests or failures, to
avoid any risk of slippage.

In addition to `--recursive`, you can use `--visited` or `--visitedList` to avoid re-visiting
already explored states during the DFS; however, this requires some
care.  If the tool fails, or the tests don't seem valid/correct, you may want to recompile your harness with
`--defaultReplay`, because state-based backtracking doesn't work.  In
many cases, due to the high cost of state comparison in this setting,
keeping track of visited states may not even be very helpful.

Random testing using `tstl_rt` is probably almost always more
effective than this approach, but `tstl_smallcheck` can provide
guarantees that `tstl_rt` cannot, such as that no test with fewer than
four steps can
cause any failures.  Starting a smallcheck from existing quick tests using the `--fromTests` option is one way to add extra confidence in your testing.

TSTL and Hypothesis
------------------------

Some of you may be asking: "How does TSTL differ from the Hypothesis
https://hypothesis.readthedocs.io/en/latest/ testing tool?"  There are a few
answers.  First, TSTL is probably much less polished than Hypothesis,
right now!  More importantly, however, Hypothesis and TSTL both
generate tests, but they are primarily intended to generate different
kinds of tests.  Hypothesis is in what we consider the QuickCheck
family: if you have a function `f` that takes as input a list, a
string, or something more complex, Hypothesis is very likely what you
want to use.  If you have a set of functions, `f`, `g`, and `h`, and
they don't just return things, but modify invisible system state (but
also return things that may be inputs to other functions), you may
want TSTL.  You can do state-based sequence-of-method-calls testing
with Hypothesis, but it may be easier with TSTL, and it's what TSTL is
built for.  So, if you're testing a sorting implementation, Hypothesis
is almost certainly much better.  If you're testing something like a
file system, you might want to look into TSTL.  If you're testing a
parser that takes a string as input, both tools might be useful,
depending on your situation.  One additional difference for the typical user is that TSTL has considerable built-in support for performing differential/reference testing, where your SUT is compared to a reference implementation, possibly with some code to handle expected differences (see the `pyfakefs` example for a good look at how powerful this can be).  Finally, TSTL is built as a practical testing tool, but the design is strongly influenced by the decision to make it useful as a platform for experimenting with novel software testing algorithms.

The similarity is that both TSTL and Hypothesis don't look like
traditional unit testing.  They instead let you define the idea of a
valid input (either some data values, or in TSTL a sequence of method
calls and assignments that more resembles a traditional
do-some-stuff-and-then-check-it unit test) and assert general
properties about the behavior of a system under valid input.

Tips for Handling Numerous Bugs
---------------

If you test real software with a good harness, you may well find many
issues.  There are a few ways to deal with this.  First, using
`--normalize` when doing `--multiple` runs with `tstl_rt` can help.
In some cases (file systems) normalization (or even reduction) goes
too far.  In testing at NASA, we found that "last operation" was a
good heuristic for different bugs.  Using `--keepLast` in testing (or when
using `tstl_reduce`) forces reduction and normalization to leave the
last step  alone.  Normalization can still move it around, or
change the pool it uses, but is much more careful about changing the
actual action performed.  There is also a tool `tstl_triage` that
takes a _glob expression for a set of tests_, runs them all, and reports ones with
different (heuristic) failure signatures.  In particular, it gives you
the shortest test for each signature.  Remember that triage requires a
glob expression (in quotes) not a list of files.  This is so it can
handle even sets of tests that go beyond the shell expansion limit.
We assume that you won't need to handle that many tests in regression,
but for triage, who knows?  Another tool, `tstl_fpf` takes similar
arguments to `tstl_triage` but instead of clustering tests into groups
that are likely the same bug, it ranks all tests, such that very
different tests are high in the ranking, using the
"furthest-point-first" (FPF) method proposed by
Chen et. al in PLDI 2013.

Further Details
----------------

For more details on TSTL, the best starting point is a comprehensive
journal paper in STTT:
http://agroce.github.io/sttt17.pdf.
There are also NASA Formal Methods (NFM) and International Symposium
on Software Testing and Analysis (ISSTA) 2015 papers at
http://agroce.github.io/nfm15.pdf and
http://agroce.github.io/issta15.pdf, with some implementation
details or concepts that are not present in the more up-to-date and
complete paper.  In particular, the NFM paper, "A Little* Language for
Testing" has a deprecated syntax and other issues, but is the most
concise explanation of the core TSTL idea: a DSL embedding a full
programming language,
designed to make testing (and building testing tools) easy.

There is a more recent paper describing test normalization, a feature
unique to TSTL, in more detail, http://agroce.github.io/issta17.pdf, as well as a
tool paper describing how to use TSTL's test manipulation commands 
(http://agroce.github.io/issta17tool.pdf).

The NFM and ISSTA papers use an early version of TSTL syntax, which marks
pools and TSTL constructs with % signs.  "Modern" TSTL uses <> by
default, though if for some reason you need <> in your code (and to
prepare for a future C++ version) this can be turned off and only % supported.

Note that documentation above is preliminary.  The best way to get started, once you understand the basic tools (`tstl`, `tstl_rt`, `tstl_replay`, and `tstl_reduce`) is to examine the examples directory and try out real TSTL test
harnesses.  For the brave, reading tstl/randomtester.py provides
considerable guidance in how to (efficiently) use TSTL in a generic
testing tool, with TSTL providing an interface to the underlying
application/library to be tested.

Caveats
-------

Note that TSTL was originally written for Python 2.7, has mostly been developed/tested that way, and is not extremely well-tested yet with Python 3.0+.
However, it should work ok, thanks to mrbean-bremen, and the Travis
tests check that TSTL works fine on Python 3.6.  Earlier 3.0+ versions
may have some "gotchas."

Developer Info
--------------

There are no developer docs yet, which will hopefully change in the future.
The best shakedown test for tstl is to compile and run (using `tstl_rt`) the AVL
example.  Removing any call to the balancing function in the avl.py
code should cause TSTL to produce a failing test case.

Credits
--------------

Who is responsible for TSTL?

- Alex Groce (agroce) wrote this file, and most of the current code base, and is running the show.  If there is a problem with TSTL, it is my fault, and don't blame anyone below.

- Josie Holmes (josieholmes) contributed to core language design changes, and is responsible for the ideas (and some of the code) for the various slippage reduction strategies, plus the LOC bias work and Markov things.  Before Josie's work, TSTL was extremely hard to read, and considerably less efficient.

- Jervis Pinto was the other original TSTL-er, and has his fingerprints on various parts of the early design and code that form the foundations of TSTL.

- Pranjal Mittal contributed a number of critical elements, including the initial effort to prepare TSTL for a pip release as a useful tool, and has helped publicize TSTL.

- Pooria Azimi added the `<int,1>` notation, which turns out to be one of the most important changes, and eliminated the need for the exceedingly awkward way of handling binding via Python functions and commit point based guards.  Without this, you really don't have a useful TSTL.

- Kevin Kellar developed a (beta) Java version of TSTL: https://github.com/flipturnapps/TSTL-Java.

- My (Alex's) other graduate students (Amin Alipour, Rahul Gopinath, Arpit Christi, Chaoqiang Zhang, Shalini Shamasunder) and almost-mine graduate student (Iftekhar Ahmed) contributed to the general intellectual climate in which TSTL was born.

- Students in CS 499 at Northern Arizona University and CS 362, 562, and 569 at Oregon State University contributed a lot of ideas, and a few concrete language/tool changes or bug reports.  These are too numerous to mention, and in some cases I don't recall who asked "why do you do it that stupid way?" in class, and got me thinking that it was in fact a stupid way to do things.

- Ned Batchelder, David R. MacIver, and John Regehr have no actual code in TSTL, but all contributed in significant ways to various implementation aspects, in ways that go beyond the general disclaimer that TSTL freely steals from the entire software testing (research) community.

- The pyfakefs team (mrbean-bremen and jmcgeheeiv on github) really
  worked with me to test pyfakefs, which resulted in a number of nice
  improvements to TSTL and to differential testing in particular.
  More recently, mrbean-bremen has taken the lead in making TSTL
  compatible with Python 3, which seems to mostly be done now!

- Jakub Wilk helped with modifications to python-afl that made
  TSTL/AFL integration work much better.

- Corey Kosak helped turn this README into something that you might
  actually enjoy reading, and gets to the point much faster than
  previous versions.

\* Do you actually remember that asterisk way up there?  The footnote is that TSTL _is_ a little language.  However, in another sense, it embeds all of Python which makes it pretty big.  It depends on how you think about it.
