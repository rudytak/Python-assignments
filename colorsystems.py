
import colorsys
from re import M
import turtle as t

(r, g, b) = [int(ch) for ch in input("Zadejte RGB barvu: ").split(" ")]
(h, s, v) = colorsys.rgb_to_hsv(r, g, b)

t.bgcolor((0,0,0))
t.colormode(255)
t.speed(0)

m = int(input("Zadejte počet barev, co vygenerovat: ")) + 1
for i in range(m):
    (rr,gg,bb) = colorsys.hsv_to_rgb((h+i/m)%1,s,v)
    print(rr,gg,bb)

    t.color((int(rr),int(gg),int(bb)))
    t.fillcolor((int(rr),int(gg),int(bb)))
    
    t.begin_fill()
    t.circle(100, 360/m)
    t.left(90)
    t.forward(100)
    t.end_fill()

    t.backward(100)
    t.right(90)

input()