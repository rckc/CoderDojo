# Author: Robert Cheung
# Date: 29 March 2014
# License: CC BY-SA
# For CoderDojo WA

# Python Intro Turtle Graphics

import turtle
# see https://docs.python.org/2/library/turtle.html#filling

def drawPolygon(numsides, width=20):
    angle = 360.0 / numsides
    for i in range(numsides):
        turtle.forward(width)
        turtle.right(angle)

if __name__ == "__main__":
    # Setup our drawning surface
    turtle.setup(800,600)     # Sets up the size of the window
    turtle.Screen()           # Turns on the graphics window
    # Set how fast we want the turtle to draw
    # Also look at turtle.tracer() and turtle.update()
    turtle.speed(6);          # 0 (fastest) .. 10 (slowest)

    ret = ""
    while (ret != "q"):
        print("Enter:")
        print("<number> for a n-sided polygon")
        print("c for clear screen")
        print("q for quit")
        ret = input("?")
        if (ret == "c"):
            turtle.Screen().clearscreen()
        elif (ret.isdigit()):
            # http://docs.python.org/2/library/stdtypes.html#str.isdigit
            drawPolygon(int(ret))
        elif (ret == "q"):
            print("Bye")
        else:
            print("Do not know command: ", ret)

    ret = input("Press enter to exit.")
    turtle.Screen().bye()     # Turn off the graphics window

# Library reference: http://docs.python.org/2/library/turtle.html
