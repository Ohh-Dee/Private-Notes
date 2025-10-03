# example using a set

students = {"Spongebob", "Patrick", "Sandy"}

student = input("Enter the name of a student: ")

if student in students:
    print(f"{student} is a student.")
else:
    print(f"{student} was not found.")