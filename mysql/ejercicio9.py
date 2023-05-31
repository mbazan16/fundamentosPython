import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="HR",
    password="hr",
    database="hr"
)
mycursor = mydb.cursor()

sql = "DELETE FROM REGIONS WHERE REGION_ID = %s"
params = (100,)

mycursor.execute(sql, params)

mydb.commit()

print(mycursor.rowcount, 'filas insertadas')


mycursor = mydb.cursor()

sql = "SELECT * FROM REGIONS"

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
  print(x)