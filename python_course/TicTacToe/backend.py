# imports
from typing import List, Tuple


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
        return -1
    
    board[pos[0]][pos[1]] = player
    return 1


# check if game over
def is_game_over(board: List[List[str]]) -> None:
    
    # check if there are 3 in a row anywhere
    for i in range(len(board)):
        if board[i].count('X') == 3:
            print("Player X won")
            return True
        if board[i].count('O') == 3:
            print("player O won")
            return True
    
    # check if there are 3 in a coloumn anywhere
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i]:

            # make sure that spaces don't count
            if board[0][i] != ' ':
                print('player ',board[0][i],"won")
                return True
    
    # make sure that spaces don't count
    if board[1][1] != ' ':

        # check for diagonals
        if board[2][2] == board[1][1] == board[0][2]:
            print("player ",board[1][1],"won")
            return True
        if board[0][0] == board[1][1] == board[2][2]:
            print("player ",board[1][1],"won")
            return True
    
    # check to see if board isn't full
    for row in board:
        if row.count(' ') != 0:
            return False
    
    # else it is full and a tie
    print("It's a tie!")
    return True


# main function
if __name__ == "__main__":
    # test 1
    board = [
        [' ','X','O'],
        [' ','O','X'],
        [' ','O','X']
    ]
    print(is_game_over(board))

