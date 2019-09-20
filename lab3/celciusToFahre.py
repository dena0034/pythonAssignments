#this program convert fahrenheit to celcius and celcius to fahrenheit

typeConvertion = input("Type 1 to convert celcius to Fahrenheit or 2 to convert Fahrenheit to Celcius: ")

if typeConvertion == 1:
    degreeFah = float(input("What is the tempeture in Fahrenheit?: "))
    degreeCelcius = ( (degreeFah - 32) * 5/9)
    print("The degree in Celcius is: ", degreeCelcius)
else:
    degreeCelcius = float(input("What is the tempeture in Celcius?: "))
    degreeFah = ( 32 + (degreeCelcius * 5/9))
    print("The temperature in Fahrenheit is: ", degreeFah)