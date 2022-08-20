# set up the graphics library.
from Tkinter import *
window = Tk()
canvas = Canvas(window, width=500, height=500, background="black")
canvas.pack()


#All your code (including function definitions) goes here in the middle

def getStarPixelX(star_string):
	list = star_string.split(",")
	x_pixel = float(list[0])
	x_pixel_coordinate = 250 + (250 * x_pixel)
	return x_pixel_coordinate
def getStarPixelY(star_string):
	list = star_string.split(",")
	y_pixel = float(list[1])
	y_pixel_coordinate = 250 - (250 * y_pixel)
	return y_pixel_coordinate
def getStarSize(star_string):
	list = star_string.split(",")
	magnitude = float(list[4])
	star_size = 10.0/(magnitude + 2)
	return star_size
def getStarName(star_string):
	list = star_string.split(",")
	if len(list) == 7:
		star_name = list[-1]
		return star_name
	else:
		star_name = ""
		return star_name
	
def drawStar(star_string):
	x = getStarPixelX(star_string)
	y = getStarPixelY(star_string)
	size = getStarSize(star_string)
	leftX = x - (size / 2)
	topY = y - (size / 2)
	rightX = x + (size / 2)
	bottomY = y + (size / 2)
	canvas.create_rectangle(leftX, topY, rightX, bottomY, fill="white", width=0)

def drawAllStars():
	f = open("stars.txt")
	s = f.read()
	star_strings = s.split("\n")
	for star_string in star_strings:
		drawStar(star_string)
def getStarString(star_name):
	f = open("stars.txt")
	s = f.read()
	star_strings = s.split("\n")
	for star_string in star_strings:
		x = getStarName(star_string)
		if star_name == x:
			return star_string
	print("ERROR: No star called " + star_name + " could be found.")
	return ""

def drawStarByName(star_name):
	star_string = getStarString(star_name)
	drawStar(star_string)
def drawConstellationLine(star_name1, star_name2):
	star_string1 = getStarString(star_name1)
	x1 = getStarPixelX(star_string1)
	y1 = getStarPixelY(star_string1)
	star_string2 = getStarString(star_name2)
	x2 = getStarPixelX(star_string2)	
	y2 = getStarPixelY(star_string2)
	canvas.create_line(x1, y1, x2, y2, fill="yellow")
def drawConstellationFile(file_name):
	f = open(file_name)
	s = f.read()
	constellations = s.split("\n")
	for pairs in constellations:
		star = pairs.split(",")
		star_name1 = star[0]
		star_name2 = star[1]
		drawConstellationLine(star_name1, star_name2)
drawAllStars()
drawConstellationFile("BigDipper_lines.txt")
drawConstellationFile("Bootes_lines.txt")
drawConstellationFile("Cas_lines.txt")
drawConstellationFile("Cyg_lines.txt")
drawConstellationFile("Gemini_lines.txt")
drawConstellationFile("Hydra_lines.txt")
drawConstellationFile("UrsaMajor_lines.txt")
drawConstellationFile("UrsaMinor_lines.txt")		
	
#complete drawing the canvas
mainloop()