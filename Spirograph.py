from turtle import Turtle, Screen
from math import cos,sin,radians
from time import sleep

# Set up the screen
screen = Screen()
screen.bgcolor("white")  # Background color

# Create a turtle object
spirograph_turtle = Turtle()
spirograph_turtle.speed(0)  # Fastest speed for drawing

# Spirograph Function
def draw_spirograph(R, r, O):
    """
    R: Radius of the outer circle
    r: Radius of the inner circle
    O: Offset from the center of the inner circle
    """
    # Set initial angle
    spirograph_turtle.penup()
    spirograph_turtle.goto(R - O, 0)
    spirograph_turtle.pendown()    
    revolutions = 2
    initialAngle = 0
    finalAngle = 360

    # Draw the spirograph using parametric equations
    for angle in range(initialAngle, finalAngle * revolutions, 1):  # Loop over 2 revolutions
        a = radians(angle)
        x = (R - r) * cos(a) + O * cos(((R - r) / r) * a)
        y = (R - r) * sin(a) - O * sin(((R - r) / r) * a)
        spirograph_turtle.goto(x, y)

# Function to draw multiple spirographs with different colors
def multi_spirograph():
    colors = ['red', 'blue', 'green', 'purple', 'orange', 'yellow']
    spirograph_turtle.width(2)
    
    for i in range(60):
        spirograph_turtle.pencolor(colors[i % len(colors)])  # Change color
        draw_spirograph(150, 75 + (i * 10), 50)  # Modify inner circle size for variation

def choose_shape():
    sides = int(input("Input number of sides of shape "))
    if sides < 3:
        print("Shape invalid")
    elif sides > 15:
        print("Shape too complex")
    else:
        return sides
    
def draw_shape(sides):
    angle = 360 / sides # Calculate angle for the shape (exteriors)
    spirograph_turtle.width(2)
    spirograph_turtle.pencolor('blue')
    for _ in range(sides):
        spirograph_turtle.forward(100)
        spirograph_turtle.right(angle)

draw_shape(choose_shape())

# Hide the turtle and display the result
spirograph_turtle.hideturtle()

# Keep the window open
screen.mainloop()
