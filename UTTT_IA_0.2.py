import random, copy, time, math


datas = [[' '] * 9 for _ in range(9)]
values = [[0] * 9 for _ in range(9)]
turn = 0
lastplayerinputs = [None] * 2
possiblexplay = [None] * 3
possibleyplay = [None] * 3
winTtt = [None] *9
start:float = 0
counter = 0


def printBoard(board):
    lig = 0
    print('    1   2   3    4   5   6    7   8   9')
    for i in range(3):
        for i in range(3):
            print("  |---|---|---||---|---|---||---|---|---|")
            print(str(lig+1) +' | ' + datas[lig][0] + ' | ' + datas[lig][1] + ' | ' + datas[lig][2] +  ' || ' + datas[lig][3] + ' | ' + datas[lig][4] + ' | ' + datas[lig][5] + ' || ' + datas[lig][6] + ' | ' + datas[lig][7] + ' | ' + datas[lig][8] + ' |')
            lig += 1
        print("  |---|---|---||---|---|---||---|---|---|")

def printValues():
    lig = 0
    global values
    print('    1 2 3   4 5 6   7 8 9')
    for i in range (3):
        print('  -------------------------')
        for i in range(3):
            print(str(lig+1) +' | ' + str(values[lig][0]) + ' ' + str(values[lig][1]) + ' ' + str(values[lig][2]) +  ' | ' + str(values[lig][3]) + ' ' + str(values[lig][4]) + ' ' + str(values[lig][5]) + ' | ' + str(values[lig][6]) + ' ' + str(values[lig][7]) + ' ' + str(values[lig][8]) + ' |')
            lig += 1
    print('  -------------------------')
        
def resetBoard():
    global datas
    datas = [[' '] * 9 for _ in range(9)]

def checkXValue(x):
    global possiblexplay
    return x not in possiblexplay

def checkYValue(y):
    global possibleyplay
    return y not in possibleyplay

def aiCheckXvalue(x,tmppossibleplay):
    return x not in tmppossibleplay
def aiCheckYvalue(y,tmppossibleplay):
    return y not in tmppossibleplay

def checkWinTTT(board):
    global winTtt
    wins = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]

    for tttNum in range(9):
        raw = tttNum // 3
        col = tttNum % 3
        tttX = [0] * 9
        tttO = [0] * 9

        if winTtt[tttNum] == None:
            for i in range(3):
                for j in range(3):
                    if board[raw * 3 + i][col * 3 + j] == 'X':
                        tttX[i * 3 + j] = 1
                    if board[raw * 3 + i][col * 3 + j] == 'O':
                        tttO[i * 3 + j] = 1
            for win in wins:
                if all(tttX[i] == 1 for i in win):
                    winTtt[tttNum] = 'X'
                    return True
            for win in wins:
                if all(tttO[i] == 1 for i in win):
                    winTtt[tttNum] = 'O'
                    return True
    return False
 
def iaCheckWinTTT(board):
    global winTtt
    tmpwinTtt = [None]*9
    wins = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    for tttNum in range(9):
        raw = tttNum // 3
        col = tttNum % 3
        tttX = [0] * 9
        tttO = [0] * 9

        if winTtt[tttNum] == None:
            for i in range(3):
                for j in range(3):
                    if board[raw * 3 + i][col * 3 + j] == 'X':
                        tttX[i * 3 + j] = 1
                    if board[raw * 3 + i][col * 3 + j] == 'O':
                        tttO[i * 3 + j] = 1
            for win in wins:
                if all(tttX[i] == 1 for i in win):
                    tmpwinTtt[tttNum] = 'X'
                    return True
            for win in wins:
                if all(tttO[i] == 1 for i in win):
                    tmpwinTtt[tttNum] = 'O'
                    return True
    return False

def checkWin():
    wins = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    global winTtt
    for win in wins:
        if all(winTtt[i] == 'O' for i in win):
            print('Le joueur O a remporté la Partie')
            return True
        if all(winTtt[i] == 'X' for i in win):
            print('Le joueur X a remporté la Partie')
            return True
    return False
                
def checkPossiblePlays(x,y):
    global possiblexplay
    global possibleyplay
    if x == 1 or x == 4 or x == 7:
        possiblexplay[0] = 1
        possiblexplay[1] = 2
        possiblexplay[2] = 3
    elif x == 2 or x == 5 or x == 8:
        possiblexplay[0] = 4
        possiblexplay[1] = 5
        possiblexplay[2] = 6
    elif x == 3 or x == 6 or x == 9:
        possiblexplay[0] = 7
        possiblexplay[1] = 8
        possiblexplay[2] = 9
    if y == 1 or y == 4 or y == 7:
        possibleyplay[0] = 1
        possibleyplay[1] = 2
        possibleyplay[2] = 3
    elif y == 2 or y == 5 or y == 8:
        possibleyplay[0] = 4
        possibleyplay[1] = 5
        possibleyplay[2] = 6
    elif y == 3 or y == 6 or y == 9:
        possibleyplay[0] = 7
        possibleyplay[1] = 8
        possibleyplay[2] = 9
    possiblesPlays = [possiblexplay,possibleyplay]
    return possiblesPlays

def iaCheckPossiblePlays(x,y):
    
    tmppossiblexplay = [None] * 3
    tmppossibleyplay = [None] * 3
    if x[0] == 1 or x[0] == 4 or x[0] == 7:
        tmppossiblexplay[0] = 1
        tmppossiblexplay[1] = 2
        tmppossiblexplay[2] = 3
    elif x[0] == 2 or x[0] == 5 or x[0] == 8:
        tmppossiblexplay[0] = 4
        tmppossiblexplay[1] = 5
        tmppossiblexplay[2] = 6
    elif x[0] == 3 or x[0] == 6 or x[0] == 9:
        tmppossiblexplay[0] = 7
        tmppossiblexplay[1] = 8
        tmppossiblexplay[2] = 9
    if y[0] == 1 or y[0] == 4 or y[0] == 7:
        tmppossibleyplay[0] = 1
        tmppossibleyplay[1] = 2
        tmppossibleyplay[2] = 3
    elif y[0] == 2 or y[0] == 5 or y[0] == 8:
        tmppossibleyplay[0] = 4
        tmppossibleyplay[1] = 5
        tmppossibleyplay[2] = 6
    elif y[0] == 3 or y[0] == 6 or y[0] == 9:
        tmppossibleyplay[0] = 7
        tmppossibleyplay[1] = 8
        tmppossibleyplay[2] = 9
    possiblesPlays = [tmppossiblexplay,tmppossibleyplay]
    return possiblesPlays

def printPossiblePlays():
    global turn
    global datas
    if turn == 0:
        print("Les coups possibles sont : All")
    else:
        print("Les coups possibles sont :")
        for i in possiblexplay:
            for j in possibleyplay:
                if datas[i-1][j-1] == ' ':
                    print(str(i) + ' ' + str(j))

def playerTurn():
    printPossiblePlays()
    try:    
        global turn
        inx = int(input('Ligne : '))
        if turn == 0:
            if (inx < 1 or inx >= 9 ):
                print("La valeur doit etre comprise etre 1 et 9 compris")
                return False
        elif checkXValue(inx):
            print("La valeur est incorrect")
            return False
        iny = int(input('Colonne : '))
        if turn == 0:
            if (iny < 1 or inx >= 9):
                print("La valeur doit etre comprise etre 1 et 9 compris")
                return False
        elif checkYValue(iny):
            print("La valeur est incorrect")
            return False
        global datas
        if datas[inx - 1][iny - 1] == ' ':
                datas[inx - 1][iny - 1] = 'X'
                lastplayerinputs[0]= inx
                lastplayerinputs[1]= iny
                turn += 1
                return True
        else:
            print("La case est déja prise")
            return False
    except ValueError:
        print("La saisie doit être un entier.")
        return False

def aiTurn():
   # print(lastplayerinputs)
    res = minimax(datas, 3, -math.inf, math.inf, True, lastplayerinputs[0], lastplayerinputs[1], [[None,None]])
    xandy = res[1]
   # print('Max value = ' + str(res[0]))
    rxandy = random.choice(xandy)
    datas[rxandy[0]][rxandy[1]] = 'O'
    lastplayerinputs[0]=rxandy[0]+1
    lastplayerinputs[1]=rxandy[1]+1
    checkPossiblePlays(rxandy[0]+1, rxandy[1]+1)
    global turn
    turn +=1

def minimax(state, depth, alpha, beta, isplayerO, x, y, xandy):
    
    global counter
    maxdepth= depth
    tmpDatas = copy.deepcopy(state)
    lastinputs = [[x], [y]]
    possiblesPlays = iaCheckPossiblePlays(lastinputs[0], lastinputs[1])
    if isplayerO:
        maxRes = -math.inf
        for x_val in possiblesPlays[0]:
            for y_val in possiblesPlays[1]:
                #print('test')
                if tmpDatas[x_val - 1][y_val - 1] == ' ':
                    tmpDatas[x_val - 1][y_val - 1] = 'O'
                    counter += 1
                    if iaCheckWinTTT(tmpDatas):
                        res = 1000
                        
                    elif depth == 0:
                        tmpvalues = tttAnalysis(tmpDatas)
                        addedvalues = addValues(tmpvalues)
                        res = addedvalues
                        tmpvalues = resetValues(tmpvalues)
                    else:
                        res = minimax(tmpDatas, depth - 1, alpha, beta, not isplayerO, x_val, y_val, [[None,None]])[0]
                    if res>= maxRes and depth ==maxdepth:
                        xandy.append([x_val - 1,y_val - 1])
                        if res > maxRes:
                           xandy = [[x_val - 1,y_val - 1]]
                    maxRes = max(maxRes, res)
                    alpha = max(alpha, res)
                    tmpDatas[x_val - 1][y_val - 1] = ' '
                    if beta <= alpha:
                        break
        return maxRes, xandy
    else:
        minRes = math.inf
       # print('les coups possibles sont : ' + str(possiblesPlays))
        for x_val in possiblesPlays[0]:
            for y_val in possiblesPlays[1]:
                if tmpDatas[x_val - 1][y_val - 1] == ' ':
                    tmpDatas[x_val - 1][y_val - 1] = 'X'
                    if iaCheckWinTTT(tmpDatas) == True:
                        res = -1000
                    if depth == 0:
                        tmpvalues = tttAnalysis(tmpDatas)
                        #printBoard(tmpDatas)
                        #print(tmpDatas)
                        #printBoard(tmpvalues)
                        addedvalues = addValues(tmpvalues)
                        #print(addedvalues)
                        res = addedvalues
                        tmpvalues = resetValues(tmpvalues)
                    else:
                        res = minimax(tmpDatas, depth - 1, alpha, beta, not isplayerO, x_val, y_val, [[None,None]])[0]             
                    minRes = min(minRes, res)
                    beta = min(beta, res)
                    tmpDatas[x_val - 1][y_val - 1] = ' '
                    if beta <= alpha:
                        break
        
        return minRes, xandy
  
def tttAnalysis(tmpdatas): 
    tmpvalues = [[0] * 9 for _ in range(9)]
    for i in range(3):
        for j in range(3):
            startX = i*3
            startY = j%3*3
            for x in range(3):
                for y in range(3):
                    #Permet de valoriser les cases sur la meme colonne et ligne.
                    indicex = 1
                    indiceo = 1
                    for i in range(2):
                        if tmpdatas[(x)%3+startX][(y+4+i)%3+startY] == 'O':
                            tmpvalues[startX +x][startY +y] +=indiceo
                            indiceo += 1
                        elif tmpdatas[(x)%3+startX][(y+4+i)%3+startY] == 'X':
                            tmpvalues[startX +x][startY +y] -=indicex
                            indicex -= 1
                        if tmpdatas[(x+4+i)%3+startX][(y)%3+startY] == 'O':
                            tmpvalues[startX +x][startY +y] +=indiceo
                            indiceo += 1
                        elif tmpdatas[(x+4+i)%3+startX][(y)%3+startY] == 'X':
                            tmpvalues[startX +x][startY +y] -=indicex   
                            indicex -= 1  
                    #Permet de valoriser les cases en diagonales (de haut/gauche à bas/droit).
                    indiceo = 1
                    indicex = 1
                    for i in range(2):
                        if y%3 == x%3:
                            if tmpdatas[(x+4+i)%3+startX][(y+4+i)%3+startY] =='O':
                                tmpvalues[startX +x][startY +y] +=indiceo
                                indiceo +=1
                            elif tmpdatas[(x+4+i)%3+startX][(y+4+i)%3+startY] =='X':
                                tmpvalues[startX +x][startY +y] -=indicex
                                indicex -=1
                    #Permet de valoriser les cases en diagonales (de haut/droite à bas/gauche).
                    indiceo = 1
                    indicex = 1
                    for i in range(2):
                        if (x + y) % 3 == 2:
                            if tmpdatas[(x + 4 + 1 - i) % 3+startX][(y + 4 + 3 - i*2) % 3+startY] == 'O':
                                tmpvalues[startX + x][startY + y] += indiceo 
                                indiceo +=1
                            elif tmpdatas[(x + 4 + 1 - i) % 3+startX][(y + 4 + 3 - i*2) % 3+startY] == 'X':
                                tmpvalues[startX + x][startY + y] -= indicex
                                indicex -=1   
    return tmpvalues 

def resetValues(values):
    values = [[0] * 9 for _ in range(9)]
    return values

def test():
    global winTtt
    winTtt[0] = 'O'
    winTtt[2] = 'O'
    winTtt[1] = 'O'

def addValues(tmpvalues):
    addedvalues = 0
    for x in range(9):
        for y in range(9):
            addedvalues += tmpvalues[x][y]
    return addedvalues



#=========================================================================================================

turn = 0
x = None
while x != 'y' and x != 'n':
    x = input('Voulez-vous commencer ? (y/n)')

if x == 'y':
    while True:
        while not playerTurn():
            pass
        if checkWin():
                break
        counter = 0
        aiTurn()
        printBoard(datas)
        print("L'ia a joué en : "+ str(lastplayerinputs))
        if checkWinTTT(datas):
            print('un ttt a été gagné')
        resetValues(values)
        if checkWin():
                break
else:
    lastplayerinputs[0] = random.randint(1, 9)
    lastplayerinputs[1] = random.randint(1, 9)
    while True:
        aiTurn()
        printBoard(datas)
        print("L'ia a joué en : "+ str(lastplayerinputs))
        if checkWin():
                break
        if checkWinTTT(datas):
            print('un ttt a été gagné')
        while not playerTurn():
            pass
        counter = 0
        if checkWinTTT(datas):
            print('un ttt a été gagné')
        resetValues(values)
        if checkWin():
                break



    

