#from gfxhat import lcd, backlight
#import labLibrary
import sys

def mainMenu():
    print( )
    print("------------ Main Menu -------------------")
    print( )

    option = input(" Choose:\n 1 to draw a vertical line\n 2 to draw a horizontal line\n 3 to create a staicase\n 4 to display randow pixels\n 5 to reset backlight color\n 6 to exit\n")

    if option == "1":
        #lcd.clear()
        #lcd.show()
        withX = int(input("Give the X point: "))
        print(withX)
        #labLibrary.verticalLine(withX)   
        mainMenu()
    elif option == "2":
        #lcd.clear()
        #lcd.show()
        heightY = int(input("Give the Y ponit: "))
        print(heightY)
        #labLibrary.horizontalLine(heightY)
        mainMenu()
    elif option == "3":
        #lcd.clear()
        #lcd.show()       
        print("Something")
        mainMenu()
    elif option == "4":
        #lcd.clear()
        #lcd.show()
        print("Something")
        mainMenu()
    elif option == "5":
        #lcd.clear()
        #lcd.show()
        #labLibrary.clearBacklight()
        print("Something")
        mainMenu()
    elif option == "6":
        #lcd.clear()
        #lcd.show()
         sys.exit
    else:
        print("Please type a valid option") 
        mainMenu()


mainMenu()