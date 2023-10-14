import tkinter as tk
from tkinter import messagebox
from tkinter import *
import json
import subprocess
import sending_data_script as sds

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

def jsondumpbutton():
    messagebox.showinfo("Information",'Trying to Log in with entered specs')
    config()
    #call()
    subprocess.run(['python','sending_data_script.py'])
    #sds.gen_data
    if sds.gen_data()!=1:
        messagebox.showinfo("Database",'All good')
    else:
        messagebox.showerror("Database",'Not Good')

def Auselatestjsonbutton():
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
root.title("LogIn")
root.geometry("400x500")

#login
Loglabel=tk.Label(root,text="Login")
Loglabel.pack()

Logentry = tk.Entry(root)
Logentry.pack()

#password
Passlabel=tk.Label(root,text="Password")
Passlabel.pack()

Passentry = tk.Entry(root)
Passentry.pack()

#host
Hostlabel=tk.Label(root,text="Host")
Hostlabel.pack()

Hostentry = tk.Entry(root)
Hostentry.pack()

#database
dblabel=tk.Label(root,text="DataBase")
dblabel.pack()

dbentry = tk.Entry(root)
dbentry.pack()


dumpJsonbutton = tk.Button(root, text="Log In", command=jsondumpbutton)
dumpJsonbutton.pack()

uselatestjsonbutton = tk.Button(root, text="Use Latest Config", command=Auselatestjsonbutton)
uselatestjsonbutton.pack()


root.mainloop()