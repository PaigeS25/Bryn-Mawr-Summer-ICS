on = True 

print("Welcome to the calculator!")
print("the operations are: addition, subtraction, multiplication, division, or modular division. If you are done, enter: quit.")

while on == True:
    option = input("enter the name of the operation you would like: ").lower().strip()
    if option == "addition":
        num1 = int(input("enter num1: "))
        num2 = int(input("enter num2: "))
        sum = num1 + num2 
        print(f"the sum of {num1} and {num2} is {sum}")
    elif option == "subtraction":
        difference = num1 - num2
        product = num1 * num2
        quotient = num1 / num2 
        remainder = num1 % num2
        num1 = int(input("enter num1: "))
        num2 = int(input("enter num2: "))
        print(f"the difference of {num1} and {num2} is {difference}")
    elif option == "multiplication":
        sum = num1 + num2 
        difference = num1 - num2
        product = num1 * num2
        quotient = num1 / num2 
        remainder = num1 % num2
        num1 = int(input("enter num1: "))
        num2 = int(input("enter num2: "))
        print(f"the product of {num1} and {num2} is {product}")
    elif option == "division":
        sum = num1 + num2 
        difference = num1 - num2
        product = num1 * num2
        quotient = num1 / num2 
        remainder = num1 % num2
        num1 = int(input("enter num1: "))
        num2 = int(input("enter num2: "))
        print(f"the quotient of {num1} and {num2} is {quotient}") 
    elif option == "modular division":
        sum = num1 + num2 
        difference = num1 - num2
        product = num1 * num2
        quotient = num1 / num2 
        remainder = num1 % num2
        num1 = int(input("enter num1: "))
        num2 = int(input("enter num2: "))
        print(f"the remainder of {num1} and {num2} is {remainder}")
    elif option == "quit": 
        on = False 
    else:
        print("Invalid operation.")
