print("Welcome to the rollercoaster!")
height = int(input("what is your height? "))

if height >= 58:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age >= 18:
        print("Your ticket cost $7 dollars.")
    elif age >= 12:
        print("Your ticket cost $6 dollars.")
    else:
        print("Your ticket cost $5 dollars.")
else:
    print("Sorry, you cannot ride the rollercoaster!")