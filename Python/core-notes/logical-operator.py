# Logical operators = evaluate mutiple conditions (Or, and, not)
# or = at least one is true
# and = both
# not = false

temp = 25
is_raining = False

if temp > 35 or temp < 0 or is_raining:
    print("The outdoor event is canceled")
else:
    print("The outdoor event is still going!")