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
letters = set(letters)

def get_children(word):
    w = set()
    count = 0
    for x in word:
        for y in letters:
            x2 = word[0 : count : 1] + y + word[count + 1 : len(word) : 1]
            if x2 != word and x2 in line_list:
                w.add(x2)
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


def bibfs(start, end):
    f1 = deque()
    f2 = deque()
    f1.append(start)
    f2.append(end)
    fringe = [f1, f2]
    visited = [{start : " "}, {end : " "}]
    count = 0
    while fringe[0] and fringe[1]:
        count = 1 - count
        for x in range(len(fringe[count])):
            v = fringe[count].popleft()
            for c in d[v]:
                if c in visited[1 - count]:
                    visited[count][c] = v
                    temp = c
                    start2, goal2 = [], []
                    while c != " ":
                        goal2.append(c)
                        c = visited[1][c]
                    c = temp
                    while c != " ":
                        start2.append(c)
                        c = visited[0][c]
                    return start2[::-1] + goal2[1 : len(goal2) : 1]
            for c in d[v]:
                if c not in visited[count]:
                    fringe[count].append(c)
                    visited[count][c] = v
    return None
start = time.perf_counter()
for x in range(0, len(line_list2)):
    l = bibfs(line_list2[x][0], line_list2[x][1])
end = time.perf_counter()
s3 = "%s" % (end - start)

for x in range(0, len(line_list2)):
    print("Line:", x)
    l = bfs(line_list2[x][0], line_list2[x][1])
    if l == None:
        print("No Solution !")
    else:
        print("Length is:", len(l))
        for y in l:
            print(y)
        print("")
print("Time to solve all of these puzzles was:", s3, "seconds")