#this program convert fahrenheit to celcius and celsius to fahrenheit

typeConvertion = input("Type 1 to convert celsius to Fahrenheit or 2 to convert Fahrenheit to Celsius: ")

if typeConvertion == 1:
    degreeFah = float(input("What is the temperature in Fahrenheit?: "))
    degreeCelsius = ( (degreeFah - 32) * 5/9)
    print("The degree in Celsius is: ", degreeCelcius)
else:
    degreeCelsius = float(input("What is the temperature in Celsius?: "))
    degreeFah = ( 32 + (degreeCelsius * 5/9))
    print("The temperature in Fahrenheit is: ", degreeFah)