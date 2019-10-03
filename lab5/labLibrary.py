
from gfxhat import lcd,backlight
from time import sleep
from random import randint


def setLight(r,g,b):
    backlight.set_all(r, g, b)
    backlight.show()


def verticalLine(x):
    lcd.clear()
    lcd.show()
    i = 0
    while(i < 64):
        lcd.set_pixel(x, i, 1)
        i = i+1
    lcd.show()

def horizontalLine(y):
    lcd.clear()
    lcd.show()
    i = 0
    while(i < 64):
        lcd.set_pixel(i, y, 1)
        i = i+1
    lcd.show()


def clearBacklight():
    backlight.set_all(0,0,0)
    backlight.show()

def stairCase(xPoint, yPoint, width, height, rightLeft, upDown):
    lcd.clear()
    lcd.show()

    while xPoint < 128 and xPoint >= 0 and yPoint < 64 and yPoint >= 0:
        w = 1
    h = 1
    while(w < width):
        lcd.set_pixel(xPoint, yPoint, 1)
        if(rightLeft == 1):
            xPoint = xPoint - 1
        elif(rightLeft ==2):
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
   
   
def randomPixel(num):
    
    count = 0
    while count <=  num:
        x = randint(0, 128)
        y = randint(0, 64)
        lcd.set_pixel(x, y, 1)
        lcd.show()
        count += 1
    sleep(2) 
        