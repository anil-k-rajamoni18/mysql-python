import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  port=3306,
  user="root",
  password="SqlAk@18",

)

mycursor = mydb.cursor()

mycursor.execute("SHOW DATABASES")

for x in mycursor:
  print(x)

print(mydb)