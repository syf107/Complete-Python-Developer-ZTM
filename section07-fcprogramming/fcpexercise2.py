some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

list1 = list(set([char for char in some_list if some_list.count(char) > 1]))

print(list1)