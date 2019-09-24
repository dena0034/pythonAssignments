
import dena0034Library


x = int(input("What is the x of point1?: "))
y = int(input("What is the y of point1?: "))

x1 = int(input("What is the x of point2?: "))
y1 = int(input("What is the y of point2?: "))

dist = dena0034Library.calculateDistanceBetweenPoints(x, y, x1, y1)

print("The distance between point 1: ({},{}) and point 2: ({},{}) is: {}".format(x,y,x1,y1,dist))