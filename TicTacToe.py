# establishing the board. A dictionary with empty values attatched to the 9 keys. 




theBoard = [        # Creating the board for the player and computer
        ["-","-","-"],
        ["-","-","-"],
        ["-","-","-"]
]
def printBoard(theBoard):       # the function to print the board. 
    for row in theBoard:
        for place in row:
            print(f"{place} ", end="")       # an f string to print the variable and not the string.
        print()
printBoard(theBoard)
def exit(input):                # quit function
    if input.lower == "q":      # changing all user input to lowercase in case the user enters a capital letter
        return True
    else: 
        return False
while True:
    choices = input("Make a move, 1(bottom left) to 9(top right) or \"q\" to quit: ")
    if exit:
        print("Exiting game")
        break
    













'''
board_keys=[]
for key in theBoard:
    board_keys.append(key)
player, opponent = 'X','O'
'''




# user input (index 1-9)
# check if the index is taken
# else - invalid, try again
# else - add it to the board
# check rows, columns, and diagonals if user has won. 



'''
def game():
    turn = 'X'
    count = 0
    for i in range(10):     # beginning the for loop 
        printBoard(theBoard)
        print("It is now "+ turn + "'s turn, where do you move?")
        move = input()                  # ask the user for input
        if theBoard[move] == ' ':       # if the user inputs a key for a value that is empty
            theBoard[move] = turn       # fill the block
            count = count + 1           # iterate the count by 1
        else:                           # any other user input
            print("That spot is taken.\n Choose another space")         # tell the user the choice is invalid and to choose another. 
            continue
        

        # If neither X nor O wins and the board is full, we'll declare the result as 'tie'.
        if count == 9:
            print("\nGame Over.\n")                
            print("It's a Tie!!")

        # we have to change the player after every move.
    def next_player(turn):
        if turn == 'X':
            turn = 'O'
        if turn == 'O':
            turn = 'X'
        return turn

    restart = input("Play again? (y for yes/n for no)")
    if restart == "y":
        for key in board_keys:
            theBoard[key] = " "

        game()
if __name__=="__main__":
    game()

'''    
