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
                              
    # In programming, computer follows instructions
    # A "sequence" of instructions is the most basic construct
    # It is simply a list of instructions
    turtle.forward(width)     # Step 1: Move forward 20 steps
    turtle.right(90)          # Step 2: Turn right 90 degrees  
    turtle.forward(width)     # Step 3: Move forward 20 steps
    turtle.right(90)          #  ... and so on
    turtle.forward(width)     
    turtle.right(90)
    turtle.forward(width)     
    turtle.right(90)

    ret = input("Press enter to exit.")
    turtle.Screen().bye()     # Turn off the graphics window

# Library reference: http://docs.python.org/2/library/turtle.html
