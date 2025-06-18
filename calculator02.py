print("Welcome to the calculator!")
num1 = int(input("enter num1: "))
num2 = int(input("enter num2: "))
option = input("enter the name of the operation you would like: ").lower().strip()

sum = num1 + num2 
difference = num1 - num2
product = num1 * num2
quotient = num1 / num2 
remainder = num1 % num2

if option == "addition":
    print(f"the sum of {num1} and {num2} is {sum}")
elif option == "subtraction":
    print(f"the difference of {num1} and {num2} is {difference}")
elif option == "multiplication":
    print(f"the product of {num1} and {num2} is {product}")
elif option == "division":
    print(f"the quotient of {num1} and {num2} is {quotient}") 
elif option == "modular division":
    print(f"the remainder of {num1} and {num2} is {remainder}")