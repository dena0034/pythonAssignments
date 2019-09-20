milesDrivenString = input("How many miles were driven? ")
numberGallonsString = input("How many gallona were used? ")


milesDriven = float(milesDrivenString)
numberGallons = float(numberGallonsString)

mpg = milesDriven/numberGallons

print("The car MPG is:" , mpg)