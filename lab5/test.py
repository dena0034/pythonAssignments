import time
from random import randint
from gfxhat import lcd, backlight


#seconds = input("Type the time (seconds): ")
#time = int(time)
while True:
    x = randint(1,128)
    y = randint(0,64)
    lcd.set_pixel(x,y,1)
    lcd.show()
    time.sleep(1)
