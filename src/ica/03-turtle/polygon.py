import turtle

n = 7

t = turtle.Turtle()
t.begin_fill()

for i in range(n):
    t.forward(100)
    t.left(360 / n)

t.end_fill()
turtle.done()
