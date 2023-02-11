import pandas as pd
import sqlite3

# Data 
conn = sqlite3.connect('Records.db')
c = conn.cursor()

table_data = c.execute("SELECT * FROM Inventory").fetchall()

table_dict = {
    "name": [],
    "avail": [],
    "stocks": [],
    "price": [],
    "size": [],
    "category": [],
}

for index, element in enumerate(table_data):
    table_dict['name'].append(element[1])
    table_dict['avail'].append(element[2])
    table_dict['stocks'].append(element[3])
    table_dict['price'].append(element[4])
    table_dict['size'].append(element[5])
    table_dict['category'].append(element[6])
    
df = pd.DataFrame(table_dict)
print(df)
