class A:
    def __init__(self, name):
        self.__name = name

    # @property
    # def name(self):
    #     return self.__name
    #
    # @name.setter
    # def name(self, value):
    #     self.__name = value

a = A("martin")

print(a.__dict__)
print(a.name)
a.name = 1
print(a.__dict__)
print(a.name)
