# module = a file containing code you want to include in your program
#          use 'import' to include a module (bult-in or your own)
#          useful to break up a large program reusable separate files

# import math
import math as m
# from math import pi | could have name conflicts
import examplemodule



print(m.pi)

result=examplemodule.square(3)

print(result)