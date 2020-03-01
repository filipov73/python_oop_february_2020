class Cup:
    def __init__(self, size, quantity):
        self.size = size
        self.quantity = quantity

    def fill(self, add_quantity):
        new_quantity = self.quantity + add_quantity
        if self.size >= new_quantity:
            self.quantity += add_quantity

    def status(self):
        return self.size - self.quantity


cup = Cup(100, 50)
cup.fill(30)
cup.fill(10)
print(cup.status())
