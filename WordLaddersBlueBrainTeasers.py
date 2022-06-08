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
    p = []
    count = 0
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
        p.append(path)
    return p

def bfs2(startnode, endnode):
    fringe = deque()
    visited = set()
    fringe.append((startnode, 0))
    visited.add(startnode)
    while len(fringe) > 0:
        v, moves = fringe.popleft()
        if v == endnode:
            return moves + 1
        for c in d[v]:
            if c not in visited and c in line_list:
                fringe.append((c, moves + 1))
                visited.add(c)
    return None

#1 Answer : 1568
# count = 0
# b = False
# for x in line_list:
#     for y in line_list:
#         if x != y:
#             l = bfs(x, y)
#             if l != None:
#                 b = True
#                 break
#     if b == False:
#         count += 1
#     b = False
# print("There are", count, "singletons")
    
#2
# def bfs2(startnode):
#     fringe = deque()
#     visited = set()
#     fringe.append((startnode, 0))
#     visited.add(startnode)
#     while len(fringe) > 0:
#         v, moves = fringe.popleft()
#         for c in d[v]:
#             if c not in visited and c in line_list:
#                 fringe.append((c, moves + 1))
#                 visited.add(c)
#         if len(fringe) == 0:
#             return moves
#     return None
# s = "abased"
# x = bfs2(s)
# m = []
# m2 = []
# def bfs3(startnode):
#     fringe = deque()
#     l2 = []
#     count = 1 
#     temp = ""
#     for j in d[startnode]:
#         l2.append(j)
#         if count == 1:
#             temp = j
#     visited = {startnode : temp}
#     fringe.append((startnode, 0))
#     visited2 = []
#     temp = ""
#     count = 1
#     while len(fringe) > 0:
#         v, moves = fringe.popleft()
#         for c in d[v]:
#             if count == 1:
#                 visited[v] = c
#             if c not in visited and c in line_list:
#                 fringe.append((c, moves + 1))
#                 visited[c] = v
#                 if moves == x:
#                     temp = v
#         count += 1
#         if moves == x:
#             m.append(v)
#             visited[v] = "s"
#             visited2.append(visited)
#             visited[v] = temp
#         if len(fringe) == 0:
#             return visited2
#     return None
# def bfs4(startnode, endnode):
#     fringe = deque()
#     visited = set()
#     fringe.append((startnode, [startnode]))
#     visited.add(startnode)
#     while len(fringe) > 0:
#         v, path = fringe.popleft()
#         if startnode == endnode:
#             return path
#         for c in d[v]:
#             if c not in visited and c in line_list:
#                 c_path = path.copy()
#                 c_path.append(c)
#                 fringe.append((c, c_path))
#                 visited.add(c)
#     return None
# print("Number of Moves:")
# print(bfs2(s))
# max =  0
# print(bfs2("abased", "abases"))
# for x in line_list:
#     print(x)
#     for y in line_list:
#         if x != y:
#             l = bfs2(x, y)
#             if l != None:
#                 if l > max:
#                     max = l
# p = bfs("garden", None)

# count = 0
# for x in p:
#     if len(x) > 2:
#         count += 1
# print(count)
#2 Answer: 1625

#3 Answer: 450
# count = 0
# b = False
# p = []
# temp = set()
# for x in line_list:
#     if x not in temp:
#         j = bfs(x, None)
#         for y in j:
#             for z in y:
#                 temp.add(z)
#         if len(j) != 1:
#             p.append(j)
# print(len(p))

#4
#Answer: ['drafty', 'drafts', 'grafts', 'grants', 'grands', 'brands', 'braids', 'brains', 'trains', 'traits', 'tracts', 'traces', 'graces', 'grapes', 'drapes', 'draper', 'diaper', 'dipper', 'tipper', 'tapper', 'tamper', 'hamper', 'hammer', 'hummer', 'summer', 'simmer', 'dimmer', 'dimmed']
# Length: 28
# drafty dimmed
b = False
u = []
max = []
for x in line_list:
    u = bfs(x, None)
    for x in u:
        if len(x) > len(max):
            max = x
print(max)
print(len(max))
print(max[0], max[len(max) - 1])
