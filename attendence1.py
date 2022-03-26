from tkinter import *
from tkinter import ttk
from csv import  DictWriter,reader
import os


def sumbit():
	name= name_var.get()
	date = date_var.get()
	srn = srn_var.get()
	gender = gender_var.get()
	status = status_var.get()
	print(f"{name} {date} {gender} {srn} {status}")

	with open('abc.csv','a') as f:
		logger = DictWriter(f,fieldnames=['Name  ','Date ','Gender ','Srn ','Status '])
		if os.stat('abc.csv').st_size==0:
			logger.writeheader()

		logger.writerow({
			'Name  ':name,
			'Date ':date,
			'Srn ':srn,
			'Gender ':gender,
			'Status ':status,
			})
		Label(register_screen,text="",height='1',width='20').pack()
		Label(register_screen,text="registered successfully!",height='1',width='20',bg='green',fg='white').pack()
		name_entry.delete(0,END)
		srn_entry.delete(0,END)




def register():
	global register_screen
	global name_var
	global date_var
	global srn_var
	global gender_var
	global status_var
	global name_entry
	global date_entry
	global srn_entry
	name_var = StringVar()
	date_var = StringVar()
	srn_var  = StringVar()
	gender_var = StringVar()
	status_var = StringVar()
	register_screen = Toplevel(mainscreen)
	register_screen.geometry("500x400")
	register_screen.title("register")


	name_label=Label(register_screen,text="Name*",height='2',width='20',font='bold')
	name_label.pack()
	name_entry = Entry(register_screen,width='25',textvariable=name_var)
	name_entry.focus()
	name_entry.pack()
	Label(register_screen,text="",height='1',width='20').pack()


	gender_label=Label(register_screen,text="Gender*",width='20',font='bold')
	gender_label.pack()
	gender_combobox = ttk.Combobox(register_screen,width='20',textvariable=gender_var)
	gender_combobox['value']=('Male','Female','Others')
	gender_combobox.current(0)
	gender_combobox.pack()
	Label(register_screen,text="",height='1',width='20').pack()



	srn_label=Label(register_screen,text="Srn*",width='20',font='bold')
	srn_label.pack()
	srn_entry = Entry(register_screen,width='25',textvariable=srn_var)
	srn_entry.focus()
	srn_entry.pack()
	Label(register_screen,text="",height='1',width='20').pack()

	date_label=Label(register_screen,text="Date*",height='1',width='20',font='bold')
	date_label.pack()
	Label(register_screen,text="DD/MM/YY",width='20').pack()
	date_entry = Entry(register_screen,textvariable=date_var).pack()

	Label(register_screen,text="",height='1',width='20').pack()

	Label(register_screen,text="Status",width='20').pack()
	status_combobox = ttk.Combobox(register_screen,height='1',width='20',textvariable=status_var)
	status_combobox['value']=('Present','Absent')
	status_combobox.current(0)
	status_combobox.pack()
	Label(register_screen,text="",height='1',width='20').pack()

	sumbit_btn = Button(register_screen,text='sumbit',bg='blue',fg= 'white',width='15',font='bold',command=sumbit).pack()



def check():
	check_screen = Toplevel(mainscreen)
	check_screen.geometry("400x1200")
	check_screen.title("check Attendance")
	Label(check_screen,text="Attendance ",height='1',width='20',bg='red',fg='white',font='bold').pack()

	with open('abc.csv','r') as f:
		data = reader(f)
		for i in data:
			Label(check_screen,text=i,fg='green').pack()







def mainscreen():
	global mainscreen

	mainscreen = Tk()
	mainscreen.geometry("500x400")
	mainscreen.title("Attendance management system")
	Label(text='Attendance management system',bg='green',fg='white',font='bold').pack()
	Label(text="",height='5',width='20').pack()
	Attendence_btn = Button(text='Register',bg='blue',fg='white',font='bold',width='30',command = register)
	Attendence_btn.pack()

	Label(text="",height='2',width='20').pack()

	check_btn = Button(text='Check Attandence',bg='brown',fg='white',font='bold',width='30',command = check)
	check_btn.pack()






	mainscreen.mainloop()

mainscreen()
