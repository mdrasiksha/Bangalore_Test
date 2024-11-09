def my_decorator(func):
    def wrapper():
        print("yes")
        func()
        print("no")
    return wrapper
@my_decorator
def say_hello():
    print("hello")

say_hello()