class dictionary_iter:
    def __init__(self, dict_):
        self.dictionary = dict_
        self.keys_list = list(self.dictionary.keys())
        self.index = 0
        self.length = len(self.keys_list)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == self.length:
            raise StopIteration
        key = self.keys_list[self.index]
        value = self.dictionary[key]
        self.index += 1
        return key, value


result = dictionary_iter({1: '1', 2: '2'})
for x in result:
    print(x)
""""        
(1, '1')
(2, '2')
"""
