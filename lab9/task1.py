# Task 1:
# Download File Package Week9Files
# The two text files 2000_BoysNames.txt and 2000_GirlsNames.txt list the popularity of boys names and girls names in 2000.
# The format of the file is simple, one line per entry with the name followed by a space followed by the number of children carrying that name.
# You must write a python program that reads each text file then converts it into a csv format: "name",count then saves the entry in a csv file.
# The output csv file must include the following header as its first line: "First Name","Count"

# open file
# go through the lines
# save in a variable
# change the space into commas
# save in a csv file
# insert in the first line: "First Name" | "Count"

#fBoyOpen = open("2000_BoysNames.txt", "r+")
#fGirlOpen = open("2000_GirlsNames.txt", "r+")
fileName = "2000_GirlsNames.txt"
fileCSV = "2000_GirlsNames.csv"
fileBoys = "2000_BoysNames.txt"
fileCSVBoys = "2000_BoysNames.csv"

def transformTxtCvs(fileName, fileCSV):
    fileCreateCSV = open(fileCSV, "a")
    fileCreateCSV.write("First Name" +","+ "Count""\n")
    fileOpen = open(fileName, "r+")

    for line in fileOpen:
        lineStr = line.split(" ")
        newLine = lineStr[0] + "," + lineStr[1]
        fileCreateCSV.write(newLine)

    fileOpen.close()
    fileCreateCSV.close()
    fileCreateCSV.close()

#transformTxtCvs(fileName, fileCSV)
#transformTxtCvs(fileBoys, fileCSVBoys)

def openCSV(file):
    fileOpen = open(file, "r+")
    newList = []
    for line in fileOpen:
        lineList = line.splitlines()
        newList.append(lineList)
    print(newList)
    fileOpen.close()
# Task 2:
# Write a python program that prompts the user for the name of .csv file then reads and displays each line of the file as a Python list.
# Test your program on the 2 csv files that you generated in Task 1.

file = str(input("Name of the CSV file:"))
openCSV(file)


