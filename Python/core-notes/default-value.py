# default arguments = a default value for certain parameters
#                     default is used when that argument is omitted
#                     make your functions more flexible, reduces the # of arguments
#                     1. positional 2. Default, 3. keyword, 4. arbitrary




def net_price(list_price, discount=0, tax=0):
    return list_price * (1 - discount) * (1 * tax)

print(net_price(500, .01, .05))