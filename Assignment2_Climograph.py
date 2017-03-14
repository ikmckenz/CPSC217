# This program graphs temperature, precipitation, or both. All based on user input.
# Relies on the SimpleGraphics library 

from SimpleGraphics import *

userChoice =  str(input("What type of graph do you want? Temperature, Precipitation or Both?: "))

# Draw the base graph
line(100, 50, 100, 500) # main y axis
line(100, 500, 700, 500) # main x axis
for i in range(11): # y axis tick marks
	i = i * 45
	line(95, i+50, 105, i+50)
for i in range(13): # x axis tick marks
	i = i * 50
	line(i+100, 495, i+100, 505)
# Write on all the months
y = 520
setFont("Ariel", "8")
text(125, y, "Jan")
text(175, y, "Feb")
text(225, y, "Mar")
text(275, y, "Apr")
text(325, y, "May")
text(375, y, "Jun")
text(425, y, "Jul")
text(475, y, "Aug")
text(525, y, "Sep")
text(575, y, "Oct")
text(625, y, "Nov")
text(675, y, "Dec")

# If statements for deciding which type of graph to display

# The first if statement is for temperature.
if userChoice == "1" or userChoice == "T" or userChoice == "t" or userChoice == "temperature" or userChoice == "Temperature":
	userChoice = "T"
	# Draw the temperature ticks
	temp = 20
	for i in range(11):
		ii = i * 45
		text(75, ii+50, str(temp - i*4) + " " + u'\u2103')
	# Draw the temperature ellipses and lines
	setFill("red")
	for i in range(12):
		ii = i * 50
		y = 275-temp*11.25
		temp = int(input("Input month " + str(i+1) + " temperature: ")) 
		ellipse(ii+125, 275-temp*11.25, 1, 1)
		if (i>0):
			line(ii+75, y, ii+125, 275-temp*11.25)

# This if statement is for precipitation
elif userChoice == "2" or userChoice == "P" or userChoice == "p" or userChoice == "precipitation" or userChoice =="Precipitation":
	userChoice = "P"
	# Draw the precipitation scale
	prec = 200
	for i in range(11):
		ii = i * 45
		text(70, ii+50, str(prec - i*20) + " mm")

	# Draw the precipitation bars
	setFill("royal blue")
	for i in range(12):
		ii = i * 50
		prec = int(input("Input month " + str(i+1) + " precipitation: "))
		rect(ii+104, 500-prec*2.25, 43, prec*2.25 + 1)

# This if statement is for both
elif userChoice == "3" or userChoice == "B" or userChoice == "b" or userChoice == "both" or userChoice == "Both":
	userChoice = "B"
	# Draw temperature scale
	temp = 20
	for i in range(11):
		ii = i * 45
		text(75, ii+50, str(temp - i*4) + " " + u'\u2103')
	# Draw precipitation ticks and scale
	line(700, 50, 700, 500)
	prec = 200
	for i in range(11):
		ii = i * 45
		text(730, ii+50, str(prec - i*20) + " mm")
	for i in range(11): # y axis tick marks
		i = i * 45
		line(695, i+50, 705, i+50)
	# Draw the precipitation bars
	i = 0
	ii = 0
	setFill("royal blue")
	for i in range(12):
		ii = i * 50
		prec = int(input("Input month " + str(i+1) + " precipitation: "))
		rect(ii+104, 500-prec*2.25, 43, prec*2.25 + 1)
	# Draw the temperature ellipses and lines
	setFill("red")
	for i in range(12):
		ii = i * 50
		y = 275-temp*11.25
		temp = int(input("Input month " + str(i+1) + " temperature: ")) 
		ellipse(ii+125, 275-temp*11.25, 1, 1)
		if (i>0):
			line(ii+75, y, ii+125, 275-temp*11.25)

else:
	print("That's not a valid choice, try again. (Hint: 1,2,3; t,p,b; etc.)")
