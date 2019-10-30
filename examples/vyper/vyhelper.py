from __future__ import print_function
import re
import sys
import vyper.cli.vyper_compile

seen={}
seenExcept = set([])

declaredVars = set([])

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

def handle(e, c):
    if (type(e)) in seenExcept:
        return
    else:
        seenExcept.add(type(e))
        print(c)
        print(e)
def run(c, loud=False):
    if c in seen:
        return seen[c]
    if loud:
        print("RUNNING:")
        print(c)
    with open("vfile.vy", 'w') as vf:
        vf.write(c)
    try:
        vyper.cli.vyper_compile.compile_files(["vfile.vy"], ["bytecode", "abi", "ast", "bytecode_runtime"])
    except vyper.exceptions.StructureException as e:
        handle(e, c)
    except vyper.exceptions.NonPayableViolationException as e:
        handle(e, c)
    except vyper.exceptions.InvalidLiteralException as e:
        handle(e, c)
    except vyper.exceptions.TypeMismatchException as e:
        handle(e, c)
    except vyper.exceptions.ParserException as e:
        handle(e, c)
    except SyntaxError as e:
        handle(e, c)
    seen[c] = True
    return True

def indent4(code):
    c = code.split("\n")
    newc = ""
    for line in c:
        newc += "    " + line + "\n"
    return newc
