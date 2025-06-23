board = [
    ["X",".","."],  #row 0
    ["X",".","."],  #row 1
    ["X",".","."]]  #row 2 

for row in board:
    print("|", end = "")
    for number in row:
        print(number, end = "|")
    print()

current_player = "X" 

#row victory
for i in range(len(board)):
    if board[i][0] == board[i][1] == board[i][2] == current_player:
        print(f"Player {current_player} wins with row victory!")

#left diagonal victory
if board[0][0] == board[1][1] == board[2][2] == current_player: 
    print(f"Player {current_player} wins with diagonal victory!")

#right diagonal victory
if board[0][2] == board[1][1] == board[2][0] == current_player:
    print(f"Player {current_player} wins with a diagonal victory!")

#column victory
for i in range(len(board)):
    if board[0][i] == board[1][i] == board[2][i] == current_player:
        print(f"Player {current_player} wins with a column victory!")
