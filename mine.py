import random





# game variables..
run = True
mine = False
numCount = 0
mainList = []        # main board for the game
mineList = []        # mine list





print('''It's a square board so enter your board size in a single number like,
      3 for 3*3 = 9 box board
      4 for 4*4 = 16 box board''')
boardSize = int(input("Enter board size: "))

# n - number of mines..
n = int((boardSize**2)*(0.25))         # (0.25)25% of total size





# creating list of mines..
a1 = random.sample(range(boardSize), n)     # for creating non-repeating random nums
a2 = random.sample(range(boardSize), n)
for i in range(n):
    mineList.append((a1[i], a2[i]))
    



# creating mainList for the game..
mainList = [['-' for i in range(boardSize)] for j in range(boardSize)]




#print(mineList)     # To see the mine locations







#function to print current status of the board..
def currentBoardStatus(boardSize, mainList):
    
    # prints the current status of the board..
    print('\nCurrent status of your board is:')
    for i in range(-1, boardSize):
        if (i == -1):
            print(" ", end = " ")
        else:
            print(i, end = " ")
    print("\n")
    
    for i in range(boardSize):
        print(i, end = " ")
        for j in range(boardSize):
            print(mainList[i][j], end=" ")
        print("\n")
    
    



# main game loop..
print('''Here starts your Minesweeper Game.''')

while(run):    
    currentBoardStatus(boardSize, mainList)
    
    # user inputs..
    row = int(input('Enter row number: '))
    column = int(input('Enter column number: '))
    
    # if user choice is out of index then show error..
    if (row > boardSize-1 or row < 0 or column > boardSize-1 or column < 0):
        print('\nWrong choice, choose again.')
        continue
        
    # checks if user select mine or not..
    if ((row,column) in mineList):
        print('\nYou Lost!')
        run = False
        for i in mineList:
            a = i[0]
            b = i[1]
            mainList[a][b] = '*'
    else:
        if (mainList[row][column] == '-'):
            mainList[row][column] = random.randint(0,9)
            numCount += 1
        else:
            pass
        



    #checks if user won or not..
    if (numCount == boardSize**2-n):
        print('\nYou Won!')
        run = False
    else:
        pass
# prints the final status of the board..
currentBoardStatus(boardSize, mainList)
