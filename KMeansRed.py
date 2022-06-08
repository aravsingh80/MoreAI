import urllib.request
import io
import random
import sys
import time
from PIL import Image
# URL = sys.argv[1]
# k = int(sys.argv[2])
URL = 'https://i.pinimg.com/originals/95/2a/04/952a04ea85a8d1b0134516c52198745e.jpg'
k = 8
f = io.BytesIO(urllib.request.urlopen(URL).read()) 
img = Image.open(f)
width, height = img.size
pix = img.load()
dataSet = dict()
for x in range(0, width):
    for y in range(0, height): dataSet[(x, y)] = pix[x, y] 
def kMeans(k):
    means = []
    points = set()
    m = random.sample(list(dataSet), 1)[0]
    means.append([m, dataSet[m], []])
    points.add(m)
    count = 0
    while len(means) < k:
        ogLen = len(means)
        vals = []
        totalVal = 0
        for y in dataSet: 
            if y not in points:
                x1, x2, x3 = means[count][1]
                y1, y2, y3 = dataSet[y]
                vals.append([((((x1-y1)**2)+((x2-y2)**2)+((x3-y3)**2))/3)**2, y])
                totalVal += (((((x1-y1)**2)+((x2-y2)**2)+((x3-y3)**2))/3)**2)
        for x in range(0, len(vals)): vals[x][0] = vals[x][0] / totalVal
        r = random.random()
        tot = 0
        c = 0
        while tot < r:
            tot += vals[c][0]
            if tot > r: 
                means.append([vals[c][1], dataSet[vals[c][1]], []])
                break
            c += 1
        if ogLen != len(means): count += 1
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
colors = set()
def sqError(newCol):
    r, g, b = newCol
    value = 0
    count = 0
    minValue = 0
    for z in numMeans:
        z1, z2, z3 = z[1]
        sqError = (((z1-r)**2)+((z2-g)**2)+((z3-b)**2))/3
        if count == 0: minValue = sqError
        else:
            if sqError < minValue:
                value = count
                minValue = sqError
        count += 1
    r2, g2, b2 = numMeans[value][1]
    p = (int(r2), int(g2), int(b2))
    return p
for x in numMeans:
    r, g, b = x[1]
    p = (int(r), int(g), int(b))
    for y in x[2]: numDict[y[0]] = p
for y in range(height):
    for x in range(width): 
        colors.add(numDict[(x, y)])
        oldPixel = dataSet[(x, y)]
        r, g, b = oldPixel
        newPixel = numDict[(x, y)]
        r2, g2, b2 = newPixel
        r_error = r - r2
        g_error = g - g2
        b_error = b - b2
        if x + 1 < width: pix[x + 1, y] = sqError((pix[x + 1, y][0] + round(r_error * (7/16)), pix[x + 1, y][1] + round(g_error * (7/16)), pix[x + 1, y][2] + round(b_error * (7/16))))
        if y + 1 < height: pix[x, y + 1] = sqError((pix[x, y + 1][0] + round(r_error * (5/16)), pix[x, y + 1][1] + round(g_error * (5/16)), pix[x, y + 1][2] + round(b_error * (5/16))))
        if x - 1 > 0 and y + 1 < height: pix[x - 1, y + 1] = sqError((pix[x - 1, y + 1][0] + round(r_error * (3/16)), pix[x - 1, y + 1][1] + round(g_error * (3/16)), pix[x - 1, y + 1][2] + round(b_error * (3/16))))
        if x + 1 < width and y + 1 < height: pix[x + 1, y + 1] = sqError((pix[x + 1, y + 1][0] + round(r_error * (1/16)), pix[x + 1, y + 1][1] + round(g_error * (1/16)), pix[x + 1, y + 1][2] + round(b_error * (1/16))))
bandLen = height + int(width / len(colors))
bLen = int(width / len(colors))
img2 = Image.new('RGB', (width, bandLen), 0)
pix2 = img2.load()
for x in range(0, width):
    for y in range(0, height): pix2[x, y] = pix[x, y]
count = 0
for z in colors:
    for x in range(count, count + bLen):
        for y in range(height, height + bLen): pix2[x, y] = z
    count += bLen
img2.show()
img2.save("kmeansout.png")