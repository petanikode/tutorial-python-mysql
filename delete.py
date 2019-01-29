import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user="admin",
  passwd="admin",
  database="toko_mainan"
)

cursor = db.cursor()
sql = "DELETE FROM customers WHERE customer_id=%s"
val = (1, )
cursor.execute(sql, val)

db.commit()

print("{} data dihapus".format(cursor.rowcount))