import sys
b = "          #         #         #      #  #      #  #      #  #     ##  #     ##  #     ## ##     ## #####  ########  ######### ######### ######### ######### ########## #### # # # # ##### ###   ########"
#b = sys.argv[1]
HEIGHT = 20
WIDTH = 10
def findTopBlocks(board):
    tops = []
    for x in range(0, 10):
        pos = x
        for y in range(0, 20):
            if board[pos] == "#" and pos not in tops: 
                tops.append(pos)
                break
            pos += 10
        if pos not in tops: tops.append(pos)
    return tops
def findIOrientations(board, top, gameOvers):
    orientations = set()
    count = 0
    for x in top:
        if count <= 6:
            if x - 10 < 0: gameOvers += 1
            elif board[x-10] != '#' and board[x-9] != '#' and board[x-8] != '#' and board[x-7] != '#': orientations.add(board[0:x-10]+"####"+board[x-6:])
        if count <= 7 and count >= 1: 
            if x - 11 < 0: gameOvers += 1
            elif board[x-11] != '#' and board[x-10] != '#' and board[x-9] != '#' and board[x-8] != '#': orientations.add(board[0:x-11]+"####"+board[x-7:])
        if count <= 8 and count >= 2: 
            if x - 12 < 0: gameOvers += 1
            elif board[x-12] != '#' and board[x-11] != '#' and board[x-10] != '#' and board[x-9] != '#': orientations.add(board[0:x-12]+"####"+board[x-8:])
        if count >= 3: 
            if x - 13 < 0: gameOvers += 1
            elif board[x-13] != '#' and board[x-12] != '#' and board[x-11] != '#' and board[x-10] != '#': orientations.add(board[0:x-13]+"####"+board[x-9:]) 
        if x - 10 < 0 or x - 20 < 0 and x - 30 < 0 or x - 40 < 0: gameOvers += 1
        elif board[x-10] != '#' and board[x-20] != '#' and board[x-30] != '#' and board[x-40] != '#': orientations.add(board[0:x-40]+"#"+board[x-39:x-30]+"#"+board[x-29:x-20]+"#"+board[x-19:x-10]+"#"+board[x-9:])
        count += 1
    return [orientations, gameOvers]

def findOOrientations(board, top, gameOvers):
    orientations = set()
    count = 0
    for x in top: 
        if count <= 8: 
            if x - 10 < 0 or x - 20 < 0: gameOvers += 1
            elif board[x-10] !='#' and board[x-20] !='#' and board[x-9] !='#' and board[x-19] !='#': orientations.add(board[0:x-20]+"##"+board[x-18:x-10]+"##"+board[x-8:])
        if count >= 1: 
            if x - 11 < 0 or x - 21 < 0: gameOvers += 1
            elif board[x-10] !='#' and board[x-20] !='#' and board[x-11] !='#' and board[x-21] !='#': orientations.add(board[0:x-21]+"##"+board[x-19:x-11]+"##"+board[x-9:])
        count += 1
    return [orientations, gameOvers]

def findTOrientations(board, top, gameOvers):
    orientations = set()
    count = 0
    for x in top:
        if count <= 7: 
            if x - 10 < 0 or x - 19 < 0: gameOvers += 1
            elif board[x-10] !='#' and board[x-9] !='#' and board[x-8] !='#' and board[x-19] !='#': orientations.add(board[0:x-19]+"#"+board[x-18:x-10]+"###"+board[x-7:])
        if count <= 8 and count >= 1: 
            if x - 11 < 0 or x - 20 < 0: gameOvers += 1
            elif board[x-11] !='#' and board[x-10] !='#' and board[x-9] !='#' and board[x-20] !='#': orientations.add(board[0:x-20]+"#"+board[x-19:x-11]+"###"+board[x-8:])
        if count >= 2: 
            if x - 12 < 0 or x - 21 < 0: gameOvers += 1
            elif board[x-12] !='#' and board[x-11] !='#' and board[x-10] !='#' and board[x-21] !='#': orientations.add(board[0:x-21]+"#"+board[x-20:x-12]+"###"+board[x-9:])
        if count <= 8: 
            if x - 10 < 0 or x - 20 < 0 and x - 30 < 0: gameOvers += 1
            elif board[x-10] !='#' and board[x-20] !='#' and board[x-30] !='#' and board[x-19] !='#': orientations.add(board[0:x-30]+"#"+board[x-29:x-20]+"##"+board[x-18:x-10]+"#"+board[x-9:])
        if count >= 1 and x - 1 >= 0 and x - 1 <= 199: 
            if x - 11 < 0 or x - 21 < 0: gameOvers += 1
            elif board[x-1] !='#' and board[x-11] !='#' and board[x-10] !='#' and board[x-21] !='#': orientations.add(board[0:x-21]+"#"+board[x-20:x-11]+"##"+board[x-9:x-1]+"#"+board[x:])
        if count <= 7 and x + 1 <= 199: 
            if x - 10 < 0: gameOvers += 1
            elif board[x-10] !='#' and board[x-9] !='#' and board[x-8] !='#' and board[x+1] !='#': orientations.add(board[0:x-10]+"###"+board[x-7:x+1]+"#"+board[x+2:])
        if count <= 8 and count >= 1: 
            if x - 10 < 0 or x - 21 < 0: gameOvers += 1
            elif board[x-10] !='#' and board[x-21] !='#' and board[x-20] !='#' and board[x-19] !='#': orientations.add(board[0:x-21]+"###"+board[x-18:x-10]+"#"+board[x-9:])
        if count >= 2 and x - 1 >= 0 and x - 1 <= 199: 
            if x - 12 < 0: gameOvers += 1
            elif board[x-10] !='#' and board[x-11] !='#' and board[x-12] !='#' and board[x-1] !='#': orientations.add(board[0:x-12]+"###"+board[x-9:x-1]+"#"+board[x:])
        if count <= 8 and x + 1 <= 199: 
            if x - 9 < 0 or x - 10 < 0 or x - 19 < 0: gameOvers += 1
            elif board[x-10] !='#' and board[x-9] !='#' and board[x-19] !='#' and board[x+1] !='#': orientations.add(board[0:x-19]+"#"+board[x-18:x-10]+"##"+board[x-8:x+1]+"#"+board[x+2:])
        if count >= 1: 
            if x - 10 < 0 or x - 30 < 0 or x - 21 < 0: gameOvers += 1 
            elif board[x-10] !='#' and board[x-21] !='#' and board[x-20] !='#' and board[x-30] !='#': orientations.add(board[0:x-30]+"#"+board[x-29:x-21]+"##"+board[x-19:x-10]+"#"+board[x-9:])
        count += 1
    return [orientations, gameOvers]

def findSOrientations(board, top, gameOvers):
    orientations = set()
    count = 0
    for x in top:
        if count <= 7: 
            if x - 10 < 0 or x - 19 < 0: gameOvers += 1
            elif board[x-10] !='#' and board[x-9] !='#' and board[x-19] !='#' and board[x-18] !='#': orientations.add(board[0:x-19]+"##"+board[x-17:x-10]+"##"+board[x-8:])
        if count <= 8 and count >= 1: 
            if x - 11 < 0 or x - 20 < 0: gameOvers += 1
            elif board[x-11] !='#' and board[x-10] !='#' and board[x-20] !='#' and board[x-19] !='#': orientations.add(board[0:x-20]+"##"+board[x-18:x-11]+"##"+board[x-9:])
        if count >= 2 and x - 2 >= 0 and x - 2 <= 199: 
            if x - 11 < 0: gameOvers += 1
            elif board[x-11] !='#' and board[x-10] !='#' and board[x-2] !='#' and board[x-1] !='#': orientations.add(board[0:x-11]+"##"+board[x-9:x-2]+"##"+board[x:])
        if count <= 8 and x + 1 <= 199: 
            if x - 10 < 0 or x - 20 < 0: gameOvers += 1
            elif board[x-10] !='#' and board[x-9] !='#' and board[x-20] !='#' and board[x+1] !='#': orientations.add(board[0:x-20]+"#"+board[x-19:x-10]+"##"+board[x-8:x+1]+"#"+board[x+2:])
        if count >= 1: 
            if x - 10 < 0 or x - 21 < 0 or x - 31 < 0: gameOvers += 1
            elif board[x-10] !='#' and board[x-21] !='#' and board[x-20] !='#' and board[x-31] !='#': orientations.add(board[0:x-31]+"#"+board[x-30:x-21]+"##"+board[x-19:x-10]+"#"+board[x-9:])
        count += 1
    return [orientations, gameOvers]

def findZOrientations(board, top, gameOvers):
    orientations = set()
    count = 0
    for x in top:
        if count <= 7 and x + 2 <= 199: 
            if x - 10 < 0: gameOvers += 1
            elif board[x-10] !='#' and board[x-9] !='#' and board[x+1] !='#' and board[x+2] !='#': orientations.add(board[0:x-10]+"##"+board[x-8:x+1]+"##"+board[x+3:])
        if count <= 8 and count >= 1: 
            if x - 10 < 0 or x - 21 < 0: gameOvers += 1
            elif board[x-10] !='#' and board[x-9] !='#' and board[x-21] !='#' and board[x-20] !='#': orientations.add(board[0:x-21]+"##"+board[x-19:x-10]+"##"+board[x-8:])
        if count >= 2: 
            if x - 11 < 0 or x - 22 < 0: gameOvers += 1
            elif board[x-11] !='#' and board[x-10] !='#' and board[x-22] !='#' and board[x-21] !='#': orientations.add(board[0:x-22]+"##"+board[x-20:x-11]+"##"+board[x-9:])
        if count <= 8: 
            if x - 10 < 0 or x - 20 < 0 or x - 29 < 0: gameOvers += 1
            elif board[x-10] !='#' and board[x-20] !='#' and board[x-19] !='#' and board[x-29] !='#': orientations.add(board[0:x-29]+"#"+board[x-28:x-20]+"##"+board[x-18:x-10]+"#"+board[x-9:])
        if count >= 1 and x - 1 >= 0 and x - 1 <= 199: 
            if x - 11 < 0 or x - 20 < 0: gameOvers += 1
            elif board[x-1] !='#' and board[x-10] !='#' and board[x-11] !='#' and board[x-20] !='#': orientations.add(board[0:x-20]+"#"+board[x-19:x-11]+"##"+board[x-9:x-1]+"#"+board[x:])
        count += 1
    return [orientations, gameOvers]

def findJOrientations(board, top, gameOvers):
    orientations = set()
    count = 0
    for x in top:
        if count <= 7: 
            if x - 10 < 0 or x - 20 < 0: gameOvers += 1
            elif board[x-10] !='#' and board[x-20] !='#' and board[x-9] !='#' and board[x-8] !='#': orientations.add(board[0:x-20]+"#"+board[x-19:x-10]+"###"+board[x-7:])
        if count <= 8 and count >= 1: 
            if x - 11 < 0 or x - 21 < 0: gameOvers += 1
            elif board[x-11] !='#' and board[x-21] !='#' and board[x-10] !='#' and board[x-9] !='#': orientations.add(board[0:x-21]+"#"+board[x-20:x-11]+"###"+board[x-8:])
        if count >= 2: 
            if x - 12 < 0 or x - 22 < 0: gameOvers += 1
            elif board[x-12] !='#' and board[x-22] !='#' and board[x-11] !='#' and board[x-10] !='#': orientations.add(board[0:x-22]+"#"+board[x-21:x-12]+"###"+board[x-9:])
        if count <= 8: 
            if x - 10 < 0 or x - 20 < 0 or x - 30 < 0: gameOvers += 1
            elif board[x-10] !='#' and board[x-20] !='#' and board[x-30] !='#' and board[x-29] !='#': orientations.add(board[0:x-30]+"##"+board[x-28:x-20]+"#"+board[x-19:x-10]+"#"+board[x-9:])
        if count >= 1 and x - 1 >= 0 and x + 9 <= 199: 
            if x - 11 < 0: gameOvers += 1
            elif board[x-11] !='#' and board[x-10] !='#' and board[x-1] !='#' and board[x+9] !='#': orientations.add(board[0:x-11]+"##"+board[x-9:x-1]+"#"+board[x:x+9]+"#"+board[x+10:])
        if count <= 7 and x + 2 <= 199: 
            if x - 10 < 0: gameOvers += 1
            elif board[x-10] !='#' and board[x-9] !='#' and board[x-8] !='#' and board[x+2] !='#': orientations.add(board[0:x-10]+"###"+board[x-7:x+2]+"#"+board[x+3:])
        if count <= 8 and count >= 1 and x + 1 <= 199: 
            if x - 11 < 0: gameOvers += 1
            elif board[x-10] !='#' and board[x-9] !='#' and board[x-11] !='#' and board[x+1] !='#': orientations.add(board[0:x-11]+"###"+board[x-8:x+1]+"#"+board[x+2:])
        if count >= 2: 
            if x - 10 < 0 or x - 22 < 0: gameOvers += 1
            elif board[x-22] !='#' and board[x-21] !='#' and board[x-20] !='#' and board[x-10] !='#': orientations.add(board[0:x-22]+"###"+board[x-19:x-10]+"#"+board[x-9:])
        if count <= 8: 
            if x - 10 < 0 or x - 19 < 0 or x - 29 < 0: gameOvers += 1
            elif board[x-10] !='#' and board[x-9] !='#' and board[x-19] !='#' and board[x-29] !='#': orientations.add(board[0:x-29]+"#"+board[x-28:x-19]+"#"+board[x-18:x-10]+"##"+board[x-8:])
        if count >= 1: 
            if x - 11 < 0 or x - 20 < 0 or x - 30 < 0: gameOvers += 1
            elif board[x-11] !='#' and board[x-10] !='#' and board[x-20] !='#' and board[x-30] !='#': orientations.add(board[0:x-30]+"#"+board[x-29:x-20]+"#"+board[x-19:x-11]+"##"+board[x-9:])
        count += 1
    return [orientations, gameOvers]

def findLOrientations(board, top, gameOvers):
    orientations = set()
    count = 0
    for x in top:
        if count <= 7: 
            if x - 10 < 0 or x - 18 < 0: gameOvers += 1
            elif board[x-10] !='#' and board[x-9] !='#' and board[x-8] !='#' and board[x-18] !='#': orientations.add(board[0:x-18]+"#"+board[x-17:x-10]+"###"+board[x-7:])
        if count <= 8 and count >= 1: 
            if x - 11 < 0 or x - 19 < 0: gameOvers += 1
            elif board[x-10] !='#' and board[x-9] !='#' and board[x-11] !='#' and board[x-19] !='#': orientations.add(board[0:x-19]+"#"+board[x-18:x-11]+"###"+board[x-8:])
        if count >= 2: 
            if x - 12 < 0 or x - 20 < 0: gameOvers += 1
            elif board[x-10] !='#' and board[x-12] !='#' and board[x-11] !='#' and board[x-20] !='#': orientations.add(board[0:x-20]+"#"+board[x-19:x-12]+"###"+board[x-9:])
        if count <= 8:
            if x - 10 < 0 or x - 20 < 0 or x - 30 < 0: gameOvers += 1
            elif board[x-10] !='#' and board[x-20] !='#' and board[x-30] !='#' and board[x-9] !='#':  orientations.add(board[0:x-30]+"#"+board[x-29:x-20]+"#"+board[x-19:x-10]+"##"+board[x-8:])
        if count >= 1: 
            if x - 11 < 0 or x - 21 < 0 or x - 31 < 0: gameOvers += 1
            elif board[x-11] !='#' and board[x-21] !='#' and board[x-31] !='#' and board[x-10] !='#': orientations.add(board[0:x-31]+"#"+board[x-30:x-21]+"#"+board[x-20:x-11]+"##"+board[x-9:])
        if count <= 7: 
            if x - 10 < 0 or x - 20 < 0: gameOvers += 1
            elif board[x-20] !='#' and board[x-19] !='#' and board[x-18] !='#' and board[x-10] !='#': orientations.add(board[0:x-20]+"###"+board[x-17:x-10]+"#"+board[x-9:])
        if count <= 8 and count >= 1 and x - 1 >= 0 and x - 1 <= 199: 
            if x - 11 < 0: gameOvers += 1
            elif board[x-11] !='#' and board[x-10] !='#' and board[x-9] !='#' and board[x-1] !='#': orientations.add(board[0:x-11]+"###"+board[x-8:x-1]+"#"+board[x:])
        if count >= 2 and x - 2 >= 0 and x - 2 <= 199: 
            if x - 10 < 0: gameOvers += 1
            elif board[x-12] !='#' and board[x-11] !='#' and board[x-10] !='#' and board[x-2] !='#': orientations.add(board[0:x-12]+"###"+board[x-9:x-2]+"#"+board[x-1:])
        if count <= 8 and x + 1 <= 199 and x + 11 <= 199: 
            if x - 10 < 0: gameOvers += 1
            elif board[x-10] !='#' and board[x-9] !='#' and board[x+1] !='#' and board[x+11] !='#': orientations.add(board[0:x-10]+"##"+board[x-8:x+1]+"#"+board[x+2:x+11]+"#"+board[x+12:])
        if count >= 1: 
            if x - 10 < 0 or x - 20 < 0 or x - 31 < 0: gameOvers += 1
            elif board[x-10] !='#' and board[x-20] !='#' and board[x-30] !='#' and board[x-31] !='#': orientations.add(board[0:x-31]+"##"+board[x-29:x-20]+"#"+board[x-19:x-10]+"#"+board[x-9:])
        count += 1
    return [orientations, gameOvers]

def transform(board):
    count = 0
    for x in range(0, 20):
        if " " not in board[count:count+10]: board = "          " + board[0:count]+board[count+10:]
        count += 10
    return board

finalOrients = []
f = []
tops = findTopBlocks(b)
f.append(findIOrientations(b, tops, 0))
f.append(findOOrientations(b, tops, 0))
f.append(findTOrientations(b, tops, 0))
f.append(findSOrientations(b, tops, 0))
f.append(findZOrientations(b, tops, 0))
f.append(findJOrientations(b, tops, 0))
f.append(findLOrientations(b, tops, 0))
for x in f:
    for y in x[0]:
        y2 = transform(y)
        if y2 not in finalOrients: finalOrients.append(y2)
    for x2 in range(0, x[1]): finalOrients.append("GAME OVER")
with open("tetrisout.txt", 'w') as f:
    for x in finalOrients:
        f.write(x)
        f.write('\n')