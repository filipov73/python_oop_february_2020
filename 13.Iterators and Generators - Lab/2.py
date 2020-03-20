import timeit
a = """
class custom_range_iterator:
    def __init__(self, first, last):
        self.index = first
        self.last = last

    def __next__(self):
        if self.index > self.last:
            raise StopIteration
        index = self.index
        self.index += 1
        return index


class custom_range:
    def __init__(self, first, last):
        self.first = first
        self.last = last

    def __iter__(self):
        return custom_range_iterator(self.first, self.last)


one_to_ten = custom_range(1, 10000000)
for num in one_to_ten:
    pass
    # print(num)
"""
b = "[x for x in range(10000000)]"

c = """
def custom_random(min, max):
    for i in range(min, max):
        yield i

[x for x in custom_random(1, 10000000)]
"""

aa = timeit.timeit(a, number=1)
bb = timeit.timeit(b, number=1)
cc = timeit.timeit(c, number=1)

print(aa)
print(bb)
print(cc)
