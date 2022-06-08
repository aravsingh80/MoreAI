import random
import math
k = 6
with open("star_data.csv") as f: line_list = [line.strip() for line in f]
dataSetWithType = []
dataSet = []
for x in line_list[1:]:
    dataPoint = x.split(",")
    dataSetWithType.append((float(dataPoint[0]), float(dataPoint[1]), float(dataPoint[2]), float(dataPoint[3]), int(dataPoint[4])))
    dataSet.append((math.log(float(dataPoint[0])), math.log(float(dataPoint[1])), math.log(float(dataPoint[2])), float(dataPoint[3])))
def kMeans():
    m = random.sample(dataSet, k)
    means = []
    for x in m: means.append([x, []])
    mBool = False
    while mBool == False:
        for x in dataSetWithType:
            d1, d2, d3, d4, type = x
            value = 0
            count = 0
            minValue = 0
            for y in means:
                m1, m2, m3, m4 = y[0]
                sqError = ((m1-math.log(d1))**2)+((m2-math.log(d2))**2)+((m3-math.log(d3))**2)+((m4-d4)**2)
                if count == 0: minValue = sqError
                if sqError < minValue:
                    minValue = sqError
                    value = count
                count += 1
            count = 0
            for y in means:
                if count == value:
                    y2 = y[1]
                    y2.append(x)
                    means[count] = [y[0], y2]
                    break
                count += 1
        newMeans = []
        for x in means:
            starList = x[1]
            s1 = 0
            s2 = 0
            s3 = 0
            s4 = 0
            for y in starList:
                y1, y2, y3, y4, type = y
                s1 += math.log(y1)
                s2 += math.log(y2)
                s3 += math.log(y3)
                s4 += y4
            if len(starList) > 0:
                s1 /= len(starList)
                s2 /= len(starList)
                s3 /= len(starList)
                s4 /= len(starList)
                newMeans.append([(s1, s2, s3, s4), x[1]])
            else: newMeans.append([x[0], x[1]])
        mBool = True
        count = 0
        for x in means:
            m1, m2, m3, m4 = x[0]
            n1, n2, n3, n4 = newMeans[count][0]
            if (m1) != (n1) or (m2) != (n2) or (m3) != (n3) or (m4) != (n4):
                mBool = False
                break
            count += 1
        if mBool == False:
            means.clear()
            for x in newMeans: means.append([x[0], []])
        else: means = newMeans
    return means

m = kMeans()

for x in m:
    print("MEAN:", x[0])
    for z in x[1]:
        z1, z2, z3, z4, t = z
        preZ = (z1, z2, z3, z4)
        print("    ", preZ, ":", t)
    print("    ", "END")