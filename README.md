TSTL: the Template Scripting Testing Language
===========================================

TSTL is a "little"* language that makes it easy to test software.  This
implementation targets Python.  There is also a (beta) Java version,
at https://github.com/flipturnapps/TSTL-Java.

TSTL produces a simple, universal interface for test generators to use
-- it essentially turns a definition of valid tests into a graph of system states with test actions as the transitions; you, the tester, can largely ignore this, and view TSTL as a testing tool supporting test generation, test replay, test reduction, and code coverage analysis, with some sophisticated additions to pure random testing to provide effective testing.

TSTL is not purely an academic toy: it's been used to find (and, thus, usually, fix) 
real faults in real code, including ESRI's ArcPy (http://desktop.arcgis.com/en/arcmap/latest/analyze/arcpy/what-is-arcpy-.htm), sortedcontainers (https://github.com/grantjenks/sorted_containers),
gmpy2 (https://github.com/aleaxit/gmpy), sympy (http://www.sympy.org/en/index.html), pyfakefs (https://github.com/jmcgeheeiv/pyfakefs),
Python itself (https://bugs.python.org/issue27870), and even OS X.

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

For more details on TSTL, the best starting point is a comprehensive
journal paper in STTT:
https://github.com/agroce/tstl/blob/master/doc/papers/STTTjournal/maintstl.pdf.
There are also NASA Formal Methods (NFM) and International Symposium
on Software Testing and Analsysis (ISSTA) 2015 papers at
http://www.cefns.nau.edu/~adg326/nfm15.pdf and
http://www.cefns.nau.edu/~adg326/issta15.pdf, with some implementation
details or concepts that are not present in the more up-to-date and
complete paper.  There is a more recent paper descrbing the "normalization"
idea in more detail, http://www.cefns.nau.edu/~adg326/issta17.pdf, as well as a
tool paper describing how to use TSTL's test manipulation commands 
(http://www.cefns.nau.edu/~adg326/issta17tool.pdf).

The NFM and ISSTA papers use an early version of TSTL syntax, which marks
pools and TSTL constructs with % signs.  "Modern" TSTL uses <> by
default, though if for some reason you need <> in your code (and to
prepare for a future C++ version) this can be turned off and only % supported.

Note that documentation below is preliminary.  A better guide to usage
might be to examine the examples directory and see real TSTL test
harnesses.  The generators directory includes some simple but useful
testing tools for finding bugs in systems defined in TSTL.  Only the
random tester is extensively tested and supports all TSTL features
well at this point.  Reading src/randomtester.py provides
considerable guidance in how to (efficiently) use TSTL in a generic
testing tool, with TSTL providing an interface to the underlying
application/library to be tested.

Installation
------------

You can grab a recent (but not always the latest) tstl most easily using pip.  `pip install tstl` should work fine.  If you want something even more recent you can:

    git clone https://github.com/agroce/tstl.git
    cd tstl
    python setup.py install
    # Might need to do a sudo on the last step if not using virtualenv

Note that TSTL expects a Python 2.7 version, is developed/tested that way, and is not well-tested yet with Python 3.0+.
However, in theory it should work ok, thanks to mrbean-bremen.  Also, you probably want to
install (pip will do the trick) Ned Batchelder's coverage.py
(https://coverage.readthedocs.io).  Feel free to be careful and use virtualenv or whatever.  If you're planning to test anything that touches the filesystem, or might touch the filesystem, or could do bad things if you found a nasty bug, I suggest using a virtual machine for testing, in fact.

The documentation below is preliminary, generated by some early
adapters of TSTL, and may not perfectly match the current version.
Use at your own risk.  Code in examples directories should be up to
date.

Using TSTL
------------

TSTL installs a few standard tools: the TSTL compiler itself, `tstl` (technically all
you really need to do something useful); a random test generator
`tstl_rt`; a tool for producing standalone tests, `tstl_standalone`;
a tool for replaying TSTL test files `tstl_replay`; a tool for
delta-debugging and normalization of TSTL tests, `tstl_reduce`; and a tool for running a set of tests as a regression, `tstl_regress`.  The
`tstl_reduce` tool is not essential, since the random tester performs
delta debugging and alpha conversion by default (you have to add
`--normalize` to also get normalization of tests, however).

The simplest usage is to go to a directory with a .tstl file, and
type:

    tstl mytstlfile.tstl
    tstl_rt

The first line compiles mytstlfile.tstl and produces sut.py, which the
random tester will automatically import and test.  Both tstl and the
random tester take a variety of command line options, which --help
will show.

Example
-----

The easiest way to understand TSTL may be to examine
examples/AVL/avlnew.tstl (https://github.com/agroce/tstl/blob/master/examples/AVL/avlnew.tstl), which is a simple example file in the latest
language format (easier to read) (the file avlblocks.tstl has this
same harness in a different format).

These are pretty full-featured testers for an AVL tree class.  You can
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
AVL tree implementation testing:  `int` and `avl`.   We define (in
Python, almost) how to create these things, and what we can do with
these things, and then TSTL produces sequences that match our
definition.  It also checks that all AVL trees, at all times, are
properly balanced.  If we wanted, as in avlnew.tstl, we could also
make sure that our AVL tree "acts like" a set --- when we insert
something, we can find that thing, and when we delete something, we
can no longer find it.

Note that we start with "raw Python" to import the avl module, the SUT.  While TSTL
supports using from, aliases, and wildcards in imports, you should always
import the module(s) under test with a simple import.  This allows TSTL to identify
the code to be tested and automatically provide coverage, static analysis-aided
testing methods, and proper module management.  Utility code in the standard library,
on the other hand, can be imported any way you wish.

If we test this (or avlnew.tstl) for 30 seconds, something like this will appear:

~/tstl/examples/AVL$ tstl_rt --timeout 30

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
http://www.cefns.nau.edu/~adg326/issta12.pdf).

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
not require TSTL itself.

    ~/tstl/examples/AVL$ tstl_rt --timeout 30 --output failure.test
    Random testing using config=Config(swarmSwitch=None, verbose=False, fastQuickAnalysis=False, failedLogging=None, maxtests=-1, greedyStutter=False, exploit=None, seed=None, generalize=False, localize=False, uncaught=False, speed='FAST', internal=False, normalize=False, highLowSwarm=None, replayable=False, essentials=False, quickTests=False, coverfile='coverage.out', uniqueValuesAnalysis=False, swarm=False, ignoreprops=False, total=False, swarmLength=None, noreassign=False, profile=False, full=False, multiple=False, relax=False, swarmP=0.5, stutter=None, running=False, compareFails=False, nocover=False, swarmProbs=None, gendepth=None, quickAnalysis=False, exploitCeiling=0.1, logging=None, html=None, keep=False, depth=100, throughput=False, timeout=30, output=None, markov=None, startExploit=0)
    ...
    ~/tstl/examples/AVL$ tstl_reduce failure.test failure_norm.test
    REDUCING...
    ...
    NORMALIZING...
    ...
    ~/tstl/examples/AVL$ tstl_standalone failure_norm.test failure.py
    ~/tstl/examples/AVL$ python failure_small.py
    Traceback (most recent call last):
      File "failure.py", line 98, in <module>
        check()
      File "failure.py", line 45, in check
        assert avl2.check_balanced()
    AssertionError

The final useful hint for getting started is that sometimes you may want to test something
(for example, a library implemented in C) where failing tests crash the Python interpreter.  This is possible,
but requires some effort.  First, run `tstl_rt` with the `--replayable` option.  This causes the generator to
keep a file, currtest.test, in the directory you are running testing in: this file holds the current test.  If the random tester crashes, this will include the action that caused the crash.  In a few rare cases, the behavior of past tests is also relevant to a crash (reloading the module does not really reset state of the system -- e.g., interacting with hardware).  For these cases, use `--total` and look at the file fulltest.test, which contains ALL actions ever performed by the random tester.

The currtest.test and fulltest.test files work just like normal TSTL files, and can be replayed with the replay utility or turned into standalone files.  However, for test reduction and normalization to work correctly, they must be reduced by passing the `--sandbox` argument to `tstl_reduce`.

What about tests that fail by entering an infinite loop?  The same technique as is used for crashes works.  However, you need to run `tstl_rt` with a time limit (using ulimit if you are on UNIX-like systems, for example).  The `tstl_reduce` utility provides a `--timeout` argument to handle such tests, but this only works on systems supporting ulimit, for now.  In very rare cases, you might have a test execution lock up because, for example, the failure causes a read from standard input.  If you hit this, contact me.

Finally, how do you integrate TSTL testing with more conventional approaches, e.g., pytest?  The file `test_tstl_regressions.py` in the examples directory shows one way.  If you add all your TSTL tests of interest to a `tstl_tests` directory under the directory where `sut.py` lives, you can make pytest run all your TSTL tests.  Perhaps more interestingly, this file also wraps a simple caller that forces 60 seconds of random testing to be executed by pytest, as a sanity check.  You can tweak the configuration of the random testing easily -- often, adding "--swarm" is a good idea.

Hints for Better Testing
-----

Sometimes just doing `tstl_rt` or even `tstl_rt --swarm` isn't enough.  There are other options for improving testing.  A particularly powerful one in many cases is using the size of functions in terms of lines-of-code to guide testing.  To do this, you first let TSTL determine the sizes:

`tstl_rt --generateLOC sut.loc --timeout 120`

Then you use that generated file to guide testing:

`tstl_rt --biasLOC sut.loc`

It's also a good idea, for faster testing (since the power of random testing is partly in generating huge numbers of tests every minute), to turn off code coverage collection with `--noCover`.  This isn't so great if you are looking to see if your tests cover your code well, but for pedal-to-the-metal bug-hunting, it is often the way to go.

You can also try a "genetic algorithms" approach guided by coverage, that exploits "high coverage" tests:

`tstl_rt --exploit 0.8 --Pmutate 0.5`

Adding `--reducePool` sometimes also improves the performance of this method.

You can tune the exploit and mutate parameters to see if they improve results.  You can even combine lines-of-code bias with the `exploit` approach and/or swarm testing.  Sometimes testing benefits from having all three!  Unfortunately, using `--exploit` does mean you can't get away with `--noCover` to avoid the overhead of computing code coverage.

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

- My (Alex's) other graduate students (Amin Alipour, Rahul Gopinath, Arpit Christi, Chaoqiang Zhang, Shalini Shamasunder) and almost-mine graduate student (Iftekhar Ahmed) contributed to the general intellectual climate in which TSTL was born.

- Students in CS 499 at Northern Arizona University and CS 362, 562, and 569 at Oregon State University contributed a lot of ideas, and a few concrete language/tool changes or bug reports.  These are too numerous to mention, and in some cases I don't recall who asked "why do you do it that stupid way?" in class, and got me thinking that it was in fact a stupid way to do things.

- Ned Batchelder, David R. MacIver, and John Regehr have no actual code in TSTL, but all contributed in significant ways to various implementation aspects, in ways that go beyond the general disclaimer that TSTL freely steals from the entire software testing (research) community.

- The pyfakefs team (mrbean-bremen and jmcgeheeiv on github) really worked with me to test pyfakefs, which resulted in a number of nice improvements to TSTL and to differential testing in particular.  More recently, mrbean-bremen has taken the lead in making TSTL compatible with Python 3, which seems to mostly be done now!




\* Do you actually remember that asterisk way up top?  The footnote is that TSTL _is_ a little language.  However, in another sense, it embeds all of Python which makes it pretty big.  It depends on how you think about it.
