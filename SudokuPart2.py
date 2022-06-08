import sys
import random
import time
import copy
s = sys.argv[1]
with open(s) as f:
    puzzles = [line.strip() for line in f]

N = 0
subLockHeight = 0
subLockWidth = 0
neighbors2 = dict()
rows2 = []
columns2 = []
blocks2 = []
constraintValues = []
board = dict()
letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers_set = dict()
symbol_set = dict()

def getAllValues():
    s = ""
    for x in range(1, N + 1): 
        if x < 10: s += str(x)
        else: s += numbers_set[x]
    return s

def createBoard(puzzle2):
    b = dict()
    count = 0
    s = getAllValues()
    for x in puzzle2:
        if x == ".": b[count] = s
        else: b[count] = x
        count += 1
    return b
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
        for y in range(0, size):
            row.add((x * size) + y)
            column.add((y * size) + x)
        rows.append(row)
        columns.append(column)
    block = set()
    for a in range(0, size, sHeight):
        for x in range(0, size):
            for y in range(0, sHeight):
                temp = y
                y += a
                block.add((x * size) + y)
                if (x + 1) % sWidth == 0 and temp == sHeight - 1:
                    temp = copy.copy(block)
                    blocks.append(temp)
                    block.clear()
    neighbors = dict()
    x = 0
    for p in puzzle:
        neighbor = set()
        for r in rows:
            if x in r:
                for y in r:
                    if y != x and len(board2[y]) > 1: neighbor.add(y)
        for c in columns:
            if x in c:
                for y in c:
                    if y != x and len(board2[y]) > 1: neighbor.add(y)
        for b in blocks:
            if x in b:
                for y in b: 
                    if y != x and len(board2[y]) > 1: neighbor.add(y)
        neighbors[x] = neighbor
        x += 1
    return (rows, columns, blocks, neighbors)

def get_most_constrained_var(board):
    count = 0
    for x in board:
        if len(board[x]) > 1: break
        count += 1
    min = count
    for x in board:
        if len(board[x]) > 1:
            if len(board[x]) < len(board[min]): min = x
    return min

def goal_test(board):
    for x in board:
        if len(board[x]) > 1: return False
    return True

def constraint_propagation(puzzle):
    for x in constraintValues:
        for x2 in range(1, N + 1):
            count = 0
            c = 0
            value = ""
            if x2 >= 10: value = numbers_set[x2]
            else: value = str(x2)
            for y in x:
                if value in puzzle[y]: 
                    c = y
                    count += 1
                    if count > 1: break
            if count == 0: return None
            if count == 1: puzzle[c] = value 
    return puzzle

def getSortedValues(puzzle, var): return list(set(puzzle[var]))

def forward_looking(puzzle):
    l = {x for x in puzzle if len(puzzle[x]) == 1}
    l2 = copy.copy(l)
    while len(l) > 0:
        for x in l:
            l4 = x
            break
        l3 = list(neighbors2[l4])
        for y in l3:
            puzzle[y] = puzzle[y].replace(puzzle[l4], "")
            if len(puzzle[y]) == 0: return None
            if len(puzzle[y]) == 1 and y not in l2: l.add(y)
            l2.add(y)
        l.remove(l4)
    return puzzle

def csp_backtracking_with_forward_looking(board):
    if goal_test(board): return board
    var = get_most_constrained_var(board)
    x = getSortedValues(board, var)
    for val in x:
        new_puzzle = copy.copy(board)
        new_puzzle[var] = val
        first_checked_board = constraint_propagation(new_puzzle)
        if first_checked_board is not None:
            checked_board = forward_looking(first_checked_board)
            if checked_board is not None: 
                result = csp_backtracking_with_forward_looking(checked_board)
                if result is not None: return result
    return None

for x2 in puzzles:
    N = int(len(x2) ** 0.5)
    subLockWidth = findSublockWidth(N)
    subLockHeight = findSublockHeight(N)
    board2 = createBoard(x2)
    rows2, columns2, blocks2, neighbors2 = getNeighbors(x2)
    for x in rows2: constraintValues.append(x)
    for x in columns2: constraintValues.append(x)
    for x in blocks2: constraintValues.append(x)
    FW = csp_backtracking_with_forward_looking(board2)
    w = ""
    for f in FW: w += FW[f]
    print(w)
    constraintValues.clear()