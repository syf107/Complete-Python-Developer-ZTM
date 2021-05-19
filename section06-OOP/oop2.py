# 4 PILLARS OF OOP
class PlayerCharacter:
    def __init__(self, name, age):
        self._name = name #the way to private by adding _ (underscore)
        self._age = age
    
    def run(self):
        print('run')

    def speak(self):
        print(f'my name is {self._name}. I am {self._age} years old')


# ENCAPSULATION EXAMPLE
player1 = PlayerCharacter('andrei', 100)
# player1.speak()

#Private and Public Variable
print(player1.speak())