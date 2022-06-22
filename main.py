from tkinter import *
from tkinter import messagebox
import os

def check_loginfo():
	user_list=[]
	user_details=open("userlog.txt", "r+")
	a=user_details.readlines()
	for each in a:
		user_list.append(each.split(","))

	for each in user_list:
		if each[0]==name_box.get() and each[1]== pass_box.get():
			global current_user
			current_user=each
			return True
	else:
		return False


def enter(event=None):
	login()

def login():

	if check_loginfo():
		print(current_user)
		usrlogin_details=",".join(current_user)
		print("LOGIN SUCCSUSSFUL")
		fp=open('login.txt','w+')
		fp.write(usrlogin_details)
		fp.close()
		root.destroy() 
		os.system("python3 login_opt.py")
		#messagebox.showinfo("Information","Sucessfully Login")
		
	else:
		no_match=Label(root, text="Password and Email id  dont match")
		no_match.pack()

current_user=[]

root = Tk()
root.title("Login")

name=Label(root,text="Email")
name.pack()
name_entry=StringVar()
name_box=Entry(root,textvariable=name_entry)
name_box.pack()


password=Label(root,text="Password")
password.pack()
pass_entry=StringVar()
pass_box=Entry(root,textvariable=pass_entry,show="*")
pass_box.pack()

bt_login=Button(root,text="LOGIN", command=login)
bt_login.bind('<Return>',enter)
root.bind('<Return>',enter)
bt_login.pack()

root.mainloop()