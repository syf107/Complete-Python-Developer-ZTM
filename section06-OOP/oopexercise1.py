#Given the below class:
class Cat:
    species = 'mammal'
    def __init__(self, name, age):
        self.name = name
        self.age = age


# 1 Instantiate the Cat object with 3 cats
garfield = Cat("Garfield", 2)
madarao = Cat("Madarao", 5)
tom = Cat("Tom", 3)
print(garfield.name, madarao.name, tom.name, sep="\n")


# 2 Create a function that finds the oldest cat
def oldest_cat(*cats):
    return max(*cats)

oldest = oldest_cat(garfield.age, madarao.age, tom.age)
print(oldest)

# 3 Print out: "The oldest cat is x years old.". x will be the oldest cat age by using the function in #2
print("The oldest cat is {} years old".format(oldest))