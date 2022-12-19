import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  port=3306,
  user="root",
  password="SqlAk@18",
  database="food"

)

mycursor = mydb.cursor()


# DELETE 
sql = "DELETE FROM items WHERE ID =5"


mycursor.execute(sql)

mydb.commit()

sql2 = "SELECT * FROM items"

mycursor.execute(sql2)

for x in mycursor:
  print(x)