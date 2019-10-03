from gfxhat import lcd, backlight
import labLibrary
import sys

def mainMenu():
    print( )
    print(" _________________Main Menu_________________")
    print("  ||   Select:                           ||\n  ||   1 - change the backlight color    || \n  ||   2 - for a vertical line           ||\n  ||   3 - for a horizontal line         ||\n  ||   4 - create a staicase             ||\n  ||   5 - display randow pixel          ||\n  ||   6 - reset backlight color         ||\n  ||   7 - exit                          ||")
    print(" ___________________________________________")
    option = input()
    
    

    if option == "1":
        lcd.clear()
        lcd.show()
        r = int(input("Give the r: "))
        g = int(input("Give the g: "))
        b = int(input("Give the b: "))
        labLibrary.setLight(r,g,b)  
        mainMenu()
    elif option == "2":
        lcd.clear()
        lcd.show()
        widthX = int(input("Give the X point: "))
        print(widthX)
        labLibrary.verticalLine(widthX)   
        mainMenu()
    elif option == "3":
        lcd.clear()
        lcd.show()
        heightY = int(input("Give the Y ponit: "))
        print(heightY)
        labLibrary.horizontalLine(heightY)
        mainMenu()
    elif option == "4":
        lcd.clear()
        lcd.show()  
        xPoint = int(input("Give the x position (from 0 to 127):"))
        yPoint = int(input("Give the y position (from 0 to 63):"))
        width = int(input("What is the width?: "))
        height = int(input("What is the height?: "))
        stairWay = int(input("Type 1 for left OR 2 for right: "))
        upDown = int(input("Type 1 for up OR 2 for down: "))   
        labLibrary.stairCase(xPoint, yPoint, width, height,stairWay, upDown)  
        mainMenu()
    elif option == "5":
        lcd.clear()
        lcd.show()
        num = float(input("Type the seconds: "))
        labLibrary.randomPixel(num)
        mainMenu()
    elif option == "6":
        lcd.clear()
        lcd.show()
        labLibrary.clearBacklight()
        mainMenu()
    elif option == "7":
        lcd.clear()
        lcd.show()
        sys.exit
    else:
        print("Please choose a valid option!") 
        mainMenu()


mainMenu()