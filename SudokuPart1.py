import sys
import random
import time
s = "puzzles_1_standard_easy.txt"
with open(s) as f:
    puzzles = [line.strip() for line in f]

N = 0
subLockHeight = 0
subLockWidth = 0
neighbors2 = dict()
letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers_set = dict()
symbol_set = dict()
def findSublockHeight(N2):
    if int(N2 ** 0.5) == (N2 ** 0.5):
        return int(N2 ** 0.5)
    else:
        x = int(N2 ** 0.5) + 1
        while N2 % x != 0:
            x += 1
        return x
def findSublockWidth(N2):
    if int(N2 ** 0.5) == (N2 ** 0.5):
        return int(N2 ** 0.5)
    else:
        x = int(N2 ** 0.5)
        while N2 % x != 0:
            x -= 1
        return x

for y in range(10, 36):
    symbol_set[letters[y - 10]] = y
    numbers_set[y] = letters[y - 10]

def displayBoard(puzzle, N):
    s = ""
    count = 1
    for x in puzzle:
        if x in letters:
            s += str(symbol_set[x])
            s += " "
        elif x == ".":
            s += " x "
        else:
            s += " "
            s += x 
            s += " "
        if count % N == 0:
            print(s)
            s = ""
        count += 1

def getNeighbors(puzzle):
    size = int(len(puzzle) ** 0.5)
    sHeight = subLockHeight
    sWidth = subLockWidth
    rows = []
    columns = []
    blocks = []
    for x in range(0, size):
        row = set()
        column = set()
        row.clear()
        column.clear()
        for y in range(0, size):
            row.add((x * size) + y)
            column.add((y * size) + x)
        rows.append(row)
        columns.append(column)
    # row = set()
    # for x in range(0, len(puzzle)):
    #     row.add(x)
    #     if x == N - 1: 
    #         temp = row.copy()
    #         rows.append(temp)
    #         row.clear()
    # c = dict()
    # for x in range(0, N):
    #     c[x] = set()
    # for x in range(0, len(puzzle)):
    #     c[x % N].add(x)
    # for x in c:
    #     columns.append(c[x])
    block = set()
    for a in range(0, size, sHeight):
        for x in range(0, size):
            for y in range(0, sHeight):
                temp = y
                y += a
                block.add((x * size) + y)
                if (x + 1) % sWidth == 0 and temp == sHeight - 1:
                    temp = block.copy()
                    blocks.append(temp)
                    block.clear()
    neighbors = dict()
    x = 0
    for p in puzzle:
        neighbor = set()
        for r in rows:
            if x in r:
                for y in r:
                    if y != x: neighbor.add(y)
        for c in columns:
            if x in c:
                for y in c:
                    if y != x: neighbor.add(y)
        for b in blocks:
            if x in b:
                for y in b: 
                    if y != x: neighbor.add(y)
        neighbors[x] = neighbor
        x += 1
    return neighbors

def getNextSpace(puzzle):
    return puzzle.index(".")

def symbolInstances(puzzle):
    instances = dict()
    for x in puzzle:
        if x in symbol_set:
            if x not in instances:
                instances[x] = 1
            else:
                instances[x] += 1
    return instances

def goal_test(puzzle):
    return "." not in puzzle

def getSortedValues(puzzle, var):
    values = set()
    v = set()
    n = neighbors2[var]
    for y in n:
        if puzzle[y] != ".": 
            if puzzle[y] not in symbol_set: v.add(int(puzzle[y]))
            else: v.add(int(symbol_set[puzzle[y]]))
    for x in range(1, int(len(puzzle) ** 0.5) + 1):
        if x not in v:
            if x <= 9 : values.add(str(x))
            else: values.add(numbers_set[x])
    return sorted(values)


def csp_backtracking(puzzle):
    if goal_test(puzzle): return puzzle
    var = getNextSpace(puzzle)
    x = getSortedValues(puzzle, var)
    print(x)
    while len(x) > 0:
        val = random.choice(list(x))
        new_puzzle = list(puzzle)
        new_puzzle[var] = val
        x.remove(val)
        result = csp_backtracking(''.join(new_puzzle))
        if result is not None: return result
    return None
count = 0
for x in puzzles:
    if count == 2:
        N = int(len(x) ** 0.5)
        subLockWidth = findSublockWidth(N)
        subLockHeight = findSublockHeight(N)
        neighbors2 = getNeighbors(x)
        print(csp_backtracking(x))
    count += 1
        
