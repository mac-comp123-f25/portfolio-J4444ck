import turtle
import math
def sepal_T(sepalTurtle,circle,left):
    for i in range(5):
        sepalTurtle.begin_fill()
        sepalTurtle.circle(50)
        sepalTurtle.end_fill()
        sepalTurtle.left(72)
        sepalTurtle.hideturtle()

def petal_T(petalTurtle,circle,left):
    for i in range(5):
        petalTurtle.begin_fill()
        petalTurtle.circle(25)
        petalTurtle.end_fill()
        petalTurtle.left(72)

def drawFiveCircles(turt,radius,centerX,centerY):
    for i in range(5):
        sepalTurtle.penup()
        sepalTurtle.goto(centerX, centerY)
        sepalTurtle.pendown()
        sepalTurtle.begin_fill()
        sepalTurtle.circle(50)
        sepalTurtle.end_fill()
        sepalTurtle.left(72)
        sepalTurtle.hideturtle()
        
def drawAnotherFiveCircles(turt,radius,centerX,centerY):
    for i in range(5):
        petalTurtle.penup()
        petalTurtle.goto(centerX, centerY)
        petalTurtle.down()
        petalTurtle.begin_fill()
        petalTurtle.circle(25)
        petalTurtle.end_fill()
        petalTurtle.left(72)

win = turtle.Screen()
win.bgcolor("light sky blue")

sepalTurtle = turtle.Turtle()
sepalTurtle.speed(0)
sepalTurtle.color("dark green", "spring green")
sepalTurtle.hideturtle()

petalTurtle = turtle.Turtle()
petalTurtle.speed(0)
petalTurtle.color('dark red', 'light coral')
petalTurtle.hideturtle()

centerTurtle = turtle.Turtle()
centerTurtle.speed(0)
centerTurtle.color('purple4')
centerTurtle.hideturtle()

stampTurtle = turtle.Turtle()
stampTurtle.color("gold")
stampTurtle.speed(0)
stampTurtle.shape("turtle")
stampTurtle.hideturtle()

drawFiveCircles(sepalTurtle, 50, 0, 0)
drawFiveCircles(sepalTurtle, 50, 220, 0)
drawFiveCircles(sepalTurtle, 50, 0, 220)
drawFiveCircles(sepalTurtle, 50, -220, 0)
drawFiveCircles(sepalTurtle, 50, 0, -220)

drawAnotherFiveCircles(petalTurtle, 50, 0, 0)
drawAnotherFiveCircles(petalTurtle, 50, 220, 0)
drawAnotherFiveCircles(petalTurtle, 50, 0, 220)
drawAnotherFiveCircles(petalTurtle, 50, -220, 0)
drawAnotherFiveCircles(petalTurtle, 50, 0, -220)

centerTurtle.up()
centerTurtle.goto(0, -15)
centerTurtle.down()
centerTurtle.begin_fill()
centerTurtle.circle(15)
centerTurtle.end_fill()

stampTurtle.up()
stampTurtle.goto(-2,0)
stampTurtle.down()
stampTurtle.stamp()

centerTurtle.up()
centerTurtle.goto(0, 205)
centerTurtle.down()
centerTurtle.begin_fill()
centerTurtle.circle(15)
centerTurtle.end_fill()

stampTurtle.up()
stampTurtle.goto(-2,220)
stampTurtle.down()
stampTurtle.stamp()

centerTurtle.up()
centerTurtle.goto(220, -15)
centerTurtle.down()
centerTurtle.begin_fill()
centerTurtle.circle(15)
centerTurtle.end_fill()

stampTurtle.up()
stampTurtle.goto(218,0)
stampTurtle.down()
stampTurtle.stamp()

centerTurtle.up()
centerTurtle.goto(0, -235)
centerTurtle.down()
centerTurtle.begin_fill()
centerTurtle.circle(15)
centerTurtle.end_fill()

stampTurtle.up()
stampTurtle.goto(-2,-220)
stampTurtle.down()
stampTurtle.stamp()

centerTurtle.up()
centerTurtle.goto(-220, -15)
centerTurtle.down()
centerTurtle.begin_fill()
centerTurtle.circle(15)
centerTurtle.end_fill()

stampTurtle.up()
stampTurtle.goto(-222,0)
stampTurtle.down()
stampTurtle.stamp()

win.exitonclick()