def shift(line):
    return [line[i:] + line[:i] for i in range(0,len(line))]

def cleanWord(word):
    return filter (lambda c: c not in [".",",","?","!",":"], word.lower())

def ignorable(word,ignoreWords):
    return cleanWord(word) in map(lambda w: w.lower(), ignoreWords)

def splitBreaks(string, periodsToBreaks):
    if not periodsToBreaks:
        return string.split("\n")
    else:
        line = ""
        lines = []
        lastChar1 = None
        lastChar2 = None
        breakChars = map(chr, range(ord('a'),ord('z')+1))
        for c in string:
            if (c == " ") and (lastChar1 == ".") and (lastChar2 in breakChars):
                lines.append(line)
                line = ""
            line += c
            lastChar2 = lastChar1
            lastChar1 = c
        lines.append(line)
        return lines

def kwic(string,ignoreWords=[], listPairs=False, periodsToBreaks=False):
    lines = splitBreaks(string, periodsToBreaks)
    splitLines = map(lambda l: l.split(), lines)
    if listPairs:
        pairs = {}
        for l in splitLines:
            seen = set([])
            for wu1 in l:
                wc1 = cleanWord(wu1)
                if len(wc1) == 0:
                    continue
                for wu2 in l:
                    wc2 = cleanWord(wu2)
                    if wc1 < wc2:
                        if (wc1,wc2) in seen:
                            continue
                        seen.add((wc1,wc2))
                        if (wc1, wc2) in pairs:
                            pairs[(wc1,wc2)] += 1
                        else:
                            pairs[(wc1,wc2)] = 1
    shiftedLines = [map(lambda x:(x,i), shift(splitLines[i])) for i in range(0,len(splitLines))]
    flattenedLines = [l for subList in shiftedLines for l in subList]
    filteredLines = filter(lambda l: not ignorable(l[0][0], ignoreWords), flattenedLines)
    if not listPairs:
        return sorted(filteredLines, key = lambda l: (map(lambda w:w.lower(), l[0]),l[1]))
    else:
        return (sorted(filteredLines, key = lambda l: (map(lambda w:w.lower(), l[0]),l[1])),
                map(lambda wp: (wp, pairs[wp]), sorted(filter(lambda wp: pairs[wp] > 1, pairs.keys()))))
