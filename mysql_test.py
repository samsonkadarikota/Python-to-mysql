import mysql.connector

conn = mysql.connector.connect(host = 'localhost',user='root',password='1478963')

if conn.is_connected():
    print('connection established')
print(conn)
print(conn.is_connected())
