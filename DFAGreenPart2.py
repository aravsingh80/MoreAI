import sys
firstArg = sys.argv[1]
secondArg = sys.argv[2]
tests = []

def checkInput(DFA, init, checker, input):
    temp = init
    for x in input:
        if x in DFA[temp]: temp = DFA[temp][x]
        else: return False
    return temp in checker

num = int(firstArg)
with open(secondArg) as f:
    for line in f: tests.append(line.strip())
if num == 1:
    dfa = {
       0: {
           "a": 1
       }, 
       1: {
           "a": 2
       },
       2: {
           "b": 3
       },
       3: {}
    }
    final = [3]
    language = ["a", "b"]
elif num == 2:
    dfa = {
        0: {
            "0": 0,
            "1": 1,
            "2": 0
        },
        1: {
            "0": 0,
            "1": 1,
            "2": 0
        }
    }
    final = [1]
    language = ["0", "1", "2"]
elif num == 3:
    dfa = {
       0: {
           "a": 0,
           "b": 1,
           "c": 0
       }, 
       1: {
           "a": 1,
           "b": 1,
           "c": 1
       }
    }
    final = [1]
    language = ["a", "b", "c"]
elif num == 4:
    dfa = {
        0: {
            "0": 1,
            "1": 0
        },
        1: {
            "0": 0,
            "1": 1
        }
    }
    final = [0]
    language = ["0", "1"]
elif num == 5:
    dfa = {
        0: {
            "0": 2,
            "1": 1
        },
        1: {
            "0": 3,
            "1": 0
        },
        2: {
            "0": 0,
            "1": 3
        },
        3: {
            "0": 1,
            "1": 2
        }
    }
    final = [0]
    language = ["0", "1"]
elif num == 6:
    dfa = {
        0: {
            "a": 1,
            "b": 0,
            "c": 0
        },
        1: {
            "a": 1,
            "b": 2,
            "c": 0
        },
        2: {
            "a": 1,
            "b": 0,
            "c": 3
        },
        3: {
            "a": 3,
            "b": 3,
            "c": 3
        }
    }
    final = [0, 1, 2]
    language = ["a", "b", "c"]
else:
    dfa = {
        0: {
            "0": 0,
            "1": 1
        },
        1: {
            "0": 2,
            "1": 1
        },
        2: {
            "0": 2,
            "1": 3
        },
        3: {
            "0": 2,
            "1": 4
        },
        4: {
            "0": 4,
            "1": 4
        }
    }
    final = [4]
    language = ["0", "1"]

s = ""
for x in language: s += x + "           "
print("*           " + s)
for x in dfa:
    s = str(x) + "           "
    for y in language:
        if y in dfa[x]: s += str(dfa[x][y]) + "           "
        else: s +=  "_           "
    print(s)
print("Final nodes:", final)

for x in tests: 
    b = checkInput(dfa, 0, final, x)
    if not b: print(b, x)
    else: print(b, " " + x)
