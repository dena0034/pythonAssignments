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
    if int(id) < 1 or int(id) > 32:
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
        print("Type 1 to update the city, 2 the country, 3 student's name or 4 to update all the data: ")
        update = input()
        if int(update) == 1:
            city = input("Name of the city: ")
            updateCity = "update lab10 set city = ? where id = ? "
            dataCity = (city, idDb)
            cursor.execute(updateCity, dataCity)
            con.commit()
            cursor.close()
            mainMenu()
        elif int(update) == 2:
            country = input("Name of the country: ")
            updateCountry = "update lab10 set  country = ? where id = ? "
            dataCountry = (country, idDb)
            cursor.execute(updateCountry, dataCountry)
            con.commit()
            cursor.close()
            mainMenu()
        elif int(update) == 3:
            student = input("Student's name: ")
            updateStudent = "update lab10 set  student = ? where id = ? "
            dataStudent = (student, idDb)
            cursor.execute(updateStudent, dataStudent)
            con.commit()
            cursor.close()
            mainMenu()
        elif int(update) == 4:
            city = input("Name of the city: ")
            country = input("Name of the country: ")
            student = input("Student's name: ")
            updateQuery = "update lab10 set city = ?, country = ?, student =? where id = ? "
            data = (city, country, student, idDb)
            cursor.execute(updateQuery, data)
            con.commit()
            cursor.close()
            print("The data was updated")
            mainMenu()
        else:
            print("Enter a valid option!")
            update = input()




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
    choice = input()
    if int(choice) == 1:
        showData(cursor)
        mainMenu()
    elif int(choice) == 2:
        id = input("Please type an id between 1 to 32: ")
        getId(id)
        indexDb = getId(id)
        idDb = getLink(cursor, indexDb)
        updateSql(con, cursor, idDb)
        mainMenu()
    elif int(choice) == 3:
        exit()
    else:
        print("Please, select a valid option")
        mainMenu()


mainMenu()