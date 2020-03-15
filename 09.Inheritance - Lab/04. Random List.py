from random import randint


class RandomList(list):
    def get_random_element(self):
        r = randint(0, len(self) - 1)
        return self.pop(r)



a = RandomList()
a.append(212)
a.append(1332)
a.append(124)
a.append(1244)
a.get_random_element()
print(a.__dict__)

li = RandomList()
li.append(4)
li.append(3)
li.append(5)
li.get_random_element()


