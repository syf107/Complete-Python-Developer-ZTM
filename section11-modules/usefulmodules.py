from collections import Counter, defaultdict, OrderedDict

list =  [1, 2, 3, 4, 5, 6, 7]
print(Counter(list))

dictio = defaultdict(lambda: "doesn't exist", {'a': 2, 'b':3})
print(dictio[7])