import sqlite3
import base64
import webbrowser
# mysql.connector.connect(host='localhost',database='mysql',user='root',password='12345678')
con = sqlite3.connect('week10.db')
cursor = con.cursor()
query = "select id, link from lab10"
result = cursor.execute(query)

for r in result.fetchall():
    link = r[1]
    url = base64.urlsafe_b64decode(link)
    # print(url)
    newUrl = str(url)
    url2 = newUrl.strip().split("'")
    # url1 = url2[-2:2]
    print(url2)

# print(type(newUrl))

    #webbrowser.open(url, new=0, autoraise=True)

# connect db
# query
# execute query
# process the result
# open de db
# get the link
# decritpt de link
# update the city, country and student
# base64

