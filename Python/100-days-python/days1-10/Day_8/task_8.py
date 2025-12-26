# Functions that allows for inputs
#def greet_with_name(name):
#    print(f"Hello {name}!")
#    print("How are you?")
#    print("How is the weather?")

#name = input("What is your name? ")
#greet_with_name(name)

def greet_with(name, location):
    print(f"Hello, {name}!")
    print(f"You are from {location}?")
    print(f"Ive never been there hows {location}?")

name = input("What is your name? ")
location = input("Where do you live? ")
greet_with(name, location)
