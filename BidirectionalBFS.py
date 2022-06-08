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

def bibfs(startnode, size):
    f1 = deque()
    f2 = deque()
    f1.append(startnode)
    f2.append(find_goal(startnode))
    fringe = [f1, f2]
    visited = [{startnode : " "}, {find_goal(startnode) : " "}]
    count = 0
    moves = 0
    while len(fringe[0]) > 0 and len(fringe[1]) > 0:
        if count == 0:
            count = 1
        else:
            count = 0
        for x in range(len(fringe[count])):
            v = fringe[count].popleft()
            for c in get_children(v, size):
                if c in visited[1 - count]:
                    visited[count][c] = v
                    temp = c
                    while c != " ":
                        moves += 1
                        c = visited[1][c]
                    c = temp
                    while c != " ":
                        moves += 1
                        c = visited[0][c]
                    return moves - 2
            for c in get_children(v, size):
                if c not in visited[count]:
                    fringe[count].append(c)
                    visited[count][c] = v
    return None

count = 0
print("Normal BFS:")
for x in line_list:
    x2 = x[0]
    y2 = x[2 : len(x) : 1]
    start = time.perf_counter()
    s = bfs(y2, x2)
    end = time.perf_counter()
    s2 = "%s" % (end - start)
    print("Line", str(count) + ":", str(y2) + ",", s,"moves found in", s2, "seconds")
    count += 1
count = 0
print("")
print("Bidirectional BFS:")
for x in line_list:
    x2 = x[0]
    y2 = x[2 : len(x) : 1]
    start = time.perf_counter()
    s3 = bibfs(y2,x2)
    end = time.perf_counter()
    s2 = "%s" % (end - start)
    print("Line", str(count) + ":", str(y2) + ",", s3,"moves found in", s2, "seconds")
    count += 1






    

