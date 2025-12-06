import turtle

def tele_turtle(n):
    win = turtle.Screen()
    tele_t = turtle.Turtle()
    for i in range(n):
        move = input("Enter next move: ")
        do_move(tele_t, move)
    win.exitonclick()

def do_move(turt, move):
    if move == "w":
        turt.forward(15)
    elif move == "s":
        turt.backward(15)
    elif move == "d":
        turt.right(90)
    elif move == "a":
        turt.left(90)
    else:
        print("Invalid command")

if __name__ == "__main__":
    tele_turtle(10)
