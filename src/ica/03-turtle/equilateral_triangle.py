import turtle

t = turtle.Turtle()
t.begin_fill()

for i in range(3):
    t.forward(150)
    t.left(120)

t.end_fill()
turtle.done()
