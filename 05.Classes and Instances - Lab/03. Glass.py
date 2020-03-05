class Glass:
    capacity = 250

    def __init__(self):
        self.content = 0

    def fill(self, ml):
        if Glass.capacity >= self.content + ml:
            self.content += ml
            return f"Glass filled with {ml} ml"
        else:
            return f"Cannot add {ml} ml"

    def empty(self):
        self.content = 0
        return f"Glass is now empty"

    def info(self):
        left_space = Glass.capacity - self.content
        return f"{left_space} ml left"



"""
-	fill(ml) - fill the glass with the given milliliters if there is enough space in it and return "Glass filled with {ml} ml", otherwise return "Cannot add {ml} ml"
-	empty() - empty the glass and return "Glass is now empty" 
-	info() - returns info about the glass in the format "{left_space} ml left"
"""

glass = Glass()
print(glass.fill(100))
print(glass.fill(200))
print(glass.empty())
print(glass.fill(200))
print(glass.info())

"""
Glass filled with 100 ml
Cannot add 200 ml
Glass is now empty
Glass filled with 200 ml
50 ml left
"""