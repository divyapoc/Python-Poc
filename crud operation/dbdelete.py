import mysql.connector
mydb = mysql.connector.Connect(host="localhost", user="root", password="project", database="employe")
mycursor = mydb.cursor()

delete_data="Delete from records where name='Divya'"
mycursor.execute(delete_data)
mydb.commit()
