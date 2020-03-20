def create_adder(x):
    def adder(y):
        return x + y
    return adder


add_10 = create_adder(10)
add_10(3)  # => 13
a = 5


