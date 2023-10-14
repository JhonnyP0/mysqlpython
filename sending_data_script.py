import mysql.connector as SQLCN
import random
import datetime as dt
import json
from tkinter import messagebox


with open ("config.json", "r") as config_file:
    config_data=json.load(config_file)

db= SQLCN.connect(**config_data)
db_cursor=db.cursor()

def push_data(temp,acc_time,acc_date):
    try:
        sql_msg="INSERT INTO table_of_temp (value, time, date) VALUES (%s,%s,%s)"
        msg_val=(temp,acc_time,acc_date)
        db_cursor.execute(sql_msg,msg_val)
        db.commit()
        #print("push succeeded")

    except SQLCN.connector.Error as err:
        print(f"Error: {err}")
        #print("not succeeded")
        return 1
    else:
        print("succeeded")
    finally:
        #print("exited")
        db_cursor.close()
        db.close()


def gen_data():
    date=dt.datetime.now()
    temp=random.randint(-30,50)
    acc_time=date.strftime("%H"+":"+"%M")
    acc_date=date.strftime(date.strftime("%d")+"."+date.strftime("%m")+"."+date.strftime("%Y"))
    push_data(temp,acc_time,acc_date)