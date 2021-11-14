import math

# establishing the board and the victor. 
def __init__(self):
    self.board = self.printBoard()
    self.victor = None

def theBoard():     #   creating a board with 9 total places to fill.
        return [' ' for _ in range(9)]


def printBoard(self):                        # the function to print the board. 
    for row in [self.theBoard[i * 3:
        (i + 1) * 3]
        for i in range(3)]:
            print('| '+' | '.join(row)+' |')        # joining strings to print complete rows.


def boardPlaces():
    places = [[str(i) for i in range(a * 3, (a + 1)*3)]for a in range(3)]       # assigning numbers to the places for clarity.
    for row in places:
        print('| '+' | '.join(row)+' |')

def playerMoves(self,square,letter):        # making the player choose a space and letter 
    if self.theBoard[square] == ' ':
        self.theBoard[square] == letter
        if self.won(square,letter):
            self.victor = letter
        return True
    return False

#   Are the moves ending the game? this function checks
def checkWin(self, square, letter):     # checking the the rows for same letter
    rowcheck = math.floor(square/3)
    row = self.theBoard[rowcheck * 3: (rowcheck + 1) * 3]

    if all([s == letter for s in row]):            # if player has occupied all of the places in the row, they are the victor.
        return True

    columnCheck = square % 3
    column = [self.theBoard[columnCheck + i * 3] for i in range()]






# user input (index 1-9)
# check if the index is taken
# else - invalid, try again
# else - add it to the board
# check rows, columns, and diagonals if user has won. 

