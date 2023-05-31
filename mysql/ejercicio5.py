import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="HR",
    password="hr",
    database="hr"
)
print(mydb)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM employees")

myresult = mycursor.fetchone()

print(myresult)