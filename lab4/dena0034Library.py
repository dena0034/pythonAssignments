import math
def areaCircle(radius): # This function calculates the area of a circle, it has radius as a paramnter*/
    area = (radius ** 2) * math.pi
    return area


def carMPG(miles, gallons): # this function calculates the MPG, miles and gallons are the parameters
    mpg = miles / gallons
    return mpg


def fahrenCelcius(degreeFah):
    degreeCelcius = ((degreeFah - 32) * 5/9)
    return degreeCelcius


def calculateDistanceBetweenPoints(coordx, coordy, coordx1, coordy1):
    a = (coordx1 - coordx)**2
    b = (coordy1-coordy)**2
    distance = math.sqrt(a + b)
    return distance

