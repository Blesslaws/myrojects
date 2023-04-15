import turtle

# Set up turtle screen
turtle.speed(0)
turtle.bgcolor("black")

# Define mandala function
def mandala(size, color):
    for i in range(8):
        turtle.color(color)
        turtle.circle(size)
        turtle.right(45)

# Draw mandala art
for i in range(8):
    mandala(100, "red")
    turtle.right(45)

# Hide turtle and exit program
turtle.hideturtle()
turtle.done()