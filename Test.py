import sys
import ast
import math
import random
import numpy as np
def sigmoidPrime(num): return sigmoid(num) * (1 - sigmoid(num))
def intToBinary(num):
    b = str(bin(num))
    return int(b[2:])

def truth_table(bits, n):
    num = 0
    l = []
    s = ""
    while len(s) != bits or '0' in s:
        n2 = intToBinary(num)
        ns = str(n2)
        while len(ns) < bits: ns = '0' + ns
        s = ns
        l2 = [int(y) for y in ns]
        l.append(tuple(l2))
        num += 1
    l = l[::-1]
    n2 = intToBinary(n)
    ns = str(n2)
    while len(ns) < len(l): ns = '0' + ns
    count = 0
    mainL = []
    for x in ns:
        mainL.append((l[count], int(x)))
        count += 1
    return tuple(mainL)

def step(num):
    if num > 0: return 1
    else: return 0

def sigmoid(num): return 1/(1+math.exp(-num))

def perceptron(A, w, b, x):
    w = list(w)
    x = list(x)
    dProd = 0
    count = 0
    for z in w:
        dProd += (z * x[count])
        count += 1
    num = dProd + b
    return A(num)

def check(n, w, b):
    t = truth_table(len(w), n)
    count = 0
    for x in t:
        if x[1] == perceptron(step, w, b, x[0]): count += 1
    return count / len(t)

def p_net(A, x, w_list, b_list):
    new_a = np.vectorize(A)
    a = list()
    a.append(np.array([list(x)]))
    for l in range(1, len(w_list) + 1): a.append(new_a((a[l-1]@w_list[l-1]) + b_list[l-1]))
    return a[len(w_list)]

#XOR HAPPENS HERE
def xor(initTuple, w_list, b_list): return p_net(step, initTuple, w_list, b_list)

def backProp(epochs, f, fP, trainingSet, w, b, lam):
    dot = [None]
    for e in range(0, epochs):
        AFunct = np.vectorize(f)
        APrime = np.vectorize(fP)
        for z in trainingSet:
            x, y  = z
            a = []
            a.append(np.array([list(x)]))
            for l in range(1, len(w)):
                dot.append((a[l-1]@w[l] + b[l]))
                a.append(AFunct(dot[l]))
            delta = [None for n in range(0, len(dot) - 1)]
            n = len(dot) - 1
            delta.append(APrime(dot[n])*(y-a[n]))
            for l in range(n - 1, 0, -1): delta[l] = APrime(dot[l])*(delta[l+1]@(w[l+1].transpose()))
            for l in range(1, len(w)):
                b[l] = b[l] + (lam*delta[l][0])
                w[l] = w[l] + (lam*(a[l-1][0].transpose()@delta[l][0]))
            dot = [None]
    return [w[1:], b[1:]]
wlist1 = np.array([[1, -0.5], [1, 0.5]])
wlist2 = np.array([[1, 2], [-1, -2]])
mainWList = [None, wlist1, wlist2]
blist1 = np.array([[1, -1]])
blist2 = np.array([[-0.5, 0.5]])
mainBList = [None, blist1, blist2]
x = np.array([[2, 3]])
y = np.array([[0.8, 1]])
p = p_net(sigmoid, (np.array([[2, 3]]), np.array([[0.8, 1]])), mainWList[1:], mainBList[1:])
p2 = p[0][0]
print(0.5*(np.linalg.norm(y-p2)**2))
back = backProp(1, sigmoid, sigmoidPrime, [(x, y)], mainWList, mainBList, 0.1)
w = back[0]
b = back[1]
print("Weights:", w)
print("Bias:", b)
p = p_net(sigmoid, (np.array([[2, 3]]), np.array([[0.8, 1]])), w, b)
p2 = p[0][0]
#print(0.5*(np.linalg.norm(y-p2)**2))