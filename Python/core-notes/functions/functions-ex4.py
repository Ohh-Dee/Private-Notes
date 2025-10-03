

first = input("What is your first namme?: ")
last = input("What is your last name:? ")


def create_name(first, last):
    first = first.capitalize()
    last = last.capitalize()
    return first + " " + last



fullname = create_name(first, last)

print(f"Hello there {fullname}!")