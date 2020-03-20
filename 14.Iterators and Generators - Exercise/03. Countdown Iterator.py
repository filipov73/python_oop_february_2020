class countdown_iterator:
    def __init__(self, count):
        self.count = count

    def __iter__(self):
        return self

    def __next__(self):
        if self.count < 0:
            raise StopIteration
        c = self.count
        self.count -= 1
        return c


iterator = countdown_iterator(10)
for item in iterator:
    print(item, end=" ")

""""
10 9 8 7 6 5 4 3 2 1 0
"""
