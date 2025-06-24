
board = [
    [".",".","."],  #row 0
    [".",".","."],  #row 1
    [".",".","."]]  #row 2 


#Variables:
player = "X" 


#functions
def printBoard(grid): #prints the board
    for row in grid:
        print("|",end = "")
        for number in row:
            print(number, end = "|")
        print()

def checkWinner(current_player,grid): #checks if someone wins 
    for i in range(len(grid)): 
        if grid[i][0] == grid[i][1] == grid[i][2] == current_player:
            print(f"Player {current_player} wins with a row victory!")
            return True
    if grid[0][0] == grid[1][1] == grid[2][2] == current_player:
        print(f"{current_player} wins with a left diagonal victory!")
        return True
    if grid[0][2] == grid[1][1] == grid[2][0] == current_player:
        print(f"{current_player} wins with a right diagonal victory!")
        return True
    for i in range(len(grid[0])):
        if grid[0][i] == grid[1][i] == grid[2][i] == current_player:
            print(f"{current_player} wins with a column victory!")
            return True

def switchPlayer(current_player): #switches the player
    if current_player == "X":
        return "O"
    elif current_player == "O":
        return "X" 
"""
test switchPlayer: 

print(player)
player = switchPlayer(player) 
print(player) 
"""

def main():
    board = [
    [".",".","."],  #row 0
    [".",".","."],  #row 1
    [".",".","."]]  #row 2 
    player = "O" 
    check = True 
    while check == True:
        printBoard(board)
        print(f"Player {player}'s turn.") 
        row = int(input("Enter the row in which you would like to place your peice:"))
        column = int(input("Enter the column in which you would like to place your peice: "))
        board[row][column] = player 
        if checkWinner(player, board) == True:
            check = False 
        player = switchPlayer(player) 

main() 

