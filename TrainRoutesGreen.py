import sys
import time
from math import pi , acos , sin , cos
from collections import deque
from heapq import heappush, heappop, heapify
s = sys.argv[1]
with open("rrNodes.txt") as f:
    line_list = [line.strip() for line in f]
s2 = sys.argv[2]
with open("rrEdges.txt") as f:
    line_list2 = [line.strip() for line in f]
with open("rrNodeCity.txt") as f:
    line_list3 = [line.strip() for line in f]

def calcd(node1, node2):
   # y1 = lat1, x1 = long1
   # y2 = lat2, x2 = long2
   # all assumed to be in decimal degrees
   y1, x1 = node1
   y2, x2 = node2

   R   = 3958.76 # miles = 6371 km
   y1 *= pi/180.0
   x1 *= pi/180.0
   y2 *= pi/180.0
   x2 *= pi/180.0

   # approximate great circle distance with law of cosines
   return acos( sin(y1)*sin(y2) + cos(y1)*cos(y2)*cos(x2-x1) ) * R

start = time.perf_counter()
nodeCity = dict()
for x in line_list3:
    l = x.split()
    if len(l) > 2:
        nodeCity[l[1] + " " + l[2]] = l[0]
    else:
        nodeCity[l[1]] = l[0]
nodes = dict()
for x in line_list:
    l = x.split()
    nodes[l[0]] = [l[1], l[2]]
backupStructure = dict()
for x in line_list2:
    l = x.split()
    x2 = calcd((float(nodes[l[0]][0]), float(nodes[l[0]][1])), (float(nodes[l[1]][0]), float(nodes[l[1]][1])))
    if l[0] not in backupStructure:
        x3 = set()
        x3.add((l[1], x2))
        backupStructure[l[0]] = x3
    else:
        backupStructure[l[0]].add((l[1], x2))
    if l[1] not in backupStructure:
        x4 = set()
        x4.add((l[0], x2))
        backupStructure[l[1]] = x4
    else:
        backupStructure[l[1]].add((l[0], x2))
end = time.perf_counter()
t = "%s" % (end - start)
print("Time to create data structure:", t)

def dijkstra(start, end):
    closed = set()
    startnode = (0, start)      
    fringe = []
    heappush(fringe, startnode)
    while len(fringe) > 0:
        depth, v = heappop(fringe)
        if v == end:
            return depth 
        if v not in closed:
            closed.add(v)
            for c in backupStructure[v]:
                c2, d = c
                if c2 not in closed:
                    temp = (depth + d, c2)
                    heappush(fringe, temp)

def heuristic(startstate, endstate):
    if startstate == endstate:
        return 0
    else:
        x2 = calcd((float(nodes[startstate][0]), float(nodes[startstate][1])), (float(nodes[endstate][0]), float(nodes[endstate][1])))
        return x2

def astar(start, end):
    closed = set()
    startnode = (heuristic(start, end), 0, start)      
    fringe = []
    heappush(fringe, startnode)
    while len(fringe) > 0:
        f, depth, v = heappop(fringe)
        if v == end:
            return depth 
        if v not in closed:
            closed.add(v)
            for c in backupStructure[v]:
                c2, d = c
                if c2 not in closed:
                    temp = (heuristic(c2, end) + depth + d, depth + d, c2)
                    heappush(fringe, temp)

n1 = nodeCity[s]
n2 = nodeCity[s2]
start = time.perf_counter()
DIJKSTRA = dijkstra(n1, n2)
end = time.perf_counter()
t1 = "%s" % (end - start)
start2 = time.perf_counter()
ASTAR = astar(n1, n2)
end2 = time.perf_counter()
t2 = "%s" % (end2 - start2)
print(s, "to", s2, "with Dijkstra:", DIJKSTRA, "in", t1, "seconds.")
print(s, "to", s2, "with A*:", ASTAR, "in", t2, "seconds.")
    
    