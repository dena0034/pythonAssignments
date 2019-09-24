#this program convert fahrenheit to celcius

import dena0034Library

dF = float(input("What is the temperature in Fahrenheit?: "))

dC = dena0034Library.fahrenCelsius(dF)

print("{} degrees Fahrenheit is {} degrees Celsius".format(dF, dC))