
import dena0034Library

milesDriven = float(input("How many miles were driven?: "))
numberGallons = float(input("How many gallons were used?: "))

m = dena0034Library.carMPG(milesDriven, numberGallons)

print("The car MPG is: {}" .format(m))
