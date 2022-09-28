import turtle as t
import math

PI = 3.141596

def draw_poly(n, sl):
    ang = ((n-2) * 180)/n

    t.pendown()
    for s in range(n):
        t.forward(sl)
        t.left(180 - ang)
    t.penup()

    pass

def rect(w,h):
    t.pendown()

    t.forward(w)
    t.left(90)
    
    t.forward(h)
    t.left(90)

    t.forward(w)
    t.left(90)
    
    t.forward(h)
    t.left(90)

    t.penup()

def draw_house(size):
    draw_poly(4, size)

    t.left(90)
    t.forward(size)
    t.right(90)

    draw_poly(3, size)

    t.right(90)
    t.forward(size)
    t.left(90)

    t.forward(size/3)
    rect(size/3, size * 2/3)
    t.backward(size/3)


def draw_kumiko_cell(sl):

    for r in range(6):
        t.left(60)

        draw_poly(3,sl)
        for i in range(3):
            draw_poly(3,sl/5)
            t.forward(sl)
            t.left(120)

def draw_kumiko_grid(sl):
    w,h = t.screensize()
    t.penup()
    for x in range(-math.ceil(w/(2*sl)) - 1, 1 + math.ceil(w/(2*sl)), 1):
        for y in range(-math.ceil(h/((3)**(.5)*sl)) - 1, 1 + math.ceil(h/((3)**(.5)*sl)), 1):
            t.goto(
                x * 2 * sl + (sl if (y)%2==0 else 0),
                y * sl * (3)**(.5)
            )
            draw_kumiko_cell(sl)

def draw_row(sl, cells):
    draw_kumiko_cell(sl)

if(__name__ == "__main__"):
    t.speed(0)
    t.width(1)

    # draw_poly(4, 100)
    # t.goto(200, 0)
    
    # t.pendown()
    # t.circle(50)
    # t.penup()
    # t.goto(0, 200)

    # t.fillcolor("#000000")
    # t.begin_fill()
    # t.circle(50)
    # t.end_fill()
    # t.goto(200, 200)

    # draw_house(100)

    # for s in range(1,5):
    #     draw_house(s * 25)
    #     t.goto(100*s, 0)
    
    # cols = [
    #     "#ff0000",
    #     "#00ff00",
    #     "#0000ff",
    #     "#ff00ff",
    #     "#00ffff",
    # ]
    # for s in range(4, 0, -1):
    #     t.fillcolor(cols[s-1])
    #     t.begin_fill()
    #     t.circle(25 * s)
    #     t.end_fill()

    draw_kumiko_grid(100)

    input()
