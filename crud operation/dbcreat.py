import mysql.connector
mydb = mysql.connector.Connect(host="localhost", user="root", password="project")
mycursor = mydb.cursor()

#mycursor.execute("create database student")
mycursor.execute("create database employe")




