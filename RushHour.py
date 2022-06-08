import sys
import time
from collections import deque
from heapq import heappush, heappop, heapify
#s = sys.argv[1]
s = "LOBBPELOVVPERRGYEEEEGYSEEEWYSEEEWEEE"
sBoard = []
count = 0
for x in range(0, 6):
    r = []
    for y in range(0, 6):
        r.append(s[count])
        count += 1
    sBoard.append(r)

def isVertical(s, board):
    xCount = 0
    for x in board:
        yCount = 0
        for y in board:
            if board[x][y] == s:
                yCount += 1
        if yCount > 0:
            xCount += 1
        if xCount > 1:
            return True
    return False

def getChildren(board):
    letters = set()
    children = set()
    letters.add("E")
    count = 0
    for x in board:
        temp = x.copy()
        if x not in letters:
            if isVertical(x):
                s2 = board[count : len(board) : 6]
                sPos = count / 6
                
        count += 1
        letters.add(x)
        if len(letters) == 11:
            return children
    return children

        
#use a*