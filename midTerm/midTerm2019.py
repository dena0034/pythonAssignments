#!/usr/bin/env python

import time,click
from gfxhat import touch, lcd, backlight, fonts
from PIL import Image, ImageFont, ImageDraw

f1South =  [
[1,1,1,1,1,1,1,1],
[1,1,1,1,1,1,1,1],
[0,1,1,1,1,1,1,0],
[1,0,1,1,1,1,0,1],
[1,0,0,1,1,0,0,1],
[1,0,0,1,1,0,0,1],
[0,0,0,1,1,0,0,0],
[0,0,0,0,0,0,0,0]
]

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



# create a function drawSquare() that draw a square of sides starting at x, y

def drawSquare(x = 0, y = 0, s = 0):

    verticalSegmetS(x, y, s)
    horizontalSegmentE(x, y, s)
    y1 = verticalSegmetS(x, y, s)
    x1 = horizontalSegmentE(x, y, s)
    verticalSegmetS(x1, y, s)
    horizontalSegmentE(x, y1, s+1)


# create a function drawRectangle() that draw a rectangle of sides w , h starting at x, y


def drawRectangle(x = 0, y = 0, w = 5, h = 5):

    verticalSegmetS(x, y, w)
    horizontalSegmentE(x, y, h)
    y1 = verticalSegmetS(x, y, w)
    x1 = horizontalSegmentE(x, y, h)
    verticalSegmetS(x1, y, w)
    horizontalSegmentE(x, y1, h+1)


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




def rotateObject(obj):
    rotated_image = [[] for x in range(len(obj))]
    for i in range(len(obj)):
        for j in range(len(obj[i])):
          rotated_image[len(obj) - j - 1].append(obj[i][j])
    return rotated_image

def displayObject(obj,x,y):
    i=0
    for line in obj:
        j=0
        for pixel in line:
            lcd.set_pixel(x+j,y+i,pixel)
            j=j+1
        i=i+1
    lcd.show()

def moveObject(obj,x,y,vx,vy):
    eraseObject(obj, x, y)
    x = x + vx
    y = y + vy
    return [x, y]

def eraseObject(obj,x,y):
    xp = x
    for y1 in obj:
        for x2 in y1:
            lenY = len(obj)
            lenX = len(y1)
            # print(x2)
            # xp = x
            lcd.set_pixel(xp, y, 0)
            xp = xp + 1
        y = y + 1
        lcd.set_pixel(xp, y, 0)
        xp = x
    lcd.show()

def clearScreen(lcd):
    lcd.clear()
    lcd.show()

def displayText(text,lcd,x,y):
    lcd.clear()
    width, height = lcd.dimensions()
    image = Image.new('P', (width, height))
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype(fonts.AmaticSCBold, 38)
    w, h = font.getsize(text)
    draw.text((x,y), text, 1, font)
    for x1 in range(x,x+w):
        for y1 in range(y,y+h):
            pixel = image.getpixel((x1, y1))
            lcd.set_pixel(x1, y1, pixel)
    lcd.show()

def eraseText(text,lcd,x,y):
    width, height = lcd.dimensions()
    image = Image.new('P', (width, height))
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype(fonts.AmaticSCBold, 38)
    w, h = font.getsize(text)
    draw.text((x,y), text, 1, font)
    for x1 in range(x,x+w):
        for y1 in range(y,y+h):
            lcd.set_pixel(x1, y1, 0)
    lcd.show()

clearScreen(lcd)
backlight.set_all(0,255,0)
backlight.show()
displayText("Spaceship",lcd,25,1)
time.sleep(2)
eraseText("Spaceship",lcd,25,1)

f1East=rotateObject(f1South)
f1North=rotateObject(f1East)
f1West=rotateObject(f1North)

x=y=0
w=h=8
vx=vy=3
f1=f1South
displayObject(f1,x,y)


studNumb = '040981007'

listStudNumb = list(studNumb)
sum = 0
for i in range(0, len(listStudNumb)):
    value = int(listStudNumb[i])
    sum = sum + value

print(sum)

# write the code to draw a vertical segmente going south at x= 20 y = 20 an h = 16
verticalSegmetS(20, 20, 16)

# write the code to draw a horizontal segmente going eats at x= 20 y = 20 an w = 16
horizontalSegmentE(20, 20, 16)

# write the code to draw a diagonal segmente  at x= 20 y = 20 and w = 16
diagonalSegmentNE(20, 20, 16)

# write the code to draw a square    at x= 35 y = 5 and s = 12
drawSquare(34,5,12)

# write the code to draw a rectangle    at x= 0 y = 0 and w = 5 and h = 7
drawRectangle(0,0,5,7)

quit=False
while not quit:
    c = click.getchar()

    #Erase Everything
    eraseObject(f1,x,y)

    #Move everything
    if c == 'q':
        quit=True

    elif c == '\x1b[A': #up
        f1=f1North
        y=y-vy

    elif c == '\x1b[B': #down
        f1=f1South
        y=y+vy

    elif c == '\x1b[C': #right
        f1=f1East
        x=x+vx

    elif c == '\x1b[D': #left
        f1=f1West
        x=x-vx

    #Collision Detection
    if y < 0 or y+h>63 or x + w>127 or x < 0:
        displayText("Ouch Boom",lcd,5,1)
        time.sleep(0.4)
        eraseText("Ouch Boom",lcd,5,1)
        if y<0:y=0
        if y+h>63:y=63-h
        if x<0:x=0
        if x+w>127:x=127-w

    #Display Everything
    displayObject(f1,x,y)



backlight.set_all(0,0, 0)
backlight.show()
lcd.clear()
lcd.show()


