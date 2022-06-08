import urllib.request
import io
import random
import sys
import time
from PIL import Image
#URL = 'https://i.pinimg.com/originals/95/2a/04/952a04ea85a8d1b0134516c52198745e.jpg'
URL = sys.argv[1]
k = int(sys.argv[2])
# start = time.perf_counter()
f = io.BytesIO(urllib.request.urlopen(URL).read()) 
img = Image.open(f)
width, height = img.size
pix = img.load()
dataSet = dict()
for x in range(0, width):
    for y in range(0, height): dataSet[(x, y)] = pix[x, y] 
def kMeans(k):
    means = []
    points = []
    colors = []
    for z in range(0, k):
        m = random.sample(list(dataSet), 1)[0]
        while dataSet[m] in colors or m[0] in points: m = random.sample(list(dataSet), 1)[0]
        means.append([m[0], dataSet[m], []])
        points.append(m[0])
        colors.append(dataSet[m])
    mBool = False
    while mBool == False:
        meanValues = []
        count = 0
        for x in means:
            vals = []
            count2 = 0
            x1, x2, x3 = x[1]
            for y in means:
                y1, y2, y3 = y[1]
                if count2 != count: vals.append((((x1-y1)**2)+((x2-y2)**2)+((x3-y3)**2))/3)
                count2 += 1
            count += 1
            meanValues.append([x, 0.25 * min(vals)])
        for x in dataSet:
            r, g, b = dataSet[x]
            value = 0
            count = 0
            minValue = 0
            b2 = False
            for y in meanValues:
                m1, m2, m3 = y[0][1]
                sqError = (((m1-r)**2)+((m2-g)**2)+((m3-b)**2))/3
                if sqError < y[1]:
                    y2 = y[0][2]
                    y2.append([x, dataSet[x]])
                    means[count] = [y[0][0], y[0][1], y2]
                    b2 = True
                    break
                count += 1
            if not b2:
                count = 0
                for y in means:
                    m1, m2, m3 = y[1]
                    sqError = ((m1-r)**2)+((m2-g)**2)+((m3-b)**2)
                    if count == 0: minValue = sqError
                    if sqError < minValue:
                        minValue = sqError
                        value = count
                    count += 1
                count = 0
                for y in means:
                    if count == value:
                        y2 = y[2]
                        y2.append([x, dataSet[x]])
                        means[count] = [y[0], y[1], y2]
                        break
                    count += 1
        newMeans = []
        for x in means:
            colorList = x[2]
            s1 = 0
            s2 = 0
            s3 = 0
            for y in colorList:
                y1, y2, y3 = y[1]
                s1 += y1 
                s2 += y2
                s3 += y3
            if len(colorList) > 0:
                s1 /= len(colorList)
                s2 /= len(colorList)
                s3 /= len(colorList)
                newMeans.append([x[0], (s1, s2, s3), x[2]])
            else: newMeans.append([x[0], x[1], x[2]])
        mBool = True
        count = 0
        for x in means:
            m1, m2, m3 = x[1]
            n1, n2, n3 = newMeans[count][1]
            if (m1) != (n1) or (m2) != (n2) or (m3) != (n3):
                mBool = False
                break
            count += 1
        if mBool == False:
            means.clear()
            for x in newMeans: means.append([x[0], x[1], []])
        else: means = newMeans
    return means
numMeans = kMeans(k)
numDict = dict()
for x in numMeans:
    r, g, b = x[1]
    p = (int(r), int(g), int(b))
    for y in x[2]: numDict[y[0]] = p
for x in range(width):
    for y in range(height): pix[x, y] = numDict[(x, y)]
# end = time.perf_counter()
# s2 = "%s" % (end - start)
# print(s2)
img.show() 
img.save("kmeansout.png")