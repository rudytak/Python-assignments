from PIL import Image

im = Image.open("./in.bmp", "r")

pixels = list(im.getdata())

print(pixels[0], im.width, im.height)

out = {
    "w": im.width,
    "h": im.height
}

i = 0
while i < len(pixels):
    p = pixels[i]
    l = 1

    if(not p in out):
        out[p] = []

    while i+l < len(pixels):
        if(pixels[i] == pixels[i + l]):
            l+=1
        else:
            break

    if(l == 1):
        out[p].append(i)
    else:
        out[p].append((i, l))

    i+=l
    # print(p)

with open("./out.txt", "w") as f:
    f.write(str(out))