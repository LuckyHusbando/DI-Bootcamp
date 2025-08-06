#DC Circle - Week 3 Day 4

import math
print(math.pi)

class Circle:

    def __init__(self, radius):
        self.radius = radius
        self.diameter = radius*2
        self.area = math.pi * radius**2
        self.circumference = 2 * math.pi * radius

    def __repr__(self):
        return (f'Circle(radius={self.radius}, diameter={self.diameter}, area={self.area}, circumference={self.circumference:.2f})')
    
    def __add__(self, other_circle):
        if not isinstance(other_circle, Circle):
            raise TypeError("Cannot add a circle to a non-circle object.")
        new_radius = self.radius + other_circle.radius
        return Circle(new_radius)    
    
    def __gt__(self, other):
        """Returns True if this circle's radius is greater than the other's."""
        if not isinstance(other, Circle):
            return NotImplemented
        return self.radius > other.radius
    
    def __lt__(self, other):
        """Returns True if this circle's radius is less than the other's."""
        if not isinstance(other, Circle):
            return NotImplemented
        return self.radius < other.radius
        
    def __eq__(self, other):
        """Returns True if this circle's radius is equal to the other's."""
        if not isinstance(other, Circle):
            return NotImplemented
        return self.radius == other.radius

my_circle = Circle(5)
other_circle = Circle(3)
radius = 5

area = (math.pi)*radius**2
print(area)
print(my_circle)
print(my_circle > other_circle)
print(my_circle < other_circle)
print(my_circle == other_circle)

circle3 = my_circle + other_circle

print(f'Circle 1: {my_circle}')
print(f'Circle 2: {other_circle}')
print(f'New Circle (my+other): {circle3}')

circles = [Circle(10), Circle (5), Circle(7), Circle(8)]
print("Original List:", circles)

circles.sort()
print("Sorted in-place by radius (using list.sort()):", circles)
print("-" * 40)


