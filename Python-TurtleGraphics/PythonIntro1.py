# Author: Robert Cheung
# Date: 29 March 2014
# License: CC BY-SA
# For CoderDojo WA

import turtle
# see https://docs.python.org/2/library/turtle.html#filling

def intro():
    print("Welcome to CoderDojo WA Python/Turtle graphics demo v0.1")
    print("Author: Robert Cheung")

def cleanup():
    # Close the screen
    turtle.Screen().bye()

def printOptions():
    print("s = Square")
    print("q = quit")

def square(length=10):
    turtle.pendown()
    turtle.forward(length)
    turtle.right(90)
    turtle.forward(length)
    turtle.right(90)
    turtle.forward(length)
    turtle.right(90)
    turtle.forward(length)
    turtle.right(90)

if __name__ == "__main__":
    intro()
    turtle.Screen()

    _quit = False
    while not _quit:
        printOptions()
        ret = input("command?")

        if ret == "s":
            square()
        if ret == "q":
            _quit = True

    ret = input("Press enter to exit.")
    cleanup()

