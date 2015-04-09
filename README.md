tstl: A template scripting testing language
===========================================

TSTL is a langauge that greatly simplifies testing a system using multiple testing approaches and generating a test harness quickly.
It simplifies the definition of system under test.

TSTL is based on the research done by [Dr. Alex Groce](http://eecs.oregonstate.edu/people/groce-alex) and Jervis Pinto. School of Electrical Engineering and Computer Science, Oregon State University. The origial code can be found here: [harness-maker](https://code.google.com/p/harness-maker/). TSTL was taught in `CS562 Applied Softwre Engineering` Winter 2015 (at Oregon State University). The current repository packages the original code into a python package so that it can be installed easily and used conveniently by the name `tstl`

There is not much documentation yet but that should change soon.

`harnessmaker.py` is renamed as `tstl` and once package is installed there is no need to write `python harnessmaker.py`.
You can simply use `tstl` instead.


Installation
------------


    git clone https://github.com/pramttl/tstl.git
    cd tstl
    python setup.py install
    # Might need to do a sudo on the last step if not using virtualenv


Definitions
-----------

### ACT file definitions
------------

#### tstl variable

Any valid python identifier with a % before and after it.

####tstl keywords or types

* pool:
* source:
* reference:
* compare:

####literal code

Any code that is specified between `<@` .. `@>`. There could be multi-line literal code. Single line literal code is a line preceded by an `@`.
This code is maintained as is in the generated target file i.e. **sut.py** by default. The `<@`  `@>` pair are called TSTL literal tags.

####action line

Any line that doesn’t start with a TSTL keyword and is not literal code.

#### pool variable

Any variable that is declared using the pool keyword. E.g: `pool: %N% 2`. This means there are 2 %N%’s `p_N[0]` and `p_N[1]`. For each pool varaible a pool range must be defined which is the range of values which the pool varaible can take.

Example:

	`%N% := %[1..10]%`

This implies %N% can take values 1, 2 .. 10. If N can take more values other than integers then the assignment must be done over multiple lines.

Example:  

	%N% := "foo"
	%N% := "bar"
	%N% := %[1..3]%

This means %N% can take the values: "foo", "bar", 1, 2, 3


#### pool variable with a REF

(Or simply a REF varaible)

If a pool variable at the time of its TSTL declaration can be defined with a REF keyword. Example:

	pool: %N% 2 REF

**REF** tells that this is a reference variable. This means that a `reference` statement must be defined in a way such that each action line consuming a **REF variable** has a reference action line. The lines on which pool variables with a reference are defined are called **refdef** lines i.e. reference-variable-definition lines.


#### varef line

(Varaiable Reference line)

A line which uses a REF variable. Varef lines have to be action lines.

	pool: %GAME% 1 REF						# This is refdef line
	%GAME% := g1							# This is a varef line
	%GAME%.start()							# This is also a varef line

#### reference line

Any line that uses the `reference` keyword is a reference line.

	reference: function1 ==> function2

When TSTL parser encounters this line, then for each action line that uses a REF variable, a reference action line is created where `funtion1` is replaced by `function2` if and only if **function1** exists in that line. Currently TSTL does a regex replace. So **function1** can be any regular expression and **function2** is the word that replaces it.


#### compare line

This line is a very important line from testing perspective. It is basically the assert line which compares the output of an **action** to it's **reference action**.

E.g.:

	compare: function1

**function1** tells the TSTL parser that for every action that contains the word **function1** within it, do a comparison of the output with the correspoding reference action. If a reference action for that line does not exisit TSTL will not be able to generate the SUT. Thus appropriate **compare** and **reference** lines must coexisit and work in harmony.

**Note**: REF, reference and compare can be catchy. All 3 are dependent on each other.

### SUT definitions
------------

#### action tuple

(name, guard, action)

Action tuple is a 3-tuple that contains the name of the action, the guard and the action method.

##### action

Simply put:

action_tuple[2] is the action. An action is basically a function and it can be called like:

    action()

Doing so, invokes the action.


### SUT API methods
------------

The following API functions are available on the generated SUT.

	t = sut.t()


#### t.enabled()

Return all the enabled action tuples of the SUT. All actions are not enabled by default. TSTL generates an SUT that imposes restrictions on which actions are enabled and which are disabled. If a varaible has not been defined yet (i.e. has not been assigned a value yet) then any action that consumes that variable will be disabled. This is one of the key ideas of TSTL.

Each action has a guard that checks whether that action is enabled.

#### t.check()

Checks if all properties are correct. So the assertion check does not happen magically. In the code where we test our SUT we have to call.

#### t.actions()

Return all the action tuples of the SUT irrespective of whether it is enabled or not.


Usage
-----

    tstl -a <action_file_name>

This will generate a file called `sut.py` which is the System Under Test.

Correctly not much user documentation is available for TSTL. For details please refer to this [paper](http://www.cs.cmu.edu/~agroce/nfm15.pdf).


Developer Info
--------------

There are no developer docs yet which will hopefully change in future. TSTL package includes simple unit tests to test modules within `tstl/src/harnessmaker.py`, which is the main file that makes up most of the TSTL langauge. Once you clone the repository to run the tests do the following:

    python test/unit_tests.py

Writing tests for TSTL is currently work in progress. But we know that testing everything is important, even if it is testing the code for a langauge for testing.

