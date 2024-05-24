

```python
# Exercise 15.1 
import math

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

"""Write a function named point_in_circle that takes a Circle and a Point 
and returns True if the Point lies in or on the boundary of the circle."""
def point_in_circle(circle, point):
    # Calculate the distance between the point and the center of the circle using the distance formula
    distance = math.sqrt((point.x - circle.center.x) ** 2 + (point.y - circle.center.y) ** 2)
    # Check if the distance is less than or equal to the radius of the circle
    return distance <= circle.radius


"""Write a function named rect_in_circle that takes a Circle and a Rectangle 
and returns True if the Rectangle lies entirely in or on the boundary of the circle."""
def rect_in_circle(circle, rectangle):
    # Check if all corners of the rectangle are within the circle by using the point_in_circle function
    return (point_in_circle(circle, rectangle.corner) and
        point_in_circle(circle, Point(rectangle.corner.x + rectangle.width, rectangle.corner.y)) and
        point_in_circle(circle, Point(rectangle.corner.x, rectangle.corner.y + rectangle.height)) and
        point_in_circle(circle, Point(rectangle.corner.x + rectangle.width, rectangle.corner.y + rectangle.height)))

"""Write a function named rect_circle_overlap that takes a Circle and a Rectangle 
and returns True if any of the corners of the Rectangle fall inside the circle.""" 
def rect_circle_overlap(circle, rectangle):
    # Check if any of the corners of the rectangle fall inside the circle by using the point_in_circle function
    return (point_in_circle(circle, rectangle.corner) or
        point_in_circle(circle, Point(rectangle.corner.x + rectangle.width, rectangle.corner.y)) or
        point_in_circle(circle, Point(rectangle.corner.x, rectangle.corner.y + rectangle.height)) or
        point_in_circle(circle, Point(rectangle.corner.x + rectangle.width, rectangle.corner.y + rectangle.height)))

# Instantiate a Circle object with center at (150, 100) and radius 75
center = Point(150, 100)
radius = 75
circle = Circle(center, radius)

# Instantiate a Rectangle object with width 50, height 50, and corner at (100, 50)
width = 50
height = 50
corner = Point(100, 50)
rectangle = Rectangle(width, height, corner)

# Test point_in_circle function
point = Point(160, 80)
print(point_in_circle(circle, point))  

# Test rect_in_circle function
print(rect_in_circle(circle, rectangle)) 

# Test rect_circle_overlap function
print(rect_circle_overlap(circle, rectangle))

```


```python
# Exercise 15.1 Output
    True
    True
    True

```

---

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



---

[Return to Module 2 Unit 1](OOP_Unit01.md)

