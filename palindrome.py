word = input("Enter word: ").lower().strip().split()
word = "".join(word)  
copy = "" 

for char in word:
    copy = char + copy 
    print(copy) 

if copy == word:
    print(f"{word} is a palindrome!")
else:
    print(f"{word} is not a palindrome. :(")