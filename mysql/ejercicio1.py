import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="HR",
    password="hr"
)
print(mydb)

