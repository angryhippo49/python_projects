# imports
from typing import List, Tuple, Union
from random import randint

# create a function to print the board
def print_board(l: List[List[str]]) -> None:
    for i in range(len(l)):
        for c in range(len(l[i])):
            print(l[i][c] + ' | ', end='')
        print("\n-----------")


# create a function to update the board
# given a board, a position and player, put the
# player's coin in the board, in the given position
def update_board(board: List, pos: Tuple, player: str) -> int:

    # if position is already taken, then print and return.
    if board[pos[0]][pos[1]] != ' ':
        print("Invalid move!")
        return False
    
    board[pos[0]][pos[1]] = player
    return True


def three_in_a_row(board: List, player = str) -> Union[Tuple, None]:
    mtlist = []
    mtlist1 = []
    mtlist2 = []
    diagonal1 = [board[0][0],board[1][1],board[2][2]]
    diagonal2 = [board[2][0],board[1][1],board[0][2]]
    for i in range(len(board)):
        if board[i].count(player) == 2:
            for c in range(len(board[i])):
                if board[i][c] == ' ':
                    return (i,c)

        mtlist += [board[i][0]]
        mtlist1 += [board[i][1]]
        mtlist2 += [board[i][2]]
    if mtlist.count(player) == 2:
        for i in range(len(mtlist)):
            if mtlist[i] == ' ':
                return (i,0)
    if mtlist1.count(player) == 2:
        for i in range(len(mtlist1)):
            if mtlist1[i] == ' ':
                return (i,1)
    if mtlist2.count(player) == 2:
        for i in range(len(mtlist2)):
            if mtlist2[i] == ' ':
                return (i,2)
    if diagonal1.count(player) == 2:
        for i in range(len(diagonal1)):
            if diagonal1[i] == ' ':
                return (i,i)
    if diagonal2.count(player) == 2:
        for i in range(len(diagonal2)):
            if diagonal2[i] == ' ':
                return (2-i,i)
    return None



# check if game over
def is_game_over(board: List[List[str]]) -> None:
    
    # check if there are 3 in a row anywhere
    for i in range(len(board)):
        if board[i].count('X') == 3:
            print("Player X won")
            return True
        if board[i].count('O') == 3:
            print("Player O won")
            return True
    
    # check if there are 3 in a coloumn anywhere
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i]:

            # make sure that spaces don't count
            if board[0][i] != ' ':
                print('Player',board[0][i],"won")
                return True
    
    # make sure that spaces don't count
    if board[1][1] != ' ':

        # check for diagonals
        if board[2][0] == board[1][1] == board[0][2]:
            print("Player",board[1][1],"won")
            return True
        if board[0][0] == board[1][1] == board[2][2]:
            print("Player",board[1][1],"won")
            return True
    
    # check to see if board isn't full
    for row in board:
        if row.count(' ') != 0:
            return False
    
    # else it is full and a tie
    print("It's a tie!")
    return True


# function for the computer move
def computer_move(board: List, player = str, comp = str) -> None:

    # use three in a row function but to try to win instead
    win = three_in_a_row(board = board, player = comp)
    if win != None:
        update_board(board = board, pos = win, player = comp)
        return
    # see if player needs to be blocked
    blockpos = three_in_a_row(board = board, player = player)
    # if three_in_a_row returned a required block, update with the needed position. Else, choose a random spot to fill
    if blockpos != None:
        update_board(board = board, pos = blockpos, player = comp)
        return
    else:
        # create an empty list for available spots for the computer
        validinputs = []

        # add the available spots to the list
        for i in range(len(board)):
            for c in range(len(board[i])):
                if board[i][c] == ' ':
                    validinputs += [(i,c)]
        
        # select a random valid spot for the computer
        comploc = validinputs[randint(0,len(validinputs)-1)]

        # update the board with this spot
        update_board(board,comploc,comp)


def create_board() -> List:
    l = [[' ' for _ in range(3)] for _ in range(3)]
    return l


def main():
    sym = input("What symbol do you want (X/O)? ")
    if sym == 'X':
        compsym = 'O'
    else:
        compsym = 'X'
    board = create_board()
    
    print("------ Empty Board -------")
    print_board(l = board)
    print("----------------------------")
    turn = input("Do you want to go first? ")
    if turn == 'No':
        computer_move(board = board, player = sym, comp = compsym)
        print("------ Computer's move -------")
        print_board(l = board)
        print("------------------------------")
    while True:

        # player's move
        player = eval(input('Where do you want to play, enter (i, j) in python index: '))
        check = update_board(board = board, pos = player, player = sym)
        if check == False:
            raise ValueError("Invalid move")
        print("------ Player's move -------")
        print_board(l = board)
        print("----------------------------")

        if is_game_over(board = board):
            break

        # computer's move
        computer_move(board = board, player = sym, comp = compsym)
        print("------ Computer's move -------")
        print_board(l = board)
        print("------------------------------")

        if is_game_over(board = board):
            break

# script
if __name__ == "__main__":
    main()