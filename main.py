import turtle
import random
import svgwrite

# Set up turtle graphics window
screen = turtle.Screen()
screen.setup(600, 600)

# Create turtle object
t = turtle.Turtle()

# Define a function to draw a random shape
def random_shape():
    sides = random.randint(3, 10)
    angle = 360 / sides
    length = random.randint(50, 150)
    for i in range(sides):
        t.forward(length)
        t.right(angle)

# Define a function to draw a turtle
def turtle_shape():
    t.pensize(5)
    t.fillcolor("green")
    t.begin_fill()
    t.circle(50)
    t.end_fill()
    t.penup()
    t.goto(0, 70)
    t.pendown()
    t.fillcolor("yellow")
    t.begin_fill()
    t.circle(20)
    t.end_fill()
    t.penup()
    t.goto(20, 100)
    t.pendown()
    t.fillcolor("black")
    t.begin_fill()
    t.circle(10)
    t.end_fill()
    t.penup()
    t.goto(-20, 100)
    t.pendown()
    t.begin_fill()
    t.circle(10)
    t.end_fill()
    t.penup()
    t.goto(-50, 50)
    t.pendown()
    t.right(45)
    t.forward(60)
    t.right(180)
    t.forward(60)
    t.right(90)
    t.forward(60)

# Draw some random shapes and a turtle
for i in range(5):
    t.penup()
    t.goto(random.randint(-250, 250), random.randint(-250, 250))
    t.pendown()
    random_shape()

t.penup()
t.goto(0, 0)
t.pendown()
turtle_shape()

# Convert turtle graphics to SVG
svg = svgwrite.Drawing("shapes.svg")
for command in t.get_svg_commands():
    svg.add(svgwrite.path.Path(command))
svg.save()

# Close turtle graphics window
screen.bye()