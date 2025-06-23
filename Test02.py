twoDlist = [
    [1,2,3,4,],      #row 0
    [5,6,7,8],      #row 1
    [9,10,11,12],   #row 2 
    [13,14,15,16]]  #row 3 
print(twoDlist)

print(twoDlist[0][1])
print(twoDlist[0])
twoDlist.append([17,18,19,20])
print(twoDlist)

"""
twoDlist[0].append(10)
print(twoDlist)
""" 

for row in twoDlist:
    for item in row:
        print(item) 

for i in range(len(twoDlist)):
    for j in range(len(twoDlist[0])): #right now it doesn't matter what index you put in len(twoDlist[])
        print(twoDlist[i][j])

twoDlist = [
    [1,2,],
    [3,4]
]

"""
for i in range(len(twoDlist)):
    for j in range(len(twoDlist[0])):
        if twoDlist[i][j] == 2:
            twoDlist[0].append(100)
        print(twoDlist) 
""" 

for i in range(len(twoDlist)):
    j = 0
    while j < len(twoDlist[i]):
        if twoDlist[i][j] == 2:
            twoDlist[0].append(100)
        print(twoDlist[i][j])
        j = j + 1 

board = [
    [".",".",".","."],  #row 0
    [".",".",".","."],  #row 1
    [".",".",".","."],  #row 2 
    [".",".",".","."]]  #row 3 

for row in board:
    print("|", end = "")
    for number in row:
        print(number, end = "|")
    print()