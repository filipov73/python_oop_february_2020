class Animal:
    @staticmethod
    def eat():
        return "eating..."


class Dog(Animal):
    @staticmethod
    def bark():
        return "barking..."


print(Animal.eat())
print(Dog.eat())
print(Dog.bark())

