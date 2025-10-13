import random

def spin_row():
    symbols = ["🍒", "🍉", "🍋", "🔔", "⭐"]
    return [random.choice(symbols) for _ in range(3)]

def print_row(row):
    print(" | ".join(row))

def get_payout(row, bet):
    # Pay only on three-of-a-kind
    if row[0] == row[1] == row[2]:
        if row[0] == "🍒":
            return bet * 3
        elif row[0] == "🍉":
            return bet * 4
        elif row[0] == "🍋":
            return bet * 5
        elif row[0] == "🔔":
            return bet * 10
        elif row[0] == "⭐":
            return bet * 20
    return 0

def main():
    balance = 100
    print("Welcome to Python Slots!")
    print("Symbols: 🍒 🍉 🍋 🔔 ⭐")
    print("Payouts (3 in a row): 🍒x3, 🍉x4, 🍋x5, 🔔x10, ⭐x20\n")

    while balance > 0:
        print(f"Current Balance: ${balance}")
        bet = input("Place your bet amount (or Q to quit): ").strip()

        if bet.upper() == "Q":
            print("Cashing out. Thanks for playing!")
            break

        if not bet.isdigit():
            print("Please enter a valid number.\n")
            continue

        bet = int(bet)

        if bet > balance:
            print("Insufficient funds.\n")
            continue
        if bet <= 0:
            print("Bet must be greater than 0.\n")
            continue

        balance -= bet

        print("Spinning...\n")
        row = spin_row()
        print_row(row)

        payout = get_payout(row, bet)
        if payout > 0:
            balance += payout
            print(f"🎉 You won ${payout}! New balance: ${balance}\n")
        else:
            print(f"Sorry, you lost this round. New balance: ${balance}\n")

        if balance <= 0:
            print("You're out of funds. Game over!")
            break

        play_again = input("Do you want to spin again? (Y/N): ").strip().upper()
        if play_again != "Y":
            print("Cashing out. Thanks for playing!")
            break

if __name__ == '__main__':
    main()
