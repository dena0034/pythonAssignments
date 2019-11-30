from flask import Flask, render_template
import sqlite3
import base64
import webbrowser


app = Flask(__name__)

# Using Pycharm,  create a flask application with three routes:
# Default page displays a simple menu:
# Option 1 of the menu is used to display the Google map of the city of a specific student.
#
# Option 2 of the menu displays a table of all students, country and cities.
# the findStudent page displays a form where the user can select a student and the page then opens a Google map of the city from where the student is from.
#
# The displayAll page displays a simple table of all students, cities and countries stored in the database.
# Each student name is also a hyperlink that opens in a new window a Google map of the city from where the student is from.
# Bonus: The table headings sort the table according to the heading.

class Database:
    def createConnectionSql(self, db_file):
        con = None
        cursor = None
        try:
            con = sqlite3.connect(db_file)
            cursor = con.cursor()
        except:
            print("Database not found")
            exit()
        return con, cursor

    def showData(self, cursor):
        query = "SELECT * from lab10 order by student"
        result = cursor.execute(query)
        studentList = []
        for r in result.fetchall():
            studentList.append(r)
        # print(studentList)
        return studentList


def main():
    studentData = Database()
    con, cursor = studentData.createConnectionSql("week10.db")
    data = list(studentData.showData(cursor))
    # print(type(data))
    listData = [list(r) for r in data]
    for r in listData:
        link = r[1]
        url = base64.urlsafe_b64decode(link).decode('utf-8')
        r[1] = url
    #     print(r[1])
    # print(listData)
    return listData



@app.route('/')
def index():
    data = main()
    # print("oi")
    return render_template('index.html', data=data)


@app.route('/displayAll')
def displayAll():
    data = main()
    # print("oi")
    return render_template('displayAll.html', data=data)
# @app.route('/<num>')
# def index(num):
#     data =  main()
#     for r in data:
#         link = r[1]
#         idLink = r[0]
#         if idLink == num:
#             url = base64.urlsafe_b64decode(link).decode('utf-8')
#             break
#
#     return url

@app.route('/menu')
def menu():
    data = main()
    # print("oi")
    return render_template('menu.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
