nums = []

print("Welcome to the calculator!")
option = input("enter the name of the operation you would like: ").lower().strip()
 

if option == "addition":
    num1 = int(input("enter num1: "))
    num2 = int(input("enter num2: "))
    nums.append(num1)
    nums.append(num2)
    sum = nums[0] + nums[1]
    print(f"the sum of {nums[0]} and {nums[1]} is {sum}")
    nums.append(sum)
elif option == "subtraction":
    num1 = int(input("enter num1: "))
    num2 = int(input("enter num2: "))
    nums.append(num1)
    nums.append(num2)
    difference = nums[0] - nums[1]
    print(f"the difference of {nums[0]} and {nums[1]} is {difference}")
    nums.append(difference)
elif option == "multiplication":
    num1 = int(input("enter num1: "))
    num2 = int(input("enter num2: "))
    nums.append(num1)
    nums.append(num2)
    product = nums[0] * nums[1]
    print(f"the product of {nums[0]} and {nums[1]} is {product}")
    nums.append(product)
elif option == "division":
    num1 = int(input("enter num1: "))
    num2 = int(input("enter num2: "))
    nums.append(num1)
    nums.append(num2)
    quotient = nums[0] / nums[1]
    print(f"the quotient of {nums[0]} and {nums[1]} is {quotient}") 
    nums.append(quotient)
elif option == "modular division":
    num1 = int(input("enter num1: "))
    num2 = int(input("enter num2: "))
    nums.append(num1)
    nums.append(num2)
    remainter = nums[0] % nums[1]
    print(f"the remainder of {nums[0]} and {nums[1]} is {remainder}")
    nums.append(remainder) 

print(nums)