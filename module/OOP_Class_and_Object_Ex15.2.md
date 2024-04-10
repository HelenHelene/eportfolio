

```python
# Exercise 15.2 
import math
import turtle

# Define the Point class
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

# Define the Circle class
class Circle:
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius

# Define the Rectangle class
class Rectangle:
    def __init__(self, width, height, corner):
        self.width = width
        self.height = height
        self.corner = corner

"""Write a function called draw_rect that takes a Turtle object and a Rectangle 
and uses the Turtle to draw the Rectangle.""" 
def draw_rect(turtle, rect):
    turtle.penup()
    turtle.goto(rect.corner.x, rect.corner.y)
    turtle.pendown()
    for _ in range(2):
        turtle.forward(rect.width)
        turtle.left(90)
        turtle.forward(rect.height)
        turtle.left(90)

"""Write a function called draw_circle that takes a Turtle and a Circle and draws the Circle."""
def draw_circle(turtle, circle):
    turtle.penup()
    turtle.goto(circle.center.x, circle.center.y - circle.radius)
    turtle.pendown()
    turtle.circle(circle.radius)

# Create a Turtle object
my_turtle = turtle.Turtle()

# Create a Rectangle object
rectangle = Rectangle(100, 50, Point(-50, -25))

# Create a Circle object
circle = Circle(Point(0, 0), 75)

# Draw the rectangle
draw_rect(my_turtle, rectangle)

# Move the turtle to a new position
my_turtle.penup()
my_turtle.goto(0, -100)
my_turtle.pendown()

# Draw the circle
draw_circle(my_turtle, circle)

# Keep the turtle window open
turtle.done()

```
