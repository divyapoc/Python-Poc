import mysql.connector
mydb = mysql.connector.Connect(host="localhost", user="root", password="project", database="employe")

mycursor = mydb.cursor()
# mycursor.execute("create table records(name varchar(200), salary int(20))")
mycursor.execute("show tables")

for tb in mycursor:
    print(tb)
