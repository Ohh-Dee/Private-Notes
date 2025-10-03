#Membership Operators = used to test whether a value or variable is founed in a sequenced
#                      (string, list, tuple, set, or dictionary)
#                      1. in
#                      2. not in


word = "APPLE"

letter = input("Guess a letter in the secret word: ")

if letter in word:
    print(f"There is a {letter}.")
else:
    print(f"{letter} was not found.")