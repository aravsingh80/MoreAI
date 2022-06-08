import sys
import random
from math import log
textBlock = sys.argv[1]
POPULATION_SIZE = 500
NUM_CLONES = 1
TOURNAMENT_SIZE = 20
TOURNAMENT_WIN_PROBABILITY = .75
CROSSOVER_LOCATIONS = 5
MUTATION_RATE = .8

ngrams = dict()
with open("ngrams.txt") as f: 
    for line in f:
        line = line.strip()
        i = line.index(" ")
        ngrams[line[0:i]] = line[i + 1:]

source = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def encode(s, cipher):
    toRet = ""
    for x in s:
        if x.isalpha(): toRet += cipher[source.index(x.upper())]
        else: toRet += x
    return toRet

def decode(s, cipher):
    toRet = ""
    for x in s:
        if x.isalpha(): toRet += source[cipher.index(x.upper())]
        else: toRet += x
    return toRet

def nGramFitness(n, s, cipher):
    decS = decode(s, cipher)
    fitness = 0
    words = decS.split()
    for w in words:
        i = 0
        while(i + n <= len(w)):
            sub = w[i : i + n]
            if sub in ngrams:
                val = int(ngrams[sub])
                fitness += log(val, 2)
            i += 1
    return fitness

population = dict()
genNumber = 0
r = dict()
while(len(population) < POPULATION_SIZE):
    lets = [x for x in source]
    cipher = ""
    for x in range(0, 26):
        rL = random.choice(lets)
        cipher += rL
        lets.remove(rL)
    x = nGramFitness(3, textBlock, cipher)
    population[cipher] = x
    r[x] = cipher
rSort = (sorted(r))[::-1]
while genNumber < POPULATION_SIZE:
    nextGen = [r[x] for x in rSort[0 : NUM_CLONES]]
    while(len(nextGen) < POPULATION_SIZE):
        population2 = random.sample(list(population), 2 * TOURNAMENT_SIZE)
        subOne = random.sample(list(population2), TOURNAMENT_SIZE)
        for x in subOne: population2.remove(x)
        subTwo = population2

        rankD = dict()
        ranking = dict()
        for x in subOne: rankD[population[x]] = x
        rankL = (sorted(rankD))[::-1]
        for x in rankL: ranking[x] = rankD[x]
        for x in ranking:
            parent1 = ranking[x]
            break
        for x in ranking:
            if random.random() <= TOURNAMENT_WIN_PROBABILITY: 
                parent1 = ranking[x]
                break
        rankD2 = dict()
        ranking2 = dict()
        for x in subTwo: rankD2[population[x]] = x
        rankL2 = (sorted(rankD2))[::-1]
        for x in rankL2: ranking2[x] = rankD2[x]
        for x in ranking2:
            parent2 = ranking2[x]
            break
        for x in ranking2:
            if random.random() <= TOURNAMENT_WIN_PROBABILITY: 
                parent2 = ranking2[x]
                break

        crossovers = dict()
        cLet = []
        lets = [[x, parent1.index(x)] for x in parent1]
        while(len(crossovers) < CROSSOVER_LOCATIONS):
            r1 = random.choice(lets)
            lets.remove(r1)
            crossovers[r1[1]] = r1[0]
            cLet.append(r1[0])
        
        child = ""
        i = 0
        count = 0
        while(len(child) < 26):
            if count not in crossovers: 
                if parent2[i] not in cLet: 
                    child += parent2[i]
                else:
                    while(parent2[i] in cLet): i += 1
                    child += parent2[i]
                i += 1
            else: child += crossovers[count]
            count += 1
        
        if(random.random() <= MUTATION_RATE):
            num = [x for x in range(0, 26)]
            vals = sorted(random.sample(num, 2))
            temp = child[0:vals[0]] + child[vals[1]] + child[vals[0] + 1:vals[1]] + child[vals[0]] + child[vals[1] + 1:]
            child = temp
        
        nextGen.append(child)
    addGen = dict()
    r2 = dict()
    for cipher in nextGen:
        if cipher not in population: x = nGramFitness(3, textBlock, cipher)
        else: x = population[cipher]
        addGen[cipher] = x
        r2[x] = cipher
    r2Sort = (sorted(r2))[::-1]
    population = addGen
    r = r2
    rSort = r2Sort
    genNumber += 1
    finalRank = rSort
    for x in rSort: 
        mainCiph = r[x]
        break
    for x in rSort:
        if random.random() <= TOURNAMENT_WIN_PROBABILITY:
            mainCiph = r[x]
            break

    print(decode(textBlock, mainCiph))
    print()
    print()

# finalRank = rSort
# for x in rSort: 
#     mainCiph = r[x]
#     break
# for x in rSort:
#     if random.random() <= TOURNAMENT_WIN_PROBABILITY:
#         mainCiph = r[x]
#         break

# print(decode(textBlock, mainCiph))