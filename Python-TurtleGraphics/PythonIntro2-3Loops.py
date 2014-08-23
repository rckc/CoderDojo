# Author: Robert Cheung
# Date: 29 March 2014
# License: CC BY-SA
# For CoderDojo WA

# Python Intro Turtle Graphics

import turtle

# drawSquare version 1, using the "for" loop construct
def drawSquare(width=20):
    print "In drawSquare(", width, ")"
    for i in range(4):
        print i
        turtle.forward(width)
        turtle.right(90)          

# drawSquare version 2, using the "while" loop construct
def drawSquare2(width=20):
    print "In drawSquare2(", width, ")"
    i=0
    while i<4:
        print i
        turtle.forward(width)
        turtle.right(90)          
        i += 1

if __name__ == "__main__":
    # Setup our drawning surface
    turtle.setup(320,240)     # Sets up the size of the window
    turtle.Screen()           # Turns on the graphics window

    width = 20                # Create a variable called "width"
                              # and make it equal to 10

    drawSquare(5)             
    turtle.penup()            
    turtle.forward(10)
    turtle.pendown()

    drawSquare2(10)           # Lets use our second version of drawSquare
    turtle.penup()
    turtle.forward(15)
    turtle.pendown()
    
    drawSquare()              
                              

    ret = raw_input("Press enter to exit.")
    turtle.Screen().bye()     # Turn off the graphics window

# Library reference: http://docs.python.org/2/library/turtle.html
