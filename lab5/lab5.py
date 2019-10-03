#Create a function that displays a vertical line at a given x coordinate on the gfx hat.
from gfxhat import lcd, backlight
import labLibrary

labLibrary.light()

widthX = int(input("Give the X point: "))
labLibrary.verticalLine(widthX)      


heightY = int(input("Give the Y ponit: "))

labLibrary.horizontalLine(heightY)


xPoint = int(input("Give the x position (from 0 to 127):"))
yPoint = int(input("Give the y position (from 0 to 63):"))
width = int(input("What is the width?: "))
height = int(input("What is the height?: "))
stairWay = int(input("Type 1 for left OR 2 for right: "))
upDown = int(input("Type 1 for up OR 2 for down: "))

while xPoint < 128 and xPoint >= 0 and yPoint < 64 and yPoint >= 0:
    w = 1
    h = 1
    while(w < width):
        lcd.set_pixel(xPoint, yPoint, 1)
        if(stairWay == 1):
            xPoint = xPoint - 1
        elif(stairWay ==2):
            xPoint = xPoint + 1
    
        if xPoint > 127 and xPoint < 0 and yPoint > 63 and yPoint < 0:
            lcd.show()
            break
        w = w +1
   
    while(h < height):
        lcd.set_pixel(xPoint, yPoint, 1)
        if(upDown == 1):
            yPoint = yPoint - 1
        elif(upDown == 2):
            yPoint = yPoint + 1
    
        if xPoint > 127 and xPoint < 0 and yPoint > 63 and yPoint < 0:
            lcd.show()
            break
        h = h +1

lcd.show()
   
   



