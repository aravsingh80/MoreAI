import sys
import time
from collections import deque
s = sys.argv[1]
s2 = sys.argv[2]
with open(s) as f:
    line_list = [line.strip() for line in f]
    line_list = set(line_list)
with open(s2) as f:
    line_list2 = [line.strip().split() for line in f]

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def get_children(word):
    w = set()
    count = 0
    for x in word:
        for y in letters:
            if y != x:
                w.add(word[0 : count : 1] + y + word[count + 1 : len(word) : 1])
        count += 1
    return w

start = time.perf_counter()
d = dict()
for s in line_list:
    d[s] = get_children(s)
end = time.perf_counter()
s3 = "%s" % (end - start)
print("Time to create the data structure was:", s3, "seconds")
print("There are", len(d), "words in this dict.")
def bfs(startnode, endnode):
    fringe = deque()
    visited = set()
    fringe.append((startnode, 0, [startnode]))
    visited.add(startnode)
    while len(fringe) > 0:
        v, moves, path = fringe.popleft()
        if v == endnode:
            return [moves + 1, path]
        for c in d[v]:
            if c not in visited and c in line_list:
                c_path = path.copy()
                c_path.append(c)
                fringe.append((c, moves + 1, c_path))
                visited.add(c)
    return None

start = time.perf_counter()
for x in range(0, len(line_list2)):
    print("Line:", x)
    l = bfs(line_list2[x][0], line_list2[x][1])
    if l == None:
        print("No Solution !")
    else:
        print("Length is:", l[0])
        for y in l[1]:
            print(y)
        print("")
end = time.perf_counter()
s3 = "%s" % (end - start)
print("Time to solve all of these puzzles was:", s3, "seconds")