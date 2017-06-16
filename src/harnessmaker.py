# harnessmaker.py -- TSTL core language
# Core code by Alex Groce (http://www.cs.cmu.edu/~agroce), 2013-2015
# Additional features by Jervis Pinto, Pooria Azimi, and Pranjal Mittal
# Research performed at Oregon State University, Corvallis, Oregon
# See NASA Formal Methods 2015 paper, "A Little Language for Testing" for
# core concepts behind TSTL; note language definition has changed, however.

import sys
import argparse
import os
import re
from collections import namedtuple

# For packaging harnessmaker to tstl package
import pkg_resources

############## GLOBAL VARIABLES #############
# These variables will be modified when needed

config = None
poolSet = {}
poolType = {}
initSet = []
finallySet = []
firstInit = True
baseIndent = ""
poolPrefix = None
genCode = None
originalCode = {}
#############################################

def parse_args():
    """
    To parse command line arguments. Makes use of built-in python library argprase
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('tstl', metavar='filename', type=str, default=None,
                        help='Path to the .tstl file.')
    parser.add_argument('-v', '--version', action='store_true',
                        help='Display the tstl version.')    
    parser.add_argument('-o', '--output', type=str, default="sut.py",
                        help='Name of the file containing the generated harness code (default = sut.py)')
    parser.add_argument('-c', '--classname', type=str, default='sut',
                        help='Name of the class representing the SUT (default = sut)')
    parser.add_argument('-n', '--noCover', action='store_true',
                        help='Disable generating coverage collection support.  Faster testing, but no coverage info!')
    parser.add_argument('-r', '--coverReload', action='store_true',
                        help='Generate coverage for module reload behavior.')
    parser.add_argument('-i', '--coverInit', action='store_true',
                        help='Generate coverage for SUT initialization behavior.')
    parser.add_argument('-e', '--enumerateEnabled', action='store_true',
                        help='Enumerate enabled actions instead of trying to find one, useful when |actions| typically >> |enabled|.')    
    parser.add_argument('-R', '--defaultReplay', action='store_true',
                        help='Backtracking defaults to replay method.')
    parser.add_argument('-a', '--ignoreAngles', action='store_true',
                        help='Do not use angle brackets as TSTL markers, for use with some languages.')
    parser.add_argument('-s', '--stats', action='store_true',
                        help='Enable statistics on each action.  Slows exection considerably.')
    parser.add_argument('-p', '--pylib', action='store_true',
                        help='Add if you need to test something in the standard Python library.  Will blow up coverage!')            

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
    Config(output='sut.py', classname='sut', noCover=False, tstl='yourfile.tstl',
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
    
def preprocess_angle_brackets(line):
    if config.ignoreAngles:
        return line
    repLine = line.replace("<[","%[")
    repLine = repLine.replace("]>","]%")
    repLine = repLine.replace("<,[","%,[")
    repLine = repLine.replace("],>","],%")        
    repLine = repLine.replace("PRE<","pre<")
    prePos = repLine.find("pre<(")
    while prePos != -1:
        repLine = repLine.replace("pre<(","PRE%(",1)
        closePos = repLine.find(")>",prePos)
        repLine = repLine[0:closePos] + ")%" + repLine[closePos+2:]
        prePos = repLine.find("pre<(")
    newLine = ""
    sawLeft = False
    alphaNumeric = ""
    for c in repLine:
        if sawLeft:
            if (c.isalnum()) or (c == ","):
                alphaNumeric += c
            elif c == ">":
                newLine += "%" + alphaNumeric + "%"
                sawLeft = False
            else:
                newLine += "<" + alphaNumeric + c
                sawLeft = False
        else:
            if c == "<":
                alphaNumeric = ""
                sawLeft = True
            else:
                newLine += c
    return newLine
            

def parse_import_line(line):
    """
    Parses an import line in the raw python code.
    Input --> Output (Example)
    :
    :    "from math import sqrt" --> ['sqrt']
    :
    """
    global import_froms
    global need_imports
    
    #print "IMPORT:",line
    raw = line.split('import ')
    if "from " in line:
        import_froms.append(line)
        return []
        #return [line.split()[1]]
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
        if ' as ' in si:
            ts = si.split(' as ')
            assert len(ts) == 2, 'Parse error on "as" during import of {}'.format(name)
            name = ts[1].rstrip()  # remove the trailing newline or whitespace if any
        else:
            name = si.rstrip()
        mod_names.append(name)
    assert len(mod_names) > 0
    return mod_names

def expandPool(original,trackOriginal=False):
    """
    Expand pool references
    """
    newVersion = []
    for c in original:
        if trackOriginal:
            oldCode = originalCode[c]
        for p in poolSet:
            if poolSet[p] == 1:
                pexpr = p + " [0]"
            else:
                pexpr = p + " [%[0.." + str(poolSet[p]-1) + "]%]"
            c = c.replace(p, pexpr)
        if trackOriginal:
            originalCode[c] = oldCode
        newVersion.append(c)
    return newVersion


def expandRange(original,trackOriginal=False):
    """
    Expand all range expressions
    """
    current = original
    anyChanged = True
    while anyChanged:
        anyChanged = False
        newVersion = []
        for c in current:
            if trackOriginal:
                oldCode = originalCode[c]
            if "%,[" in c:
                anyChanged = True
                lpos = c.find("%,[")
                endpos = c.find("],%",lpos)
                rexp = c[lpos:endpos+3]
                ilist = c[lpos+3:endpos].split(",,")
                for i in ilist:
                    if trackOriginal:
                        originalCode[c.replace(rexp, i, 1)] = oldCode
                    newVersion.append(c.replace(rexp, i, 1))                
            elif "%[" in c:
                anyChanged = True
                lpos = c.find("%[")
                endpos = c.find("]%",lpos)
                dotpos = c.find("..",lpos)
                commapos = c.find(",",lpos)
                rexp = c[lpos:endpos+2]
                if (dotpos != -1) and (dotpos < endpos):
                    if c[lpos+2] == "'": # must be 'a'..'b' etc.
                        lowc = c[lpos+3:dotpos-1]
                        highc = c[dotpos+3:endpos-1]
                        for x in xrange(ord(lowc),ord(highc)+1):
                            if trackOriginal:
                                originalCode[c.replace(rexp, "'" + chr(x) + "'", 1)] = oldCode
                            newVersion.append(c.replace(rexp, "'" + chr(x) + "'", 1))
                    else:
                        low = int(c[lpos+2:dotpos])
                        high = int(c[dotpos+2:endpos])
                        for x in xrange(low,high+1):
                            if trackOriginal:
                                originalCode[c.replace(rexp, str(x), 1)] = oldCode
                            newVersion.append(c.replace(rexp, str(x), 1))
                elif (commapos != -1) and (commapos < endpos):
                    ilist = c[lpos+2:endpos].split(",")
                    for i in ilist:
                        if trackOriginal:
                            originalCode[c.replace(rexp, i, 1)] = oldCode
                        newVersion.append(c.replace(rexp, i, 1))
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
            if trackOriginal:
                originalCode[line] = originalCode[newVersion[index]]
            newVersion[index] = line

    return newVersion

def replaceRefs(str):
    newStr = str
    for p in poolSet:
        if p in refSet:
            pRaw = poolPrefix + p.replace("%","")
            newStr = newStr.replace("REF:" + pRaw, pRaw+"_REF")
    return newStr

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


def prettyName(pools, name):
    newName = name
    for pn in pools:
        p = poolPrefix + pn.replace("%","")
        pfind = newName.find(p+"[")
        while pfind != -1:
            closePos = newName.find("]",pfind)
            index = newName[newName.find("[",pfind)+1:closePos]
            access = newName[pfind:newName.find("]",pfind)+1]
            newAccess = p.replace(poolPrefix,"") + index                
            newName = newName.replace(access, newAccess)
            pfind = newName.find(p+"[")
    return newName

def genInitialization():
    """
    Generate initialization from configuration, poolSet
    """
    global firstInit, import_modules
    genCode.append(baseIndent + "self.__test = []\n")
    genCode.append(baseIndent + "self.__failure = None\n")
    genCode.append(baseIndent + "self.__warning = None\n")
    for p in poolSet:
        s = baseIndent
        s += poolPrefix + p.replace("%","") + " = {}"
        genCode.append(s + "\n")
        s = baseIndent
        s += poolPrefix + p.replace("%","") + "_used = {}"
        genCode.append(s + "\n")
        for x in xrange(0,poolSet[p]):
            s = baseIndent
            s += poolPrefix + p.replace("%","") + "[" + str(x) + "] = None"
            genCode.append(s + "\n")    
            s = baseIndent
            s += poolPrefix + p.replace("%","") + "_used[" + str(x) + "] = True"
            genCode.append(s + "\n")
    if (not config.noCover) and config.coverInit:
        genCode.append(baseIndent + "if self.__collectCov: self.__cov.start()\n")
    if firstInit:
        genCode.append("# BEGIN INITIALIZATION CODE\n")
    for i in initSet:
        s = baseIndent
        s += i
        genCode.append(s)
    if firstInit:
        genCode.append("# END INITIALIZATION CODE\n")
        firstInit = False    
    if (not config.noCover) and config.coverInit:
        genCode.append(baseIndent + "if self.__collectCov: self.__cov.stop()\n")        
        genCode.append(baseIndent + "if self.__collectCov: self.__updateCov()\n")


def main():
    
    global config
    global import_froms
    global import_modules
    global ignoredExcepts
    global poolSet
    global refSet
    global poolType
    global initSet
    
    global finallySet
    global constSet
    global opaqueSet
    global absSet
    global firstInit
    global baseIndent
    global poolPrefix
    global genCode
    global originalCode

    baseIndent = "    "

    if "-v" in sys.argv or "--version" in sys.argv:
        print "TSTL, version 1.0.10"
        print "Documentation at https://github.com/agroce/tstl"
        sys.exit(0)
        

    
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
    outf.write("import inspect\n")    
    outf.write("import re\n")
    outf.write("import sys\n")
    outf.write("import time\n")
    outf.write("import os.path\n")        
    outf.write("from itertools import chain, combinations\n")    

    if not config.noCover:
        outf.write("import coverage\n")

    outf.write("# BEGIN STANDALONE CODE\n")
        
    code = []
    import_modules = []             # We will call reload on these during restart
    import_froms = []
    inside_literal_block = False    # To check whether we are inside raw python code
    
    inside_function = False         # Are we inside a function def, so need to consider PRE?
    function_code = []
    anyPre = False
    continuedLine = False
    contLine = ""
    origContLine = ""

    with open(config.tstl, 'r') as fp:
        for l in fp:
            fileLine = str(l).replace("\r","")
            l = preprocess_angle_brackets(l)
            if l[-1] != "\n":
                l += "\n"
            l = l.replace("\r","")
            if len(l)>1:
                if l[-2] == "'":
                    l = l[:-1] + ' ' + "\n"
                if l[-2] == "\\":
                    continuedLine = True
                    origContLine += fileLine[:-2]
                    contLine += l[:-2]
                    continue
                elif continuedLine:
                    l = contLine + l
                    fileLine = origContLine + fileLine
                    contLine = ""
                    origContLine = ""
                    continuedLine = False
            if l[0] == "#":
                continue # COMMENT
            if (l.split() != []) and (l.split()[0][0] == "#"):
                continue # also COMMENT

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
                if "import" in l: #re.match("import ", l):
                    #outf.write(l[:])
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
                    m = re.match(r".*PRE%\((.+)\)%.*",l)
                    while m:
                        anyPRE = True
                        pre_expr = m.groups()[0]
                        spre_expr = "'''" + pre_expr + "'''"
                        l = l.replace("PRE%(" + pre_expr + ")%", "__pre[" + spre_expr + "]", 1)
                        function_code = [(baseIndent + "__pre[" + spre_expr + "] = " + pre_expr + "\n")] + function_code
                        m = re.match(r".*PRE%\((.+)\)%.*",l)
                    function_code.append(l)                    
                else:
                    outf.write(l)
            elif l[0] == "*":       # include action multiple times
                spos = l.find(" ")
                times = int(l[1:spos]) 
                originalCode[l[spos:]] = fileLine 
                for n in xrange(0,times):
                    code.append(l[spos:])
            else:
                originalCode[l] = fileLine[:-1]
                code.append(l)
    if function_code != []:
        if anyPRE:
            outf.write(baseIndent + "__pre = {}\n")
        for fl in function_code:
            outf.write(fl)       

    outf.write("# END STANDALONE CODE\n")
                            
    assert len(code) > 0, 'No non-comment lines found in .tstl file'

    # Build up the pool, initialization values

    poolPrefix = "self.p_"

    sourceSet = []

    initSet = []
    firstInit = True
    propSet = []
    ignoredExcepts = []
    refSet = []
    constSet = []
    opaqueSet = []
    absSet = {}
    compareSet = []
    featureSet = []
    logSet = []
    hintSet = []
    referenceMap = {}
    autoPrefix = ""
    
    # Parse the code to process the "tag lines"
    newCode = []
    noAutoPrefix = ["pools:","actions:","properties:","logs:","inits:","references:","compares:","features:","sources:"]
    
    for c in code:
        fileCode = originalCode[c]
        if config.debug:
            print "CODE:",c
        cs = c.split()
        if cs == []:
            continue
        if (cs[0] not in noAutoPrefix) and (cs[0][0] != "#"):
            c = autoPrefix + c.lstrip()
        cs = c.split()
        if cs[0][0] == "#":
            continue
        elif cs[0] == "pools:":
            autoPrefix = "pool: "
        elif cs[0] == "properties:":
            autoPrefix = "property: "
        elif cs[0] == "logs:":
            autoPrefix = "log: "
        elif cs[0] == "hints:":
            autoPrefix = "hint: "            
        elif cs[0] == "inits:":
            autoPrefix = "init: "
        elif cs[0] == "finallys:":
            autoPrefix = "finally: "            
        elif cs[0] == "references:":
            autoPrefix = "reference: "
        elif cs[0] == "compares:":
            autoPrefix = "compare: "
        elif cs[0] == "features:":
            autoPrefix = "feature: "
        elif cs[0] == "sources:":
            autoPrefix = "source: "
        elif cs[0] == "exceptions:":
            autoPrefix = "exception: "
        elif cs[0] == "actions:":
            autoPrefix = ""                        
        elif cs[0] == "init:":
            initSet.append(c.replace("init: ",""))
        elif cs[0] == "finally:":
            finallySet.append(c.replace("finally: ",""))            
        elif cs[0] == "log:":
            logSet.append(c.replace("log: ",""))
        elif cs[0] == "hint:":
            hintSet.append(c.replace("hint: ",""))            
        elif cs[0] == "property:":
            propSet.append(c.replace("property: ",""))
        elif cs[0] == "exception:":
            ignoredExcepts.append(c.replace("exception: ",""))            
        elif cs[0] == "pool:":
            poolSet[cs[1]] = int(cs[2])
            if (len(cs)>3) and ("REF" in cs):
                refSet.append(cs[1])
                poolSet[cs[1]+"_REF"] = int(cs[2])
            if (len(cs)>3) and ("CONST" in cs):
                constSet.append(cs[1])
            if (len(cs)>3) and ("OPAQUE" in cs):
                opaqueSet.append(cs[1])
            if (len(cs)>3) and ("OPAQUEREF" in cs):
                opaqueSet.append(cs[1]+"_REF")                                
            if (":" in cs):
                tpos = cs.index(":")
                poolType[cs[1]] = cs[tpos+1]
            if "ABSTRACT" in cs:
                absp = 0
                while cs[absp] != "ABSTRACT":
                    absp += 1
                absSet[cs[1]] = cs[absp+1]
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
            originalCode[c] = fileCode
            newCode.append(c)
    code = newCode
        
    dependencies = {}
    classDefs = {}

    codeClasses = []
    for c in code:
        if originalCode[c] not in codeClasses:
            codeClasses.append(originalCode[c] + ' ')
    
    # get definitions
    for c in codeClasses:
        if ":=" in c:
            (lhs,rhs) = c.split(":=")
            for p in poolSet:
                pSub = p.replace("%","")
                pAngle = "<" + pSub + ">"
                if ((p in lhs) or (pAngle in lhs)) and not ((p in rhs) or (pAngle in rhs)):
                    if pSub not in classDefs:
                        classDefs[pSub] = []
                    classDefs[pSub].append(c)

    
    for c in codeClasses:
        dependencies[c] = []
        if ":=" in c:
            rhs = c.split(":=")[1]
        else:
            rhs = c
        for p in poolSet:
            pSub = p.replace("%","")
            pAngle = "<" + pSub + ">"
            pComma = "<" + pSub + ","
            pPerc = "%" + pSub + "%"
            pPercComma = "%" + pSub + ","            
            if (pAngle in rhs) or (pComma in rhs) or (pPerc in rhs) or (pPercComma in rhs):
                if pSub in classDefs:
                    fc = filter(lambda x:x != c, classDefs[pSub])
                    if fc != []:
                        dependencies[c].append(fc)
                
    if config.debug:
        print("-------- :code: --------")
        pprint(code)
        print("------------------------")

    # ------------------------------------------ #
    code = expandPool(code,trackOriginal=True)
    propSet = expandPool(propSet)
    initSet = expandPool(initSet)
    finallySet = expandPool(finallySet)
    logSet = expandPool(logSet)
    hintSet = expandPool(hintSet)

    if config.debug:
        print(":code: after expandPool(code)")
        pprint(code)
        print("------------------------")

    code = expandRange(code,trackOriginal=True)
    propSet = expandRange(propSet)
    initSet = expandRange(initSet)
    finallySet = expandRange(finallySet)    
    logSet = expandRange(logSet)
    hintSet = expandRange(hintSet)

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
        newFinallys = []
        for c in finallySet:
            newFinallys.append(c.replace(p + " ", poolPrefix + p.replace("%","")))
        finallySet = newFinallys

    for p in poolSet:
        newLogs = []
        for c in logSet:
            newLogs.append(c.replace(p + " ", poolPrefix + p.replace("%","")))
        logSet = newLogs

    for p in poolSet:
        newHints = []
        for c in hintSet:
            newHints.append(c.replace(p + " ", poolPrefix + p.replace("%","")))
        hintSet = newHints

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
    nind = 0

    allNames = {}

    warnedAbout = []
    
    for corig in code:
        act = genAct()
        guard = genGuard()

        guardCode = "True"
        guardConds = []

        changes = []

        okExcepts = ""
        for e in ignoredExcepts:
            okExcepts += e[:-1] + ","
        warnExcepts = ""
        if corig[0] == "{":
            c = corig[corig.find("}")+1:]
            while c[0] == " ":
                c = c[1:]
            for e in corig[1:corig.find("}")].split(","):
                if e[0] != "!":
                    okExcepts += e + ","
                else:
                    warnExcepts += e[1:] + ","
            okExcepts = okExcepts[:-1]
            warnExcepts = warnExcepts[:-1]
        else:
            c = corig
            if len(ignoredExcepts) > 0:
                okExcepts = okExcepts[:-1]

        newC = c
            
        forVerbose = []

        cParts = c.split("; ")

        for p in poolSet:
            newC = newC.replace(p + " ", poolPrefix + p.replace("%",""))
            newC = newC.replace(p, poolPrefix + p.replace("%",""))
            plhs = []
            prhs = []
            drhs = []
            earlylhs = []
            for subC in cParts:
                newEarly = []
                eqPos = subC.find(":=")
                if eqPos == -1:
                    eqPos = 0
                found = subC.find(p)
                while (found != -1):
                    use = subC[found:subC.find("]", found)+1]
                    twiddle = (found > 0) and (subC[found-1]=='~')
                    if (found >= eqPos):
                        if use not in earlylhs:
                            prhs.append((use,twiddle))
                        else:
                            drhs.append((use,twiddle))
                    else:
                        plhs.append(use)
                    found = subC.find(p,found+1)
                earlylhs.extend(newEarly)
            hrhs = []
            for (used,twiddle) in prhs:
                if (used,twiddle) in hrhs:
                    continue
                hrhs.append((used,twiddle))
                g = used
                g = g.replace("%","")
                g = poolPrefix + g
                g = g.replace(" ","")
                if g not in forVerbose:
                    forVerbose.append(g)
                    if (not twiddle):
                        changes.append(g.replace("[","_used[") + "=True")
                g += " != None"
                guardConds.append(g)
            for (used,twiddle) in drhs:
                if (used,twiddle) in hrhs:
                    continue
                hrhs.append((used,twiddle))
                g = used
                g = g.replace("%","")
                g = poolPrefix + g
                g = g.replace(" ","")
                if g not in forVerbose:
                    forVerbose.append(g)
                if (not twiddle):
                    changes.append(g.replace("[","_used[") + "=True")
            hlhs = []
            for assign in plhs:
                if assign in hlhs:
                    continue
                hlhs.append(assign)
                g = assign
                g = g.replace("%","")
                g = poolPrefix + g
                g = g.replace(" ","")
                gval = g
                if gval not in forVerbose:
                    forVerbose.append(gval)
                g = g.replace("[", "_used[")
                gguard = "((" + g + ") or (" + gval + " == None) or (self.__relaxUsedRestriction))"
                guardConds.append(gguard)
                changes.append(g + "=False")                    

        newC = newC.replace(":=","=")
        newC = newC.replace("~"+poolPrefix,poolPrefix)
        newC = replaceRefs(newC)

        bad = re.findall("%\w*%",newC)
        for b in bad:
            if b in warnedAbout:
                continue
            warnedAbout.append(b)
            print "*"*70
            print "WARNING: did you forget to declare the pool",b.replace("%","")+"?"
            print "first used in this code:"
            print originalCode[corig]
            print "*"*70            

        
        interestingGuard = ""
        newCguard = ""
        if newC.find(" -> ") > -1:
            inlineGuardSplit = newC.split(" -> ")
            guardConds.append(inlineGuardSplit[0])
            interestingGuard = inlineGuardSplit[0]
            newCguard = inlineGuardSplit[0]
            newC = inlineGuardSplit[1]

        checkRaised = False
        checkRefRaised = False
        postCode = None
        if newC.find(" => ") > -1:
            postCodeSplit = newC.split(" => ")
            newC = postCodeSplit[0] + "\n"
            postCode = postCodeSplit[1].rstrip('\n')
            if "raised" in postCode:
                checkRaised = True
            if "refRaised" in postCode:
                checkRefRaised = True

        preSet = []
        if postCode:
            m = re.match(r".*PRE%\((.+)\)%.*",postCode)
            while m:
                pre_expr = m.groups()[0]
                spre_expr = "'''" + pre_expr + "'''"
                postCode = postCode.replace("PRE%(" + pre_expr + ")%", "__pre[" + spre_expr + "]", 1)
                if preSet == []:
                    preSet.append("__pre = {}\n")
                preSet.append("__pre[" + spre_expr + "] = " + pre_expr + "\n")
                m = re.match(r".*PRE%\((.+)\)%.*",postCode)
            
        expectCode = None
        if newC.find(" ==> ") > -1:
            codeExpectkSplit = newC.split(" ==> ")
            newC = codeExpectkSplit[0] + "\n"
            expectCode = codeExpectkSplit[1].rstrip('\n')

        verboseRef = list(forVerbose)
            
        refC = newC
        for p in poolSet:
            if p in refSet:
                pRaw = poolPrefix + p.replace("%","")
                refC = refC.replace(pRaw,pRaw+"_REF")
                verboseRef = map(lambda x:x.replace(pRaw,pRaw+"_REF"), verboseRef)

        verboseRef = filter(lambda x:"_REF" in x, verboseRef)

        for base in referenceMap:
            if re.match(r"^[a-zA-Z_0-9]+$", refC):  # base is not a regex; treat it like a function name
                refC = re.sub(r'\b'+base+r'\b',referenceMap[base],refC)
            else:   # base is a regex; treat it like one
                refC = re.sub(base,referenceMap[base],refC)

        comparing = False
        for comp in compareSet:
            if re.match(".*" + comp + ".*", newC):
                if (refC != newC):
                    if (" = ") not in newC:
                        newC = "result = " + newC
                        refC = "result_REF = " + refC
                    else:
                        newC = newC[:-1] + " ; " + "result = " + newC.split(" = ")[0] + "\n"
                        refC = refC[:-1] + " ; " + "result_REF = " + refC.split(" = ")[0] + "\n"
                    comparing = True
        if comparing:
            checkRaised = True
            checkRefRaised = True

        beforeSig = afterSig = checkSig = ""
        if expectCode:
            beforeSig = re.sub('([^\(]+)\(', "\\1_before(", expectCode, count=1)
            afterSig = re.sub('([^\(]+)\(', "\\1_after(", expectCode, count=1)
            checkSig = re.sub('([^\(]+)\(', "\\1_check(__before_res, __after_res, ", expectCode, count=1)

        genCode.append("def " + act + "(self):\n")
        genCode.append(baseIndent + "'''\n")
        genCode.append(baseIndent + prettyName(poolSet,newC[:-1]) + "\n")
        genCode.append(baseIndent + "'''\n")        
        d = "self.__test.append(("
        d += "'''" + newC[:-1] +" ''',"
        d += "self." + guard + ","
        d += "self." + act + "))\n"
        genCode.append(baseIndent + d)
        if logSet != []:
            genCode.append(baseIndent + "self.log('''" + newC[:-1] + "''')\n")
        if checkRaised:
            genCode.append(baseIndent + "raised = None\n");
        genCode.append(baseIndent + "if self.__verboseActions:\n")
        genCode.append(baseIndent + baseIndent + "__bV = {}\n")        
        genCode.append(baseIndent + baseIndent + "print 'ACTION:',self.prettyName('''" + newC[:-1] + " ''')\n")
        for p in forVerbose:
            genCode.append(baseIndent + baseIndent + "try: __bV['''" + p + "'''] = repr(" + p + "); print self.prettyName('''" + p + "''') + ' =', __bV['''" + p + "'''], ':',type(" + p + ")\n")
            genCode.append(baseIndent + baseIndent + "except: pass\n")
        for p in verboseRef:
            genCode.append(baseIndent + baseIndent + "try: __bV['''" + p + "'''] = repr(" + p + "); print self.prettyName('''" + p + "''') + ' =', __bV['''" + p + "'''], ':',type(" + p + ")\n")
            genCode.append(baseIndent + baseIndent + "except: pass\n")            
        if not config.noCover:
            genCode.append(baseIndent + "if self.__collectCov: self.__cov.start()\n")
            genCode.append(baseIndent + "try: test_before_each(self)\n")
            genCode.append(baseIndent + "except: pass\n")
        if warnExcepts != "":
            genCode.append(baseIndent + "self.__warning = None\n")            
        genCode.append(baseIndent + "try:\n")
        if preSet != []:
            for p in preSet:
                genCode.append(baseIndent + baseIndent + p)
        if expectCode:
            genCode.append(baseIndent + baseIndent + "__before_res = " + beforeSig + "\n")
        genCode.append(baseIndent + baseIndent + newC)
        if postCode and (not checkRaised) and (not checkRefRaised):
            genCode.append(baseIndent + baseIndent + "assert " + postCode + "\n")
        if expectCode:
            genCode.append(baseIndent + baseIndent + "__after_res = " + afterSig + "\n")
            genCode.append(baseIndent + baseIndent + "__check_res = " + checkSig + "\n")
            genCode.append(baseIndent + baseIndent + "assert __check_res == True, \" check of (%s) for before and after values (%s) and (%s) failed\" % (\"" + expectCode + "\", __before_res, __after_res)\n")

        if okExcepts != "":
            genCode.append(baseIndent + "except (" + okExcepts + ") as raised:\n")
            genCode.append(baseIndent + baseIndent + "if self.__verboseActions: print 'RAISED EXPECTED EXCEPTION:',type(raised),raised\n")
            
        if warnExcepts != "":
            genCode.append(baseIndent + "except (" + warnExcepts + ") as raised:\n")
            genCode.append(baseIndent + baseIndent + "if self.__verboseActions: print 'RAISED WARNING EXCEPTION:',type(raised),raised\n")            
            genCode.append(baseIndent + baseIndent + "self.__warning = raised\n")            

        genCode.append(baseIndent + "except Exception as raised:\n")
        genCode.append(baseIndent + baseIndent + "if self.__verboseActions: print 'RAISED EXCEPTION:',type(raised),raised\n")            
        genCode.append(baseIndent + baseIndent + "raise\n")                    
            
        genCode.append(baseIndent + "finally:\n")
        if postCode and checkRaised and not (checkRefRaised):
            genCode.append(baseIndent + baseIndent + "assert " + postCode + "\n")
        genCode.append(baseIndent + baseIndent + "try: test_after_each(self)\n")
        genCode.append(baseIndent + baseIndent + "except: pass\n")
        if len(forVerbose) > 0:
            genCode.append(baseIndent + baseIndent + "if self.__verboseActions:\n")
            for p in forVerbose:
                genCode.append(baseIndent + baseIndent + baseIndent + "try:\n")
                genCode.append(baseIndent + baseIndent + baseIndent + baseIndent + "__aV = repr(" + p + ")\n")
                genCode.append(baseIndent + baseIndent + baseIndent + baseIndent + "if __aV != __bV['''" + p + "''']: print '=>',self.prettyName('''" + p + "''') + ' =',__aV, ':',type(" + p + ")\n")                        
                genCode.append(baseIndent + baseIndent + baseIndent + "except: pass\n")
  
        if not config.noCover:
            genCode.append(baseIndent + baseIndent + "if self.__collectCov: self.__cov.stop(); self.__updateCov()\n")

        if checkRefRaised:
            genCode.append(baseIndent + "refRaised = None\n")
        
        if refC != newC:
            genCode.append(baseIndent + "try:\n")
            genCode.append(baseIndent + baseIndent + "if self.__verboseActions: print 'REFERENCE ACTION:',self.prettyName('''"+refC[:-1]+" ''')\n")            
            genCode.append(baseIndent + baseIndent + refC)
            genCode.append(baseIndent + "except KeyboardInterrupt:\n")
            genCode.append(baseIndent + baseIndent + "raise\n")            
            genCode.append(baseIndent + "except Exception as refRaised:\n")
            genCode.append(baseIndent + baseIndent + "if self.__verboseActions: print 'REFERENCE ACTION RAISED EXCEPTION:',type(refRaised),refRaised\n")                        
            genCode.append(baseIndent + "if self.__verboseActions:\n")
            for p in verboseRef:
                genCode.append(baseIndent + baseIndent + "try:\n")
                genCode.append(baseIndent + baseIndent + baseIndent + "__aV = repr(" + p + ")\n")
                genCode.append(baseIndent + baseIndent + baseIndent + "if __aV != __bV['''" + p + "''']: print '=>',self.prettyName('''" + p + "''') + ' =',__aV, ':',type(" + p + ")\n") 
                genCode.append(baseIndent + baseIndent + "except: pass\n")
            if postCode and checkRefRaised:
                genCode.append(baseIndent + "assert " + postCode + "\n")
            if comparing:
                genCode.append(baseIndent + "assert (raised == None) == (refRaised == None)\n")
                genCode.append(baseIndent + "try: assert result == result_REF, \" (%s) == (%s) \" % (result, result_REF)\n")
                genCode.append(baseIndent + "except UnboundLocalError: pass\n")
        genCode.append(baseIndent + "if self.__verboseActions: print '='*50\n")                                      
        if logSet != []:
            genCode.append(baseIndent + "self.logPost('''" + newC[:-1] + "''')\n")
        for ch in changes:
            genCode.append(baseIndent + ch + "\n")

        for g in guardConds:
            guardCode += " and (" + g + ")"

        if newC.find("guarded") == 0:
            guardCode += " and (" + newC.replace(")\n",",True))")

        genCode.append("def " + guard + "(self):\n")
        if interestingGuard != "":
            genCode.append(baseIndent + "'''\n")
            genCode.append(baseIndent + prettyName(poolSet, interestingGuard) + "\n")
            genCode.append(baseIndent + "'''\n")
        genCode.append(baseIndent + "return " + guardCode + "\n")

        genCode.append("\n")

        while (newC[:-1] in allNames) and (allNames[newC[:-1]] != newCguard):
            newC = newC[:-1] + " " + newC[-1]

        allNames[newC[:-1]] = newCguard
        
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
        d = "self.__actionClass[" + "'''" + newC[:-1] + " '''] = '''" + originalCode[corig] + " '''\n"
        actDefs.append(d)        
        nind += 1
        d = "self.__orderings[" + "'''" + newC[:-1] + " '''] = " + str(nind) + "\n"
        actDefs.append(d)
        d = "self.__okExcepts[" + "'''" + newC[:-1] + " '''] = '''" + okExcepts + "'''\n"
        actDefs.append(d)

        if refC != newC:
            d = "self.__refCode[" + "'''" + newC[:-1] + " '''] = []\n"
            actDefs.append(d)
            d = "self.__refCode[" + "'''" + newC[:-1] + " '''].append('''" + refC[:-1] + " ''')\n"
            actDefs.append(d)
            if comparing:
                d = "self.__refCode[" + "'''" + newC[:-1] + " '''].append(\"assert result == result_REF, \\\" (%s) == (%s) \\\" % (result, result_REF)\\n\")\n"
                actDefs.append(d)
            
        
        if postCode:
            d = "self.__propCode[" + "'''" + newC[:-1] + " '''] = \"\"\"" + postCode + " \"\"\"\n"
            actDefs.append(d)
        
        if preSet != []:
            d = "self.__preCode[" + "'''" + newC[:-1] + " '''] = []\n"
            actDefs.append(d)
            for p in preSet:
                d = "self.__preCode[" + "'''" + newC[:-1] + " '''].append(r\"" + p[:-1] + "\")\n"
                actDefs.append(d)

    # ------------------------------------------ #
    genCode.append("def __init__(self):\n")
    genCode.append(baseIndent + "try:\n")
    genCode.append(baseIndent + baseIndent + "test_before_all(self)\n")
    genCode.append(baseIndent + "except:\n")
    genCode.append(baseIndent + baseIndent + "pass\n")
    genCode.append(baseIndent + "self.__modules = []\n")
    for s in sourceSet:
        genCode.append(baseIndent + 'self.__modules.append(r"' + s + '")\n')
    genCode.append(baseIndent + "self.__importModules = []\n")        
    for i in import_modules:
        genCode.append(baseIndent + "self.__importModules.append(" + i + ")\n")
    genCode.append(baseIndent + "self.__features = []\n")
    for f in featureSet:
        genCode.append(baseIndent + 'self.__features.append(r"' + f + '")\n')

    if not config.defaultReplay:
        genCode.append(baseIndent + "self.__replayBacktrack = False\n")
    else:
        genCode.append(baseIndent + "self.__replayBacktrack = True\n")
    if not config.noCover:
        covc = baseIndent + "self.__cov = coverage.coverage(branch=True, source="
        if len(sourceSet) > 0:
            covc += "["
        for s in sourceSet:
            covc += '"' + s + '",'
        if len(sourceSet) > 0:
            covc = covc[:-1] + "] + self.moduleFiles()"
        else:
            covc = covc + "self.moduleFiles()"
        genCode.append(covc)
        if config.pylib:
            genCode.append(",cover_pylib=True")
        genCode.append(",omit='sut.py'")
        genCode.append(")\n")
        genCode.append(baseIndent + "self.__cov._warn_no_data = False\n")
        genCode.append(baseIndent + "self.__collectCov = True\n")
        genCode.append(baseIndent + "self.__allBranches = set()\n")
        genCode.append(baseIndent + "self.__allStatements = set()\n")
        genCode.append(baseIndent + "self.__newBranches = set()\n")
        genCode.append(baseIndent + "self.__newStatements = set()\n")
        genCode.append(baseIndent + "self.__currBranches = set()\n")
        genCode.append(baseIndent + "self.__currStatements = set()\n")
        genCode.append(baseIndent + "self.__newCurrBranches = set()\n")
        genCode.append(baseIndent + "self.__newCurrStatements = set()\n")
        genCode.append(baseIndent + "self.__oldCovData = None\n")
    genInitialization()
    genCode.append(baseIndent + "self.__actions = []\n")
    genCode.append(baseIndent + "self.__names = {}\n")
    genCode.append(baseIndent + 'self.__poolPrefix = "' + poolPrefix + '"\n')
    genCode.append(baseIndent + 'self.__names["<<RESTART>>"] = ("<<RESTART>>", lambda x: True, lambda x: self.restart())\n')
    genCode.append(baseIndent + "self.__actionClass = {}\n")
    genCode.append(baseIndent + "self.__swarmConfig = None\n")    
    genCode.append(baseIndent + "self.__actionClasses = []\n")
    for c in codeClasses:
        genCode.append(baseIndent + "self.__actionClasses.append('''" + c + "''')\n")
    genCode.append(baseIndent + "self.__dependencies = {}\n")
    for c in codeClasses:
        genCode.append(baseIndent + "self.__dependencies['''"+c+"'''] = []\n")
        for d in dependencies[c]:
            genCode.append(baseIndent + "self.__dependencies['''"+c+"'''].append(" + str(d) + ")\n")
    genCode.append(baseIndent + "self.__orderings = {}\n")
    genCode.append(baseIndent + "self.__okExcepts = {}\n")
    genCode.append(baseIndent + "self.__preCode = {}\n")
    genCode.append(baseIndent + "self.__refCode = {}\n")
    genCode.append(baseIndent + "self.__propCode = {}\n")
    genCode.append(baseIndent + 'self.__orderings["<<RESTART>>"] = -1\n')
    genCode.append(baseIndent + "self.__log = None\n")
    if config.enumerateEnabled:
        genCode.append(baseIndent + "self.__enumerateEnabled = True\n")
    else:
        genCode.append(baseIndent + "self.__enumerateEnabled = False\n")        
    genCode.append(baseIndent + "self.__verboseActions = False\n")    
    genCode.append(baseIndent + "self.__logAction = self.logPrint\n")
    genCode.append(baseIndent + "self.__relaxUsedRestriction = False\n")
    genCode.append(baseIndent + "self.__noReassigns = False\n")
    genCode.append(baseIndent + "self.__safeSafelyMode = False\n")    
    genCode.append(baseIndent + "self.__simplifyCache = {}\n")
    genCode.append(baseIndent + "self.__pools = []\n")
    genCode.append(baseIndent + "self.__psize = {}\n")        
    genCode.append(baseIndent + "self.__consts = []\n")
    genCode.append(baseIndent + "self.__opaque = []\n")
    genCode.append(baseIndent + "self.__abstraction = {}\n")
    for p in poolSet:
        s = baseIndent
        s += 'self.__psize["' + p.replace("%","") + '"] = ' + str(poolSet[p])
        genCode.append(s + "\n")
        s = baseIndent
        s += 'self.__pools.append("' + poolPrefix + p.replace("%","") + '")'
        genCode.append(s + "\n")
        if p in constSet:
            s = baseIndent
            s += 'self.__consts.append("' + poolPrefix + p.replace("%","") + '")'
            genCode.append(s + "\n")
        if p in opaqueSet:
            s = baseIndent
            s += 'self.__opaque.append("' + poolPrefix + p.replace("%","") + '")'
            genCode.append(s + "\n")
        if p in absSet:
            s = baseIndent
            s += 'self.__abstraction["' + poolPrefix + p.replace("%","") + '"] = "' + absSet[p] + '"'
            genCode.append(s + "\n")
            
    for d in actDefs:
        genCode.append(baseIndent + d + "\n")
    genCode.append(baseIndent + "self.__actions_backup = list(self.__actions)\n")

    genCode.append("def restart(self):\n")
    if finallySet != []:
        for f in finallySet:
            genCode.append(baseIndent + "try:\n")
            genCode.append(baseIndent + baseIndent + f)
            genCode.append(baseIndent + "except: pass\n")
            refF = f
            for p in poolSet:
                if p in refSet:
                    pRaw = poolPrefix + p.replace("%","")
                    refF = refF.replace(pRaw,pRaw+"_REF")
            for base in referenceMap:
                if re.match(r"^[a-zA-Z_0-9]+$", refF):  # base is not a regex; treat it like a function name
                    refF = re.sub(r'\b'+base+r'\b',referenceMap[base],refF)
                else:   # base is a regex; treat it like one
                    refF = re.sub(base,referenceMap[base],refF)
            if refF != f:
                genCode.append(baseIndent + "try:\n")
                genCode.append(baseIndent + baseIndent + refF)
                genCode.append(baseIndent + "except: pass\n")
            
    genCode.append(baseIndent + "try:\n")
    genCode.append(baseIndent + baseIndent + "test_before_restart(self)\n")
    genCode.append(baseIndent + "except:\n")
    genCode.append(baseIndent + baseIndent + "pass\n")    
    if not config.noCover:
        genCode.append(baseIndent + "self.cleanCov()\n")
        #genCode.append(baseIndent + "self.__currBranches = set()\n")
        #genCode.append(baseIndent + "self.__currStatements = set()\n")
        #genCode.append(baseIndent + "self.__newCurrBranches = set()\n")
        #genCode.append(baseIndent + "self.__newCurrStatements = set()\n")
        if config.coverReload:
            genCode.append(baseIndent + "if self.__collectCov: self.__cov.start()\n")
    genCode.append("# BEGIN RELOAD CODE\n")
    for l in import_modules:
        s = baseIndent + 'reload({})\n'.format(l)
        genCode.append(s)
    #for l in import_froms:
    #    s = baseIndent + l
    #    genCode.append(s)
    genCode.append("# END RELOAD CODE\n")        
    if (not config.noCover) and config.coverReload:
        genCode.append(baseIndent + "if self.__collectCov: self.__cov.stop()\n")        
        genCode.append(baseIndent + "if self.__collectCov: self.__updateCov()\n")
    genInitialization()
    genCode.append(baseIndent + "try:\n")
    genCode.append(baseIndent + baseIndent + "test_after_restart(self)\n")
    genCode.append(baseIndent + "except:\n")
    genCode.append(baseIndent + baseIndent + "pass\n")    

    genCode.append("def hints(self):\n")
    if hintSet == []:
        genCode.append(baseIndent + "return []\n")
    else:
        genCode.append(baseIndent + "hvals = []\n")
        for h in hintSet:
            genCode.append(baseIndent + "try: hvals.append(" + replaceRefs(h[:-1]) + ")\n")
            genCode.append(baseIndent + "except: hvals.append(None)\n")
        genCode.append(baseIndent + "return hvals\n")
            

    
    genCode.append("def log(self, name):\n")
    if logSet != []:
        genCode.append(baseIndent + "if self.__log == None:\n")
        genCode.append(baseIndent + baseIndent + "return\n")
        for l in logSet:
            ls = l.split()
            if ls[0] == "POST":
                continue
            try:
                level = int(ls[0])
                lcode = l[l.find(ls[1]):]
            except ValueError:
                level = 0
                lcode = l
            genCode.append(baseIndent + "if (self.__log == 'All') or (self.__log >= " + str(level) + "):\n")
            genCode.append(baseIndent + baseIndent + "try:\n")
            genCode.append(baseIndent + baseIndent + baseIndent + "self.__logAction(name," + '"""' + lcode[:-1] + '""",' + lcode[:-1] + ",False)\n")
            genCode.append(baseIndent + baseIndent + "except:\n")
            genCode.append(baseIndent + baseIndent + baseIndent + "pass\n")
            
    else:
        genCode.append(baseIndent + "pass\n")

    genCode.append("def logPost(self, name):\n")
    if logSet != []:
        genCode.append(baseIndent + "if self.__log == None:\n")
        genCode.append(baseIndent + baseIndent + "return\n")
        for lv in logSet:
            ls = lv.split()
            if ls[0] != "POST":
                continue
            l = lv.replace("POST ","")
            ls = ls[1:]
            try:
                level = int(ls[0])
                lcode = l[l.find(ls[1]):]
            except ValueError:
                level = 0
                lcode = l
            genCode.append(baseIndent + "if (self.__log == 'All') or (self.__log >= " + str(level) + "):\n")
            genCode.append(baseIndent + baseIndent + "try:\n")
            genCode.append(baseIndent + baseIndent + baseIndent + "self.__logAction(name," + '"""' + lcode[:-1] + '""",' + lcode[:-1] + ",True)\n")
            genCode.append(baseIndent + baseIndent + "except:\n")
            genCode.append(baseIndent + baseIndent + baseIndent + "pass\n")
            
    else:
        genCode.append(baseIndent + "pass\n")
        
    genCode.append("def state(self):\n")
    genCode.append(baseIndent + "if self.__replayBacktrack:\n")
    genCode.append(baseIndent + baseIndent + "return self.captureReplay(self.__test)\n")    
    st = baseIndent + "return [ "
    for p in poolSet:
        st += "copy.deepcopy(" + poolPrefix + p.replace("%","") + "),"
        st += "copy.deepcopy(" + poolPrefix + p.replace("%","") + "_used),"
    st = st[:-1]
    if len(poolSet) > 0:
        st += ","
    genCode.append(st + "copy.copy(self.__test)]\n")

    genCode.append("def shallowState(self):\n")
    st = baseIndent + "return [ "
    for p in poolSet:
        st += '("' + poolPrefix + p.replace("%","") + '",'
        st += poolPrefix + p.replace("%","") + "),"
    st = st[:-1]
    genCode.append(st + "]\n")

    genCode.append("def abstract(self,state):\n")
    genCode.append(baseIndent + "if self.__replayBacktrack:\n")
    genCode.append(baseIndent + baseIndent + "return state\n")        
    st = baseIndent + "return ( "
    i = 0
    for p in poolSet:
        if p not in absSet:
            st += "state[" + str(i) + "],"
            st += "state[" + str(i+1) + "],"            
        else:
            st += "{k: (" + absSet[p] + "(v) if v != None else None) for k, v in " + "(state[" + str(i) + "]).iteritems()},"
            st += "state[" + str(i+1) + "],"            
        i += 2
    st = st[:-1]
    genCode.append(st + ")\n")
    
    genCode.append("def backtrack(self,old):\n")
    genCode.append(baseIndent + "if self.__replayBacktrack:\n")
    genCode.append(baseIndent + baseIndent + "self.replay(self.replayable(old))\n")
    genCode.append(baseIndent + baseIndent + "return\n")
    n = 0
    for p in poolSet:
        genCode.append(baseIndent + poolPrefix + p.replace("%","") + " = copy.deepcopy(old[" + str(n) + "])\n")
        n += 1
        genCode.append(baseIndent + poolPrefix + p.replace("%","") + "_used = copy.deepcopy(old[" + str(n) + "])\n")
        n += 1
    genCode.append(baseIndent + "self.__test = copy.copy(old[-1])\n")

    genCode.append("def check(self):\n")
    if (propSet != []) or (len(poolType) > 0):
        genCode.append(baseIndent + "try:\n")
        if not config.noCover:
            genCode.append(baseIndent + baseIndent + "if self.__collectCov:\n")
            genCode.append(baseIndent + baseIndent + baseIndent + "self.__cov.start()\n")
        genCode.append(baseIndent + baseIndent + "# BEGIN CHECK CODE\n")
        checkGlobals = []
        for p in poolType:
            pname = poolPrefix + p.replace("%","")
            genCode.append(baseIndent+ baseIndent + baseIndent + "for __pind in " + pname + ":" + "\n")
            genCode.append(baseIndent+ baseIndent + baseIndent + baseIndent + "assert (" + pname + "[__pind] == None) or (type("+pname+"[__pind]) == " + poolType[p] + ")\n")
            
        for (p, u) in propSet:
            okExcepts = ""
            for e in ignoredExcepts:
                okExcepts += e[:-1] + ","
            porig = p
            if porig[0] == "{":
                p = porig[porig.find("}")+1:]
                while p[0] == " ":
                    p = p[1:]
                for e in porig[1:porig.find("}")].split(","):
                    okExcepts += e + ","
                okExcepts = okExcepts[:-1]
            else:
                p = porig
                if len(ignoredExcepts) > 0:
                    okExcepts = okExcepts[:-1]
            if (okExcepts != ""):
                tryPrefix = "try: "
            else:
                tryPrefix = ""
            if u != []:
                pr = baseIndent + baseIndent + "if True"
                for use in u:
                    pr += " and (" + use + " != None)"
                    if use not in checkGlobals:
                        genCode.append(baseIndent + baseIndent + "# GLOBAL " + use + "\n")
                        checkGlobals.append(use)
                pr += ": # CHECK POOL INIT\n"
                genCode.append(pr)
                genCode.append(baseIndent + baseIndent + baseIndent + tryPrefix + "assert " + replaceRefs(p))
                if okExcepts != "":
                    genCode.append(baseIndent + baseIndent + baseIndent + "except (" + okExcepts + ") as raised:\n")
                    genCode.append(baseIndent + baseIndent + baseIndent + baseIndent + "if self.__verboseActions: print 'PROPERTY RAISED EXPECTED EXCEPTION:',type(raised),raised\n")                
            else:
                genCode.append (baseIndent + baseIndent + tryPrefix + "assert " + replaceRefs(p))
                if okExcepts != "":
                    genCode.append(baseIndent + baseIndent + "except (" + okExcepts + ") as raised:\n")
                    genCode.append(baseIndent + baseIndent + baseIndent + "if self.__verboseActions: print 'PROPERTY RAISED EXPECTED EXCEPTION:',type(raised),raised\n")                
                
        genCode.append(baseIndent + baseIndent + "# END CHECK CODE\n")
        genCode.append(baseIndent + "except KeyboardInterrupt as e:\n")
        genCode.append(baseIndent + baseIndent + "raise e\n")
        genCode.append(baseIndent + "except:\n")
        genCode.append(baseIndent + baseIndent + "self.__failure = sys.exc_info()\n")
        genCode.append(baseIndent + baseIndent + "return False\n")
        if not config.noCover:
            genCode.append(baseIndent + "finally:\n")
            genCode.append(baseIndent + baseIndent + "if self.__collectCov:\n")
            genCode.append(baseIndent + baseIndent + baseIndent + "self.__cov.stop()\n")
            genCode.append(baseIndent + baseIndent + baseIndent + "self.__updateCov(extendCov=True)\n")
    genCode.append(baseIndent + "return True\n")

    for c in genCode:
        outf.write(baseIndent + c.replace("True and (","("))

    ######################## REQUIRED FOR PACKAGING TSTL ##########################
    boilerplate = pkg_resources.resource_stream('src', 'static/boilerplate.py')
    boilerplate_cov = pkg_resources.resource_stream('src', 'static/boilerplate_cov.py')
    ###############################################################################

    for l in boilerplate:
        outf.write(baseIndent + l)

    if not config.noCover:
        for l in boilerplate_cov:
            outf.write(baseIndent + l)    

    outf.close()


if __name__ == '__main__':
    main()
