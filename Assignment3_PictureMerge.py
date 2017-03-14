# This is a program to combine pictures in four different ways
# The program assumes that both images are the same size

from SimpleGraphics import *

# Width of the blended bar in the middle (in pixels)
barWidth = int(100) 


def main():
	# load the two images
	img1 = loadImage("image1.gif")
	img2 = loadImage("image2.gif")
	ctype = usrInput() # call the user input function, get the input
	# if statement to decide which funciton to call and which paramaters to pass in
	if ctype == 1:
		newImage = totalblend(img1, img2)
	elif ctype == 2:
		sizePar = int(3)
		sizeMultiple = int(1)
		newImage = barblend(img1, img2, sizePar, sizeMultiple)
	elif ctype == 3:
		sizePar = int(2)
		sizeMultiple = int(1)
		newImage = barblend(img1, img2, sizePar, sizeMultiple)
	else:
		sizePar = int(3)
		sizeMultiple = int(2)
		newImage = barblend(img1, img2, sizePar, sizeMultiple)
	# find and load the size of the two images
	imgHeight = getHeight(img1)
	imgWidth = getWidth(img1)	
	resize(imgWidth, imgHeight)
	drawImage(newImage,0,0)

# Collects correct user input
def usrInput():
	ctype = int(input("Select combination type: 1 (total), 2 (left), 3 (center), 4 (right). "))
	if ctype == 1 or ctype == 2 or ctype == 3 or ctype == 4:
		return ctype
	else:
		usrInput()
# Blends two pixels together
def blend(img1,img2,x,y):
	r, g, b = getPixel(img1, x, y) # get img1's pixel 
	r1, g1, b1 = getPixel(img2, x, y) # get img2's pixel
	# Average out the pixel values
	r = (r+r1)/2
	g = (g+g1)/2
	b = (b+b1)/2
	return (r, g, b)

# This is the function to blend the two images together totally
def totalblend(img1, img2):
	imgHeight = getHeight(img1) # find and load the size of the two images
	imgWidth = getWidth(img1)	
	newImage = createImage(imgWidth, imgHeight) # create the new image
	for x in range(imgWidth):
		for y in range(imgHeight):
			r,g,b = blend(img1,img2,x,y)
			putPixel(newImage, x, y, r, g, b) # put pixel into the blank image
	return newImage

# This is the function to blend two images together in a bar in between the two images
# It can create a range of different images depending on the values of sizePar and sizeMultiple
def barblend(img1, img2, sizePar, sizeMultiple):
	imgHeight = getHeight(img1) # find and load the size of the two images
	imgWidth = getWidth(img1)	
	newImage = createImage(imgWidth, imgHeight) # create the new image (empty)
	leftSize = int(((imgWidth/sizePar)*sizeMultiple)-(barWidth/2)) # define the size of the left side
	for x in range(leftSize): # draw the left side from pixels from img1
		for y in range(imgHeight):
			r, g, b = getPixel(img1,x,y)
			putPixel(newImage, x, y, r, g, b)
	for x in range(leftSize, leftSize+barWidth): # draw the middle bar with blended pixels
		for y in range(imgHeight):
			r, g, b = blend(img1,img2,x,y)
			putPixel(newImage,x,y,r,g,b)
	rightSize = int(leftSize+barWidth) # define where the right side begins
	for x in range(rightSize, imgWidth): # draw the right side from pixels from img2
		for y in range(imgHeight):
			r, g, b = getPixel(img2, x, y)
			putPixel(newImage,x,y,r,g,b)

	return newImage

main()
