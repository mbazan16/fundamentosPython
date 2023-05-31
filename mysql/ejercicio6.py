import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="HR",
    password="hr",
    database="hr"
)
mycursor = mydb.cursor()

"""
sql = "SELECT * FROM employees WHERE job_id = %s"
job_id = ("IT_PROG", )
"""
sql = "SELECT * FROM employees WHERE salary = %s  and job_id =%s"
salary = (4800.0, )
mycursor.execute(sql, salary)

myresult = mycursor.fetchall()

for x in myresult:
  print(x)