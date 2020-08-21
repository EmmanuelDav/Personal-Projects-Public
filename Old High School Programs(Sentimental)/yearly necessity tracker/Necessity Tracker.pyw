'''
Created By Ronald Colyar 2/13/2018
'''
import tkinter as tk
import sqlite3
from tkinter import ttk
from tkinter import *

conn1 = sqlite3.connect('Expense Data.db')
c1 = conn1.cursor()

class MainPageGui:

	def __init__(self, master):
		self.master = master
		master.title(string = 'Expense Tracker')
		master.iconbitmap('Expense.ico')
		master.resizable(width = False , height = False)
		#configuration of window
		master.grid_rowconfigure(0,weight=1)
		master.grid_rowconfigure(1,weight=1)
		master.grid_rowconfigure(2,weight=1)
		master.grid_rowconfigure(3,weight=1)
		master.grid_columnconfigure(0,weight=1)
		#placement
		w = 505
		h = 217
		ws = master.winfo_screenwidth()
		hs = master.winfo_screenheight()
		x = (ws/2) - (w/2)
		y =  (hs/2) - (h/2)
		master.geometry('%dx%d+%d+%d' % (w,h,x , y))
		#creation of widgets
		self.Header = tk.Label(root , text = 'Your Expenses:', fg = 'dark green').grid(row = 0 , column = 0 , sticky = 'we')
		self.headernames = tk.Label(master, text ='Company , Amount Due , Account Number , Amount Paid , Due Date , ID Number , First , Last' , fg = 'dark green').grid(row = 1 , column = 0 , columnspan = 5, sticky = 'we')
		self.credit = tk.Label(master, text = 'Created By : Ronald Colyar', fg = 'dark green').grid(row = 3 ,column = 0 , sticky = 'we')
		self.listbox = tk.Listbox(master , bd = 0 )
		self.listbox.grid(row = 2 , column = 0 ,columnspan = 5,  sticky = 'we')


		self.Add_expense = ttk.Button(master, text = '+', command = Add_expense_win).grid(row = 0 , column = 2 , sticky = 'we')
		self.remove_expense = ttk.Button(master, text = '-'  ,command = remove_window).grid(row = 0 , column = 3, sticky = 'we')
		self.Advanced_expense = ttk.Button(master, text = 'Advanced Statistics', command = advanced_win).grid(row = 0 , column = 4, sticky = 'we')
		self.update = ttk.Button(master , text = 'Update' , command = update_expenses).grid(row = 0 , column = 1 , sticky = 'we')
		
class Add_expense:
	def __init__(self , master):
		self.master = master
		master.title(string = 'Add Expense')
		master.iconbitmap('Expense.ico')
		master.resizable(width = False , height = True)
	

		#creation of labels
		self.first_name_label =tk.Label(master, text = 'First name', fg = 'dark green').grid(row = 1 , column = 0 , sticky = 'we')
		self.last_name_label =tk.Label(master, text = 'Last name', fg = 'dark green').grid(row = 1 , column = 1 , sticky = 'we')
		self.Company_label =tk.Label(master, text = 'Company', fg = 'dark green').grid(row = 3 , column = 0 , sticky = 'we')
		self.amount_due_label =tk.Label(master, text = 'amount due', fg = 'dark green').grid(row = 3 , column = 1 , sticky = 'we')
		self.account_number_label =tk.Label(master, text = 'account number', fg = 'dark green').grid(row = 7 , column = 0 , sticky = 'we')
		self.amount_paid_label =tk.Label(master, text = 'amount paid', fg = 'dark green').grid(row = 9 , column = 0 , sticky = 'we')
		self.due_date_label =tk.Label(master, text = 'due date', fg = 'dark green').grid(row = 9 , column = 1 , sticky = 'we')
		self.IDnum_label =tk.Label(master, text = 'ID number(Special Feature)**REQUIRED', fg = 'dark green').grid(row = 7 , column = 1 , sticky = 'we')
		self.ErrorMessage = tk.Message(master , text = None , fg = 'Red' , font = 'times 12 bold')
		self.ErrorMessage.grid(row  =12 , column = 0 , sticky = 'we' ,columnspan = 2 )
		self.credit = tk.Label(master, text= 'Creator: Ronald Colyar Jr.', fg = 'dark green').grid(row = 13 , column =0 , sticky = 'we')
		#creation of entrys
		self.first_name_entry = ttk.Entry(master)
		self.first_name_entry.grid(row = 2 , column = 0 , sticky = 'we', pady = 5 , padx = 5)
		self.last_name_entry = ttk.Entry(master)
		self.last_name_entry.grid(row = 2 , column = 1 , sticky = 'we', pady = 5 , padx = 5)
		self.Company_entry = ttk.Entry(master)
		self.Company_entry.grid(row = 4 , column = 0 , sticky = 'we', pady = 5 , padx = 5)
		self.amount_due_entry = ttk.Entry(master)
		self.amount_due_entry.grid(row = 4 , column = 1 , sticky = 'we', pady = 5 , padx = 5)
		self.account_number_entry = ttk.Entry(master)
		self.account_number_entry.grid(row = 8 , column = 0 , sticky = 'we', pady = 5 , padx = 5)
		self.amount_paid_entry = ttk.Entry(master)
		self.amount_paid_entry.grid(row = 10 , column = 0 , sticky = 'we', pady = 5 , padx = 5)
		self.due_date_entry = ttk.Entry(master)
		self.due_date_entry.grid(row = 10 , column = 1 , sticky = 'we', pady = 5 , padx = 5)
		self.IDnum_name_entry = ttk.Entry(master)
		self.IDnum_name_entry.grid(row = 8, column = 1 , sticky = 'we', pady = 5 , padx = 5)

		#menu
		self.Save_menu = tk.Menu(master)
		self.Save_menu.add_command(label = 'Save Expense' , command= Save_Info)
		master.config(menu = self.Save_menu)
	def ChangeText(self,Text):
		self.ErrorMessage.config(text = Text)

def total_debt():
	#the paid amount stored in database
	total_paid  = c1.execute("SELECT amount_paid  FROM Expenses")
	#placeholders
	combined_paid = 0
	combined_debt = 0

	for row in total_paid:
		combined_paid += int(row[0])

	#the debt stored in database
	total_owed = c1.execute("SELECT Amount_Due  FROM Expenses")	

	#combining all data from amount due 
	for num in total_owed:
		combined_debt += int(num[0])

	#getting the sum of whats left over to pay 
	results = combined_debt - combined_paid

	#checking to see if we get an negative int witch means no debt
	if results < 0:
		return 0
	#if not negative , return the amount
	else:
		return "{:,}".format(results)

def paid_combiner():
	placeholder = 0
	#searching for the price of the user
	total = c1.execute("SELECT amount_paid  FROM Expenses")
	for row in total:
		
		placeholder += int(row[0])
		
	return "{:,}".format(placeholder)

def category_searcher(category):
	global notfounderror 
	numb_of_row = 0 
	#searching the database for the information provided by user
	c1.execute("SELECT * FROM Expenses WHERE " +str(category) + "= ?" ,  (str(searchentry.get()),))

	#if the results are not there
	if c1.fetchall() == []:
		#updating user error message
		notfounderror.config(text = 'Please Search Again , No ' + str(searchvar.get()) + " '"+ str(searchentry.get())+ "'")
	else:
		#removing previous contents
		resultsbox.delete(0 , 'end')
		#insertion of data
		for row in  c1.execute("SELECT * FROM Expenses WHERE " +str(category) + "= ?" ,  (str(searchentry.get()),)):
			numb_of_row +=1
			resultsbox.insert('end' , str(numb_of_row)+ ':' + str(row))

def advanced_Statistics_algo():
	#checks
	if searchvar.get() == 'account number':
		category_searcher('account_number')
	elif searchvar.get() == 'Due date' :
		category_searcher('due_date')
	elif searchvar.get() == 'first name':
		category_searcher('first_name_on_account')
	elif searchvar.get() ==  'last name':
		category_searcher('second_name_on_account')
	else: 
		category_searcher('Company')

def advanced_win():
	global searchvar , searchentry, notfounderror , resultsbox
	advanced_window = tk.Toplevel()
	advanced_window.title(string = 'Advanced Information')
	advanced_window.iconbitmap('Expense.ico')
	advanced_window.resizable(width = 	True, height = False)

	#placement
	w = 780
	h = 270
	ws = advanced_window.winfo_screenwidth()
	hs = advanced_window.winfo_screenheight()
	x = (ws/2) - (w/2)
	y =  (hs/2) - (h/2)
	advanced_window.geometry('%dx%d+%d+%d' % (w,h,x , y))



	#creation of widgets
	headernames = tk.Label(advanced_window, text ='Company , Amount Due , Account Number , Amount Paid , Due Date , ID Number , First , Last' , fg = 'dark green').grid(row = 0 , column = 0 , sticky = 'we')
	total_paid_label = tk.Label(advanced_window , text = 'Total paid :' + str(paid_combiner())+ '$', font = 'times 15', fg = 'dark green' ).grid(row = 7 , column = 0 , sticky = 'we')
	total_debt_label = tk.Label(advanced_window , text = 'Total Amount left to pay: ' +  str(total_debt())+ '$', font = 'times 15 ', fg = 'dark green').grid(row = 6 , column = 0 , sticky = 'we')

	searchvar = tk.StringVar()
	options = ['Options' ,'account number' , 'Due date' , 'first name' , 'last name' , 'company' ]
	searchtype = ttk.OptionMenu(advanced_window , searchvar, *options ).grid(row = 0, column = 1 , sticky = 'we')

	searchentry = ttk.Entry(advanced_window)
	searchentry.grid(row = 0 , column = 2 , sticky = 'we')

	searchbutton =  ttk.Button(advanced_window , text = 'Search' , command=  advanced_Statistics_algo).grid(row = 0 , column = 3 , sticky = 'we')

	resultsbox = tk.Listbox(advanced_window, bd = 0)
	resultsbox.grid(row  = 4  , column = 0 , sticky = 'we')

	notfounderror = tk.Label(advanced_window , text = None , fg = 'Red')
	notfounderror.grid(row =8 , column = 0, sticky = 'we')

def expense_inserter():
	#all contents of the database
	info = c1.execute("SELECT * FROM Expenses")
	number_of_row = 0

	for row in info:
		number_of_row+=1
		#inserting all rows 
		mainPage.listbox.insert('end' , str(number_of_row)+ ':' + str(row))

def update_expenses():
	global mainPage
	mainPage.listbox.delete(0 , 'end')
	expense_inserter()
def remove_algo():
	info  = c1.execute("""SELECT * FROM Expenses WHERE IDnum= ?""" ,  (mainentry.get(),))
	#checking to see if the Expense is in the database

	if mainentry.get() == 'ALL':
		c1.execute("""DELETE FROM Expenses""")
		conn1.commit()
		error_msg.config(text = 'Everything Deleted')
	
	elif info.fetchall() == []:
		#updating the user on the status of the request if there is no Expense there
		error_msg.config(text = 'No Expense Under That ID number')
	else: 
		#updating the user on the status of the request if there is an Expense there
		
		c1.execute("""DELETE  FROM Expenses WHERE IDnum= ? """ , (mainentry.get(),))
		conn1.commit()
		error_msg.config(text = 'Expense Deleted')

def remove_window():
	global mainentry , error_msg
	Remove_win = tk.Toplevel()
	Remove_win.title(string = 'Remove Expense')
	Remove_win.iconbitmap('Expense.ico')
	Remove_win.resizable(width = False , height = False)

	#placement
	w = 340
	h = 200
	ws = Remove_win.winfo_screenwidth()
	hs = Remove_win.winfo_screenheight()
	x = (ws/2) - (w/2)
	y =  (hs/2) - (h/2)
	Remove_win.geometry('%dx%d+%d+%d' % (w,h,x , y))
	#creation of widgets
	mainmessage = tk.Message(Remove_win , text = 'Welcome to the remove expense section where you can remove expenses. Keep in mind once you remove an expense you cannot recover , enter in the ID number of the expense to remove it, To delete all expenses enter "ALL"' , fg = 'dark green').grid(row = 0 , sticky = 'we ' , column = 0)

	mainentry = ttk.Entry(Remove_win)
	mainentry.grid(row = 1 , column = 0 , sticky = 'we')

	submitbutton = ttk.Button(Remove_win , text = 'CONFIRM', command = remove_algo)
	submitbutton.grid(row = 1 , column = 1,  sticky = 'we')

	error_msg = tk.Label(Remove_win , text = None , fg= 'red' , font = 'times 12 bold')
	error_msg.grid(row = 2 , column = 0 , sticky = 'we')

def intcheck(Data):
	try:
		int(Data)
		return True
	except ValueError:
		return False

def Add_expense_win():
	global addpage 
	add_window = tk.Toplevel()
	#placement
	w = 350
	h = 350
	ws = add_window.winfo_screenwidth()
	hs = add_window.winfo_screenheight()
	x = (ws/2) - (w/2)
	y =  (hs/2) - (h/2)
	add_window.geometry('%dx%d+%d+%d' % (w,h,x , y))

	addpage = Add_expense(add_window)
	add_window.mainloop()

def Save_Info():
	global addpage
	#grabbing all data from user
	firstname_data = addpage.first_name_entry.get()
	last_name_data = addpage.last_name_entry.get()
	company_data = addpage.Company_entry.get()
	amount_due_data = addpage.amount_due_entry.get()
	account_number_data = addpage.account_number_entry.get()
	amount_paid_data = addpage.amount_paid_entry.get()
	due_date_data = addpage.due_date_entry.get()
	IDnumber_data = addpage.IDnum_name_entry.get()

	#checking to see if the following are integers
	if intcheck(amount_paid_data) == False or intcheck(amount_due_data) == False or len(IDnumber_data) < 3 :
		addpage.ChangeText('ERROR:Please Make Sure The following do not contain integers(numbers) : Amount paid , Amount Due , Also Make sure ID number is filled out ')
	#storing data into database
	else:
		c1.execute("INSERT INTO Expenses VALUES (?,?,?,?,?,?,?,?)", 
			((company_data) , (amount_due_data) , (account_number_data) , (amount_paid_data) , (due_date_data) , (IDnumber_data) , (firstname_data) , (last_name_data))
			)
		conn1.commit()
		addpage.ChangeText('Expense Added')

def main():
	global root , mainPage
	root = tk.Tk()
	mainPage = MainPageGui(root)
	expense_inserter()
	root.mainloop()

if __name__ == "__main__" :
	main()
conn1.close()

