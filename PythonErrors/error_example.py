1s = 5 #mistake (digit first in var name)
s2 = 6
f = 7
4e = 8 #mistake (digit first in var name)
s5 = 5
def checkIfEqual(s, s3):
    return s = s3 #mistake (= used instead of ==)
def checkIfNotEqual(s, s3) #mistake (no colon)
    return s != s3
if s2 = f: #mistake (= used instead of ==)
    if s5 == s2 #mistake (no colon)
        print(s6) #mistake (var called before defined)
s6 = 0
print(checkIfEqual(s5)) #mistake (wrong number of args)
print(checkIfNotEqual(s5, s4)) #mistake (var called before defined)
s4 = 7
if checkIfNotEqual(s4, s6, s5): #mistake (wrong number of args)
    print("yay")