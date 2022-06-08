import sys
import re
words = sys.argv[1]
listOfWords = []
regexes = []
maxLenOfCont = 0
maxRepeat = 0
maxAdjRepeat = 0
consMax = 0
e = re.compile(r"(\w)(\1)+", re.I)
e2 = re.compile(r"\b\w*(\w)(\w*\1)+\w*\b", re.I)
e3 = re.compile(r"(\w\w)(\w*\1)+\w*", re.I)
e4 = re.compile(r"[qwrtypsdfghjklmnbvcxz]")
with open(words) as f:
    for line in f: listOfWords.append(line.strip())
for s in listOfWords:
    for f in e.finditer(s):
        x, y = f.span()
        if y - x >= maxLenOfCont: maxLenOfCont = y - x
    for f in e2.finditer(s):
        lets = dict()
        for x in s:
            if x in lets: lets[x] += 1
            else: lets[x] = 1
        for x in lets:
            if lets[x] > maxRepeat: maxRepeat = lets[x]
    for f in e3.finditer(s):
        lets = dict()
        x, y = f.span()
        s = s[x: y]
        for x in range(0, len(s) - 1):
            if s[x: x + 2] in lets: lets[s[x: x + 2]] += 1
            else: lets[s[x: x + 2]] = 1
        for x in lets:
            if lets[x] > maxAdjRepeat: maxAdjRepeat = lets[x]
    consCount = 0
    for f in e4.finditer(s): consCount += 1
    if consCount > consMax: consMax = consCount
maxRepeat -= 1
maxLenOfCont -= 1
maxAdjRepeat -= 1
regexes.append([r"\b(?=\w*a)(?=\w*e)(?=\w*i)(?=\w*o)(?=\w*u)\w*\b", re.I])
regexes.append([r"\b([^aeiou]*[aeiou]){5}[^aeiou]*\b", re.I])
regexes.append([r"\b(\w)(?!\w*(\w*\1\w))(?=\w*\1\b)\w*", re.I]) 
regexes.append([r"\b(?=(\w)(\w)(\w))\w*(?=\3\2\1\b)\w*\b",re.I]) 
regexes.append([r"\b[^bt]*(bt|tb)(?!\w*\1)[^bt]*\b", re.I])
regexes.append([r"\b\w*(\w)(\1){"+str(maxLenOfCont)+r"}\w*\b", re.I])
regexes.append([r"\b\w*(\w)(\w*\1){"+str(maxRepeat)+r"}\w*\b", re.I])
regexes.append([r"\b\w*(\w\w)(\w*\1){"+str(maxAdjRepeat)+r"}\w*\b", re.I])
regexes.append([r"\b(\w*[qwrtypsdfghjklmnbvcxz]){"+str(consMax)+r"}\w*\b", re.I])
regexes.append([r"\b(?!\w*(\w)(\w*\1){2,3})\w*\b", re.I])
count = 0
for x in regexes:
    matches = []
    if len(x) == 2: exp = re.compile(x[0], x[1])
    else: exp = re.compile(r""+x[0])
    b = True
    for s in listOfWords:
        for f in exp.finditer(s):
            if b: print("#"+str(count + 1), f.re) 
            b = False
            x1, y1 = f.span()
            st = s[x1 : y1]
            if count == 0:
                if len(matches) == 0 or (len(matches) > 0 and len(st) == len(matches[0])): matches.append(st)
                if len(matches) > 0 and len(st) < len(matches[0]):
                    matches.clear()
                    matches.append(st)
            elif count == 1 or count == 2 or count == 9:
                if len(matches) == 0 or (len(matches) > 0 and len(st) == len(matches[0])): matches.append(st)
                if len(matches) > 0 and len(st) > len(matches[0]):
                    matches.clear()
                    matches.append(st)
            else: matches.append(st)
    matches2 = matches[0: 5]
    print(len(matches), "total matches")
    for m in matches2: print(m)
    print()
    count += 1