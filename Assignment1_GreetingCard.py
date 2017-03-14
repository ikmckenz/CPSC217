# This is my first ever computer program. Pretty neat.
# This program creates a Valentines day card based off user input.
# It relies on the SimpleGraphics library

# First get the input for the location and content of the message
x = int(input("Set the X value for the location of your message (default 550): ") or "550")
y = int(input("Set the Y value for the location of your message (default 300): ") or "300")
message = str(input("Write your message here (default I Love You): ") or "I Love You!")

from SimpleGraphics import *

# set background color
background("dark red")

# draw rectangle which forms the foreground
setFill("light pink")
rect(50,50,699,499)

# set style and text for title
setFont("Ariel", "24", "italic")
text(400, 100, "Happy Valentines Day")

# use a line to split the card in two
line(400, 130, 400, 510)

# display a circle and heart on the left of the card
setOutline("white")
setFill("white")
ellipse(125, 150, 200, 300)
setOutline("deep pink")
setFill("deep pink")
ellipse(150, 225, 75, 75)
ellipse(225, 225, 75, 75)
pieSlice(87, 269, 275, 175, 60, 60)

# display message on right of the card
text(x, y, message)
