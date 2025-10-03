


def is_weekend(day):
    match day:
        case "Saturday" |"Sunday":  # | acts as an or so you dont have to write two cases of the same value.
            return True
        case "Monday" | "Tuseday" | "Wednesday" | "Thursday" | "Friday":
            return False
        case _: #This will work as a wildcard if none of the cases conditions are met.
            return "Please enter a day."
        
print(is_weekend("Saturday"))