import sys; args = sys.argv[1:]
import random
height = int(args[0][0: args[0].index("x")])
width = int(args[0][args[0].index("x") + 1:])
requirement = int(args[1])
s = ""
def checkLegal(puzzle):
    print(puzzle)
    if puzzle != puzzle[::-1]: return False
    rows = []
    columns = []
    count = 0
    for x in range(0, height):
        row = []
        for y in range(0, width): 
            row.append([puzzle[count], count])
            count += 1
        rows.append(row)

    for y in range(0, width):
        column = []
        count = y
        for y in range(0, height): 
            column.append([puzzle[count], count])
            count += width
        columns.append(column)

    middleRows = []
    firstRow = True
    lastRow = True 
    totalCount = 0
    count3 = 0
    for x in rows:
        count = 0
        count2 = 0
        for y in x:
            if y[0] != "#": count += 1
            else:
                if count < 3 and count != 0: return False
                count = 0
                count2 += 1
        if count2 == width: 
            if count3 == 0: firstRow = False
            elif count3 == len(rows) - 1: lastRow = False
            else: middleRows.append(count3)
            totalCount += 1
        if count < 3 and count != 0: return False
        count3 += 1
    if totalCount > 0 and not firstRow and not lastRow: return False
    if totalCount != count3:
        if firstRow:
            b = False
            num = 1
            for x in middleRows:
                if b: 
                    if x - 1 != num: return False
                    else: num = x
                if x == 1: b = True
        if lastRow:
            b = False
            num = count3 - 1
            middleRows = middleRows[::-1]
            for x in middleRows:
                if b: 
                    if x + 1 != num: return False
                    else: num = x
                if x == count3 - 2: b = True

    middleRows = []
    firstRow = True
    lastRow = True 
    totalCount = 0
    count3 = 0
    for x in columns:
        count = 0
        count2 = 0
        for y in x:
            if y[0] != "#": count += 1
            else:
                if count < 3 and count != 0: return False
                count = 0
                count2 += 1
        if count2 == height: 
            if count3 == 0: firstRow = False
            elif count3 == len(rows) - 1: lastRow = False
            else: middleRows.append(count3)
            totalCount += 1
        if count < 3 and count != 0: return False
        count3 += 1
    if totalCount > 0 and not firstRow and not lastRow: return False
    if totalCount != count3:
        if firstRow:
            b = False
            num = 1
            for x in middleRows:
                if b: 
                    if x - 1 != num: return False
                    else: num = x
                if x == 1: b = True
        if lastRow:
            b = False
            num = count3 - 1
            middleRows = middleRows[::-1]
            for x in middleRows:
                if b: 
                    if x + 1 != num: return False
                    else: num = x
                if x == count3 - 2: b = True
    
    corners = [0, width - 1, len(puzzle) - 1, len(puzzle) - width]
    topEdge = [x for x in range(0, width)]
    bottomEdge = [x for x in range(len(puzzle) - width, len(puzzle))]
    leftEdge = [x for x in range(0, len(puzzle) - width + 1, width)]
    rightEdge = [x for x in range(width - 1, len(puzzle), width)]
    diagonals = []
    for x in range(0, len(puzzle)):
        diagonal = []
        if x != width - 1 and x != len(puzzle) - 1 and x != len(puzzle) - width and x in topEdge and x in leftEdge:
            diagonal.append(puzzle[x])
            num = x + width + 1
            while num not in corners and num not in rightEdge and num not in bottomEdge:
                diagonal.append(puzzle[num])
                num += width + 1
            diagonal.append(puzzle[num])
            diagonals.append(diagonal)

    for x in range(0, len(puzzle)):
        diagonal = []
        if x != width - 1 and x != 0 and x != len(puzzle) - width and x in rightEdge and x in bottomEdge:
            diagonal.append(puzzle[x])
            num = x - width - 1
            while num not in corners and num not in leftEdge and num not in topEdge:
                diagonal.append(puzzle[num])
                num -= (width + 1)
            diagonal.append(puzzle[num])
            diagonals.append(diagonal)

    for x in diagonals:
        if all(y == "#" for y in x): return False

    for x in range(0, len(puzzle)):
        if puzzle[x] != "#":
            activeSpaces = 0
            count = 0
            if x - 1 >= 0: 
                if puzzle[x - 1] == "#": count += 1
                activeSpaces += 1
            if x + 1 < (int(x / width) + 1) * width and x + 1 < len(puzzle): 
                if puzzle[x + 1] == "#": count += 1
                activeSpaces += 1
            if x - width >= 0: 
                if puzzle[x - width] == "#": count += 1
                activeSpaces += 1
            if x + width < len(puzzle): 
                if puzzle[x + width] == "#": count += 1
                activeSpaces += 1
            if count == activeSpaces and count != 0: 
                return False
    return True

def getSortedValues(puzzle): 
    return {x for x in range(0, len(puzzle)) if puzzle[x] == "-" and puzzle[len(puzzle) - 1 - x] == "-" and checkLegal(puzzle[0: x: 1] + "#" + puzzle[x + 1: len(puzzle) - 1 - x: 1] + "#" + puzzle[len(puzzle) - x:])}

def getBlockCount(puzzle):
        blockCount = 0
        for x in puzzle:
            if x == "#": blockCount += 1
        return blockCount

def getNextSpace(puzzle): return puzzle.index("-")

def csp_backtracking(puzzle):
    if checkLegal(puzzle) and getBlockCount(puzzle) == requirement: return puzzle
    x = getSortedValues(puzzle)
    print(x)
    while len(x) > 0:
        var = random.choice(list(x))
        new_puzzle = puzzle
        new_puzzle = puzzle[0: var: 1] + "#" + puzzle[var + 1: len(puzzle) - 1 - var: 1] + "#" + puzzle[len(puzzle) - var:]
        x.remove(var)
        result = csp_backtracking(new_puzzle)
        if result is not None: return result
    return None

if requirement == (height * width):
    for x in range(0, requirement): s += "#"
else:
    for x in range(0, height * width): s += "-"
    if len(args) > 2: 
        for x in args[2:]:
            first = x[0]
            r = int(x[1: x.index("x"): 1])
            count = x.index("x") + 1
            b = False
            for y in x[x.index("x") + 1:]:
                if y.isalpha() or y == "#": 
                    b = True
                    break
                count += 1
            c = int(x[x.index("x") + 1: count: 1])
            pos = (r * width) + c
            if not b: s = s[0: pos: 1] + "#" + s[pos + 1:]
            else:
                word = x[count:]
                if first == "H" or first == "h":
                    for y in word:
                        s = s[0: pos: 1] + y + s[pos + 1:]
                        pos += 1
                if first == "V" or first == "v":
                    for y in word:
                        s = s[0: pos: 1] + y + s[pos + 1:]
                        pos += width
    print(s)
    # count = 0
    # for x in range(0, height):
    #     s2 = ""
    #     for y in range(0, width): 
    #         s2 += s[count] + " "
    #         count += 1
    #     print(s2)
    if requirement != 0:
        s2 = csp_backtracking(s)
        s = s2[len(s2) - 1]
count = 0
for x in range(0, height):
    s2 = ""
    for y in range(0, width): 
        s2 += s[count] + " "
        count += 1
    print(s2)
# Arav Singh, 2, 2023