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

    newPoints = lab7Library.checkCollision(ball, x, y, vx, vy)
    #print(x, y)
    #print(vx,vy)
    vx = newPoints[0] # recieve the vx updated
    vy = newPoints[1] # recieve the vy updated
    #print(vx, vy)
    position = lab7Library.moveObject(ball, x, y, vx, vy)
    x = position[0] # recieve x new position
    y = position[1] # recieve y new position
    #print(x, y)
    lab7Library.displayObject(ball, x, y)
    lcd.show()
    sleep(.20)
    #print(x, y)
    # print(x1, y1)