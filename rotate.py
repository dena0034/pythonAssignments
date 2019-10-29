f1South =  [
[1,2,3],
[4,5,6],
[7,8,9]]

def rotateObject(obj):
    rotated_image = [[] for x in range(len(obj))]
    print(rotated_image)
    for i in range(len(obj)):
        for j in range(len(obj[i])):
            rotated_image[len(obj) - j - 1].append(obj[i][j])
            print(rotated_image)

    return rotated_image


#print(rotateObject(f1South))


studNumb = '040981007'

listStudNumb = list(studNumb)
sum = 0
for i in range(0, len(listStudNumb)):

    value = int(listStudNumb[i])
    sum = sum + value

print(sum)
#print(type(listStudNumb))
