import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="HR",
    password="hr",
    database="hr"
)
mycursor = mydb.cursor()

sql = "INSERT INTO REGIONS (REGION_ID,REGION_NAME) VALUES (%s,%s)"
params = (100, 'La Mia')

mycursor.execute(sql, params)

mydb.commit()

print( mycursor.rowcount, 'filas insertadas')


mycursor = mydb.cursor()

sql = "SELECT * FROM REGIONS"

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
  print(x)