from tkinter import *
from tkinter import messagebox
#import string
import os 

def send_mail():
	login.destroy()
	os.system("python3 send_mails.py")

def read_mail():
	login.destroy()
	os.system("python3 read_mails.py")

def logout():
	pass
	os.remove("login.txt")
	login.destroy()
	os.system("python3 main.py")

f=open("login.txt","r")
login_info=f.readline().split(",")
login=Tk()


username=Label(login, text=('LOGED IN AS : {}'.format(login_info[0])))
username.pack()
button_send=Button(login, text="SEND A MAIL", command=send_mail)
button_send.pack()

button_read=Button(login, text="READ THE MAILS", command=read_mail)
button_read.pack()


button_logout=Button(login, text="LOGOUT", command=logout)
button_logout.pack()

messagebox.showinfo("Sucessfull","Login Sucessfull")
login.mainloop()


