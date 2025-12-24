import random

rock = r'''
   _______
 /        \
/  _   _   \
| ( ) ( )  |
|   ___    |
\         /
 \_______/

'''

paper = r'''
   .----------.
  |          /|
  |         / |
  |        /  |
  |       /   |
  |      /    |
  |_____/_____|
'''

scissors = r'''
      ( )       ( )
        \       /
         \     /
          \   /
           \ /
           / \
          /   \
         /     \
        /       \
'''

user_choice = input("What do you want to choose? rock, paper, or scissors:\n ")

computer_choice = random.choice(["rock", "paper", "scissors"])

print("\nYou chose: ")
if user_choice =="rock":
    print(rock)
elif user_choice =="paper":
    print(paper)
elif user_choice =="scissors":
    print(scissors)

if user_choice == computer_choice:
    print("It's a tie")
elif (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "paper" and computer_choice == "rock") or
        (user_choice == "scissors" and computer_choice == "paper")
):
    print("You win!")
else:
    print("You have fallen!")
