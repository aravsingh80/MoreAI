import sys
import math
dataFile = sys.argv[1]
#dataFile = "mushroom.csv"
with open(dataFile) as f: 
    line_list = [line.split(',') for line in f]
    count = 0
    features2 = []
    valueList2 = []
    for x in line_list:
        if count == 0:
            for y in x: features2.append(y)
        else:
            lList = []
            for y in x: lList.append(y.strip())
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
i2 = infoGain(valueList2, features2)
dTree = decisionTrees(i2[0], i2[1], 0, i2[2], i2[3], i2[4], i2[5], "")
with open("treeout.txt", 'w') as f: f.write(dTree)