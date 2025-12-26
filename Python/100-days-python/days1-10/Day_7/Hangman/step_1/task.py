import random

# TODO-1 create a word_list and make it randomly select from it

word_list = ["apple", "banana", "cherry"]
chosen_word = random.choice(word_list)
print(chosen_word)
placeholder = ""
for position in range(len(chosen_word)):
    print("_", end = "")

# TODO-2 Ask user to guess a letter
game_over = False
correct_letters = []

while not game_over:
    guess = input("\nGuess a letter: ").lower()


    display = ""

    # TODO-3 Check if the letter the user gussed is right or wrong

    lives = 5

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(letter)
            print("Right!")
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"
            print("Wrong!")


print(display)