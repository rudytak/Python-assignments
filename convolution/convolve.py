import numpy as np
from PIL import Image 
 
def convolve(big, kernel):
    if (len(kernel) == 0 or len(kernel[0]) == 0):
        raise "Kernel has to have both sides larger than 0."
 
    if (len(big) < 2 or len(big[0]) < 2):
        raise "Convoluted matrix has to be larger than 2x2."
 
    if (len(kernel) > len(big) or len(kernel[0]) > len(big[0])):
        raise "Kernel cannot be larger than the convoluted matrix."
 
    if (len(kernel) % 2 == 0 or len(kernel[0]) % 2 == 0):
        raise "Cannot convolve with a even-sided kernel."
 
    out = np.array(
        [
            [0 for x in range(len(big[0]) - 2)]
            for y in range(len(big) - 2)
        ]
    )
 
    for y in range(1, len(out)+1):
        for x in range(1, len(out[y - 1])+1):
            for yy in range(
                int(-(len(kernel)-1)/2), 
                int((len(kernel)-1)/2 +1)
                ):
                for xx in range(
                    int(-(len(kernel[0])-1)/2), 
                    int((len(kernel[0])-1)/2 +1)
                    ):
                    out[y-1][x-1] += big[y + yy][x + xx] * kernel[(yy + int((len(kernel)-1)/2))][(xx + int((len(kernel[0])-1)/2))]
 
    # print(out)
    return out

def main():
    im = Image.open("./dubai.png", "r")

    pixels = list(im.getdata())

    k = np.array([
        [0, 1, 0],
        [1, -4, 1],
        [0, 1, 0]
    ], dtype=np.float64)

    # k /= k.sum()

    r = []
    g = []
    b = []

    for y in range(im.height):
        rr = []
        gg = []
        bb = []
        for x in range(im.width):
            p = pixels[y * im.width + x]

            rr.append(p[0])
            gg.append(p[1])
            bb.append(p[2])

        r.append(rr)
        g.append(gg)
        b.append(bb)
 
    r_out = convolve(np.array(r), k)
    g_out = convolve(np.array(g), k)
    b_out = convolve(np.array(b), k)

    out = Image.new(mode="RGB", size=(im.width, im.height))
    for y in range(len(r_out)):
        for x in range(len(r_out[0])):
            out.putpixel((x,y), tuple(map(int, [r_out[y][x], g_out[y][x], b_out[y][x]])))

    out.save("out.bmp")
 
main()