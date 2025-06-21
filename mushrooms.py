mushrooms = [] 
small_mushrooms = 0
large_mushrooms = 0
medium_mushrooms = 0
check = True 

while check == True:
    mushrooms.append(input("Enter the weight of your mushroom, or STOP to end: ").upper().strip())
    if mushrooms[-1] == "STOP":
        check = False 
        mushrooms.pop(-1) 
    elif int(mushrooms[-1]) < 1:
        print("Weight must be greater than 0!")

for m in mushrooms:
    if int(m) >= 1000:
        large_mushrooms = large_mushrooms + 1
    elif int(m) <= 100:
        small_mushrooms = small_mushrooms + 1
    else:
        medium_mushrooms = medium_mushrooms + 1

print(f"The weights you entered were {mushrooms}")
print(f"There were {small_mushrooms} small mushrooms, {medium_mushrooms} medium mushrooms, and {large_mushrooms} large mushrooms.")

    
