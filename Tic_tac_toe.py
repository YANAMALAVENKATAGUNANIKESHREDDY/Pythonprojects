#importing Module
import turtle
#creating Environment 
ws=turtle.Screen()
t=turtle.Turtle() # Instance of module
t.color("Red")
t.width("3")
t.speed(3)
# Loop for Outside Square 
for i in range(4):
    t.forward(300)
    t.left(90)
#For Internal Grids
t.penup()
t.goto(0,100)
t.pendown()

t.forward(300)

t.penup()
t.goto(0,200)
t.pendown()

t.forward(300)

t.penup()
t.goto(100,0)
t.pendown()
t.left(90)
t.forward(300)

t.penup()
t.goto(200,0)
t.pendown()

t.forward(300)