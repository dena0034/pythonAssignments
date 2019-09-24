import math



circleRadiusString =  input("What is the radius?: ")
circleRadius = float(circleRadiusString)
circleArea = math.pi * circleRadius ** 2

print("The area of a circle with ", circleRadius, "radius is: ", circleArea)