from gfxhat import lcd,  fonts
from click import getchar
import labLibrary1

labLibrary1.setLight(141, 120, 30)
#
f1 = [
[1,1,1,1,1,1,1,1],
[1,1,1,1,1,1,1,1],
[0,1,1,1,1,1,1,0],
[1,0,1,1,1,1,0,1],
[1,0,0,1,1,0,0,1],
[1,0,0,1,1,0,0,1],
[0,0,0,1,1,0,0,0],
[0,0,0,0,0,0,0,0]
]

pm = [[0,0,0,1,1,1,1,1,0,0,0],
[0,0,1,1,1,1,1,1,1,0,0],
[0,1,1,1,1,1,1,1,1,1,0],
[1,1,1,1,1,1,1,1,0,0,0],
[1,1,1,1,1,1,1,0,0,0,0],
[1,1,1,1,1,1,0,0,0,0,0],
[1,1,1,1,1,1,0,0,0,0,0],
[1,1,1,1,1,1,1,0,0,0,0],
[1,1,1,1,1,1,1,1,0,0,0],
[0,1,1,1,1,1,1,1,1,1,0],
[0,0,1,1,1,1,1,1,1,0,0],
[0,0,0,1,1,1,1,1,0,0,0]
]

#print(len(pm))

labLibrary1.clearScreen(lcd)

x = 20
y = 20


def displayObject(obj, x, y):
    lcd.clear()
    xp = x
    for y1 in obj:
        #print(y1)
        for x2 in y1:
            lenY = len(obj)
            lenX = len(y1)
            #print(x2)
            #xp = x
            if x2 == 1:
                pixel = 1
            else:
                pixel = 0
            lcd.set_pixel(xp, y, pixel)
            xp = xp + 1
        y = y + 1
        lcd.set_pixel(xp, y, pixel)
        xp = x

    # print("hello")
    lcd.show()
    print(lenX)
    print(lenY)



displayObject(pm , 20, 20)






