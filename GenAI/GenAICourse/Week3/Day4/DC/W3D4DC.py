#W3D4DC

import math

class Circle:
    def __init__(self, radius=1.0):
        # Initialize using our property setter to ensure validation
        self.radius = radius

    # --- Properties and Decorators ---
    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError("Radius cannot be negative.")
        self._radius = value

    @property
    def diameter(self):
        return self.radius * 2

    @diameter.setter
    def diameter(self, value):
        # Setting the diameter updates the radius under the hood
        self.radius = value / 2

    # --- Methods ---
    def compute_area(self):
        return math.pi * (self.radius ** 2)

    # --- Dunder Methods for Printing ---
    def __str__(self):
        return f"Circle(Radius: {self.radius}, Diameter: {self.diameter})"

    def __repr__(self):
        return f"Circle({self.radius})"

    # --- Dunder Methods for Math & Comparisons ---
    def __add__(self, other):
        if isinstance(other, Circle):
            return Circle(self.radius + other.radius)
        return NotImplemented

    def __lt__(self, other):
        # Less than (<) - required for sorting
        if isinstance(other, Circle):
            return self.radius < other.radius
        return NotImplemented

    def __gt__(self, other):
        # Greater than (>)
        if isinstance(other, Circle):
            return self.radius > other.radius
        return NotImplemented

    def __eq__(self, other):
        # Equal to (==)
        if isinstance(other, Circle):
            return self.radius == other.radius
        return NotImplemented


# ==========================================
# Testing the Implementation
# ==========================================
if __name__ == "__main__":
    print("--- 1. Initialization and Properties ---")
    c1 = Circle(radius=5)
    c2 = Circle()
    c2.diameter = 20 # Setting via diameter
    
    print(c1)
    print(c2)
    print(f"c1 Area: {c1.compute_area():.2f}")

    print("\n--- 2. Addition ---")
    c3 = c1 + c2
    print(f"c1 + c2 = {c3}")

    print("\n--- 3. Comparisons ---")
    print(f"c2 > c1: {c2 > c1}")
    print(f"c1 == Circle(5): {c1 == Circle(5)}")

    print("\n--- 4. Sorting ---")
    circles = [Circle(12), Circle(3), Circle(7), Circle(1)]
    print(f"Unsorted: {circles}")
    circles.sort()
    print(f"Sorted:   {circles}")

    import turtle

def draw_sorted_circles(circles_list):
    """Sorts a list of Circle objects and draws them side-by-side using turtle."""
    
    # Sort the circles utilizing the __lt__ dunder method we built
    sorted_circles = sorted(circles_list)
    
    # Setup the turtle screen and pen
    screen = turtle.Screen()
    screen.title("Sorted Circles Visualization")
    t = turtle.Turtle()
    t.speed(3)
    t.pensize(2)
    
    # Move the turtle to the left side of the screen to start drawing
    t.penup()
    t.goto(-300, 0)
    t.pendown()
    
    for c in sorted_circles:
        # Draw the circle
        t.circle(c.radius)
        
        # Move forward past the drawn circle so the next one doesn't overlap
        t.penup()
        t.forward(c.diameter + 20) # 20px of padding between circles
        t.pendown()
        
    print("Drawing complete! Click the screen to exit.")
    screen.exitonclick()

# --- Run the visualizer ---
if __name__ == "__main__":
    # Create a random list of circles
    my_circles = [Circle(50), Circle(10), Circle(35), Circle(75)]
    
    # Draw them
    draw_sorted_circles(my_circles)