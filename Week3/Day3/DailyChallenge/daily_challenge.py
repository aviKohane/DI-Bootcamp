# The goal is to create a class that represents a simple circle.
# A Circle can be defined by either specifying the radius or the diameter.
# The user can query the circle for either its radius or diameter.

# Other abilities of a Circle instance:

# Compute the circle’s area
# Print the attributes of the circle - use a dunder method
# Be able to add two circles together, and return a new circle with the new radius - use a dunder method
# Be able to compare two circles to see which is bigger, and return a Boolean - use a dunder method
# Be able to compare two circles and see if there are equal, and return a Boolean- use a dunder method
# Be able to put them in a list and sort them
# Bonus (not mandatory) : Install the Turtle module, and draw the sorted circle


import math

class Circle:
    def __init__(self, radius=None, diameter=None):
        if radius is not None:
            self.radius = radius
            self.diameter = radius * 2
        elif diameter is not None:
            self.diameter = diameter
            self.radius = diameter / 2
        else:
            raise ValueError("Please specify either radius or diameter")

    @property
    def area(self):
        return math.pi * self.radius ** 2

    def __str__(self):
        return f"Circle(radius={self.radius}, diameter={self.diameter})"

    def __add__(self, other):
        return Circle(radius=self.radius + other.radius)

    def __gt__(self, other):
        return self.radius > other.radius

    def __eq__(self, other):
        return self.radius == other.radius

    def __lt__(self, other):
        return self.radius < other.radius

# Test the Circle class
circle1 = Circle(radius=3)
circle2 = Circle(diameter=10)

print(circle1.area)  # Output: 28.274333882308138
print(circle2.area)  # Output: 78.53981633974483

print(circle1)  # Output: Circle(radius=3, diameter=6)
print(circle2)  # Output: Circle(radius=5.0, diameter=10)

print(circle1 + circle2)  # Output: Circle(radius=8.0, diameter=16.0)

print(circle1 > circle2)  # Output: False
print(circle1 == circle2)  # Output: False
print(circle1 < circle2)  # Output: True

circle_list = [Circle(radius=2), Circle(radius=5), Circle(radius=1)]
sorted_circles = sorted(circle_list)
print([str(circle) for circle in sorted_circles])  # Output: ['Circle(radius=1, diameter=2)', 'Circle(radius=2, diameter=4)', 'Circle(radius=5, diameter=10)']

