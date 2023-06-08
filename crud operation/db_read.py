import mysql.connector
mydb = mysql.connector.Connect(host="localhost", user="root", password="project", database="employe")

mycursor = mydb.cursor()
mycursor.execute("select * from records")
#to fetch single data
result = mycursor.fetchone()
print("detail:")
for i in result:
    print(i)

#to fetch all detail in db
result = mycursor.fetchall()
print("all data:")
for datas in result:
    print(datas)

mycursor.execute("select name from records")
#to get  all names in db
result = mycursor.fetchall()
print("all data:")
for datas in result:
    print(datas)