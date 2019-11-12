import sqlite3
import base64
import webbrowser


def createConnection(db_file):
    try:
        con = sqlite3.connect(db_file)
        cursor = con.cursor()
    except:
        print("Database not found")
    return con, cursor


def getId(id):

    if int(id) < 1 or int(id) > 24:
        print("Please type a valid number!")
        id = input("Please type an id between 1 to 24: ")
    if id == 'q':
        exit()
    else:
        return id


def getLink(cursor, index):
    query = "select id, link from lab10"
    result = cursor.execute(query)
    for r in result.fetchall():
        link = r[1]
        idLink = r[0]
        if idLink == int(index):
            url = base64.urlsafe_b64decode(link).decode('utf-8')
            webbrowser.open(url, new=0, autoraise=True)
            return idLink


def updateSql(con, cursor, idDb):
    query = "SELECT 	Id, City, Country, Student from lab10"
    result = cursor.execute(query)
    for r in result.fetchall():
        # print(r)
        city = r[1]
        country = r[2]
        student = r[3]
        if city is None:
            city = input("Name of the city: ")
        if country is None:
            country = input("Name of the country: ")
        if student is None:
            fName = input("Student's name: ")
        updateQueyy = ("update lab10 set city = ?, country = ?, student =? where id = ? ")
        data = (city, country, fName, idDb)
        cursor.execute(updateQueyy, data)
        con.commit()
        print("The data was updated")
    cursor.close()


def showData(cursor):
    query = "SELECT 	Id, City, Country, Student from lab10"
    result = cursor.execute(query)
    for r in result.fetchall():
        print(r)


def mainMenu():
    db_file = 'week10.db'
    createConnection(db_file)
    con, cursor = createConnection(db_file)
    print("Choose: \n 1 to show the data from the BD \n 2 to update one data \n Press 3 to exit")
    choice = int(input())
    if choice == 1:
        showData(cursor)
        mainMenu()
    elif choice == 2:
        id = input("Please type an id between 1 to 24: ")
        getId(id)
        indexDb = getId(id)
        idDb = getLink(cursor, indexDb)
        updateSql(con, cursor,idDb)
        mainMenu()
    elif choice == 3:
        exit()
    else:
        print("Please, select a valid option")
        mainMenu()


mainMenu()