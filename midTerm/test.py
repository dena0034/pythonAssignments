#!/usr/bin/env python

import time,click
from gfxhat import touch, lcd, backlight, fonts
from PIL import Image, ImageFont, ImageDraw

lcd.clear()
lcd.show()

# write  code below that creates a vertical line of height h at a given x, y
# going south
#


def verticalSegmetS(x=0, y= 0, h = 5):

    for i in range(0, h):
        lcd.set_pixel(x, y, 1)
        if 0 <= y < 63:
            y = y+1
        else:
            break
    lcd.show()

    return y

#verticalSegmetS(30, 50, 20)

# write  code below that creates a horizontal line of with w at a given x, y
# going east
#


def horizontalSegmentE(x = 0, y = 0, w = 5):

    i = 0
    while i <= w:
        lcd.set_pixel(x, y, 1)
        if 0 <= x < 127:
            x = x+1
        else:
            break
        i = i+1
    lcd.show()
    return x


#horizontalSegmentE(110, 50, 20)


# create a function drawSquare() that draw a square of sides starting at x, y

def drawSquare(x = 0, y = 0, s = 0):

    verticalSegmetS(x, y, s)
    horizontalSegmentE(x, y, s)
    y1 = verticalSegmetS(x, y, s)
    x1 = horizontalSegmentE(x, y, s)
    verticalSegmetS(x1, y, s)
    horizontalSegmentE(x, y1, s+1)

#drawSquare(60,30,10)

# create a function drawRectangle() that draw a rectangle of sides w , h starting at x, y


def drawRectangle(x = 0, y = 0, w = 5, h = 5):

    verticalSegmetS(x, y, w)
    horizontalSegmentE(x, y, h)
    y1 = verticalSegmetS(x, y, w)
    x1 = horizontalSegmentE(x, y, h)
    verticalSegmetS(x1, y, w)
    horizontalSegmentE(x, y1, h+1)

#drawRectangle(60,30,10,5)

# write a function diagonalSegmenteNE() that creates a dioganla line of lengh l given at x, y
# the line goes from x y toward the right of the screen going north of the scren

def diagonalSegmentNE(x = 0, y = 63, l = 5):

    for i in range(0, l):
        lcd.set_pixel(x, y, 1)
        if 0 <= y < 63:
            y = y - 1
        else:
            break
        if 0 <= x < 127:
            x = x +1
        else:
            break

    lcd.show()


#diagonalSegmentNE(10, 50, 10)



#write the code to initialize a str variable stusNumb to your personla student number
# convert the str to a list
# loop though the list to calculate the sum of every digit and print it
studNumb = '040981007'

listStudNumb = list(studNumb)
sum = 0
for i in range(0, len(listStudNumb)):

    value = int(listStudNumb[i])
    sum = sum + value

print(sum)
#print(type(listStudNumb))

#write the code to draw a vertical segmente going south at x= 20 y = 20 an h = 16


verticalSegmetS(20, 20, 16)

#write the code to draw a horizontal segmente going eats at x= 20 y = 20 an w = 16

horizontalSegmentE(20, 20, 16)


#write the code to draw a diagonal segmente  at x= 20 y = 20 and w = 16

diagonalSegmentNE(20, 20, 16)

#write the code to draw a square    at x= 35 y = 5 and s = 12

drawSquare(34,5,12)

#write the code to draw a rectangle    at x= 0 y = 0 and w = 5 and h = 7
drawRectangle(0,0,5,7)