from colorama import init, Back, Fore
import sys
import re
s = sys.argv[1]
init()
backslash = s[1:].index("/") + 1
flags = s[backslash + 1:]
s2 = "While inside they wined and dined, safe from the howling wind.\nAnd she whined, it seemed, for the 100th time, into the ear of her friend,\nWhy indeed should I wind the clocks up, if they all run down in the end?"
color = Back.LIGHTRED_EX
l = 0
if len(flags) == 3: f = re.I | re.S | re.M
if len(flags) == 2: 
    if flags == "im" or flags == "mi": f = re.I | re.M
    if flags == "is" or flags == "si": f = re.I | re.S
    if flags == "sm" or flags == "ms": f = re.S | re.M
if len(flags) == 1: 
    if flags == "i": f = re.I
    if flags == "m": f = re.M
    if flags == "s": f = re.S
if len(flags) == 0: exp = re.compile(r""+s[1: backslash])
else: exp = re.compile(r""+s[1: backslash], f)
b = True
b2 = True
c = [-99, -99]
matches = []
num = 0
for x2 in exp.finditer(s2):
    b2 = True 
    x, y = x2.span()
    elem = (s2[num : x], s2[x : y], Back.LIGHTRED_EX, y)
    if b and (x - 1 == c[1] or c[0] <= x <= c[1]): 
        elem = (s2[num : x], s2[x : y], Back.GREEN, y)
        b = False
        b2 = False
    l += 1
    c = [x, y]
    matches.append(elem)
    num = y
    if b2: b = True
s3 = ""
count = 0
for x2 in matches:
    s4, s5, color, y = x2 
    s3 += s4 + color + s5 + Back.RESET
    count += 1
    if len(matches) == count and y != len(s2) - 1: s3 += s2[y:]
print(s3)