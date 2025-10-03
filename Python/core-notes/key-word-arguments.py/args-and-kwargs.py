# *args   = allows you to pass multiple non-key- arguments  (Tuple)
# **kwargs = allows you to pass mutiple keyword-arguments   (Dictionary)
#           1. positional 2. default 3. keyword    >4.Arbitrary<

def add(*args):
    total = 0
    for arg in args:
        total += arg
    return total
        

print(add(1, 2, 3))
    