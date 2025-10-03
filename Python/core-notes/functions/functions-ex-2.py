#2nd example of functions

def display_invoice(username, amount, due_date):
    print(f"Hello {username}!")
    print(f"Your bill of ${amount:.2f} is due on: {due_date}")
     


display_invoice("Alby", 100000, "10/02/2025")    