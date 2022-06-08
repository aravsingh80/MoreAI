import urllib.request
import io
import random
import sys
import time
from PIL import Image
URL = 'https://i.ebayimg.com/images/g/xpoAAOSwzuxgmtbQ/s-l300.jpg'
k = 8
# URL = sys.argv[1]
# k = int(sys.argv[2])
# start = time.perf_counter()
f = io.BytesIO(urllib.request.urlopen(URL).read()) 
img = Image.open(f)
width, height = img.size
pix = img.load()
dataSet = dict()
for x in range(0, width):
    for y in range(0, height): dataSet[(x, y)] = pix[x, y] 
def newKmeans(k):
    means = []
    points = []
    m = random.sample(list(dataSet), 1)[0]
    means.append([m, dataSet[m], []])
    points.append(m)
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