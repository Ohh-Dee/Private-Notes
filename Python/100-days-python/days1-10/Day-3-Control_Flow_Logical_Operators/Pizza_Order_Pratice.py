print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L: \n").lower()
pepperoni = input("Do you want pepperoni? Y or N: \n").lower()
extra_cheese = input("Do you want extra cheese? Y or N: \n").lower()
state_tax = input("Which state are you in?: (NY, PA, NJ)\n").lower()

while state_tax not in ["ny", "pa", "nj"]:
    print("Please enter a valid state. NY or PA even NJ will do!")
    state_tax = input("Which state are you in?: (NY, PA, NJ)\n").lower()

bill = 0

match size:
    case "s":
        bill += 15
    case "m":
        bill +=  20
    case "l":
        bill += 25
    case _:
        print("Please enter a valid size.")


match pepperoni:
    case "y" if size == "s":
        bill += 2
    case "y" if size != "s":
        bill += 5

if extra_cheese == "y":
    bill += 1

match state_tax:
    case 'ny':
        bill *= 1.07
    case 'pa':
        bill *= 1.03
    case 'nj':
        bill *= 1.02



print(f"Your bill is ${bill:.2f}")