from tkinter import *
import os

def show_data(data):
	pass


def list_mails():
	f=open("login.txt","r")
	login_info=f.readline().split(",")
	path=login_info[3].rstrip("\n")
	global new
	new=path
	f = []
	for (dirpath, dirnames, filenames) in os.walk(path):
		f.extend(filenames)
		break
	txtchng_list=[]
	for each in f:
		txtchng_list.append(each.rstrip(".txt"))
	listbox_update(txtchng_list)
		
def listbox_update(data):
	mail_listbox.delete(0, 'end') 
	data = sorted(data, key=str.lower)
	for item in data:
		mail_listbox.insert('end', item)

def view_mail():
	new_path=new+"/"+mail_listbox.get(mail_listbox.curselection())+".txt"
	print(new_path)
	file=open(new_path,"r+")
	global data
	data =file.read()#.replace('\n', '')
	data_in.set(data)

def backtolog():
	readmails.destroy()
	os.system("python3 login_opt.py")

readmails=Tk()
mail_listbox=Listbox(readmails)
mail_listbox.bind('<<ListboxSelect>>') 
mail_listbox.pack()
list_mails()
view_button=Button(readmails, text="View", command=view_mail)
view_button.pack()
back_btn=Button(readmails, text="go Back", command=backtolog)
back_btn.pack()
data_in=StringVar()
view_mail_txt=Label(readmails,text="",textvariable=data_in)
#view_mail_txt.insert()
view_mail_txt.pack()

readmails.mainloop()




