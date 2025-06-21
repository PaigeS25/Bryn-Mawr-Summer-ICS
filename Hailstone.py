hailstone = int(input("Enter an integer greater than 2: "))

while hailstone >= 2: 
    if hailstone % 2 == 0:
        hailstone = hailstone / 2 
        print(f"The current hailstone's hight is: {hailstone}")
    elif hailstone % 2 == 1:
        hailstone = hailstone * 3
        hailstone = hailstone + 1
        print(f"The current hailstone's hight is: {hailstone}")
        
