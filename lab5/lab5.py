#Create a function that displays a vertical line at a given x coordinate on the gfx hat.
from gfxhat import lcd, backlight
import labLibrary

labLibrary.light()

#heightY = int(input("Give the Y ponit: "))
withX = int(input("Give the X ponit: "))

labLibrary.verticalLine(withX)