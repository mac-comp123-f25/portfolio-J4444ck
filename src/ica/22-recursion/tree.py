import turtle
import random

def draw_fractal_tree(turt, length):
    if length < 5:
        return
    turt.forward(length)
    turt.left(30)
    draw_fractal_tree(turt, length * 0.7)
    turt.right(60)
    draw_fractal_tree(turt, length * 0.7)
    turt.left(30)
    turt.backward(length)

def draw_weeping_tree(turt, length):
    if length < 5:
        return
    turt.forward(length)
    angle = random.randint(20, 40)
    shrink1 = random.uniform(0.6, 0.8)
    shrink2 = random.uniform(0.6, 0.8)
    turt.left(angle)
    draw_weeping_tree(turt, length * shrink1)
    turt.right(angle * 2)
    draw_weeping_tree(turt, length * shrink2)
    turt.left(angle)
    turt.backward(length)

def check_draw_fractal_tree(size):
    win = turtle.Screen()
    t = turtle.Turtle()
    t.left(90)
    draw_fractal_tree(t, size)
    win.exitonclick()

def check_draw_weeping_tree(size):
    win = turtle.Screen()
    t = turtle.Turtle()
    t.left(90)
    draw_weeping_tree(t, size)
    win.exitonclick()

check_draw_fractal_tree(75)