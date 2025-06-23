print("Hello World")

print(5 + 10)

number = 10

print(number)

num2 = 5

print(number + num2)

name = "Paige Stevens"

print(name)

number = 10 
print(number)

number = 25
print (number)

print("demo input")

#name = input("what is your name? ")

print(name)

#print("input and math") 

#num1 = int(input("type in num 1: "))
#num2 = int(input("type in num 2: "))
#sum = num1 + num2

#print(f"the sum of {num1} and {num2} is {sum} ")

var1 = True
if var1 == True:
    print("Hello, World!")

var2 = False 
if var2 == True: 
    print("hello")
print("hey")

var3 = 5
if var3 > 4: 
    print("cat")
"""
num = int(input("enter number: "))
if num % 2 == 1:
    print(f"{num} is an odd number.")
else:
    print(f"{num} is an even number.")

if num % 5 == 0:
    print(f"{num} is divisable by 5.")
if num % 2 == 0:
    print(f"{num} is divisable by 2.")
else:
    print(f"{num} is not divisable by 5 or 2.") 

print("welcome to our baltimore sports program:")
print("1, football.")
print("2, baseball.")
option = input("enter the sport you like best: ")
if option == "football":
    print("Ravens!")
elif option == "baseball":
    print("Orioles!")
"""

text = "HELLO"
print(text)
text = text.lower()
print(text) 

str1 = " "
str2 = "world"

newstr = " ".join(str2)

print(newstr)

fruits = ["mangoes","bananas","apples","strawberries","grapes"]
#Strawberries is at index 3, because
#lists start at index zero (0) 

print(fruits)
print(fruits[3])

fruits[3] = "raspberries"

print(fruits)

fruits.append("strawberries")

print(fruits) 

mylist = [1,2,3,"Paige Stevens",True]
print(mylist) 

"""
x = 0
while x < 5:
    print(x)
    x = x + 1

x = 1
while x <= 100:
    if x % 3 == 0:
        print(f"{x} is divisable by 3.")
    x = x + 1 
"""
"""
cash = 0
bank = 100
check = True
print("Welcome to the bank!")
print("1. Withdraw.")
print("2. Deposit")
print("3. Quit")
while check == True:
    print(f"your balence is {cash}: ")
    print(f"bank's balence is {bank}: ")
    print("Select your option from the list above: ")
    if option == "withdraw":
        bank = bank - 10
        cash = cash + 10
    elif option == "deposit":
        bank = bank + 10
        cash = cash - 10
    elif option == "quit":
        check = False
    else:
        print("Invalid option.")
"""
nums = [10,20,30,40,50]
for x in nums:
    print(x)

fruits = ["oranges", "apples", "mangoes", "cherries", "grapes"]
for fruit in fruits:
    if fruit == "cherries" or fruit == "grapes": 
        print(f"{fruit} is a small fruit.")
    elif fruit == "apples" or fruit == "oranges" or fruit == "magoes":
        print(f"{fruit} is a large fruit.") 
"""
nums = [23,13,45,40,87,35,63,22,9,1,50,27,95,100,21,28,38,80,29,53,16,32,60,65,79,8,66,7,70,4,99,78,88,10,46,25,47,93,83,36,56,91,97,96,2,57,26,54,55,98,51,37,17,49,69,72,59,64,77,94,24,82,30,31,39,43,76,92,52,74,11,84,58,67,34,12,41,68,81,85,19,20,44,18,15,14,61,42,3,86,48,75,6,62,89,73,90,71,5,33]
total = 0 
for num in nums:
    total = total + num
print(f"sum of nums is {total}")
amt = len(nums)
print(amt) 

avg = total/amt 

print(f"the average of nums is {avg}")

nums = list(range(100))
#list() makes the inbetween () a list. 

print(nums) 
"""

mylist = [5,7,1,3,6,8,2,10]
nums = list(range(len(mylist)))
print(nums) 

total = 0 
for i in range(len(mylist)):
    total = total +mylist[i] 

mylist = [1,2,3,4]
for i in range(len(mylist)):
    mylist[i] = mylist[i] + 2

print(mylist) 

fruits = ["orage", "mango", "grapes"]
prices = [1.25,1.50,2.25]

#these lists are connected with indices. 

"""
print("Welcome to our store!")
for i in range(len(fruits)):
    print(f"fruit name: {fruits[i]}")
    print(f"fruit price: {prices[i]}")

code = "aabbbabbabababbabbabbababababbabbabbabbaabbaaababaababaaabaaababababababaaaabab"
total_a = 0
total_b = 0

for char in code:
    if char == "a":
        total_a = total_a + 1
    elif char == "b":
        total_b = total_b + 1 

print(f"Total a's = {total_a}.")
print(f"Total b's = {total_b}.")
"""
"""
for char in str:
    strcopy = strcopy + char
    print(strcopy)  
"""
str = "hello" 
strcopy = "" 

for char in str:
    strcopy = char + strcopy 
    print(strcopy) 
"""
for i in range(1,13):
    for j in range(1,13):
        print(i*j, end = " ")
    print()  
"""
entrees = ["Steak", "Pasta", "Roasted Chicken", "Grilled Shrimp"]
sides = ["Fries", "Breadsticks", "Side Salad"]

print("Welcome to Olive Garden!")
for dish in entrees:
    for side in sides:
        print(f"Main dish: {dish}, Side: {side}")

for i in range(1,6):
    for j in range(i): 
        print("*", end = " ")
    print() 