import math
import sys
let = sys.argv[1]
def a(point):
    x, y = point
    return (4*x*x)-(3*x*y)+(2*y*y)+(24*x)-(20*y)
def b(point):
    x, y = point
    return ((1-y)*(1-y)) + ((x-(y*y))**2)
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
if let == "A" or let == "a": 
    f = aDescent
    ogF = a
if let == "B" or let == "b": 
    f = bDescent 
    ogF = b
lam = 0.1
currPoint = (0, 0)
val = f(currPoint)
def magnitude(point):
    x, y = point
    z = math.sqrt((x**2) + (y**2))
    return z
def one_d_minimize(f, left, right, tolerance):
    if (right - left) < tolerance: return (right + left) / 2
    else:
        oneThird = left + ((right - left) / 3)
        twoThird = left + (2 * ((right - left) / 3))
        if f(oneThird) > f(twoThird): return one_d_minimize(f, oneThird, right, tolerance)
        else: return one_d_minimize(f, left, twoThird, tolerance)
def make_funct(x1, x, y1, y, f):
    def funct(l): return f((x - (l*x1), y - (l*y1)))
    return funct
while magnitude(val) > (10**-8): 
    print("Current Location:", currPoint)
    print("Current Gradient:", val)
    print()
    x, y = currPoint
    x1, y1 = val
    g = make_funct(x1, x, y1, y, ogF)
    lam = one_d_minimize(g, 0, 5, (10**-8)) #line optimization
    x -= (x1 * lam)
    y -= (y1 * lam)
    currPoint = (x, y)
    val = f(currPoint)