#Create a function that displays a vertical line at a given x coordinate on the gfx hat.
from gfxhat import lcd, backlight
import labLibrary

labLibrary.light()

withX = int(input("Give the X point: "))
labLibrary.verticalLine(withX)      


heightY = int(input("Give the Y ponit: "))

labLibrary.horizontalLine(heightY)

xPoint = int(input("Give the x position (from 0 to 127):"))
yPoint = int(input("Give the y position (from 0 to 63):"))
width = int(input("What is the width?: "))
height = int(input("What is the height?: "))

for xPoint in range(0, 128):
    lcd.set_pixel(xPoint, yPoint, 1)
    xPoint = xPoint + width
    for yPoint in range(0,64):
        lcd.set_pixel(xPoint, yPoint, 1)
        yPoint = yPoint + height


lcd.show()