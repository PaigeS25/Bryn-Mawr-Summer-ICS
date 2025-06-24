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

entrees = ["Steak", "Pasta", "Grilled Shrimp"]
prices = [25,18,19]

for i in range(len(entrees)):
    print(f"Entree: {entrees[i]} Price: {prices[i]}")

print("-------------")

entrees = {"Steak":25, "Pasta":18, "Grilled Shrimp":19}

print(entrees) 

keys = entrees.keys() 

print(keys) 

print("----------")

entrees["Lobster"] = 60
print(entrees["Lobster"])
print(entrees) 

#mutable: objects that can be modified without having to do a variable reassignment.
    #1) lists 
    #2) dictionaries 
#imutable: objects that can't be modified without having to do a variable reassignment.
    #1) numbers , integers, floats, etc.
    #2) strings 

print("---------")

mylist = [1,2,3,4]
mydict = {}
mydict["List"] = mylist 

print(mydict) 

print(mydict["List"][1])

student = {"Name": "John Smith", "Grade Level": 9, "Email": "Smithj@brynmawrschool.org"}
grades = {"English":65, "Math":100,"Social Studies":85, "Bio":70}

student["Grades"] = grades 

print(student["Grades"]["English"]) 

"""
mydict2 = {"Hello":"World"}
mydict4 = {"Mylist": [1,2,3,4]}
mydict3 = ["subdict"] = mydict4 
""" 
print(entrees) 

entrees.pop("Lobster")
print(entrees) 

for item in entrees:
    print(item)

for item in entrees:
    print(entrees[item])

for item in entrees: 
    entrees[item] += 5 

print(entrees) 

#to make functions: 
    #def<name of function>(<Optional: inputs>):
        #code

def hello():
    print("hello world!")

hello() 

def hello(name):
    print(f"Hello, {name}")

hello("Tim Cheese")
hello("John Pork")

def mean(nums):
    average = 0
    for num in nums:
        average += num 
    return(average/len(nums))

numbers = [1,2,3,4,5]
avg = mean(numbers)
print(avg) 
numbers2 = [2,8,25,65,100,250]
avg2 = mean(numbers2) 
print(avg2) 

print("-------")

