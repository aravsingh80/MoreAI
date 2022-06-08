import sys
import time
from collections import deque
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

count = 0
for x in line_list:
    x2 = x[0]
    y2 = x[2 : len(x) : 1]
    start = time.perf_counter()
    s = bfs(y2, x2)
    end = time.perf_counter()
    s2 = "%s" % (end - start)
    print("Line", str(count) + ":", str(y2) + ",", s,"moves found in", s2, "seconds")
    count += 1

#6
def bfs2(startnode, size):
    fringe = deque()
    visited = set()
    fringe.append((startnode, 0))
    visited.add(startnode)
    while len(fringe) > 0:
        v, moves = fringe.popleft()
        for c in get_children(v, size):
            if c not in visited:
                fringe.append((c, moves + 1))
                visited.add(c)
        if len(fringe) == 0:
            return moves
    return None
s = "12345678."
x = bfs2(s, 3)
m = []
m2 = []
def bfs3(startnode, size):
    fringe = deque()
    l2 = []
    count = 1 
    temp = ""
    for j in get_children(startnode, 3):
        l2.append(j)
        if count == 1:
            temp = j
    visited = {startnode : temp}
    fringe.append((startnode, 0))
    visited2 = []
    temp = ""
    count = 1
    while len(fringe) > 0:
        v, moves = fringe.popleft()
        for c in get_children(v, size):
            if count == 1:
                visited[v] = c
            if c not in visited:
                fringe.append((c, moves + 1))
                visited[c] = v
                if moves == x:
                    temp = v
        count += 1
        if moves == x:
            m.append(v)
            visited[v] = "s"
            visited2.append(visited)
            visited[v] = temp
        if len(fringe) == 0:
            return visited2
    return None
def bfs4(startnode, size):
    fringe = deque()
    visited = set()
    fringe.append((startnode, [startnode]))
    visited.add(startnode)
    while len(fringe) > 0:
        v, path = fringe.popleft()
        if GoalTest(v):
            return path
        for c in get_children(v, size):
            if c not in visited:
                c_path = path.copy()
                c_path.append(c)
                fringe.append((c, c_path))
                visited.add(c)
    return None
v2 = bfs3(s, 3)
print("Start States and Solution Path:")
for x2 in m:
    print_puzzle(3, x2)
    print(" ")
    fff = bfs4(x2, 3)
    for x9 in fff:
        print_puzzle(3, x9)
        print(" ")
    print("_________________________")
print("Number of Moves:")
print(bfs2(s, 3))