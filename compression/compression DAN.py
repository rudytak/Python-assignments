from PIL import Image
import json
with Image.open("./in.bmp") as img:
    pixels = img.load()
    print(pixels)
    dimensions = img.size
    img.mode = "hsv"

colours = {}
for x in range(dimensions[0]):
    for y in range(dimensions[1]):
        # The keys are stringified tuples instead of tuples because json.dumps() requires: keys must be str, int, float, bool or None, not tuple
        if (pixels[x, y] in colours):
            colours[pixels[x, y]].append((x, y))
        else:
            colours[pixels[x, y]] = [(x, y)]



# print(dimensions)
# print(colours)

with open("./compressed.txt", "w") as f:
    f.write(str(colours))