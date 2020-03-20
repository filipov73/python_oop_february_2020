class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Child(Person):
    pass


ch = Child("ma", 5)
print(ch.__dict__)
