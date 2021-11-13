# establishing the board. A dictionary with empty values attatched to the 9 keys. 
theBoard = {'7':' ','8':' ','9':' ',
        '4':' ','5':' ','6':' ',
        '1':' ','2':' ','3':' '}
board_keys=[]
for key in theBoard:
    board_keys.append(key)

def printBoard(board):
    print(board['7']+'|'+board['8']+'|'+board['9'])
    print('-+-+-')
    print(board['4']+'|'+board['5']+'|'+board['6'])
    print('-+-+-')
    print(board['1']+'|'+board['2']+'|'+board['3'])
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
            print("Invalid, that's taken.\n Choose another space")         # tell the user the choice is invalid and to choose another. 
            continue
        if count >=5:
            if theBoard['7'] == theBoard['8'] == theBoard['9'] != ' ': # across the top
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")                
                break
            elif theBoard['4'] == theBoard['5'] == theBoard['6'] != ' ': # across the middle
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break
            elif theBoard['1'] == theBoard['2'] == theBoard['3'] != ' ': # across the bottom
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break
            elif theBoard['1'] == theBoard['4'] == theBoard['7'] != ' ': # down the left side
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break
            elif theBoard['2'] == theBoard['5'] == theBoard['8'] != ' ': # down the middle
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break
            elif theBoard['3'] == theBoard['6'] == theBoard['9'] != ' ': # down the right side
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break 
            elif theBoard['7'] == theBoard['5'] == theBoard['3'] != ' ': # diagonal
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break
            elif theBoard['1'] == theBoard['5'] == theBoard['9'] != ' ': # diagonal
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break 

        # If neither X nor O wins and the board is full, we'll declare the result as 'tie'.
        if count == 9:
            print("\nGame Over.\n")                
            print("It's a Tie!!")

        # we have to change the player after every move.
    if turn =='X':
        turn = 'O'
    else:
        turn = 'O' 
    
    restart = input("Play again? (y for yes/n for no)")
    if restart == "y":
        for key in board_keys:
            theBoard[key] = " "

        game()
if __name__=="__main__":
    game()

    
