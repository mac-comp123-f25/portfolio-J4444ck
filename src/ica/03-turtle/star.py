import turtle


window = turtle.Screen()
window.bgcolor("white")

t1 = turtle.Turtle()
t1.color("blue")
t1.shape("turtle")
t1.speed(3)


for i in range(5):
    t1.forward(100)
    t1.right(144)

t2 = turtle.Turtle()
t2.color("red")
t2.shape("turtle")
t2.speed(3)

t2.penup()
t2.goto(150, 0)
t2.pendown()

for i in range(5):
    t2.forward(100)
    t2.right(144)

window.exitonclick()
