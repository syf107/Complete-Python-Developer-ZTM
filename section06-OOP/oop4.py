# INHERITANCE & POLYMORPHISM

class User:
    def __init__(self, email):
        self.email = email
    def sign_in(self):
        print('logged in')

class Wizard(User):
    def __init__(self, name, power, email):
        super().__init__(email) # User.__init__(self, email)
        self.name = name
        self.power = power
    
    def attack(self):
        print(f'attacking with power of {self.power}')


wizard1 = Wizard("Muna", 100, "munafiik@gmail.com")
print(wizard1.email)

# introspection
# print(dir(wizard1))

