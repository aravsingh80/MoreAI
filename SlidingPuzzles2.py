import sys
import time
from collections import deque
from heapq import heappush, heappop, heapify
s = sys.argv[1]
with open(s) as f:
    line_list = [line.strip() for line in f]
def GoalTest(v):
    s = ""
    for x in v:
        s += x
    return s == find_goal(s)

def print_puzzle(x, y):
    s = ""
    for x2 in range(0, len(y)):
        s += y[x2]
        if x2 % int(x) == (int(x) - 1):
            print(s)
            s = ""

def nonOrderPairCount(board, size):
    count = 0
    for x in range(0, size):
        for y in range(x + 1, size):
            if board[x] != "." and board[y] != ".":
                if board[x] > board[y]:
                    count += 1
    return count
                

def parity(board, size):
    m = []
    y = []
    non = nonOrderPairCount(board, len(board))
    for x2 in range(0, len(board)):
        y.append(board[x2])
        if x2 % int(size) == (int(size) - 1):
            m.append(y)
            y = []
        x = 0
    y = 0
    b = False
    size = int(size)
    for x2 in range(0, size):
        for x3 in range(0, size):
            if m[x2][x3] == '.':
                x = x2
                y = x3
                b = True
            if b:
                break
        if b:
            break
    if size % 2 == 0:
        if x % 2 == 0 and non % 2 == 1:
            return True
        elif x % 2 == 1 and non % 2 == 0:
            return True
        else:
            return False
    else:
        if non % 2 == 0:
            return True
        else:
            return False
def find_goal(board):
    s = ""
    for x in board:
        if x != ".":
            s += x
    s = ''.join(sorted(s)) 
    s += "."
    return s

def swap(x, y, x2, y2, m):
    m2 = m
    temp = m2[x][y]
    m2[x][y] = m2[x2][y2]
    m2[x2][y2] = temp
    return m2

def tostr(m):
    temp = ""
    for x in range(len(m)):
            temp += ''.join(m[x])
    return temp

def directionchildren(board, size):
    m5 = []
    y = []
    m9 = []
    for x2 in range(0, len(board)):
        y.append(board[x2])
        if x2 % int(size) == (int(size) - 1):
            m5.append(y)
            y = []
    boardset = set()
    x = 0
    y = 0
    b = False
    size = int(size)
    for x2 in range(0, size):
        for x3 in range(0, size):
            if m5[x2][x3] == '.':
                x = x2
                y = x3
                b = True
            if b:
                break
        if b:
            break
    if x > 0:
        temp = swap(x, y, x - 1, y, m5)
        temp2 = tostr(temp)
        boardset.add(temp2)
        m9.append("U")
        m5 = swap(x, y, x - 1, y, m5)
    if y > 0:
        temp = swap(x, y, x, y - 1, m5)
        temp2 = tostr(temp)
        boardset.add(temp2)
        m9.append("L")
        m5 = swap(x, y, x, y - 1, m5)
    if x < size - 1:
        temp = swap(x, y, x + 1, y, m5)
        temp2 = tostr(temp)
        boardset.add(temp2)
        m9.append("D")
        m5 = swap(x, y, x + 1, y, m5)
    if y < size - 1:
        temp = swap(x, y, x, y + 1, m5)
        temp2 = tostr(temp)
        boardset.add(temp2)
        m9.append("R")
        m5 = swap(x, y, x, y + 1, m5)
    return m9

def get_children(board, size):
    m = []
    y = []
    for x2 in range(0, len(board)):
        y.append(board[x2])
        if x2 % int(size) == (int(size) - 1):
            m.append(y)
            y = []
    boardset = set()
    x = 0
    y = 0
    b = False
    size = int(size)
    for x2 in range(0, size):
        for x3 in range(0, size):
            if m[x2][x3] == '.':
                x = x2
                y = x3
                b = True
            if b:
                break
        if b:
            break
    if x > 0:
        temp = swap(x, y, x - 1, y, m)
        temp2 = tostr(temp)
        boardset.add(temp2)
        m = swap(x, y, x - 1, y, m)
    if y > 0:
        temp = swap(x, y, x, y - 1, m)
        temp2 = tostr(temp)
        boardset.add(temp2)
        m = swap(x, y, x, y - 1, m)
    if x < size - 1:
        temp = swap(x, y, x + 1, y, m)
        temp2 = tostr(temp)
        boardset.add(temp2)
        m = swap(x, y, x + 1, y, m)
    if y < size - 1:
        temp = swap(x, y, x, y + 1, m)
        temp2 = tostr(temp)
        boardset.add(temp2)
        m = swap(x, y, x, y + 1, m)
    return boardset

def findCoordinate(value, board, size):
    x = board.index(value)
    return (x / size, x % size)

def bfs(startnode, size):
    fringe = deque()
    visited = set()
    fringe.append((startnode, 0))
    visited.add(startnode)
    while len(fringe) > 0:
        v, moves = fringe.popleft()
        if GoalTest(v):
            return moves
        for c in get_children(v, size):
            if c not in visited:
                fringe.append((c, moves + 1))
                visited.add(c)
    return None

def heuristic(startstate):
    size = int(len(startstate) ** 0.5)
    count = 0
    for x in startstate:
        if x != ".":
            y, y1 = findCoordinate(x, startstate, size)
            z, z1 = findCoordinate(x, find_goal(startstate), size)
            y2 = abs(y - z)
            z2 = abs(y1 - z1)
            count += y2 + z2
    return count 


def kdfs(startstate, k):
    fringe = list()
    a = set()
    a.add(startstate)
    startnode = (startstate, 0, a)
    fringe.append(startnode)
    while len(fringe) > 0:
        v, depth, ancestors = fringe.pop()
        if GoalTest(v):
            return depth
        if depth < k:
            for c in get_children(v, int(len(startstate) ** 0.5)):
                if c not in ancestors:
                    tA = ancestors.copy()
                    tA.add(c)
                    temp = (c, depth + 1, tA)
                    fringe.append(temp)
    return None
def iddfs(startstate):
    max_depth = 0
    result = None
    while result is None:
        result = kdfs(startstate, max_depth)
        max_depth = max_depth + 1
    return result

def astar(startstate):
    closed = set()
    startnode = (heuristic(startstate), 0, startstate)      
    fringe = []
    heappush(fringe, startnode)
    while len(fringe) > 0:
        f, depth, v = heappop(fringe)
        if GoalTest(v):
            return depth 
        if v not in closed:
            closed.add(v)
            for c in get_children(v, int(len(startstate) ** 0.5)):
                if c not in closed:
                    temp = (depth + 1 + heuristic(c), depth + 1, c)
                    heappush(fringe, temp)
    return None

count = 0
for x in line_list:
    x2 = x[0]
    y2 = x[2 : len(x) - 2 : 1]
    z2 = x[len(x) - 1 : len(x) : 1]
    s = ""
    start = time.perf_counter()
    if parity(y2, x2) == False:
        end = time.perf_counter()
        s2 = "%s" % (end - start)
        print("Line", str(count) + ":", str(y2) + ",", "no solution determined in", s2, "seconds")
        count += 1
    else:
        if z2 == "!":
            start = time.perf_counter()
            s = bfs(y2, x2)
            end = time.perf_counter()
            s2 = "%s" % (end - start)
            print("Line", str(count) + ":", str(y2) + ", BFS -", s,"moves found in", s2, "seconds")
            start = time.perf_counter()
            s = iddfs(y2)
            end = time.perf_counter()
            s2 = "%s" % (end - start)
            print("Line", str(count) + ":", str(y2) + ", ID-DFS -", s,"moves found in", s2, "seconds")
            start = time.perf_counter()
            s = astar(y2)
            end = time.perf_counter()
            s2 = "%s" % (end - start)
            print("Line", str(count) + ":", str(y2) + ", A* -", s,"moves found in", s2, "seconds")
            count += 1
        elif z2 == "B":
            start = time.perf_counter()
            s = bfs(y2, x2)
            end = time.perf_counter()
            s2 = "%s" % (end - start)
            print("Line", str(count) + ":", str(y2) + ", BFS -", s,"moves found in", s2, "seconds")
            count += 1
            s = str(bfs(y2, x2)) + " found"
        elif z2 == "I":
            start = time.perf_counter()
            s = iddfs(y2)
            end = time.perf_counter()
            s2 = "%s" % (end - start)
            print("Line", str(count) + ":", str(y2) + ", ID-DFS -", s,"moves found in", s2, "seconds")
            count += 1
        else:
            start = time.perf_counter()
            s = astar(y2)
            end = time.perf_counter()
            s2 = "%s" % (end - start)
            print("Line", str(count) + ":", str(y2) + ", A* -", s,"moves found in", s2, "seconds")
            count += 1
    