# Author: Robert Cheung
# Date: 29 March 2014
# License: CC BY-SA
# For CoderDojo WA

# Python Intro Turtle Graphics

# Python has a rich "library" of functions.
# We are going to use "turtle" to do some simple graphics.
import turtle

# We are going to create a procedure named "drawSquare".
# It takes one input called "width", and its default value is 10
# Inputs to a procedure is known as a "parameter".
def drawSquare(width=20):
    # We have taken the steps from the previous tutorial and put it in this
    # procedure.
    turtle.forward(width)     
    turtle.right(90)          
    turtle.forward(width)     
    turtle.right(90)          
    turtle.forward(width)     
    turtle.right(90)
    turtle.forward(width)     
    turtle.right(90)
    

if __name__ == "__main__":
    # Setup our drawning surface
    turtle.setup(320,240)     # Sets up the size of the window
    turtle.Screen()           # Turns on the graphics window

    width = 20                # Create a variable called "width"
                              # and make it equal to 10

    drawSquare(5)             # Instruct python to use or method "drawSquare"
    turtle.penup()            # space things out before drawing the next Square
    turtle.forward(10)
    turtle.pendown()

    drawSquare(10)            # Create another square, but larger this time
    turtle.penup()
    turtle.forward(15)
    turtle.pendown()
    
    drawSquare()              # Notice that no width parameter is provided
                              # Python will use the default value

    ret = raw_input("Press enter to exit.")
    turtle.Screen().bye()     # Turn off the graphics window

# Library reference: http://docs.python.org/2/library/turtle.html
