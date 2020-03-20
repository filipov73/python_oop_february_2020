def execute(f, *args):
    return f(*args)


def say_hello(name, my_name):
    print(f"Hello, {name}, I am {my_name}")


def say_bye(name):
    print(f"Bye, {name}")


execute(print, 1, 2, 3)

print(list(execute(map, lambda x: x + 1, [1, 2, 3, 4, 5])))


execute(say_hello, "Peter", "George")
execute(say_bye, "Peter")



"""
Hello, Peter, I am George
Bye, Peter
"""
