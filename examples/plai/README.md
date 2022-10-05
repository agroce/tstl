This harness requires Racket 7.2 to be installed on a mac.

It is a simple example of finding a bug in a programming language via
differential testing, based on the code in Chapter 6 of the 2nd edition
of Shriram Krishnamurthi's <i>Programming Languages: Application and
Interpretation</i> (https://cs.brown.edu/courses/cs173/2012/book/From_Substitution_to_Environments.html).  This is from CS 396 at NAU, Fall 2022.

Below is the end of a run that took about half an hour to find and reduce an example of the bug.  Note that the generator only produces a small subset of the
ExprC language.  In class we did a case analysis showing any difference between substitution and environment implementations (and static vs dynamic scoping) had to be due to function application.  I "moved the proof into the test" if you will.  No idea how long a run with everything would take -- a very long time, and it'd introduce expression size explosion.

```
================================================================================
TEST# 0
  (appC 'f (numC -3))
  (fdC 'f 'y (appC 'g (numC -3))) (fdC 'g 'x (idC 'y))
raco test: "test.rkt"

bad i_result at line 81

  expected: -987654321

  given: -3



REDUCED IN 290.68113112449646 SECONDS
Alpha converting test...
fid0 = "'f"                                                              # STEP 0
int0 = str(-3)                                                           # STEP 1
id0 = "'y"                                                               # STEP 2
fid1 = "'f"                                                              # STEP 3
expr0 = "(numC " + int0 + ")"                                            # STEP 4
expr1 = "(numC " + int0 + ")"                                            # STEP 5
expr2 = "(appC " + fid0 + " " + expr1 + ")"                              # STEP 6
fid0 = "'g"                                                              # STEP 7
id1 = "'x"                                                               # STEP 8
expr1 = "(appC " + fid0 + " " + expr0 + ")"                              # STEP 9
expr3 = "(idC " + id0 + ")"                                             # STEP 10
fd0 = "(fdC " + fid0 + " " + id1 + " " + expr3 + ")"                    # STEP 11
fd1 = "(fdC " + fid1 + " " + id0 + " " + expr1 + ")"                    # STEP 12
fds0 = fd0                                                              # STEP 13
fds1 = fd1 + " " + fds0                                                 # STEP 14
assert(plai.test(expr2, fds1))                                          # STEP 15

SAVING TEST AS failure.84369.test
FINAL VERSION OF TEST, WITH LOGGED REPLAY:
fid0 = "'f"                                                              # STEP 0
ACTION: fid0 = "'f" 
fid0 = None : <class 'NoneType'>
=> fid0 = "'f" : <class 'str'>
==================================================
int0 = str(-3)                                                           # STEP 1
ACTION: int0 = str(-3) 
int0 = None : <class 'NoneType'>
=> int0 = '-3' : <class 'str'>
==================================================
id0 = "'y"                                                               # STEP 2
ACTION: id0 = "'y" 
id0 = None : <class 'NoneType'>
=> id0 = "'y" : <class 'str'>
==================================================
fid1 = "'f"                                                              # STEP 3
ACTION: fid1 = "'f" 
fid1 = None : <class 'NoneType'>
=> fid1 = "'f" : <class 'str'>
==================================================
expr0 = "(numC " + int0 + ")"                                            # STEP 4
ACTION: expr0 = "(numC " + int0 + ")" 
expr0 = None : <class 'NoneType'>
int0 = '-3' : <class 'str'>
=> expr0 = '(numC -3)' : <class 'str'>
==================================================
expr1 = "(numC " + int0 + ")"                                            # STEP 5
ACTION: expr1 = "(numC " + int0 + ")" 
expr1 = None : <class 'NoneType'>
int0 = '-3' : <class 'str'>
=> expr1 = '(numC -3)' : <class 'str'>
==================================================
expr2 = "(appC " + fid0 + " " + expr1 + ")"                              # STEP 6
ACTION: expr2 = "(appC " + fid0 + " " + expr1 + ")" 
expr1 = '(numC -3)' : <class 'str'>
expr2 = None : <class 'NoneType'>
fid0 = "'f" : <class 'str'>
=> expr2 = "(appC 'f (numC -3))" : <class 'str'>
==================================================
fid0 = "'g"                                                              # STEP 7
ACTION: fid0 = "'g" 
fid0 = "'f" : <class 'str'>
=> fid0 = "'g" : <class 'str'>
==================================================
id1 = "'x"                                                               # STEP 8
ACTION: id1 = "'x" 
id1 = None : <class 'NoneType'>
=> id1 = "'x" : <class 'str'>
==================================================
expr1 = "(appC " + fid0 + " " + expr0 + ")"                              # STEP 9
ACTION: expr1 = "(appC " + fid0 + " " + expr0 + ")" 
expr0 = '(numC -3)' : <class 'str'>
expr1 = '(numC -3)' : <class 'str'>
fid0 = "'g" : <class 'str'>
=> expr1 = "(appC 'g (numC -3))" : <class 'str'>
==================================================
expr3 = "(idC " + id0 + ")"                                             # STEP 10
ACTION: expr3 = "(idC " + id0 + ")" 
expr3 = None : <class 'NoneType'>
id0 = "'y" : <class 'str'>
=> expr3 = "(idC 'y)" : <class 'str'>
==================================================
fd0 = "(fdC " + fid0 + " " + id1 + " " + expr3 + ")"                    # STEP 11
ACTION: fd0 = "(fdC " + fid0 + " " + id1 + " " + expr3 + ")" 
expr3 = "(idC 'y)" : <class 'str'>
fd0 = None : <class 'NoneType'>
id1 = "'x" : <class 'str'>
fid0 = "'g" : <class 'str'>
=> fd0 = "(fdC 'g 'x (idC 'y))" : <class 'str'>
==================================================
fd1 = "(fdC " + fid1 + " " + id0 + " " + expr1 + ")"                    # STEP 12
ACTION: fd1 = "(fdC " + fid1 + " " + id0 + " " + expr1 + ")" 
expr1 = "(appC 'g (numC -3))" : <class 'str'>
fd1 = None : <class 'NoneType'>
id0 = "'y" : <class 'str'>
fid1 = "'f" : <class 'str'>
=> fd1 = "(fdC 'f 'y (appC 'g (numC -3)))" : <class 'str'>
==================================================
fds0 = fd0                                                              # STEP 13
ACTION: fds0 = fd0 
fd0 = "(fdC 'g 'x (idC 'y))" : <class 'str'>
fds0 = None : <class 'NoneType'>
=> fds0 = "(fdC 'g 'x (idC 'y))" : <class 'str'>
==================================================
fds1 = fd1 + " " + fds0                                                 # STEP 14
ACTION: fds1 = fd1 + " " + fds0 
fd1 = "(fdC 'f 'y (appC 'g (numC -3)))" : <class 'str'>
fds0 = "(fdC 'g 'x (idC 'y))" : <class 'str'>
fds1 = None : <class 'NoneType'>
=> fds1 = "(fdC 'f 'y (appC 'g (numC -3))) (fdC 'g 'x (idC 'y))" : <class 'str'>
==================================================
assert(plai.test(expr2, fds1))                                          # STEP 15
ACTION: assert(plai.test(expr2, fds1)) 
expr2 = "(appC 'f (numC -3))" : <class 'str'>
fds1 = "(fdC 'f 'y (appC 'g (numC -3))) (fdC 'g 'x (idC 'y))" : <class 'str'>
================================================================================
TEST# 0
  (appC 'f (numC -3))
  (fdC 'f 'y (appC 'g (numC -3))) (fdC 'g 'x (idC 'y))
raco test: "test.rkt"

bad i_result at line 81

  expected: -987654321

  given: -3



RAISED EXCEPTION: <class 'AssertionError'> 
ERROR: (<class 'AssertionError'>, AssertionError(), <traceback object at 0x7fa2c0396870>)
TRACEBACK:
  File "/Users/adg326/tstl/examples/plai/sut.py", line 72693, in safely
    act[2]()
  File "/Users/adg326/tstl/examples/plai/sut.py", line 59435, in act1051
    assert(plai.test(self.p_expr[2], self.p_fds[1]))
STOPPING TESTING DUE TO FAILED TEST
83.96946564885496 PERCENT COVERED
1608.414703130722 TOTAL RUNTIME
61 EXECUTED
60204 TOTAL TEST OPERATIONS
1278.8366403579712 TIME SPENT EXECUTING TEST OPERATIONS
4.818864107131958 TIME SPENT EVALUATING GUARDS AND CHOOSING ACTIONS
0.03136038780212402 TIME SPENT CHECKING PROPERTIES
1278.8680007457733 TOTAL TIME SPENT RUNNING SUT
0.5232856273651123 TIME SPENT RESTARTING
290.7016530036926 TIME SPENT REDUCING TEST CASES
98 BRANCHES COVERED
```