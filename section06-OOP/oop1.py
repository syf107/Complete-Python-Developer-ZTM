# OOP
class PlayerCharacter:
    # Class Object Attribute
    membership = True
    def __init__(self, name = 'anonymous', age = 0): #Attribute
        self.name = name
        self.age = age

    def shout(self):
        print(f"my name is {self.name}")
    
    @classmethod
    def adding_things(cls, num1, num2):
        return num1 + num2

    @staticmethod
    def substract_things(num1, num2):
        return num1 + num2

player1 = PlayerCharacter("Tom", 20)

print(player1.adding_things(50, 25))

print(player1.substract_things(50, 22))