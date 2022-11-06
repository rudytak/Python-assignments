import turtle
import random, math
from tkinter import *  # Python 3
import imageio

leng = 30

def turtle_headto(t, x, y):
	t.left(t.towards(x, y) - t.heading() - 90)


def bg(t, col):
	turtle.clear()
	t.goto(0, 0)
	t.penup()
	t.fillcolor(col)
	for i in range(4):
		t.begin_fill()
		t.circle(1000)
		t.end_fill()
		t.right(90)


t = turtle.Turtle()

t.speed(0)
t.hideturtle()

for time in range(0, leng):
	random.seed(10)

	bg(t, "black")
	t.pen(pencolor="white", pensize="1", fillcolor="white")

	t.down()
	t.dot(20)
	t.up()
	t.goto(0, 0)

	x = 2

	for i in range(7):

		a = random.random() * 3.141 + i*time/25
		t.up()
		t.goto(math.cos(a) * 30 * i, math.sin(a) * 30 * i)
		turtle_headto(t, 0, 0)
		t.down()

		t.color(random.random(), random.random(), random.random())
		t.dot(2 + x)
		t.circle(30 * i)

		for j in range(i):
			t.circle(10 * j)

			t.up()
			t.right(90)
			t.forward(10)
			t.left(90)
			t.down()
		t.up()
		t.left(90)
		t.forward(10 * i)
		t.right(90)
		t.down()

		for j in range(i):
			aa = random.random() * 3.141 - j*time/25
			t.up()
			t.goto(
				math.cos(a) * 30 * i + math.cos(aa) * 10 * j,
				math.sin(a) * 30 * i + math.sin(aa) * 10 * j,
			)
			t.down()
			t.dot(x * (random.random() * 2 / 3 + 1 / 3))

		x += 2
	t.penup()

	ts = turtle.getscreen()
	ts.getcanvas().postscript(file="./"+str(time)+".eps")

# images = []
# for i in range(0,leng):
# 	images.append(imageio.imread("./"+str(i)+".eps"))

# imageio.mimsave('/gif.gif', images)