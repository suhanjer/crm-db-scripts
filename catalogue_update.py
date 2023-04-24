import pandas as pd
import mysql.connector

file_path = "catalogue.xlsx"

data = pd.read_excel(file_path, sheet_name="data")

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
cursor.execute("")

for index, i in data.iterrows():
    cursor.execute(f"UPDATE car_battery_catalogue SET type='{i['type']}', applicability='{i['applicability']}', size_group='{i['size_group']}', polarity='{i['polarity']}',voltage='{i['voltage']}',capacity='{i['capacity']}',startup='{i['startup']}',terminals='{i['terminals']}',hold='{i['hold']}',manufacturer='{i['manufacturer']}',country='{i['country']}',brand='{i['brand']}' WHERE name='{i['name']}';")

mydb.commit()

cursor.close()
mydb.close()