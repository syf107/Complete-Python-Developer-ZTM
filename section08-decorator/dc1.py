#Decorator Pattern

def my_decorator(func):
    def wrap_function(*args, **kwargs):
        print('*************')
        func(*args, **kwargs)
        print('*************')
    return wrap_function

@my_decorator
def hello(greeting):
    print(greeting)

hello("Hiiii!!")