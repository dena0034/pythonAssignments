# set
# cannot change items in set but can add items in
import flask
thisSet = {"apple", "banana", "cherry"}

print("banana" in thisSet)

# add
thisSet.add("orange")

print(thisSet)

#update add a list inside the set

thisSet.update(["orange", "mango", "grapes"])

#len returns lenth

#remove removes an item
thisSet.remove("orange")


#set constructor (creates a set)
thisset = set(("apple", "grapes", "cherry"))
print(thisset)


class gfxObject:
    def __init__(self, x = 0,y=0,vx=1,vy=1,img):
        self.y = y
        self.x = x
        self.vy = vy
        self.vx = vx
        self.img = img

    # def moveObject(self):




pacMan = gfxObject(x,y,vx,vy,img)

pacMan.moveObject





Flask / MVC
Model <=> database
View <=> Html
Controler <=>

Works separeted, which one has a very specific task

install wtforms





















