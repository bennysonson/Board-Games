import time
from random import randrange

playerR, playerY, player = 'R', 'Y', 'n'
optimalColumns = [4, 3, 5, 2, 6, 1, 7]

def printBoard(state):
    print("  1   2   3   4   5   6   7")
    print("-----------------------------")
    for x in state:
        print("| " + x[0] + " | " + x[1] + " | " + x[2] + " | " + x[3] + " | " + x[4] +
              " | " + x[5] + " | " + x[6] + " |")
        print("-----------------------------")
        
def placeMove(state, column, color):
    for i in range(6):
        if state[5 - i][column - 1] == ' ':
            state[5 - i][column - 1] = color 
            return 0
    return 42

def removeMove(state, column, color):
    for i in range(6):
        if state[i][column - 1] == color:
            state[i][column - 1] = ' '
            return 0
    return 42

def win_condition(state, color):
    #Horizontal check
    for i in range(6):
        for j in range(4):
            if state[i][j] == color and state[i][j + 1] == color and state[i][j + 2] == color and\
            state[i][j + 3] == color:
                return 1
    #Vertical check
    for i in range(3):
        for j in range(7):
            if state[i][j] == color and state[i + 1][j] == color and state[i + 2][j] == color and\
            state[i + 3][j] == color:
                return 1
    #Bottom left to top right check
    for i in range(3, 6):
        for j in range(4):
            if state[i][j] == color and state[i - 1][j + 1] == color and state[i - 2][j + 2] == color and\
            state[i - 3][j + 3] == color:
                return 1
    #Bottom right to top left check
    for i in range(3, 6):
        for j in range(3, 7):
            if state[i][j] == color and state[i - 1][j - 1] == color and state[i - 2][ j - 2] == color and\
            state[i - 3][j - 3] == color:
                return 1
    if (len(getOpenSpaces(state)) == 0):
        return 42
    return 0

def getRandom(state):
    openSpaces = getOpenSpaces(state)
    #return random open position
    return openSpaces[randrange(len(openSpaces))]

def getOpenSpaces(state):
    spaces = []
    for i in range(7):
        if state[0][i] == ' ':
            spaces.append(i + 1)
    return spaces

def copyBoard(state):
    newBoard = [[" ", " ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " ", " "], 
         [" ", " ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " ", " "], 
         [" ", " ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " ", " "]]
    for i in range(6):
        for j in range(7):
            newBoard[i][j] = state[i][j]
    return newBoard

def scoreYWin(depth):
    return depth - 1000

def scoreRWin(depth):
    return 1000 - depth

def maxAlphaBeta(state, alpha, beta, depth, maxDepth, isBaseCase):
    maxv = -1001
    if win_condition(state, playerR) == 1:
        return scoreRWin(depth)
    elif win_condition(state, playerY) == 1:
        return scoreYWin(depth)
    elif win_condition(state, playerY) == 42:
        return 0
    depth += 1
    if (depth == maxDepth):
        return 0
    for i in optimalColumns:
        if (placeMove(state, i, playerR) == 0):
            m = minAlphaBeta(state, alpha, beta, depth, maxDepth, False)
            if (m > maxv):
                maxv = m
                pos = i
            removeMove(board, i, playerR)
            if (maxv >= beta):
                return maxv
            if maxv > alpha:
                alpha = maxv
        else:
            continue
    if (isBaseCase):
        return pos
    return maxv

def minAlphaBeta(state, alpha, beta, depth, maxDepth, isBaseCase):
    minv = 1001
    if win_condition(state, playerR) == 1:
        return scoreRWin(depth)
    elif win_condition(state, playerY) == 1:
        return scoreYWin(depth)
    elif win_condition(state, playerY) == 42:
        return 0
    depth += 1
    if (depth == maxDepth):
        return 0
    for i in optimalColumns:
        if (placeMove(state, i, playerY) == 0):
            m = maxAlphaBeta(state, alpha, beta, depth, maxDepth, False)
            if (m < minv):
                minv = m
                pos = i
            removeMove(board, i, playerY)
            if (minv <= alpha):
                return minv
            if minv < beta:
                beta = minv
        else:
            continue
    if (isBaseCase):
        return pos
    return minv

#For checking if a board is one away from winning
def evaluateBoard(state, depth):
    score, pos = 0, 0
    for i in range(1, 8):
        if placeMove(state, i, playerY) == 0:
            if win_condition(state, playerY):
                score, pos =  scoreYWin(depth), i
            removeMove(state, i, playerY)
            placeMove(state, i, playerR)
            if win_condition(state, playerR):
                score, pos =  scoreRWin(depth), i
            removeMove(state, i, playerR)
    return score, pos

continuePlaying = 'Y'
while (continuePlaying.upper() == 'Y'):
    board = [
         [" ", " ", " ", " ", " ", " ", " "], 
         [" ", " ", " ", " ", " ", " ", " "], 
         [" ", " ", " ", " ", " ", " ", " "], 
         [" ", " ", " ", " ", " ", " ", " "],
         [" ", " ", " ", " ", " ", " ", " "], 
         [" ", " ", " ", " ", " ", " ", " "]]
    
    alternateOrder = 0
    turn = 1
    difficulty = input("Choose AI difficulty(1 or 77): ")
    orderOfPlay = input("Choose who goes first, R (You) or Y (AI): ")
    print("Turn: %d" % turn)
    if (orderOfPlay.upper() == 'R'):
        printBoard(board)
    #If AI goes first
    if (orderOfPlay.upper() == 'Y'):
        alternateOrder += 1
    while (win_condition(board, player) != 1 and win_condition(board, player) != 42):
        #Users move
        if alternateOrder % 2 == 0:
            player = playerR
            start = time.time()
            position = input("Enter column (1-7): ")
            position = int(position)
            end = time.time()
            #Invalid position
            if position > 7 or position < 1:
                continue
            #Place move and check if column is full
            if (placeMove(board, position, player) == 42):
                printBoard(board)
                print("Column full")
                continue
            print("Time elapsed: {}s".format(round(end - start, 7)))
            printBoard(board)
        #AIs move
        else:
            player = playerY
            #AI difficulty 1 - Random placement
            if (difficulty == '1'):
                position = getRandom(board)
                placeMove(board, position, playerY)
            #AI difficulty 99 - Unbeatable?
            #Even with heuristics, the minimax algorithm is too slow for first
            #few turns. Therefore, a less intensive search is performed during this period
            else:
                start = time.time()
                #Optimal to place in middle column first
                if (turn == 1):
                    position = 4
                #Less intensive search during beginning to improve time
                elif(turn < 16):
                    position = minAlphaBeta(board, -1001, 1001, 0, 9, True)
                #More intensive search
                else:
                    position = minAlphaBeta(board, -1001, 1001, 0, 11, True)
                end = time.time()
                print("Time elapsed: {}s".format(round(end - start, 7)))
                placeMove(board, position, playerY)
            printBoard(board)
            print("AI chose position %d" % position)
        alternateOrder += 1
        turn += 1
        if (win_condition(board, player) == 0):
            print("Turn: %d" % turn)
    if (win_condition(board, player) == 42):
        print("Draw")
    else:
        print("Winner: %s" % player)
    continuePlaying = input("Continue playing? (Y or N): ")
print("Bye!")
