# Minesweeper
Minesweeper is a classic single-player puzzle game that has been included with various operating systems, such as Microsoft Windows, since the 1990s. The goal of the game is to clear a rectangular board of hidden "mines" without detonating any of them.

The board is divided into a grid of squares, and each square may contain a mine or a number indicating how many mines are adjacent to that square. The player must use logical deduction to determine which squares are safe to click and which ones contain mines. If the player clicks on a square containing a mine, the game is over.

Minesweeper is known for its simple gameplay mechanics but can be quite challenging and addictive. It has become a popular pastime for people of all ages and skill levels.

## Instructions to run the game

* Open the Github repository where the game code is hosted.

* Click on the green "Code" button and then select "Download ZIP" to download the code as a ZIP file.

* Extract the ZIP file to a folder on your computer.

* Open a command prompt or terminal window and navigate to the folder where you extracted the code.

* Type ```python mine.py``` and press Enter to start the game.

* Follow the prompts to play the game.

## Functionality of the code

* The code imports the random module, which is used to generate random numbers.

* run, mine, numCount, mainList, and mineList are initialized as variables. mainList and mineList are empty lists.

* The code prompts the user to enter the size of the board and reads the input as boardSize. It then calculates the number of mines (n) based on the board size.

* The code uses the random.sample() method to create two lists (a1 and a2) of n random integers between 0 and boardSize (exclusive). These lists are used to create the mineList, which is a list of tuples representing the coordinates of the mines on the board.

* The code creates the mainList as a nested list of size boardSize by boardSize. Each element of the list is initialized to '-'.

* The currentBoardStatus() function is defined to print the current status of the board. It takes boardSize and mainList as arguments.

* The main game loop starts with a while loop that runs as long as run is True.

* In each iteration of the loop, the currentBoardStatus() function is called to print the current status of the board.

* The user is prompted to enter the row and column numbers of the square they want to select.

* If the user enters a row or column number that is out of bounds, the code displays an error message and continues to the next iteration of the loop.

* If the user selects a square that contains a mine, the game is over and the code sets run to False. The coordinates of the mines are revealed by replacing the '-' in the mainList with '*'.

* If the user selects a square that does not contain a mine, the code generates a random number between 0 and 9 and assigns it to the selected square in mainList. The numCount variable is incremented by 1.

* After each selection, the code checks if the user has won the game by comparing numCount to the total number of squares on the board (boardSize squared minus the number of mines n).

* If the user has won the game, the code sets run to False and displays a winning message.

* Finally, the currentBoardStatus() function is called again to print the final status of the board.
