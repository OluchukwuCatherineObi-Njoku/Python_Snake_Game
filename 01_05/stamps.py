# Import the Turtle Graphics module
import turtle

# Define program constants
WIDTH = 500
HEIGHT = 500

# Create a window where we will do our drawing.
screen = turtle.Screen()
screen.setup(WIDTH, HEIGHT)  # Set the dimensions of the Turtle Graphics window.
screen.title("Stamping")
screen.bgcolor("cyan")

# Create a turtle to do your bidding
stamper = turtle.Turtle()
stamper.shape("square") #change to square
stamper.color("red") #change to red
stamper.shapesize(50/20) #change shape size from 20 to 50
stamper.stamp() #make a stamp
stamper.penup() #don't draw anything
stamper.shapesize(10/20) #change size from 20 to 10
stamper.goto(100,100)#go to location 100,100
stamper.stamp() #make a stamp

# # Your turtle awaits your command
# stamper.forward(100)  # Sample command

# This statement (or an equivalent) is needed at the end of all your turtle programs.
turtle.done()
