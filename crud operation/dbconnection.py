import mysql.connector

mydb=mysql.connector.Connect(host="localhost", user="root", password="project")
print(mydb)
if(mydb):
    print("connection success")
else:
    print("connection failure")
