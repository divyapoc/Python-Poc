import mysql.connector
mydb = mysql.connector.Connect(host="localhost", user="root", password="project", database="employe")

mycursor = mydb.cursor()

update = "Update records SET salary=25000 where name='Divya'"
mycursor.execute(update)
mydb.commit()