import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="admin",
    password="admin"
)

if db.is_connected():
    print("Bershasil terhubung ke database")
