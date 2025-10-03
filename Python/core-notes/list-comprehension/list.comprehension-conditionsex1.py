# this example uses conditions

numbers = [1, -2, 3, -4, 5, -6]
pos_nums = [num for num in numbers if num >= 0]
neg_nums =  [neg for neg in numbers if neg < 0]
even_nums = [even for even in numbers if even % 2 == 0]

print(even_nums)

print(pos_nums)

print(neg_nums)