import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  port=3306,
  user="root",
  password="SqlAk@18",
  database="food"
)

print(mydb) # db object..

# creation of cursor 

mycursor = mydb.cursor()

# table creation 
# mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")

# print("created table....")


# show tables 

# mycursor.execute("SHOW TABLES")

# for x in mycursor:
#   print(x)


# insertion 
# sql = "INSERT INTO items (ID, name, price,review) VALUES (%s, %s,%s,%s)"
# val = ("8", "biryani", "210", "excellent")

# mycursor.execute(sql, val)

# mydb.commit()

# print(mycursor.rowcount, "record inserted.")



# FETCH or retrieve the records...

# sql = "SELECT * FROM items where price<=50"

# mycursor.execute(sql)

# for x in mycursor:
#   print(x)


# UPDATE the record..

# sql = "UPDATE items SET price = 250,review='not bad' WHERE ID =8;"
# mycursor.execute(sql)
# mydb.commit()
# print(mycursor.rowcount, "record(s) affected")


sql = "SELECT * FROM items"

mycursor.execute(sql)

for x in mycursor:
  print(x)



