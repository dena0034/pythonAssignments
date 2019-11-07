# Task 3:
# Write a function generateDictionary that reads the file font3.txt and generate a dictionary where the key is the character
# and the value is the 8*8 bit list representation of the character.
# Write a program that reads a character from the user and displays the associate character on the gfxHat at the coordinates of your choice.
# Characters not present in the dictionary are ignored and a message is displayed on the computer screen.

def genetateDictionary():
    fileRead = open("font3.txt", "r")
    fileDict = {}
    for line in fileRead:
        value, key = line.strip().split(',')
        fileDict[key.strip()] = value.strip()
    fileRead.close()
    return fileDict


def displayCharacter(character, dictionary):
    keys = dictionary.keys()
    #print(keys)
    try:
        print(dictionary.get(character))
        value = dictionary.get(character)

        n = 2
        valueTwo = [(value[i:i + n]) for i in range(0, len(value), n)]

        print(valueTwo[2:])
        print(type(valueTwo))
        hex = 16
        for x in range(2, len(valueTwo)):
            line = valueTwo[x]
            #print(line)
            #print(type(line))
            listBinary = bin(int(line, hex))
            print(type(listBinary))
                #.zfill(8)
            print(listBinary)
        #print(dictionary.values() + " here")
        #print(line[2:-4])
    except:
        print("Key not in the dictionary")



character = str(input(("Please, type a character: ")))
#character = "A"
dictionary = genetateDictionary()
displayCharacter(character, dictionary)
