import mysql.connector
mydb = mysql.connector.Connect(host="localhost", user="root", password="project", database="employe")
mycursor = mydb.cursor()
data="Insert into records(name,salary) values(%s, %s)"
records = [("Priya",10000) ,("Divya",15000),("Anitha",20000),("Krishna",25000)]
mycursor.executemany(data,records)
mydb.commit()
