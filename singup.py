from tkinter import *
from tkinter import messagebox
import os

def login_window():
	singup.destroy()
	os.system("python3 main.py")


def passwordcheck():
	if password_box_first.get() == password_box_sec.get():
		if password_box_first.get() != "":
			if email_box.get() != "":
				if username_box.get() != "":
					return True
				else:
					messagebox.showerror("Error","No name")
			else:
				messagebox.showerror("Error","Missing Email")
		else:
			messagebox.showerror("Error","Missing Passwrd")
	else:
		messagebox.showerror("Error","Password Dont match")


def email_validation():
    temp = email_box.get() 
    count=-1
    for i in temp:
        count+=1
        if i=="@":
            if temp[count:len(temp)]=="@gmail.com":
                return True
            else:
                return False
    else:
        return False

def singup_btn():
	if passwordcheck() and email_validation():

		email=email_box.get()
		pasword=password_box_sec.get()
		name=username_box.get()
		print(email,pasword,name)
		user_details=open('userlog.txt','+a')
		path='user_mail/{}'.format(name)
		user_details.writelines(email+","+pasword+","+name+","+path+"\n")
		user_details.close()
		#path='user_mail/{}'.format(name)
		os.mkdir(path)
		print(path)
		
		messagebox.showinfo("Information","singup Completed now go back to login window")
		password_entry_sec.set("")
		password_entry_first.set("")
		username_entry.set("")
		email_entry.set("")
		login_btn=Button(singup, text="Login", command=login_window)
		login_btn.pack()

singup=Tk()

email=Label(singup,text="Email")
email.pack()
email_entry=StringVar()
email_box=Entry(singup,textvariable=email_entry)
email_box.pack()

username=Label(singup, text="Name")
username_entry=StringVar()
username_box=Entry(singup,textvariable=username_entry)
username.pack()
username_box.pack()


password_first=Label(singup, text="Choose Password")
password_entry_first=StringVar()
password_box_first=Entry(singup, textvariable=password_entry_first,show="*")
password_first.pack()
password_box_first.pack()

password_sec=Label(singup, text="Re-enter Password")
password_entry_sec=StringVar()
password_box_sec=Entry(singup, textvariable=password_entry_sec, show="*")
password_sec.pack()
password_box_sec.pack()

singup_button=Button(singup, text="Sing me Up", command=singup_btn)
singup_button.pack()
singup.mainloop()

