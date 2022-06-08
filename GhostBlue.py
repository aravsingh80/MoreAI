import sys
import time
s = sys.argv[1]
min_length = int(sys.argv[2])
letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
players = ["a", "b"]
if len(sys.argv) > 3: current = sys.argv[3]
else: current = ""
line_list = []
if len(current) % 2 == 0: 
    aLetter = 1
    bLetter = 0
else:
    aLetter = 0
    bLetter = 1
with open(s) as f: 
    past = ""
    for line in f: 
        if line.strip().isalpha() and len(line.strip()) >= min_length: #and line.strip()[0: len(past): 1] != past: 
            if len(past) < min_length:
                past = line.strip()
                line_list.append(line.strip().upper())
            else:
                if line.strip()[0: len(past): 1] != past: 
                    past = line.strip()
                    line_list.append(line.strip().upper())

def swap(p):
    temp = p[0]
    p[0] = p[1]
    p[1] = temp

def game_over(word, player):
    if word in line_list:
        if len(word) % 2 == bLetter and player == "b": return [True, 1]
        if len(word) % 2 == aLetter and player == "b": return [True, -1]
        if len(word) % 2 == aLetter and player == "a": return [True, 1]
        if len(word) % 2 == bLetter and player == "a": return [True, -1]
    else: return [False, -2]

def possible_next_words(word):
    possibles = set()
    for y in line_list: 
        if y[0 : len(word): 1] > word: break
        if y[0: len(word): 1] == word: possibles.add((word + y[len(word)], y[len(word)]))
    return sorted(possibles)

def negamax(word, player):
    g = game_over(word, player)
    #if word in line_list: print(word, g)
    if g[0]: return g[1]
    swap(players)
    p = possible_next_words(word)
    for next_word in p:
        next_word2, letter = next_word
        x = -1 * negamax(next_word2, players[0])
        if x == -1: return -1
    return 1 

start = time.perf_counter()
results = set()
p = possible_next_words(current) 
swap(players)
for next_word in p:
    next_word2, letter = next_word
    if next_word2 not in line_list:
        m = negamax(next_word2, players[0])
        if m == 1: results.add(letter)
        if players[0] == "a": swap(players)
end = time.perf_counter()
if len(results) == 0: print("Next player will lose!")
else: print("Next player can guarantee victory by playing any of these letters: ", sorted(list(results)))
#print(end-start)