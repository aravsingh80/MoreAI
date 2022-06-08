import urllib.request
import io
from PIL import Image
URL = 'https://i.ebayimg.com/images/g/xpoAAOSwzuxgmtbQ/s-l300.jpg'
f = io.BytesIO(urllib.request.urlopen(URL).read()) # Download the picture at the url as a file object
img = Image.open(f)
width, height = img.size # You can also use this on a local file; just put the local filename in quotes in place of f.
#img.show() # Send the image to your OS to be displayed as a temporary file
print(img.size) # A tuple. Note: width first THEN height. PIL goes [x, y] with y counting from the top of the frame.
pix = img.load()
dataSet = dict()
for x in range(0, width):
    for y in range(0, height): dataSet[(x, y)] = pix[x, y]  # Pix is a pixel manipulation object; we can assign pixel values and img will change as we do so.
#print(pix[2,5]) # Access the color at a specific location; note [x, y] NOT [row, column].

colors = set()
for x in range(width):
    for y in range(height):
        x1 = 0
        y1 = 0
        z1 = 0
        count = 0
        for z in pix[x, y]:
            if z < (255 // 3): z = 0
            elif z > (255*2//3): z = 255
            else: z = 127
            if count == 0: x1 = z
            elif count == 1: y1 = z
            else: z1 = z
            count += 1
        colors.add((x1, y1, z1))
        pix[x,y] = (x1, y1, z1)
for b in range(0, 20): 
    x, y, z = list(colors)[b]
    colors.add((x - 1, y - 1, z - 1))
print(len(colors))
# colors = set()
# for x in range(width):
#     for y in range(height):
#         x1 = 0
#         y1 = 0
#         z1 = 0
#         count = 0
#         for z in pix[x, y]:
#             if z < 128: z = 0
#             else: z = 255
#             if count == 0: x1 = z
#             elif count == 1: y1 = z
#             else: z1 = z
#             count += 1
#         colors.add((x1, y1, z1))
#         pix[x,y] = (x1, y1, z1)
# colors.add((251,72,196))

for y in range(1, height):
    for x in range(1, width):
        oldPixel = dataSet[(x, y)]
        r, g, b = oldPixel
        newPixel = pix[x, y]
        r2, g2, b2 = newPixel
        r_error = r - r2
        g_error = g - g2
        b_error = b - b2
        if x + 1 < width: pix[x + 1, y] = (pix[x + 1, y][0] + round(r_error * (7/16)), pix[x + 1, y][1] + round(g_error * (7/16)), pix[x + 1, y][2] + round(b_error * (7/16)))
        if y + 1 < height: pix[x, y + 1] = (pix[x, y + 1][0] + round(r_error * (5/16)), pix[x, y + 1][1] + round(g_error * (5/16)), pix[x, y + 1][2] + round(b_error * (5/16)))
        if x - 1 > 0 and y + 1 < height: pix[x - 1, y + 1] = (pix[x - 1, y + 1][0] + round(r_error * (3/16)), pix[x - 1, y + 1][1] + round(g_error * (3/16)), pix[x - 1, y + 1][2] + round(b_error * (3/16)))
        if x + 1 < width and y + 1 < height: pix[x + 1, y + 1] = (pix[x + 1, y + 1][0] + round(r_error * (1/16)), pix[x + 1, y + 1][1] + round(g_error * (1/16)), pix[x + 1, y + 1][2] + round(b_error * (1/16)))

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