from PIL import Image, ImageDraw
import random

width = 20
length = 20


lineColors = []
backColors = []
for i in range(20):
    for j in range(20):
        for k in range(10):
            lineColors.append((220 + i, 150 + j, 130 + k))
            backColors.append((240 + i, 230 + j, 210 + k))

line = "".join([random.choice("01") for i in range(width)])
img = Image.new('RGB', (width, length), color = (237, 230, 209))

#rule 30
rule = {
    "000":"0",
    "001":"1",
    "010":"1",
    "011":"1",
    "100":"1",
    "101":"0",
    "110":"0",
    "111":"0"}

def update(l):
    w = len(l)
    new = ""
    for i in range(w):
        context = "".join([l[(i-1) % w], l[i], l[(i+1) % w]])
        new+=rule[context]
    return new	

data = [line]		
for i in range(length):
    data.append(update(data[-1]))

#building the image from data:
for x in range(width):
    for y in range(length):
        if data[y][x] == "1":
            color = (0,0,255)#random.choice(lineColors)
        else:
            color = (255,0,0)#random.choice(backColors)
        img.putpixel((x, y), color)

filename = "".join([random.choice("1234567890") for i in range(32)])
img.save(filename+'.png')
