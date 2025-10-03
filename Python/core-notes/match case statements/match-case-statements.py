#Match-case statement (switch): an alternative to using many "elif" statements
#                               execute some code if a value matches a 'case'
#                               benefits: cleaner and syntax is more readable

def day_of_week(day):
    match day:
        case 1:
            return "It is Sunday."
        case 2:
            return "It is Monday."
        case 3:
            return "It is Tuseday"
        case 4:
            return "It is Wednesday."
        case 5:
            return "It is Thursday."
        case 6:
            return "It is Friday."
        case 7:
            return "It  is Saturday."
        case _: #This will work as a wildcard if none of the cases conditions are met.
            return "Not a valid day."
        
print(day_of_week(4))