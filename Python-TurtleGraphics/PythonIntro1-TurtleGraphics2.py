# Author: Robert Cheung
# Date: 29 March 2014
# License: CC BY-SA
# For CoderDojo WA

# Python Intro Turtle Graphics

# Python has a rich "library" of functions.
# We are going to use "turtle" to do some simple graphics.
import turtle
# see https://docs.python.org/2/library/turtle.html#filling

if __name__ == "__main__":
    # Setup our drawning surface
    turtle.setup(800,600)     # Sets up the size of the window
    turtle.Screen()           # Turns on the graphics window
    # Set how fast we want the turtle to draw
    turtle.speed(6);          # 0 (fastest) .. 10 (slowest)

    width = 20                # Create a variable called "width"
                              # and make it equal to 10
                              
    # Do some turtle graphics commands
    # Notice all commands from the turtle library is prefixed by "turtle."
    turtle.pencolor("red")
    turtle.forward(width)     # Utilise the width variable we defined earlier
    turtle.right(45)
    turtle.pencolor("green")
    turtle.forward(width)
    turtle.right(45)
    turtle.pencolor("blue")
    turtle.pensize(3)
    turtle.forward(width)
    turtle.right(45)
    turtle.pencolor((0.5,0.5,0))
    turtle.forward(width)
    turtle.right(45)

    ret = input("Press enter to exit.")
    turtle.Screen().bye()     # Turn off the graphics window

# Library reference: http://docs.python.org/2/library/turtle.html
