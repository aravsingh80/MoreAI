import sys
import re
errorFile = sys.argv[1]
templines = []
with open(errorFile) as f:
    for line in f: templines.append(line.rstrip())
colonRegex = r"^(if|for|while|def).*(?!.*:).$"
lines = []
count = 0
for line in templines: 
    if "#" in templines[count]: lines.append(templines[count][0:templines[count].index("#")].strip())
    else: lines.append(templines[count].strip())
    count += 1
print("A colon is missing")
exp = re.compile(colonRegex)
count = 1
for x in lines:
    if exp.match(x): print(count)
    count += 1
print()
digitBeforeVarNameRegex = r"^\d(?=.*=)(?!.*(==)).*$"
print("A digit is the first character in a variable name")
exp = re.compile(digitBeforeVarNameRegex)
count = 1
for x in lines:
    if exp.match(x): print(count)
    count += 1
print()
equalBeforeDoubleEqual = r"^(if|return|while)(?!.*!)(?=.*=)(?!.*(==)).*$"
print("A = is used instead of a ==")
exp = re.compile(equalBeforeDoubleEqual)
count = 1
for x in lines:
    if exp.match(x): print(count)
    count += 1
print()
funcNamesAndNumCommas = dict()
for x in lines:
    if "def" in x:
        numRegex = r","
        name = x[x.index(" ") + 1: x.index("(")]
        numCommas = 0
        for x in re.compile(numRegex).finditer(x[x.index("("):]): numCommas += 1
        funcNamesAndNumCommas[name] = numCommas
print("The wrong number of arguments was used when calling a function")
for x in funcNamesAndNumCommas:
    if funcNamesAndNumCommas[x] == 0: wrongArgsRegex = r"^(?=.*"+x+r").*(?=.*,)([^,]*,){1,}[^,]*$"
    else: wrongArgsRegex = r"^(?=.*"+x+r")[^,]*$|^(?=.*"+x+r")(?=.*,)([^,]*,){0, "+str(funcNamesAndNumCommas[x]-1)+r"}[^,]*$|^(?=.*"+x+r")(?=.*,)([^,]*,){"+str(funcNamesAndNumCommas[x]+1)+r",}[^,]*$"
    exp = re.compile(wrongArgsRegex)
    count = 1
    for y in lines:
        if exp.match(y): print(count)
        count += 1
print()
variables = dict()
count = 1
for x in lines:
    exp = re.compile(r"^(?!.*if)(?!.*return)(?!.*while)(?=.*=).*$")
    if exp.match(x) and x not in variables: variables[x[0:x.index("=")].strip()] = count
    count += 1
lineNums = set()
print("A variable was called before it was defined")
for x in variables:
    varBeforeCalledRegex = r"^.*"+x+r".*$"
    exp = re.compile(varBeforeCalledRegex)
    count = 1
    for y in lines:
        if exp.match(y) and count < variables[x]: lineNums.add(count)
        count += 1
for x in sorted(lineNums): print(x)