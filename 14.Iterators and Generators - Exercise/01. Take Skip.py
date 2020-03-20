class take_skip:
    def __init__(self, step, count):
        self.step = step
        self.count = count
        self.counter = 1
        self.rez = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter > self.count:
            raise StopIteration
        self.counter += 1
        rez = self.rez
        self.rez += self.step
        return rez



# class take_skip_iterator:
#     def __init__(self, step, count):
#         self.counter = 1
#         self.step = step
#         self.count = count
#         self.rez = 0
#
#     def __next__(self):
#         if self.counter > self.count:
#             raise StopIteration
#         self.counter += 1
#         rez = self.rez
#         self.rez += self.step
#         return rez
#
#
# class take_skip:
#     def __init__(self, step, count):
#         self.step = step
#         self.count = count
#
#     def __iter__(self):
#         return take_skip_iterator(self.step, self.count)
#

numbers = take_skip(2, 6)
for number in numbers:
    print(number)
numbers = take_skip(10, 5)
for number in numbers:
    print(number)

""""
0
2
4
6
8
10
0
10
20
30
40
"""
