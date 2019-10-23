import lab7Library
from gfxhat import lcd
from time import sleep

ball = [
[0,0,0,1,1,0,0,0],
[0,0,1,1,1,1,0,0],
[0,1,1,1,1,1,1,0],
[0,1,1,1,1,1,1,0],
[0,1,1,1,1,1,1,0],
[0,1,1,1,1,1,1,0],
[0,0,1,1,1,1,0,0],
[0,0,0,1,1,0,0,0]
]

lab7Library.setLight(141, 120, 30)


x = 40
y = 20
vx = 4
vy = 4
while True:
    #lab7Library.displayObject(ball, x, y)
    newPoints = lab7Library.checkCollision(ball, x, y, vx, vy)
    #print(x, y)
    #print(vx,vy)
    vx = newPoints[0]
    vy = newPoints[1]
    print("depois")
    print(vx, vy)
    position = lab7Library.moveObject(ball, x, y, vx, vy)
    x = position[0]
    y = position[1]
    #print(x, y)
    lab7Library.displayObject(ball, x, y)
    lcd.show()
    sleep(.40)
    #print(x, y)
    # print(x1, y1)ç