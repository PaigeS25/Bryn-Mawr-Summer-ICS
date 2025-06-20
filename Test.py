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
        