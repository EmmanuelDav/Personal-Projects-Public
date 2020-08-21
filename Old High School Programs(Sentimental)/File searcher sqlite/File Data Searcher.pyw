from tkinter import * 
from tkinter import ttk
import tkinter as tk
import sqlite3

class SqliteGui:
	def __init__(self, master):
		self.master = master
		master.title(string = 'Advanced Data Import tool')
		
		#placement
		w = 515
		h = 350
		ws = master.winfo_screenwidth()
		hs = master.winfo_screenheight()
		x = (ws/2) - (w/2)
		y =  (hs/2) - (h/2)
		master.geometry('%dx%d+%d+%d' % (w,h,x , y))

		#creation of widgets
		

		#entrys
		self.pathentry = ttk.Entry(master )
		self.pathentry.grid(row = 1 , column = 0 ,columnspan = 6,   sticky = 'we') 
		self.catentry = ttk.Entry(master )
		self.catentry.grid(row = 2 , column = 1 ,   sticky = 'we') 
		self.tableentry = ttk.Entry(master )
		self.tableentry.grid(row = 2 , column = 4 ,   sticky = 'we') 
		#buttons
		self.submitbutton = ttk.Button(master, text = 'Submit',command = sqlite_file_searcher)
		self.submitbutton.grid(row = 2 , column = 5 , sticky = 'we')
		self.clearbutton = ttk.Button(master, text = 'Clear' , command = sqlclearlistbox).grid(row = 6 , column = 1, sticky = 'we')
		self.backbutton = ttk.Button(master , text = 'Back <--' , command = backwards).grid(row = 7 , column = 1,  sticky = 'we')
		#labels
		self.pathlabel = tk.Label(master, text = 'File Name(sqlite db)' , fg = 'Green').grid(row = 0 , sticky = 'we' , column = 0)
		self.select = tk.Label (master , text = 'SELECT' , fg = 'green').grid(row = 2 , sticky = 'we' , column = 0)
		self.fromlabel = tk.Label(master , text = 'FROM' , fg = 'green').grid(row = 2 , sticky = 'we' , column =3 )
		self.credit = tk.Label(master, text = 'Created By: Ronald Colyar' , fg= 'green').grid(row  = 6 , column = 0 , sticky = 'we' )
		#listbox
		self.listbox = tk.Listbox(master , bd = 0)
		self.listbox.grid(row = 5 , column = 0 , sticky = 'we' , columnspan = 6 , padx = 4 , pady = 4 )
		#message
		self.status = tk.Message(master , text = "Status: Good" , fg = 'Green')
		self.status.grid(row = 7 , column = 0,  sticky = 'we')



		self.titlebar = tk.Menu(master)
		self.help = tk.Menu(master , tearoff = False)
		self.help.add_command(label = 'Help' , command =help_mthd )

		self.titlebar.add_cascade(label = 'Help Options' ,menu = self.help)
		master.config(menu = self.titlebar)

	def statusUpdate(self, msg ,color):
		self.status.config(text = msg)
		self.status.config(fg = color)

class MainPage:
	def __init__(self , master) :
		self.master = master
		master.title(string = 'Data Import tool')
		#configuration of window
		master.grid_rowconfigure(0,weight=1)
		master.grid_rowconfigure(1,weight=1)
		master.grid_rowconfigure(2,weight=1)
		master.grid_rowconfigure(3,weight=1)
		master.grid_columnconfigure(0,weight=1)
		
		#placement
		w = 505
		h = 237
		ws = master.winfo_screenwidth()
		hs = master.winfo_screenheight()
		x = (ws/2) - (w/2)
		y =  (hs/2) - (h/2)
		master.geometry('%dx%d+%d+%d' % (w,h,x , y))
		#creation of widgets
		self.pathlabel = tk.Label(master, text = 'Path To File(.csv, .txt ,default iterable files)' , fg = 'Green').grid(row = 0 , sticky = 'we' , column = 0)
		self.pathentry = ttk.Entry(master )
		self.pathentry.grid(row = 1 , column = 0 , sticky = 'we' , pady = 4 , padx = 4) 
		self.submitbutton = ttk.Button(master, text = 'Submit' , command = defaultfilesearcher)
		self.submitbutton.grid(row = 1 , column = 1 , sticky = 'we')
		self.listbox = tk.Listbox(master , bd = 0)
		self.listbox.grid(row = 2 , column = 0 , sticky = 'we' , columnspan = 2 , padx = 4 , pady = 4 )
		self.credit = tk.Label(master, text = 'Created By: Ronald Colyar' , fg= 'green').grid(row  = 3 , column = 0 , sticky = 'we' )
		self.clearbutton = ttk.Button(master , text = 'Clear' ,command = mainclearlistbox).grid(row = 3 , column = 1 , sticky = 'we')
		self.statusmessage = tk.Label(master, text = 'Status: Good' , fg = 'Green')
		self.statusmessage.grid(row = 0 , column = 1 ,sticky = 'we')

		#menus
		self.titlebar = tk.Menu(master)
		self.advanced = tk.Menu(master , tearoff = False )
		self.advanced.add_command(label = 'Advanced Sqlite' , command = Sqlite_main)
		

		#config
		self.titlebar.add_cascade(label = 'sqlite' , menu = self.advanced)	
		master.config(menu = self.titlebar)
	def statusUpdate(self,msg , color):
		self.statusmessage.config(text =msg , fg = color)

def backwards():
	second_window.withdraw()
	Main_window.deiconify()

def defaultfilesearcher():
	Path = str(Main_Object.pathentry.get())
	#row identifier
	Number_of_row = 0
	#checking if error occurs
	try:
		 open(Path, 'r') 
		 errorcheck = False
	except FileNotFoundError:
		 errorcheck = True


	#if a error doesnt occur
	if errorcheck == False:
		Main_Object.statusUpdate('Status: Good' , 'green')
		with open(Path , 'r') as f :
			contents = f.readlines()

			for i in contents:
				Number_of_row +=1
				#inserting the data
				Main_Object.listbox.insert('end' , '#'+str(Number_of_row)+': '+str(i) )

	else:
		Main_Object.statusUpdate('File Not Found Try again' , 'red')
def sqlite_file_searcher():

	global sqlite_obj
	#db file
	conn = sqlite3.connect(str(sqlite_obj.pathentry.get()))
	c = conn.cursor()
	#checking for an error
	try:
		results = c.execute("SELECT " + str(sqlite_obj.catentry.get()) +" FROM " + str(sqlite_obj.tableentry.get() ))
		checkresults = True
	except sqlite3.OperationalError:
		checkresults = False
	#the handling of the error check
	if checkresults == True:
		for i in results:
			sqlite_obj.listbox.insert(0, i)
			sqlite_obj.statusUpdate("Status: Good" , 'Green')
	else:
		#updating user if error occur
		sqlite_obj.statusUpdate('Status :Error: Please Check Entered Information, View the help tab for assistance' , 'Red')

		
	conn.close()
def help_mthd():
	help_win = tk.Tk()
	message = tk.Message(help_win , text= 'Welcome to the help window , 1. For the formatted database(sqlite) , you are selecting from a certain table inside of the .db file , if the table doesnt exist or the thing you are searching for doesnt exist, you will get an error verify that your information is correct if you are having a problem , 2..db File must be in same folder as the file searcher executable')
	message.grid(row = 0 , column = 0 , sticky = 'we')
def Main():
	global Main_window, Main_Object
	Main_window = tk.Tk()
	Main_Object = MainPage(Main_window)
	Main_window.mainloop()
def Sqlite_main():
	global Main_window, sqlite_obj ,second_window
	Main_window.withdraw()
	second_window = tk.Tk()
	sqlite_obj = SqliteGui(second_window)
def sqlclearlistbox():
	sqlite_obj.listbox.delete(0 , 'end')
def mainclearlistbox():
	Main_Object.listbox.delete(0 , 'end')
if  __name__ == "__main__" :
	Main()