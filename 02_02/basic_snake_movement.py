# Import the Turtle Graphics module
import turtle

# Define program constants
WIDTH = 500
HEIGHT = 500
DELAY = 400 #milliseconds

def move_snake():
    stamper.clearstamps() #remove existing stamps made by stamper
    
    new_head = snake[-1].copy() #make a copy of the last element of the list
    new_head[0] += 20 #change the x coordinate of the new head
    
    snake.append(new_head)
    
    snake.pop(0) #remove the first element of the list
    
    for segment in snake:
        stamper.goto(segment[0], segment[1])
        stamper.stamp()
        
    #refresh screen, unless you do so, the screen will not be updated
    screen.update()
    
    turtle.ontimer(move_snake, DELAY) #wait for 400 milliseconds before calling the function again

# Create a window where we will do our drawing. Customizes screen
screen = turtle.Screen()
screen.setup(WIDTH, HEIGHT)  # Set the dimensions of the Turtle Graphics window.
screen.title("Snake")
screen.bgcolor("pink")
screen.tracer(0) # Turn off automatic screen updates

# Create a turtle to do your bidding
stamper = turtle.Turtle()
stamper.shape("square")
stamper.color()
#stamper.shapesize(50 / 20)
stamper.penup()

# Create snake as list of coordinate pairs
snake = [[0,0],[20,0],[40,0],[60,0]]

# Draw snake for the first time

for segment in snake:
    stamper.goto(segment[0], segment[1])
    stamper.stamp()
    
move_snake()

# Finish nicely
turtle.done()
