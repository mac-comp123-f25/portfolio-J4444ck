import turtle

def spiral_in(turt, side_len):
    if side_len < 5:
        return
    turt.forward(side_len)
    turt.right(90)
    spiral_in(turt, side_len - 5)

def check_spiral_in(start_len):
    win = turtle.Screen()
    t = turtle.Turtle()
    spiral_in(t, start_len)
    win.exitonclick()

check_spiral_in(200)