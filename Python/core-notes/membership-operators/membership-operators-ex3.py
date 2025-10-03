# This example uses a dictionary

grades = {"Sandy": "A", "Oscar":"B", "Omaya": "C"}

student = input("Enter the name of a student: ")

if student in grades:
    print(f"{student} grade is {grades[student]} ")
else:
    print(f"{student} was not found.")