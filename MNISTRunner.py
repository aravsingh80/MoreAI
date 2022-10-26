import sys
import ast
import math
import random
import numpy as np
import pickle

def sigmoid(num): return 1/(1+math.exp(-num))

def sigmoidPrime(num): return sigmoid(num) * (1 - sigmoid(num))

def p_net(A, x, w_list, b_list):
    new_a = np.vectorize(A)
    a = list()
    a.append(np.array(list(x)))
    for l in range(1, len(w_list) + 1): a.append(new_a((a[l-1]@w_list[l-1]) + b_list[l-1]))
    return a[len(w_list)]

def backProp(e2, epochs, f, fP, trainingSet, w, b, lam):
    AFunct = np.vectorize(f)
    APrime = np.vectorize(fP)
    for e in range(e2, epochs):
        print(e)
        for z in trainingSet:
            dot = [None]
            x, y  = z
            a = []
            a.append(x)
            for l in range(1, len(w)):
                dot.append((a[l-1]@w[l] + b[l]))
                a.append(AFunct(dot[l]))
            n = len(dot) - 1
            delta = [None for i in range(0, n)]
            delta.append((APrime(dot[n]))*(y-a[n]))
            for l in range(n - 1, 0, -1): delta[l] = (APrime(dot[l]))*(delta[l+1]@(w[l+1].transpose()))
            for l in range(1, len(w)):
                b[l] = b[l] + (lam*delta[l])
                w[l] = w[l] + (lam*((a[l-1].transpose())@delta[l]))
        f = open('mnistSave.pkl', 'wb')
        save = {'epoch': e + 1, 'trainSet': trainingSet, 'wList': w, 'bList': b}
        pickle.dump(save, f)
        f.close()
    return [w[1:], b[1:]]
print('(N)ew run or (C)ontinue old run?')
ans = input()
if str(ans) == 'N' or str(ans) == 'n':
    trainingSet = []
    wList1 = 2 * np.random.rand(784, 300) - 1
    wList2 = 2 * np.random.rand(300, 100) - 1
    wList3 = 2 * np.random.rand(100, 10) - 1
    bList1 = 2 * np.random.rand(1, 300) - 1
    bList2 = 2 * np.random.rand(1, 100) - 1
    bList3 = 2 * np.random.rand(1, 10) - 1
    mainWList = [None, wList1, wList2, wList3]
    mainBList = [None, bList1, bList2, bList3]
    epochNum = 0
    with open("mnist_train.csv") as f:
        line_list = [[int(x) for x in line.strip().split(',')] for line in f]
        for line in line_list:
            lList = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            label = line[0]
            lList[label] = 1
            image = line[1:]
            trainingSet.append((np.array([image])/255, np.array([lList])))
else:
    f = open('mnistSave.pkl', 'rb')
    saved = pickle.load(f)
    f.close()
    epochNum = saved['epoch']
    trainingSet = saved['trainSet']
    mainWList = saved['wList']
    mainBList = saved['bList']
back = backProp(epochNum, 5, sigmoid, sigmoidPrime, trainingSet, mainWList, mainBList, 0.55)
w = back[0]
b = back[1]
count2 = 0
for z in trainingSet:
    x, y = z
    p = p_net(sigmoid, x, w, b)
    count = 0
    i = 0
    max2 = p[0][0]
    for x in p[0]:
        if max2 < x: 
            x = max2
            i = count
        count += 1
    if y[0][i] != 1: count2 += 1
print("Percentage of misclassified items in the training set:", (count2 / len(trainingSet)))
count2 = 0
testSet = []
with open("mnist_test.csv") as f:
    line_list = [[int(x) for x in line.strip().split(',')] for line in f]
    for line in line_list:
        lList = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        label = line[0]
        lList[label] = 1
        image = line[1:]
        testSet.append((np.array([image])/255, np.array([lList])))
for z in testSet:
    x, y = z
    p = p_net(sigmoid, x, w, b)
    count = 0
    i = 0
    max2 = p[0][0]
    for x in p[0]:
        if max2 < x: 
            x = max2
            i = count
        count += 1
    if y[0][i] != 1: count2 += 1
print("Percentage of misclassified items in the test set:", (count2 / len(testSet)))