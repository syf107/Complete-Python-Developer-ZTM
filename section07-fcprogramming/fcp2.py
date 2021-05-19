# FUNCTIONAL PROGRAMMING MAP(), FILTER(), ZIP(), REDUCE()

from functools import reduce

my_list = [1, 2, 3]
your_list = [20, 30, 40]
def multiply_by2(li):
    return li * 2

def only_odd(li):
    return li % 2 != 0

def accumulator(my_list, num):
    return my_list + num

# MAP() 
print(list(map(multiply_by2, my_list)))

# FILTER()
print(list(filter(only_odd, my_list)))

#ZIP()
print(list(zip(my_list, your_list)))
print(my_list)


#REDUCE
print(reduce(accumulator, my_list))