from random import randrange

"""
TicTacToe program ran on command line. Two AI difficulty choices, level 1 and 99. 
Level 1 AI places moves randomly. Level 99 AI uses minimax algorithm to make perfect decisions.
"""

board = [[" ", " ", " "], [" ", " ", " "] , [" ", " ", " "]]
playerX, playerO, player = 'X', 'O', 'n'

def printBoard():
    for x in board:
        print(x)

def place_move(state, position, player):
    if position % 3 == 0:
        if (state[(position // 3) - 1][(position - 1) % 3]) == ' ':
            state[(position // 3) - 1][(position - 1) % 3] = player
        else:
            print("Spot is already occupied")
            return 42
    else:
        if (state[(position // 3)][(position - 1) % 3]) == ' ':
            state[(position // 3)][(position - 1) % 3] = player
        else:
            print("Spot is already occupied")
            return 42

def win_condition(state, player):
    if (state[0][0] == player and state[0][1] == player and state[0][2] == player) or\
     (state[1][0] == player and state[1][1] == player and state[1][2] == player) or\
     (state[2][0] == player and state[2][1] == player and state[2][2] == player) or\
     (state[0][0] == player and state[1][0] == player and state[2][0] == player) or\
     (state[0][1] == player and state[1][1] == player and state[2][1] == player) or\
     (state[0][2] == player and state[1][2] == player and state[2][2] == player) or\
     (state[0][0] == player and state[1][1] == player and state[2][2] == player) or\
     (state[0][2] == player and state[1][1] == player and state[2][0] == player):
        return 1
    if (len(getOpenSpaces(state)) == 0):
        return 42
    return 0
    
def copyBoard(state):
    newBoard = [[" ", " ", " "], [" ", " ", " "] , [" ", " ", " "]]
    for i in range(3):
        for j in range(3):
            newBoard[i][j] = state[i][j]
    return newBoard
    
def getRandomMove():
    openSpaces = getOpenSpaces(board)
    #return random open position
    return openSpaces[randrange(len(openSpaces))]

def getOpenSpaces(state):
    openSpaces = []
    #Find open spaces on board in terms of position
    for i in range(3):
        for j in range(3):
            if state[i][j] == ' ':
                openSpaces.append((i * 3) + (j % 3) + 1)
    return openSpaces


def scoreOWin(depth):
    return depth - 10

def scoreXWin(depth):
    return 10 - depth

#Minimax algorithm implementation to find best possible move. 
def getBestMove(game, depth, player, isBaseCase):
    if (win_condition(game, playerO) == 1):
        return scoreOWin(depth)
    elif (win_condition(game, playerX) == 1):
        return scoreXWin(depth)
    elif (win_condition(game, playerX) == 42 or win_condition(game, playerO) == 42):
        return 0
    depth += 1
    scores = []
    moves = []
    for availMove in getOpenSpaces(game):
        newBoard = copyBoard(game)
        if (player == playerO):
            place_move(newBoard, availMove, playerO)
            scores.append(getBestMove(newBoard, depth, playerX, False))
        elif (player == playerX):
            place_move(newBoard, availMove, playerX)
            scores.append(getBestMove(newBoard, depth, playerO, False))
        moves.append(availMove)
    if (player == playerX):
        maxScore = -100
        i = 0
        for score in scores:
            if score > maxScore:
                maxScore = score
                maxScoreIndex = i
            i += 1
        if (isBaseCase):
            return moves[maxScoreIndex]
        return scores[maxScoreIndex]
    elif (player == playerO):
        minScore = 100
        i = 0
        for score in scores:
            if score < minScore:
                minScore = score
                minScoreIndex = i
            i += 1
        if (isBaseCase):
            return moves[minScoreIndex]
        return scores[minScoreIndex]

"""
Script for playing game
"""
continuePlaying = 'Y'
while (continuePlaying.upper() == 'Y'):
    board = [[" ", " ", " "], [" ", " ", " "] , [" ", " ", " "]]
    alternateOrder = 0
    turn = 1
    difficulty = input("Choose AI difficulty(1 or 99): ")
    orderOfPlay = input("Choose who goes first, X (You) or O (AI): ")
    print("Turn: %d" % turn)
    if (orderOfPlay.upper() == 'X'):
        printBoard()
    #If AI goes first
    if (orderOfPlay.upper() == 'O'):
        alternateOrder += 1
    while (win_condition(board, player) != 1 and win_condition(board, player) != 42):
        #Users move
        if alternateOrder % 2 == 0:
            player = playerX
            position = input("Enter position (1-9): ")
            position = int(position)
            #Invalid position
            if position > 9 or position < 1:
                continue
            #Place move and check if spot is already taken
            if (place_move(board, position, player) == 42):
                printBoard()
                continue
            printBoard()
        #AIs move
        else:
            player = playerO
            #Difficulty 1, AI chooses randomly
            if (difficulty == '1'):
                position = getRandomMove()
                place_move(board, position, player)
            #Difficulty 99, AI is W O K E
            else:
                if (turn == 1):
                    cornerPos = [1, 3, 7, 9]
                    position = cornerPos[randrange(len(cornerPos))]
                    place_move(board, position, player)
                else:
                    position = getBestMove(board, 0, playerO, True)
                    place_move(board, position, player)
            printBoard()
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
