import tkinter as tk
from tkinter import messagebox
from tkinter import *
import json
import subprocess
import sending_data_script as sds
#import graphFrame

#def call():
#    with open("sending_data_script.py") as f:
#        exec(f.read())

def config():

    host=Hostentry.get()
    user=Logentry.get()
    password=Passentry.get()
    db=dbentry.get()
    
    conf={
    "host":host,
    "user":user,
    "password":password,
    "database":db
    }

    with open("config.json", "w") as config_file:
        json.dump(conf, config_file,indent=4)

def Json_Dump():
    messagebox.showinfo("Information",'Trying to Log in with entered specs')
    config()
    #call()
    subprocess.run(['python','sending_data_script.py'])
    #sds.gen_data
    if sds.gen_data()!=1:
        messagebox.showinfo("Database",'All good')
    else:
        messagebox.showerror("Database",'Not Good')

def Latest_Sett():
    with open ("config.json", "r") as config_file:
        config_data=json.load(config_file)
    
    stf1= config_data["host"]
    stf2=config_data["user"]
    stf3=config_data["password"]
    stf4=config_data["database"]
    w_stf="\n\n"+stf1+"\n"+stf2+"\n"+stf3+"\n"+stf4

    messagebox.showinfo("Information",'Trying to Log in with last specs: '+ w_stf)
    #call()
    subprocess.run(['python','sending_data_script.py'])
    #sds.gen_data
    if sds.gen_data()!=1:
        messagebox.showinfo("Database",'All good')
    else:
        messagebox.showerror("Database",'Not Good')
    

root=tk.Tk()
root.title("Log In")
root.geometry("400x500")

Log_Frame=tk.Frame(root)
Log_Frame.pack()

#login
Loglabel=tk.Label(Log_Frame,text="Login")
Loglabel.pack()

Logentry = tk.Entry(Log_Frame)
Logentry.pack()

#password
Passlabel=tk.Label(Log_Frame,text="Password")
Passlabel.pack()

Passentry = tk.Entry(Log_Frame)
Passentry.pack()

#host
Hostlabel=tk.Label(Log_Frame,text="Host")
Hostlabel.pack()

Hostentry = tk.Entry(Log_Frame)
Hostentry.pack()

#database
dblabel=tk.Label(Log_Frame,text="DataBase")
dblabel.pack()

dbentry = tk.Entry(Log_Frame)
dbentry.pack()


dumpJsonbutton = tk.Button(Log_Frame, text="Log In", command=Json_Dump)
dumpJsonbutton.pack()

uselatestjsonbutton = tk.Button(Log_Frame, text="Use Latest Config", command=Latest_Sett)
uselatestjsonbutton.pack()


root.mainloop()