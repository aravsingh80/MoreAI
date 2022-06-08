with open("states.txt") as f: line_list = [line.strip().split("  ") for line in f]
s = ''
for l in line_list:
    s += "('" + l[0]+"', " + "'" + l[1] + "'), "
print(s)