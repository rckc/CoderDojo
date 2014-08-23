# Author: Robert Cheung
# Date: 29 March 2014
# License: CC BY-SA
# For CoderDojo WA

# Python Intro Turtle Graphics

import turtle

def drawPolygon(numsides, width=20):
    angle = 360.0 / numsides
    for i in range(numsides):
        turtle.forward(width)
        turtle.right(angle)

if __name__ == "__main__":
    # Setup our drawning surface
    turtle.setup(320,240)     # Sets up the size of the window
    turtle.Screen()           # Turns on the graphics window

    ret = ""
    while (ret <> "q"):
        print "Enter:"
        print "<number> for a n-sided polygon"
        print "c for clear screen"
        print "q for quit"
        ret = raw_input("?")
        if (ret == "c"):
            turtle.Screen().clearscreen()
        elif (ret.isdigit()):
            # http://docs.python.org/2/library/stdtypes.html#str.isdigit
            drawPolygon(int(ret))
        elif (ret == "q"):
            print "Bye"
        else:
            print "Do not know command: ", ret

    ret = raw_input("Press enter to exit.")
    turtle.Screen().bye()     # Turn off the graphics window

# Library reference: http://docs.python.org/2/library/turtle.html
