class Stack:
    def __init__(self):
        self.__data = []

    def __str__(self):
        return str(self.__data[::-1])
        # return str(list(reversed(self.__data)))

    def push(self, item):
        self.__data.append(item)

    def pop(self):
        if len(self.__data):
            return self.__data.pop()

    def peek(self):
        return self.__data[-1]

    def is_empty(self):
        return len(self.__data) == 0
        # if len(self.__data):
        #     return False
        # return True



import unittest

class StackTests(unittest.TestCase):
    def test_zero(self):
        stack = Stack()
        stack.push(1)
        stack.push(2)
        self.assertEqual(str(stack), "[2, 1]")
        self.assertEqual(stack.pop(), 2)
        self.assertEqual(stack.peek(), 1)
        stack.push(5)
        self.assertEqual(str(stack), "[5, 1]")
        self.assertEqual(stack.is_empty(), False)

if __name__ == '__main__':
    unittest.main()