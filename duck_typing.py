def f(a):
    print("__len__" in dir(a))


f([1, 2, 3])  # True
f("martin")  # True
f(1)  # False

# ####

class MyClass:
    def __init__(self, size):
        self.size = size

    def __len__(self):
        return self.size


# print(len(5)) # object of type 'int' has no len()
print(len("martin"))  # 6
print(len([1, 2, 3]))  # 3
print(len(MyClass(3)))  # 3
aa = MyClass(3)
aa = 6

# ##########

def func(a):
    print(a.size)


class B:
    size = 6


class B1:
    def __init__(self, size):
        self.size = size


func(B())
func(B1(44))
