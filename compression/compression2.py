from PIL import Image
import colorsys, math, numpy

m = int(input("Zadejte počet barev, co vygenerovat: ")) + 1

im = Image.open("./in.bmp", "r")

out = Image.new(mode="RGB", size=(im.width, im.height))

for x in range(im.width):
    for y in range(im.height):
        (r,g,b) = im.getpixel((x,y))
        (h,s,v) = colorsys.rgb_to_hsv(r,g,b)

        (rr,gg,bb) = colorsys.hsv_to_rgb(
            (math.floor(h*m))/m,
            (math.floor(s*m))/m,
            (math.floor((v/360)*m))/m*360)

        out.putpixel(
            (x,y), 
            tuple(map(int, [rr, gg, bb]))
        )

out.save("out.bmp")