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


# main function
if __name__ == "__main__":
    # test 1
    board = [
        [' ',' ','O'],
        ['X',' ','X'],
        [' ',' ',' ']
    ]
    pos = (1,1)
    player = 'X'
    update_board(board, pos, player)
    print_board(board)

    # test 2
    board = [
        [' ',' ','O'],
        ['X',' ','X'],
        [' ',' ',' ']
    ]
    pos = (1,1)
    player = 'X'
    update_board(board, pos, player)
    print_board(board)



    