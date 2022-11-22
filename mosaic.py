"""
	Mosaic generator from pixel art
	Process: 
		blow up picture 10 times its size
		generate random background color
		for each pixel, generate a tesson shape centered at the right place
"""


from PIL import Image, ImageDraw
import math, random


def drawtesson(x,y,c,p):
	#x, y, color, picture
	return 0
	

im = Image.open("cavecanem.png")
print("Image source: ", im.size)
output = im.copy()
ratio = 10
