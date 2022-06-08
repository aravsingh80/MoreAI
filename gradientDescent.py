import math
import sys
let = sys.argv[1]
def aDescent(point):
    x, y = point
    a1 = (8*x) - (3*y) + 24
    a2 =  (-3*x) + (4*y) - 20
    return (a1, a2)
def bDescent(point):
    x, y = point
    b1 = (2*x)-(2*y*y)
    b2 = -2+(2*y)-(4*x*y)+(4*y*y*y)
    return (b1, b2)
if let == "A" or let == "a": f = aDescent
if let == "B" or let == "b": f = bDescent 
lam = 0.1
currPoint = (0, 0)
val = f(currPoint)
def magnitude(point):
    x, y = point
    z = math.sqrt((x**2) + (y**2))
    return z
count = 0
while magnitude(val) > (10**-8): 
    print("Current Location:", currPoint)
    print("Current Gradient:", val)
    print()
    x, y = currPoint
    x1, y1 = val
    x -= (x1 * lam)
    y -= (y1 * lam)
    currPoint = (x, y)
    val = f(currPoint)
    count += 1
print(count)