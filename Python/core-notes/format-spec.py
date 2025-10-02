# format specifiers = {value:flags} format a value

#.(number)f = round to that many decimal places (fixed point)
#:(number) = allocate that many spaces
# :03 = allocate and  zero pad that many spaces
# :<= left justify
# :> = right justify
# :^ = center align 
# :+ = use a plus to indicate postive value
# := place sign to leftmore position
# : = insert a space
# :, comma separator

price1 = 3.14159
price2 = -9.98765
price3= 12.34

print(f"Price 1 is ${price1:.2f}.")
print(f"Price 2 is ${price2:}.")
print(f"Price 3 is ${price3}.")