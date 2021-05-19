#lambda expressions.
from functools import reduce

my_list = [1, 2, 3]
your_list = [20, 30, 40]



print(list(map(lambda item: item * 2, my_list)))
print(list(filter(lambda item: item % 2 != 0, my_list)))
print((reduce(lambda acc, item: acc + item, my_list)))

# lambda exercise

