import math
def areaCircle(radius): # This function calculates the area of a circle, it has radius as a paramnter*/
    area = (radius ** 2) * math.pi
    return area


def carMPG(miles, gallons): # this function calculates the MPG, miles and gallons are the parameters
    mpg = miles / gallons
    return mpg

# convert fahrenheit to celsius, input degree in fahrenheit (degreeFah) output: degree celsius
def fahrenCelsius(degreeFah):
    degreeCelsius = ((degreeFah - 32) * 5/9)
    return degreeCelsius

#calculate the distance between two points, it receives the cordenate points and return the distance
def calculateDistanceBetweenPoints(coordx, coordy, coordx1, coordy1):
    a = (coordx1 - coordx)**2
    b = (coordy1-coordy)**2
    distance = math.sqrt(a + b)
    return distance

