import mysql.connector as SQLCN
import pandas as pd
import json

with open ("config.json", "r") as config_file:
    config_data=json.load(config_file)

try:

    conn = SQLCN.connect(**config_data)
    cursor = conn.cursor()

    select_query = "SELECT * FROM table_of_temp"
    cursor.execute(select_query)

    data = cursor.fetchall()

    for row in data:
        print(row)

except SQLCN.connector.Error as err:
    print(f"Error: {err}")

finally:
    cursor.close()
    conn.close()