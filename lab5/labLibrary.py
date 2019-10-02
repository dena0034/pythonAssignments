
from gfxhat import lcd,backlight


def light():
    backlight.set_all(107, 109, 173)
    backlight.show()


def verticalLine(x):
    i = 0
    while(i < 64):
        lcd.set_pixel(x, i, 1)
        i = i+1
    lcd.show()

def horizontalLine(y):
    i = 0
    while(i < 64):
        lcd.set_pixel(i, y, 1)
        i = i+1
    lcd.show()


def clearBacklight():
    backlight.set_all(0,0,0)
    backlight.show()
