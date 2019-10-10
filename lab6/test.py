from click import getchar,echo
from gfxhat import lcd
import sys
import labLibrary1

# The key s is use to start again a new drawing on the hat.
# The key q is used to quit.
# The character code for the arrow keys are the following:
# '\x1b[A' UP arrow key
# '\x1b[B' DOWN arrow key
# '\x1b[C' RIGHT arrow key
# '\x1b[D' LEFT arro key


def etchSketch(x,y):
    while True:
        key = getchar()
        lcd.set_pixel(x, y, 1)
        lcd.show()
        if key == 's': #restart game
            clearScreen(lcd)
        elif key == '\x1b[A': #up arrow
            #print("You tpye the ucd p key")
            y = y -1
            if y == 0:
                y = 63
            lcd.set_pixel(x, y, 1)
            lcd.show()
        elif key == '\x1b[B': # down up
            #print("You tpye the up key")
            y = y + 1
            if y == 63:
                y = 0
            lcd.set_pixel(x, y, 1)
            lcd.show()
        elif key == '\x1b[D': #left arrow
                #print('Left arrow <-')
                x = x - 1
                if x == 0:
                    x = 127
                lcd.set_pixel(x, y, 1)
                lcd.show()
        elif key == '\x1b[C': #right arrow
                #print('Right arrow ->')
                x = x + 1
                if x == 127:
                    x = 0
                lcd.set_pixel(x, y, 1)
                lcd.show()
        elif key == 'q':
            lcd.clear()
            lcd.show()
            exit()
        else:
            print("Press a valid option")
    return x,y



