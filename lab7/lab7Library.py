from gfxhat import lcd, backlight

def setLight(r,g,b):
    backlight.set_all(r, g, b)
    backlight.show()

def displayObject(obj, x, y):
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
    lcd.show()
    return x, y

def eraseObject(obj,x=0,y=0):
    xp = x
    for y1 in obj:
        # print(y1)
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

def moveObject(obj,x=0,y=0,vx=0,vy=0):
    eraseObject(obj, x, y)
    x = x + vx
    y = y + vy
    return [x, y]


def checkCollision(obj, x=0, y=0, vx=0, vy=0, Sx=127, Sy=63):
    lenthX = len(obj[0])
    lenthY = len(obj)
    totalX = lenthX + x + vx
    totalY = lenthY + y + vy
    if y <= 0 or totalY > Sy: # verify if y reached the left or right wall
        #print(totalX, totalY)
        vy = -vy
        y = y + vy
    if x <= 0 or totalX > Sx: #verify of the x reached the left or right wall
        #print(totalX, totalY)
        vx = -vx
        x = x + vx
    return [vx, vy, x, y]
