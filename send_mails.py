from tkinter import *
from tkinter import messagebox
import os

path=""
def check_mail_avail():
	user_list=[]
	user_details=open("userlog.txt", "r+")
	a=user_details.readlines()
	for each in a:
		user_list.append(each.split(","))

	for each in user_list:
		if each[0]==to_mail.get():
			#global current_user
			#current_user=each
			global path
			path=each[3]
			#print(path)
			return True

def message_read():
	a=T.get("1.0","end-1c")
	file_name=subject_entry.get()
	print("hai")
	check_mail_avail()
	loc=path.rstrip("\n")
	print(loc)
	file=open(loc+"/"+file_name+".txt","w+")
	file.writelines(a)
	file.close
	messagebox.showinfo("Sucessfull","Message send")


def backtolog():
	sen_mail.destroy()
	os.system("python3 login_opt.py")

sen_mail = Tk()

f=open("login.txt","r")
login_info=f.readline().split(",")
username=Label(sen_mail, text=('LOGED IN AS : {}'.format(login_info[0])))
username.pack()
tomail=Label(sen_mail, text="To")
tomail.pack()
to_mail=Entry(sen_mail)
to_mail.pack()
subject=Label(sen_mail,text="Subject")
subject.pack()
subject_entry=Entry(sen_mail)
subject_entry.pack()
T =Text(sen_mail)
T.pack()
#T.insert(END, quote)
singup_button=Button(sen_mail, text="Send", command=message_read)
singup_button.pack()
back_btn=Button(sen_mail, text="go Back", command=backtolog)
back_btn.pack()
sen_mail.mainloop()
