import tkinter as tk
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
lines = dict()
countR = 0
countB = 0
countC = 0
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
root = tk.Tk() #creates the frame
canvas = tk.Canvas(root, height=800, width=800, bg='black') #creates a canvas widget, which can be used for drawing lines and shapes

def make_red(r, c, line): #makes all the lines red
	c.itemconfig(line, fill="red") #changes color of one line to red
	#r.update() #update frame
	#time.sleep(0.1)

def make_blue(r, c, line): #makes all the lines blue
	c.itemconfig(line, fill="blue") #changes color of one line to blue
	#r.update() #update frame
		#time.sleep(0.1)

def make_green(r, c, line): #makes all the lines green
	c.itemconfig(line, fill="#000fff000") #changes color of one line to green
	r.update() #update frame
		#time.sleep(0.1)


def xyCoordinates(node1, node2):
   y1, x1 = node1
   y2, x2 = node2

   # approximate great circle distance with law of cosines
   return ([50 + 10 * (x1 + 130), 800 - (y1 * 10)], [50 + 10 * (x2 + 130), 800 - (y2 * 10)])

def create_network(c, x1, y1, x2, y2, node1, node2):
    line = c.create_line([(x1, y1), (x2, y2)], tag='grid_line')
    c.itemconfig(line, fill="white")
    lines[(node1, node2)] = line

t1 = []
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
    t1.append([xyCoordinates((float(nodes[l[0]][0]), float(nodes[l[0]][1])), (float(nodes[l[1]][0]), float(nodes[l[1]][1]))), l[0], l[1]])
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
temp = t1.copy()
for t2 in t1:
    c1, c2 = t2[0]
    n1 = t2[1]
    n2 = t2[2]
    x1 = c1[0]
    y1 = c1[1]
    x2 = c2[0]
    y2 = c2[1]
    create_network(canvas, x1, y1, x2, y2, n1, n2)
canvas.pack(expand=True)
# for l3 in lines.values():
#     make_red(root, canvas, l3)
t = "%s" % (end - start)
print("Time to create data structure:", t)

def dijkstra(start, end):
    closed = set()
    startnode = (0, start, [])      
    fringe = []
    countR = 0
    heappush(fringe, startnode)
    while len(fringe) > 0:
        depth, v, l4 = heappop(fringe)
        if v == end:
            for l5 in l4:
                make_green(root, canvas, l5)
            return depth 
        if v not in closed:
            closed.add(v)
            for c in backupStructure[v]:
                c2, d = c
                if c2 not in closed:
                    l3 = l4.copy()
                    if (v, c2) in lines:
                        make_red(root, canvas, lines[(v, c2)])
                        if countR % 500 == 0:
                            root.update()
                    if (c2, v) in lines:
                        make_red(root, canvas, lines[(c2, v)])
                        if countR % 500 == 0:
                            root.update()
                    if (v, c2) in lines:
                        l3.append(lines[(v, c2)])
                    if (c2, v) in lines:
                        l3.append(lines[(c2, v)])
                    countR+=1
                    temp = (depth + d, c2, l3)
                    heappush(fringe, temp)
def heuristic(startstate, endstate):
    if startstate == endstate:
        return 0
    else:
        x2 = calcd((float(nodes[startstate][0]), float(nodes[startstate][1])), (float(nodes[endstate][0]), float(nodes[endstate][1])))
        return x2

n1 = nodeCity[s]
n2 = nodeCity[s2]
start = time.perf_counter()
DIJKSTRA = dijkstra(n1, n2)
end = time.perf_counter()
t1 = "%s" % (end - start)
print(s, "to", s2, "with Dijkstra:", DIJKSTRA, "in", t1, "seconds.")
root.mainloop()


if root.mainloop() == None:
    root2 = tk.Tk()
    canvas2 = tk.Canvas(root2, height=800, width=800, bg='black')
    for t7 in temp:
        c1, c2 = t7[0]
        n1 = t7[1]
        n2 = t7[2]
        x1 = c1[0]
        y1 = c1[1]
        x2 = c2[0]
        y2 = c2[1]
        create_network(canvas2, x1, y1, x2, y2, n1, n2)
canvas2.pack(expand=True)
def astar(start, end):
    closed = set()
    startnode = (heuristic(start, end), 0, start, [])      
    fringe = []
    heappush(fringe, startnode)
    countB = 0
    while len(fringe) > 0:
        f, depth, v, l4 = heappop(fringe)
        if v == end:
            for l5 in l4:
                make_green(root2, canvas2, l5)
            return depth 
        if v not in closed:
            closed.add(v)
            for c in backupStructure[v]:
                c2, d = c
                if c2 not in closed:
                    l3 = l4.copy()
                    if (v, c2) in lines:
                        make_blue(root2, canvas2, lines[(v, c2)])
                        l3.append(lines[(v, c2)])
                        if countB % 200 == 0:
                            root2.update()
                    if (c2, v) in lines:
                        make_blue(root2, canvas2, lines[(c2, v)])
                        l3.append(lines[(c2, v)])
                        if countB % 200 == 0:
                            root2.update()
                    countB += 1
                    temp = (heuristic(c2, end) + depth + d, depth + d, c2, l3)
                    heappush(fringe, temp)
n1 = nodeCity[s]
n2 = nodeCity[s2]
start2 = time.perf_counter()
ASTAR = astar(n1, n2)
end2 = time.perf_counter()
t2 = "%s" % (end2 - start2)
print(s, "to", s2, "with A*:", ASTAR, "in", t2, "seconds.")
root2.mainloop()
        
        