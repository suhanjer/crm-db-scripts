import pandas as pd
import mysql.connector
import datetime

print(datetime.datetime.now())

mydb = 0
try:
    mydb = mysql.connector.connect(
        host = "",
        user = "anuarAdmin",
        password="",
        database="voltmandb"
    )
except Error as e:
    print(e)

cursor = mydb.cursor()

cursor.execute("SELECT DISTINCT warehouse FROM product_rest")
warehouses = cursor.fetchall()
warehouses = [i[0] for i in warehouses]
warehouses.sort()
#print(warehouses)
for i in warehouses:
    #if "елкие" not in i and "анти" not in i and "химия" not in i and "емонт" not in i and "орпоратив" not in i and "едостающ" not in i and "сновной" not in i:
    cursor.execute(f'SELECT SUM(rest) FROM product_rest WHERE warehouse = "{i}"')
    data = cursor.fetchall()
    print(f"{i} = {data[0][0]}")

mydb.commit()
mydb.disconnect()
