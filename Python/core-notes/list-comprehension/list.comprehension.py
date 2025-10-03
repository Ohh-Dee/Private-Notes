# list comprehension = A concise way to create list in Python
#                      Compact and easier to read than traditional loops
#                     [expression for value in iterable if condition]

doubles = [x * 2 for x in range(1,11)] # [expression for value in iterable if condition]
tripples = [y * 3 for y in range(1, 11)]
squares = [ z * z for z in range (1, 11)]

print(doubles)
