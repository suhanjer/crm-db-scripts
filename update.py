import pandas as pd
import mysql.connector

file_path = "file.xlsx"

data = pd.read_excel(file_path, sheet_name="distinct")

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



#for index, i in data.iterrows():
#    if pd.isna(i["good_name"]):
#        print(i["good_name"], i["name"])

cursor = mydb.cursor()

for index, i in data.iterrows():
    if pd.isna(i["good_name"]) == False:
        #print(f"UPDATE goods SET unique_good_name='{i['good_name']}' WHERE dealer_good_name='{i['name']}'")
        cursor.execute(f"UPDATE goods SET unique_good_name='{i['good_name']}' WHERE dealer_good_name='{i['name']}'")
        #print(f'UPDATE goods SET unique_good_name="{i["good_name"]}" WHERE dealer_good_name="{i["name"]}"')
        #cursor.execute(f'UPDATE goods SET unique_good_name="{i["good_name"]}" WHERE dealer_good_name="{i["name"]}"')

mydb.commit()
mydb.disconnect()
