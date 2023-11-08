import turtle
import random, math
from tkinter import *  # Python 3
import imageio

leng = 100
r_div = 100
seed = 10

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
	random.seed(seed)

	bg(t, "black")
	t.pen(pencolor="white", pensize="1", fillcolor="white")

	t.down()
	t.dot(20)
	t.up()
	t.goto(0, 0)

	x = 2

	for i in range(7):

		a = random.random() * 3.141 + i*time/r_div
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
			aa = random.random() * 3.141 - j*time/r_div
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

# source: https://stackoverflow.com/questions/44587376/oserror-unable-to-locate-ghostscript-on-paths/63262348#63262348
from PIL import EpsImagePlugin, Image
EpsImagePlugin.gs_windows_binary = r'C:/Program Files/gs/gs10.00.0/bin/gswin64c'

images = []
for i in range(0,leng):
	im = Image.open("./"+str(i)+".eps")
	im.save("./"+str(i)+".png")

	images.append(imageio.imread("./"+str(i)+".png"))

imageio.mimsave('./gif.gif', images)