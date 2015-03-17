import sys

infn = sys.argv[1]
outfn = infn.split(".py")[0]+"_INST.py"

code = []

for l in open(infn):
    code.append(l)

outf = open(outfn, 'w')
outf.write("import covertool\n")
ln = 0
inComment = False
justEnded = False
currentIndent = 0
lineIndent = 0
okChangeIndent = False
skipNext = False

doNotInstrument = ["class","def","import", "elif", "else:", "except", "}", "]", ")"]
indentChangers = ["class", "def", "if", "elif", "else:", "for", "try:", "except", "while"]
skipNextChars = [",","\\"]

conditionals = ["if","elif", "else"]

for l in code:
    ln += 1
    ls = l.split()
    if l.find('"""') != -1:
        inComment = not inComment
        justEnded = True
    if inComment:
        outf.write(l)
        continue
    if justEnded:
        outf.write(l)
        justEnded = False
        continue

    lineIndent = 0
    for c in l:
        if c != " ":
            break
        else:
            lineIndent += 1
            
    instrument = False
    if (lineIndent > currentIndent):
        if okChangeIndent and not skipNext:
            currentIndent = lineIndent
            instrument = True
    else:
        instrument = ls != []
        currentIndent = lineIndent

    if (ls != []) and ((ls[0] in doNotInstrument) or (ls[0][0] == "#")):
        instrument = False

    if (ls != []) and (ls[0] in conditionals) and (":" in l) and (ls[-1][-1] != ":"):
        if ls[0] == "if":
            ld = infn + ":" + str(ln)
            outf.write((" " * lineIndent) + 'covertool.cover("' + ld + '")\n')
        ld = infn + ":" + str(ln)+":True"
        sc = l.split(":")
        sct = ""
        started = False
        for c in sc[1]:
            if started or (c != " "):
                started = True
                sct += c
        outf.write(sc[0] + ":" + "\n")
        outf.write((" " * lineIndent) + '        covertool.cover("' + ld + '")\n')
        outf.write((" " * lineIndent) + "        " + sct + "\n")
        okChangeIndent = False
        skipNext = False
        continue

    if instrument:
        ld = infn + ":" + str(ln)
        outf.write((" " * lineIndent) + 'covertool.cover("' + ld + '")\n')

    okChangeIndent = skipNext or ((ls != []) and (ls[0] in indentChangers))

    skipNext = (len(l) > 2) and (l[-2] in skipNextChars)
    
    outf.write(l)

outf.close()
