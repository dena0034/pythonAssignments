
import gfxhat

def verticalLine(x):
    i = 0
    while(i < 64):
        lcd.set_pixel(x, i, 1)
        i = i+1
    lcd.show()
