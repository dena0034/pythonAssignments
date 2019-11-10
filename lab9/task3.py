# Task 3:
# Write a function generateDictionary that reads the file font3.txt and generate a dictionary where the key is the character
# and the value is the 8*8 bit list representation of the character.
# Write a program that reads a character from the user and displays the associate character on the gfxHat at the coordinates of your choice.
# Characters not present in the dictionary are ignored and a message is displayed on the computer screen.
from gfxhat import lcd, fonts, backlight


def setLight(r, g, b):
    backlight.set_all(r, g, b)
    backlight.show()


setLight(200, 100, 90)


# create dictionary from file
def generateDictionary():
    try:
        fileRead = open("font3.txt", "r")
        fileDict = {}
        for line in fileRead:
            value, key = line.strip().split(',')
            fileDict[key.strip()] = value.strip()
        fileRead.close()
        return fileDict
    except:
        print("File not found")


# get the users input, search the character in the dictionary passed
# break the value  each two character and save in a list of str
# and return the hexadecimal value in a list, without the '0x'
def getValueInList(character, dictionary):

    value = dictionary.get(character)
    n = 2
    valueTwo = []
    for i in range(2, len(value), n):
        valueTwo.append(value[i:i + n])
    return valueTwo


# receive the list value in hexadecimal, go through the list and convert to binary str
# add zeros to the left to complete eight bits, transform each str into a list and append to a bigger list 8x8
def listStrToBinary(valueList):
    listBinary = []
    for x in range(0, len(valueList)):
        line = valueList[x]
        strBinary = bin(int(line, 16))
        strBinary = strBinary[2:].zfill(8)
        listBinary.append(list(strBinary))
    return listBinary


# cast the list of str to a list of int, return the new int list
def castListStrToInt(listBinary):
    for i in range(len(listBinary)):
        for j in range(len(listBinary[i])):
            listBinary[i][j] = int(listBinary[i][j])

    # print(listBinary)
    return listBinary


# display the obj into the gfxhat
def displayObject(obj, x, y):
    lcd.clear()
    xp = x
    for y1 in obj:
        # print(y1)
        for x2 in y1:
            lenY = len(obj)
            lenX = len(y1)
            # print(x2)
            # xp = x
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


characterUser = str(input("Please, type a character: "))

try:
    dictionary = generateDictionary()
    obj = getValueInList(characterUser, dictionary)
    list = listStrToBinary(obj)
    listBinary2 = castListStrToInt(list)
    displayObject(listBinary2, 40, 30)
except:
        print("Character not present in the dictionary")