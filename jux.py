import mysql.connector
import csv

l = []
with open("jux.csv") as file:
    reader = csv.DictReader(file, delimiter=";")

    for i in reader:
        l.append((i["unique_good_name"], i['dealer_good_name']))

mydb = 0

try:
    mydb = mysql.connector.connect(
        host="",
        user="anuarAdmin",
        password="",
        database="voltmandb"
    )
except:
    print("Exception occured!!!")

cursor = mydb.cursor()
query = "UPDATE goods SET unique_good_name=%s WHERE dealer_good_name=%s;"
cursor.executemany(query, l)

mydb.commit()

cursor.close()
mydb.close()