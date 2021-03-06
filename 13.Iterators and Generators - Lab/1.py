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


one_to_ten = custom_range(1, 4)
for num in one_to_ten:
    print(num)













