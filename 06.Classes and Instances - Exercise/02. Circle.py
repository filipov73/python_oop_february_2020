class Circle:
    pi = 3.14

    def __init__(self, radius):
        self.radius = radius

    def set_radius(self, new_radius):
        self.radius = new_radius

    def get_area(self):
        rez = self.pi * (self.radius * self.radius)
        return round(rez, 2)
        # return f"{rez:.2f}" -> problem str output

    def get_circumference(self):
        rez = 2 * (self.pi * self.radius)
        return rez

"""
Create a class attribute called pi which should equal 3.14. Create 3 instance methods:
-	set_radius(new_radius) - changes the radius
-	get_area() - returns the area of the circle
-	get_circumference() - returns the circumference of the circle
The area should be rounded to the 2nd decimal.
"""


circle = Circle(10)
circle.set_radius(12)
print(circle.get_area())
print(circle.get_circumference())


"""
452.16
75.36
"""