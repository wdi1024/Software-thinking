import turtle
s = turtle.Screen()
t = turtle.Turtle()
t.pensize(3)
t.penup()
x = -100
y = 100
t.goto(x, y)

t.penup()
t.goto(x, y)
t.pendown()
# t.undo()

t.circle(100)
t.penup()
t.goto(x-35.62, y+120)
t.pendown()
t.dot(30)
t.penup()
t.goto(x+35.62, y+120)
t.pendown()
t.dot(30)
t.penup()
t.goto(x-60.62, y+65)
t.pendown()
t.setheading(-60)
t.circle(70, 120)
