from __future__ import print_function
import re
import sys
import os
import vyper.cli.vyper_compile

seen={}
seenExcept = set([])

declaredVars = set([])

known = ["Exception('Not an integer type: {typ}')",
         "Exception('Invalid break')",
         "KeyError('self')",
         """ValueError("Unsupported format type 'ast'")""",
         """TypeError("'<=' not supported between instances of 'int' and 'str'")"""]

def fid(functionDef):
    start = functionDef.find("def ")
    end = functionDef.find("(")
    return functionDef[start+4:end]

def vid(varDef):
    return varDef[:varDef.find(":")]

def declareVar(varDef):
    declaredVars.add(vid(varDef))
    return varDef

def declared(var):
    return var in declaredVars

compileCount = 0
HOW_OFTEN = 10

def run(c, loud=False, silent=True):
    global compileCount

    if c in seen:
        return seen[c]
    if loud:
        print("RUNNING:")
        print(c)
    elif (not silent) and ((compileCount % HOW_OFTEN) == 0):
        print("COMPILE #" + str(compileCount))
        print(c)
    compileCount += 1

    vname =  "vfile." + str(os.getpid()) + ".vy"

    with open(vname, 'w') as vf:
        vf.write(c)
    with open(os.devnull, 'w') as dnull:
        oldstdout = sys.stdout
        oldstderr = sys.stderr
        sys.stdout = dnull
        sys.stderr = dnull
        raised = None
        try:
            vyper.cli.vyper_compile.compile_files(
                [vname],
                ["bytecode", "abi", "ast", "bytecode_runtime"])
        except vyper.exceptions.ParserException:
            raised = None # just ignore these!
        except SyntaxError:
            raised = None # just ignore these!
        except ZeroDivisionError:
            raised = None # just ignore these!
        except Exception as e:
            raised = repr(e)
        finally:
            sys.stdout = oldstdout
            sys.stderr = oldstderr
    if (raised is not None) and (raised not in known):
        print("="*80)
        print("COMPILING:")
        print(c)
        print("RAISED:", raised)
        print("="*80)
        seen[c] = False
        return False
    seen[c] = True
    return True

def indent4(code):
    c = code.split("\n")
    newc = ""
    for line in c:
        newc += "    " + line + "\n"
    return newc
