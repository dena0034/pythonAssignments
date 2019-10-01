#Create a function that displays a vertical line at a given x coordinate on the gfx hat.
from gfxhat import lcd,backlight
import dena0034Libary

backlight.set_all(107, 109, 173)
backlight.show()

def verticalLine(y,x):
    i = 0
    while(i < 64):
        lcd.set_pixel(x, i, 1)
        i = i+1
    lcd.show()


heightY = int(input("Give the Y ponit: "))
withX = int(input("Give the X ponit: "))

verticalLine(heightY,withX)