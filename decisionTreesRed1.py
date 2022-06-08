from cgi import test
import matplotlib.pyplot as plot
#import sys
import math
import random

from numpy import char
# dataFile = sys.argv[1]
# testSetSize = sys.argv[2]
# minTrainingSize = sys.argv[3]
# maxTrainingSize = sys.argv[4]
#step = sys.argv[5]
dataFile = 'house-votes-84.csv'
with open(dataFile) as f: 
    line_list = [line.split(',') for line in f]
    count = 0
    features2 = []
    valueList2 = []
    nonmissing = []
    for x in line_list:
        if count == 0:
            for y in x[1:]: features2.append(y)
        else:
            lList = []
            for y in x[1:]: lList.append(y.strip())
            if '?' not in lList: nonmissing.append(lList)
            valueList2.append(lList)
        count += 1
def infoGain(valueList, features):
    featureLen = len(valueList)
    startingEntropy = 0
    featVal = dict()
    finalCol = []
    for x in valueList:
        x2 = x[len(features) - 1]
        finalCol.append(x2)
        if x2 not in featVal: featVal[x2] = 1
        else: featVal[x2] += 1
    valCol = []
    for c in range(0, len(features) - 1):
        vc = []
        for x in valueList:
            x2 = x[c]
            vc.append(x2)
        valCol.append(vc)
    for x in featVal: startingEntropy += ((featVal[x]/featureLen)*math.log((featVal[x]/featureLen), 2))
    startingEntropy *= -1
    ogEntropies = dict()
    vals = dict()
    count2 = 0
    for x in valCol:
        count = 0
        for y in x:
            if y+ "," + features[count2] not in vals: vals[y + "," + features[count2]] = [finalCol[count]]
            else: vals[y+ "," + features[count2]].append(finalCol[count])
            count += 1
        count2 += 1
    for x in vals:
        dTable = vals[x]
        fVals = dict()
        for y in dTable:
            if y not in fVals: fVals[y] = 1
            else: fVals[y] += 1
        entropy = 0
        for y in set(dTable): entropy += ((fVals[y]/len(dTable))*math.log((fVals[y]/len(dTable)), 2))
        entropy *= -1
        ogEntropies[x] = entropy
    featureInfoGains = dict()
    count = 0
    for x in valCol:
        eachCol = dict()
        for y in x: 
            if y+","+features[count] not in eachCol: eachCol[y+","+features[count]] = 1
            else: eachCol[y+","+features[count]] += 1
        entropy = 0
        for y in eachCol: entropy += ((eachCol[y]/len(x))*ogEntropies[y])
        featureInfoGains[features[count]] = startingEntropy - entropy
        count += 1
    return [featureInfoGains, ogEntropies, features, valCol, vals, valueList]

def decisionTrees(infoGains, entropies, depth, features, columns, vals, valueList, mainS):
    maxInfoGain = ""
    infoValue = 0
    count = 0
    for x in infoGains:
        if count == 0: 
            maxInfoGain = x
            infoValue = infoGains[x]
        else:
            if infoValue < infoGains[x]:
                maxInfoGain = x
                infoValue = infoGains[x]
        count += 1
    s = (depth * ("  ")) + "* " + maxInfoGain + "?"
    mainS += s +'\n'
    count = 0
    loc = 0
    for x in features:
        if maxInfoGain == x: 
            loc = count
            break
        count += 1
    values = set(columns[loc])
    tempF = features.copy()
    tempF.remove(features[loc])
    for x in values:
        for y in entropies:
            firstPart = y[0 : y.index(",")]
            secondPart = y[y.index(",") + 1 : len(y)]
            if secondPart == maxInfoGain and firstPart == x:
                if entropies[y] == -0.0 or entropies[y] == 0.0:
                    v = vals[y][0] 
                    s = ((depth + 1) * ("  ")) + "* " + firstPart + " --> " + v
                    mainS += s +'\n'
                elif entropies[y] > 0:
                    s = ((depth + 1) * ("  ")) + "* " + firstPart 
                    mainS += s +'\n'
                    newValList = []
                    for z in valueList:
                        if z[loc] == firstPart: 
                            newZ = []
                            c = 0
                            for x2 in z:
                                if c != loc: newZ.append(x2)
                                c += 1
                            newValList.append(newZ)
                    i = infoGain(newValList, tempF)
                    mainS = decisionTrees(i[0], i[1], depth + 2, i[2], i[3], i[4], i[5], mainS)
    return mainS

def chartSizeAcc(d, numCheck, count, l, testSet2, mc, depth):
    mainCount = 0
    arrowCount = 0
    #print(numCheck)
    for x in d:
        if '?' in x: 
            i = x.index('*')
            if len(x[0: i]) == ((depth) * 2): numCheck = int(x.strip()[3:x.strip().index("?")])
        elif '-->' in x:
            i = x.index('*')
            if len(x[0: i]) == ((depth+1) * 2):
                arrowCount += 1
                x = x.strip()
                i = x.index('-->') 
                i2 = x.index('*') + 2
                val = x[i2:i-1].strip()
                dec = x[i+4:].strip()
                c = 0
                for y in testSet2:
                    if c in l:
                        v = y[numCheck-1].strip()
                        if val == v:
                            if dec == y[len(y) - 1].strip(): count += 1
                            #print(dec, y[len(y) - 1].strip(), dec == y[len(y) - 1].strip())
                            mc += 1
                    c += 1
        elif ('y' in x or 'n' in x) and "-->" not in x:
            i = x.index('*')
            if len(x[0: i]) == ((depth+1) * 2):
                arrowCount += 1
                x = x.strip()[2:]
                l2 = []
                n = numCheck
                c = 0
                for y in testSet2:
                    if y[n-1] == x: l2.append(c)
                    c += 1
                lc = chartSizeAcc(d[mainCount+1:], n, count, l2, testSet2, mc, depth + 2)
                count = lc[0]
                mc = lc[1]
        if arrowCount == 2: return [count, mc]
        mainCount += 1
    #print(numCheck)
    return [count, mc]
            

testSet = nonmissing[182:]
nonmissing = nonmissing[0:182]
sizes = []
accuracies = []
for size in range(5, 182):
    #size = 181
    checker = False
    while not checker:
        train = random.sample(nonmissing, size)
        b = train[0][len(train[0]) - 1]
        checker = False
        for x in train: 
            if x[len(x) - 1] != b: 
                checker = True
                break
    i2 = infoGain(train, features2)
    dTree = decisionTrees(i2[0], i2[1], 0, i2[2], i2[3], i2[4], i2[5], "")
    #print(dTree)
    d = dTree.split('\n')
    numCheck = int(d[0].strip()[3:4])
    c2 = chartSizeAcc(d, int(d[0].strip()[3:d[0].strip().index("?")]), 0, [x for x in range(0, len(testSet))], testSet, 0, 0)
    count = c2[0]
    count2 = c2[1]
    prob = count / count2
    #print(count, count2)
    sizes.append(size)
    accuracies.append(prob)
    #break
plot.scatter(sizes, accuracies, c = "blue")
plot.xlabel("Size")
plot.ylabel("Accuracy")
plot.show()