
check = True

while check == True:
    word = input("Enter word: ").lower().strip().split()
    word = "".join(word)  
    copy = "" 
    if word == "quit":
        print("Bye!")
        break 
    for char in word:
        copy = char + copy 
    if copy == word: 
        print(f"{word} is a palindrome!")
    else:
        print(f"{word} is not a palindrome. :(")
