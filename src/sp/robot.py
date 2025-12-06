import turtle as t

t.setup(width=900, height=900)
t.bgcolor("black")
t.colormode(255)
t.speed(0)
t.hideturtle()

def move(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()

def draw_rect(x, y, w, h, line_color, fill_color=None):
    t.color(line_color)
    move(x, y)
    if fill_color is not None:
        t.fillcolor(fill_color)
        t.begin_fill()
    for _ in range(2):
        t.forward(w)
        t.left(90)
        t.forward(h)
        t.left(90)
    if fill_color is not None:
        t.end_fill()

def draw_poly(points, line_color, fill_color=None):
    if not points:
        return
    t.color(line_color)
    move(points[0][0], points[0][1])
    if fill_color is not None:
        t.fillcolor(fill_color)
        t.begin_fill()
    for x, y in points[1:]:
        t.goto(x, y)
    t.goto(points[0][0], points[0][1])
    if fill_color is not None:
        t.end_fill()

def draw_circle(x, y, r, line_color, fill_color=None):
    t.color(line_color)
    move(x, y - r)
    if fill_color is not None:
        t.fillcolor(fill_color)
        t.begin_fill()
    t.circle(r)
    if fill_color is not None:
        t.end_fill()

# Head
def draw_head():
    # Helmet sides
    draw_poly(
        [(-90, 260), (-110, 330), (-70, 380), (-40, 330), (-40, 260)],
        (0, 200, 255), (10, 40, 80)
    )
    draw_poly(
        [(90, 260), (110, 330), (70, 380), (40, 330), (40, 260)],
        (0, 200, 255), (10, 40, 80)
    )

    # Central crest
    draw_poly(
        [(-40, 380), (-20, 420), (20, 420), (40, 380)],
        (0, 220, 255), (15, 70, 120)
    )

    # Forehead plate
    draw_rect(-40, 330, 80, 40, (0, 220, 255), (10, 50, 90))

    # Face plate
    draw_poly(
        [(-90, 260), (-70, 210), (-40, 170),
         (40, 170), (70, 210), (90, 260)],
        (0, 220, 255), (15, 15, 30)
    )

    # Cheek / side guards
    draw_poly(
        [(-90, 260), (-115, 210), (-90, 160), (-70, 210)],
        (0, 220, 255), (5, 30, 60)
    )
    draw_poly(
        [(90, 260), (115, 210), (90, 160), (70, 210)],
        (0, 220, 255), (5, 30, 60)
    )

    # Mouth guard
    draw_poly(
        [(-50, 170), (-35, 120), (35, 120), (50, 170)],
        (0, 220, 255), (20, 20, 40)
    )

    # Chin
    draw_poly(
        [(-20, 120), (-12, 95), (12, 95), (20, 120)],
        (0, 220, 255), (40, 40, 70)
    )

    # Eyes
    def eye(x, y):
        t.color((0, 255, 255))
        t.fillcolor((0, 180, 255))
        move(x, y)
        t.begin_fill()
        for _ in range(2):
            t.forward(30)
            t.left(90)
            t.forward(10)
            t.left(90)
        t.end_fill()

    eye(-55, 235)
    eye(25, 235)

    # Eye underline
    t.color((0, 255, 255))
    move(-60, 230)
    t.forward(40)
    move(20, 230)
    t.forward(40)

    # Center line
    t.color((0, 120, 200))
    move(0, 260)
    t.goto(0, 170)

# Torso
def draw_torso():
    # Upper chest armor
    draw_poly(
        [(-140, 180), (-170, 140), (-150, 80),
         (150, 80), (170, 140), (140, 180)],
        (0, 200, 255), (12, 35, 70)
    )

    #chest
    draw_rect(-90, 110, 180, 50,
              (0, 255, 255), (5, 20, 40))

    draw_rect(-85, 115, 75, 35,
              (0, 255, 255), (0, 100, 180))
    draw_rect(10, 115, 75, 35,
              (0, 255, 255), (0, 100, 180))

    draw_rect(-20, 80, 40, -20,
              (0, 255, 255), (15, 15, 35))

    draw_rect(-70, 60, 140, -40,
              (0, 200, 255), (10, 25, 50))

    # ab
    t.color((0, 255, 255))
    move(-60, 40)
    t.forward(120)
    move(-60, 20)
    t.forward(120)

    # Pelvis / hip plate
    draw_poly(
        [(-90, 20), (-70, -10), (70, -10), (90, 20)],
        (0, 200, 255), (15, 25, 45)
    )

# Arms
def draw_arms():
    # Left shoulder pad
    draw_rect(-210, 170, 60, -60,
              (0, 200, 255), (10, 35, 70))
    # Right shoulder pad
    draw_rect(150, 170, 60, -60,
              (0, 200, 255), (10, 35, 70))

    # Left upper arm
    draw_rect(-200, 110, 40, -70,
              (0, 220, 255), (8, 30, 60))
    # Right upper arm
    draw_rect(160, 110, 40, -70,
              (0, 220, 255), (8, 30, 60))

    # Left forearm
    draw_rect(-210, 40, 60, -80,
              (0, 220, 255), (5, 25, 55))
    # Right forearm
    draw_rect(150, 40, 60, -80,
              (0, 220, 255), (5, 25, 55))

    # Left hand
    draw_rect(-205, -40, 50, -20,
              (0, 255, 255), (20, 20, 35))
    # Right hand
    draw_rect(155, -40, 50, -20,
              (0, 255, 255), (20, 20, 35))

# legs
def draw_legs():
    # Left upper leg
    draw_rect(-70, -10, 50, -80,
              (0, 220, 255), (10, 35, 70))
    # Right upper leg
    draw_rect(20, -10, 50, -80,
              (0, 220, 255), (10, 35, 70))

    # Left lower leg
    draw_poly(
        [(-80, -90), (-90, -200), (-40, -200), (-20, -90)],
        (0, 220, 255), (8, 25, 55)
    )
    # Right lower leg
    draw_poly(
        [(80, -90), (90, -200), (40, -200), (20, -90)],
        (0, 220, 255), (8, 25, 55)
    )

    # Knee plates
    draw_rect(-75, -70, 40, -15,
              (0, 255, 255), (15, 40, 80))
    draw_rect(35, -70, 40, -15,
              (0, 255, 255), (15, 40, 80))

    # Feet
    draw_poly(
        [(-100, -200), (-40, -200), (-40, -230), (-130, -230)],
        (0, 255, 255), (15, 35, 70)
    )
    draw_poly(
        [(100, -200), (40, -200), (40, -230), (130, -230)],
        (0, 255, 255), (15, 35, 70)
    )


    # Ground line
    t.color((0, 80, 120))
    move(-200, -230)
    t.forward(400)

def draw_transformer_full_body():
    draw_head()
    draw_torso()
    draw_arms()
    draw_legs()

    t.color((0, 200, 255))
    move(0, -270)
    t.write("It's a robot!",
            align="center",
            font=("Arial", 18, "bold"))

draw_transformer_full_body()
t.done()

