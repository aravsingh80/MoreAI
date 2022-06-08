import sys
board2 = sys.argv[1]
if board2 == ".........": current_player = input("Should I be X or O? ")
else:
    count1 = 0
    count2 = 0
    for x in board2: 
        if x == "X": count1 += 1
        if x == "O": count2 += 1
    if count1 == count2: current_player = "X"
    else: current_player = "O"
ai = current_player
if current_player == "X": other_player = "O"
else: other_player = "X"
me = other_player
players = [current_player, other_player]

def swap(p):
    temp = p[0]
    p[0] = p[1]
    p[1] = temp

def g2(board):
    if board[0] != "." and board[0] == board[1] == board[2]: return [True, board[0]]
    if board[3] != "." and board[3] == board[4] == board[5]: return [True, board[3]]
    if board[6] != "." and board[6] == board[7] == board[8]: return [True, board[6]]
    if board[0] != "." and board[0] == board[3] == board[6]: return [True, board[0]]
    if board[1] != "." and board[1] == board[4] == board[7]: return [True, board[1]]
    if board[2] != "." and board[2] == board[5] == board[8]: return [True, board[2]]
    if board[0] != "." and board[0] == board[4] == board[8]: return [True, board[0]]
    if board[2] != "." and board[2] == board[4] == board[6]: return [True, board[2]]
    return [False, -2]

def game_over(board):
    if "." not in board:
        g3 = g2(board)
        if g3[0]: 
            num = -2
            if g3[1] == "X": num = 1
            else: num = -1
            return [True, num]
        else: return [True, 0]
    else:
        g3 = g2(board)
        if g3[0]: 
            num = -2
            if g3[1] == "X": num = 1
            else: num = -1
            return [True, num]
        else: return [False, -2]

def possible_next_boards(board, p):
    temp = board
    possibles = []
    count = 0
    for x in board:
        if x == ".":
            temp = temp[0: count: 1] + p + temp[count + 1: len(temp): 1]
            possibles.append((temp, count))
            temp = board
        count += 1
    return possibles

def min_step(board):
    g = game_over(board)
    if g[0]: return g[1]
    results = list()
    swap(players)
    count1 = 0
    count2 = 0
    for x in board: 
        if x == "X": count1 += 1
        if x == "O": count2 += 1
    if count1 == count2 and players[0] == "O": swap(players)
    if count1 > count2 and players[0] == "X": swap(players)
    p = possible_next_boards(board, players[0])
    for next_board in p:
        next_board2, index = next_board
        results.append(max_step(next_board2))
    return min(results)

def max_step(board):
    g = game_over(board)
    if g[0]: return g[1]
    results = list()
    swap(players)
    count1 = 0
    count2 = 0
    for x in board: 
        if x == "X": count1 += 1
        if x == "O": count2 += 1
    if count1 == count2 and players[0] == "O": swap(players)
    if count1 > count2 and players[0] == "X": swap(players)
    p = possible_next_boards(board, players[0])
    for next_board in p:
        next_board2, index = next_board
        results.append(min_step(next_board2))
    return max(results)

def max_move(board):
    results = list()
    spaces = list()
    p = possible_next_boards(board, cp)
    c = 0
    for next_board in p:
        next_board2, index = next_board
        m = min_step(next_board2)
        results.append(m)
        spaces.append(index)
        if m == 0: print("Moving at", index, "results in a tie.")
        if m == 1: 
            if cp == "X": print("Moving at", index, "results in a win.")
            else: print("Moving at", index, "results in a loss.")
        if m == -1:
            if cp == "O": print("Moving at", index, "results in a win.")
            else: print("Moving at", index, "results in a loss.")
    i = results.index(max(results))
    return spaces[i]

def min_move(board):
    results = list()
    spaces = list()
    p = possible_next_boards(board, cp)
    for next_board in p:
        next_board2, index = next_board
        m = max_step(next_board2)
        results.append(m)
        spaces.append(index)
        if m == 0: print("Moving at", index, "results in a tie.")
        if m == 1: 
            if cp == "X": print("Moving at", index, "results in a win.")
            else: print("Moving at", index, "results in a loss.")
        if m == -1:
            if cp == "O": print("Moving at", index, "results in a win.")
            else: print("Moving at", index, "results in a loss.")
    i = results.index(min(results))
    return spaces[i]

count1 = 0
count2 = 0
for x in board2: 
    if x == "X": count1 += 1
    if x == "O": count2 += 1
if count1 == count2: cp = "X"
else: cp = "O"
while(not game_over(board2)[0]):
    print("Current board:")
    print(board2[0] + board2[1] + board2[2] + "    " + "012")
    print(board2[3] + board2[4] + board2[5] + "    " + "345")
    print(board2[6] + board2[7] + board2[8] + "    " + "678")
    print()
    if cp == ai: 
        if cp == "X":
            m2 = max_move(board2)
            print()
            print("I choose space", m2)
            print()
            board2 = board2[0: m2: 1] + cp + board2[m2 + 1: len(board2): 1]
        else:
            m2 = min_move(board2)
            print()
            print("I choose space", m2)
            print()
            board2 = board2[0: m2: 1] + cp + board2[m2 + 1: len(board2): 1]
    else: 
        count = 0
        open_spaces = list()
        for x in board2:
            if x == ".": open_spaces.append(count)
            count += 1
        print("You can move to any of these spaces:", str(open_spaces)[1: len(str(open_spaces)) - 1: 1])
        ch = int(input("Your choice? "))
        print()
        board2 = board2[0: ch: 1] + cp + board2[ch + 1: len(board2): 1]
    if cp == ai: cp = me
    elif cp == me: cp = ai

print("Current board:")
print(board2[0] + board2[1] + board2[2] + "    " + "012")
print(board2[3] + board2[4] + board2[5] + "    " + "345")
print(board2[6] + board2[7] + board2[8] + "    " + "678")
print()
if game_over(board2)[1] == 1: 
    if ai == "X": print("I win!")
    else: print("You win!")
elif game_over(board2)[1] == -1: 
    if ai == "O": print("I win!")
    else: print("You win!")
else: print("We tied!")