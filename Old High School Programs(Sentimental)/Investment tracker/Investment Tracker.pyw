'''
By Ronald Colyar 1/26/18
'''
#MODULES
import tkinter as tk
import sqlite3
from tkinter import *
from tkinter import ttk
#files
conn = sqlite3.connect('login.db')
c = conn.cursor()
conn2 = sqlite3.connect('investments.db')
c2 = conn2.cursor()


class SignUp:
	def __init__(self , master):
		self.master = master
		master.config(background = 'black')
		master.title(string = 'Sign Up window')
		master.iconbitmap('phantex.ico')
		#placing of the window
		w = 270
		h = 380
		ws = master.winfo_screenwidth()
		hs = master.winfo_screenheight()
		x = (ws/2) - (w/2)
		y =  (hs/2) - (h/2)
		master.geometry('%dx%d+%d+%d' % (w,h,x , y))
		#creation of labels
		self.signup_label = tk.Label(master, text = 'Sign Up', fg = 'white' , bg = 'black', font = 'times 15 bold').grid(row = 0 , column = 0 ,columnspan = 2, sticky = 'we')
		self.firstname_label =tk.Label(master, text = 'First ( Atleast 3)', fg = 'white' , bg = 'black').grid(row = 1 , column = 0 , sticky = 'we')
		self.lastname_label =tk.Label(master, text = 'Last (Atleast 3)', fg = 'white' , bg = 'black').grid(row = 1 , column = 1 , sticky = 'we')
		self.username_label = tk.Label(master, text = 'Username  (Atleast 6)', fg = 'white' , bg = 'black').grid(row = 3 , column = 0 ,columnspan = 2, sticky = 'we')
		self.password_label = tk.Label(master, text= 'Password  (Atleast 6)' , fg = 'white' , bg = 'black').grid(row = 5 , column = 0 ,columnspan = 2,sticky = 'we')
		self.acctype_label  = tk.Label(master, text= 'Type of Investment account' , fg = 'white' , bg = 'black').grid(row = 7 , column = 0 ,columnspan = 2, sticky = 'we')
		self.titletype_label  = tk.Label(master, text= 'Title' , fg = 'white' , bg = 'black').grid(row = 9 , column = 0 ,columnspan = 2, sticky = 'we')
		self.buisness_label  = tk.Label(master, text= 'Buisness Name (Optional)' , fg = 'white' , bg = 'black').grid(row = 11 , column = 0 ,columnspan = 2, sticky = 'we')
		self.verification_label = tk.Label(master, text= 'Status:' , fg = 'white' , bg = 'black')
		self.verification_label.grid(row = 15 , column = 0 ,columnspan = 3, sticky = 'we')
		#creation of entrys
		self.firstname = ttk.Entry(master)
		self.firstname.grid(row = 2 , column = 0 , sticky = 'we')
		self.lastname = ttk.Entry(master)
		self.lastname.grid(row = 2 , column = 1 , sticky = 'we', padx = 5, pady = 5)
		self.username = ttk.Entry(master)
		self.username.grid(row = 4 , column = 0 ,columnspan = 2, sticky = 'we')
		self.password = ttk.Entry(master, show ='*')
		self.password.grid(row = 6 , column = 0 ,columnspan = 2, sticky = 'we')
		self.buisness = ttk.Entry(master)
		self.buisness.grid(row = 12 , column = 0 ,columnspan = 2, sticky = 'we')
		#creation of option menus
		self.options = ['Select' ,'Stock' ,'multiple', 'Real Estate' , 'Bonds' , 'intellectual property' , 'Buisness','Other']
		self.accvar = StringVar()
		self.accounttype = ttk.OptionMenu(master , self.accvar, *self.options ).grid(row = 8, column = 0 ,columnspan = 2, sticky = 'we')
		self.options2 = ['Dr.' , 'Mr.' , 'Mrs.' , 'Ms.' , 'Sir.','Miss.']
		self.titlevar = StringVar()
		self.titletype = ttk.OptionMenu(master , self.titlevar, *self.options2 ).grid(row = 10, column = 0 ,columnspan = 2, sticky = 'we')
		#creation of buttons
		submit = tk.Button(master, text = 'Submit', fg = 'white' , bg = 'black' , command = submit_mthd).grid(row = 13 , column = 0 , sticky = 'we' , columnspan =3)
		backwardsbutton = tk.Button(master , text = 'Back <--', fg = 'white' , bg = 'black' , command = signupback_mthd).grid(row = 14 , column = 0 , sticky = 'we' , columnspan =3)

	def change(self , verification):
		self.verification_label.configure(text =verification )

def submit_mthd():
	#storing the values in variables makes it a bit easier to read
	firstname_data = signup_obj.firstname.get()
	lastname_data = signup_obj.lastname.get()
	username_data = signup_obj.username.get()
	password_data = signup_obj.password.get()
	buisness_data = signup_obj.buisness.get()
	accounttype_data = signup_obj.accvar.get()
	title_data = signup_obj.titlevar.get()
	c.execute("SELECT * FROM login WHERE user =:user", {'user' : str(username_data)})
	contents = c.fetchall()

	#checking the length of the entrys
	if len(str(firstname_data))  < 3 or len(str(lastname_data)) < 3 or len(str(username_data)) < 6 or len(str(password_data))<6:
		signup_obj.change('Status: Please Fill Out Full Application')

	elif len(contents) > 0:
		signup_obj.change( 'Username Already Taken on this system')

	#saving all information and updating the status
	else:	
		c.execute("INSERT INTO login VALUES (?, ? , ?, ?, ? , ? , ?)", ((firstname_data) , (lastname_data) , (username_data) ,(password_data) ,  (accounttype_data) ,  (title_data) ,  (buisness_data)))
		signup_obj.change('Status : Account created')
		conn.commit()

		
class SignInGui:
	def __init__(self , master):
		self.master = master
		master.title(string = 'Sign In')
		master.resizable(width = False , height = False)
		master.iconbitmap('phantex.ico')
		#aesthetics
		master.config(background='black')
		photo = PhotoImage(file = 'Phantex.png')
		Phantex_image = tk.Label(master, image = photo, fg = 'white' , bg = 'black')
		Phantex_image.image = photo
		Phantex_image.grid(row =7  , column = 0 , sticky = 'we' )
		#placing of the window
		w = 370
		h = 250
		ws = master.winfo_screenwidth()
		hs = master.winfo_screenheight()
		x = (ws/2) - (w/2)
		y =  (hs/2) - (h/2)
		master.geometry('%dx%d+%d+%d' % (w,h,x , y))
		#creation of entrys
		self.username = ttk.Entry(master)
		self.username.grid(row = 2 , column = 0 , sticky = 'we')
		self.password = ttk.Entry(master, show ='*')
		self.password.grid(row = 4 , column = 0 , sticky = 'we')	
		#creation of labels
		self.title = tk.Label(master, text = 'Investment Tracker',font = 'times 14 bold', fg = 'white' , bg = 'black' ).grid(row = 0 , column = 0 , sticky ='we' )
		self.username_label = tk.Label(master, text = 'Username', fg = 'white' , bg = 'black').grid(row = 1 , column = 0 , sticky = 'we')
		self.password_label = tk.Label(master, text= 'Password' , fg = 'white' , bg = 'black').grid(row = 3 , column = 0 , sticky = 'we')
		self.status_label =  tk.Label(master, text= None , fg = 'Red' , bg = 'black' , font = 'times 9')
		self.status_label.grid(row = 8 , column = 0 , sticky = 'we')
		#creation of buttons
		self.login_button = tk.Button(master, text = 'Sign In', fg = 'white' , bg = 'black' , command = signin_check).grid(row = 5, column = 0 , sticky = 'we')
		self.signup_button= tk.Button(master, text= 'Create An Account', command = signup_mthd, fg = 'white' , bg = 'black').grid(row = 6 , column = 0 , sticky = 'we')
		#making the mainwindow scale when resized
		master.grid_rowconfigure(0,weight=1)
		master.grid_rowconfigure(1,weight=1)
		master.grid_rowconfigure(2,weight=1)
		master.grid_rowconfigure(3,weight=1)
		master.grid_rowconfigure(4,weight=1)
		master.grid_rowconfigure(5,weight=1)
		master.grid_rowconfigure(6,weight=1)
		master.grid_rowconfigure(7,weight=1)
		master.grid_rowconfigure(8,weight=1)
		master.grid_columnconfigure(0,weight=1)

class mainpagegui:

	def __init__(self , master):
		self.master = master
		master.resizable(width = False, height = True)
		master.iconbitmap('phantex.ico')
		w = 420
		h = 490
		ws = master.winfo_screenwidth()
		hs = master.winfo_screenheight()
		x = (ws/2) - (w/2)
		y =  (hs/2) - (h/2)
		master.geometry('%dx%d+%d+%d' % (w,h,x , y))
		#creation of the menus
		self.titlebaroptions = tk.Menu(master)
		self.savemenu = tk.Menu(master,tearoff = False)
		self.savemenu.add_command(label = 'Save Investment' , command = save_inv_mthd)
		self.advancedmenu = tk.Menu(master,tearoff = False)
		self.advancedmenu.add_command(label = 'Advanced Investment Information' , command = advanced_mthd)
		self.removemenu = tk.Menu(master,tearoff = False)
		self.removemenu.add_command(label = 'Remove Investment Record' , command = remove_inv_mthd)
		#adding menus to the main bar
		self.titlebaroptions.add_cascade(label = 'Save Investment' , menu = self.savemenu)
		self.titlebaroptions.add_cascade(label = 'Advanced Statistics' , menu = self.advancedmenu)
		self.titlebaroptions.add_cascade(label = 'Remove Investment' , menu = self.removemenu)
		self.master.config(menu = self.titlebaroptions)

		#creation of labels
		self.Greeting = tk.Label(master ,text = usergreeting() ,bg= 'black', fg ='white').grid(row = 0 , column = 0 , sticky = W , columnspan = 2)
		self.price_label = tk.Label(master ,text = 'Price',bg= 'black', fg ='white').grid(row = 1 , column = 0 , sticky = 'we')
		self.date_label = tk.Label(master, text = 'Date',bg= 'black', fg ='white').grid(row = 1 , column = 1 , sticky = 'we')
		self.estimatedprofit_label = tk.Label(master ,text = 'Estimated Profit',bg= 'black', fg ='white').grid(row = 3 , column = 0 , sticky = 'we')
		self.aos_label = tk.Label(master, text = 'Amount of shares(Stock Investment)',bg= 'black', fg ='white').grid(row = 3 , column = 1 , sticky = 'we')
		self.seller_label = tk.Label(master, text = 'seller',bg= 'black', fg ='white').grid(row = 5 , column = 0 , sticky = 'we')
		self.buyer_label = tk.Label(master ,text = 'Buyer',bg= 'black', fg ='white').grid(row = 5 , column = 1 , sticky = 'we')
		self.pps_label = tk.Label(master ,text = 'Price per share(Stock Investment)',bg= 'black', fg ='white').grid(row = 7 , column = 0 , sticky = 'we')
		self.Lop_label = tk.Label(master ,text = 'Location of property(RealEstate)',bg= 'black', fg ='white').grid(row = 7 , column = 1 , sticky = 'we')
		self.dpr_label = tk.Label(master ,text = 'Dividend Pay Rate(Stock)',bg= 'black', fg ='white').grid(row = 9 , column = 0 , sticky = 'we')
		self.PI_label = tk.Label(master ,text = 'Passive Income',bg= 'black', fg ='white').grid(row = 9 , column = 1 , sticky = 'we')
		self.ID_label = tk.Label(master, text = 'ID Number(very important)',bg= 'black', fg ='white').grid(row = 11 , column = 0 , sticky = 'we')
		self.intERROR = tk.Message(master, text = None ,bg= 'black', fg ='red')
		self.intERROR.grid(row = 13, column = 0 , sticky = 'we')
		self.lenerror = tk.Label(master, text = None ,bg= 'black', fg ='red')
		self.lenerror.grid(row = 14, column = 0 , sticky = 'we')
		#creation of entrys
		self.price_entry = ttk.Entry(master)
		self.price_entry.grid(row = 2 , column = 0 , sticky = 'we')
		self.date_entry = ttk.Entry(master)
		self.date_entry.grid(row = 2 , column = 1 , sticky = 'we')
		self.estimatedprofit_entry = ttk.Entry(master)
		self.estimatedprofit_entry.grid(row = 4 , column =0 , sticky = 'we')
		self.aos_entry = ttk.Entry(master)
		self.aos_entry.grid(row = 4 , column = 1 , sticky = 'we')
		self.seller_entry = ttk.Entry(master)
		self.seller_entry.grid(row = 6 , column = 0 , sticky = 'we')
		self.buyer_entry = ttk.Entry(master)
		self.buyer_entry.grid(row = 6 , column = 1 , sticky = 'we')
		self.pps_entry = ttk.Entry(master)
		self.pps_entry.grid(row = 8 , column = 0 , sticky = 'we')
		self.Lop_entry = ttk.Entry(master)
		self.Lop_entry.grid(row = 8 , column = 1 , sticky = 'we')
		self.dpr_entry = ttk.Entry(master)
		self.dpr_entry.grid(row = 10 , column = 0 , sticky = 'we')
		self.PI_entry = ttk.Entry(master)
		self.PI_entry.grid(row = 10 , column = 1 , sticky = 'we')
		self.ID_entry = ttk.Entry(master)
		self.ID_entry.grid(row = 12 , column = 0 ,columnspan = 2,  sticky = 'we')
		#back button
		self.backbutton = tk.Button(master, command = mainpageback_mthd , text = 'Back<--',bg= 'black', fg ='white').grid(row = 15 , column = 0 , columnspan = 2, sticky = 'we')

		master.grid_rowconfigure(0,weight=1)
		master.grid_rowconfigure(1,weight=1)
		master.grid_rowconfigure(2,weight=1)
		master.grid_rowconfigure(3,weight=1)
		master.grid_rowconfigure(4,weight=1)
		master.grid_rowconfigure(5,weight=1)
		master.grid_rowconfigure(6,weight=1)
		master.grid_rowconfigure(7,weight=1)
		master.grid_rowconfigure(8,weight=1)
		master.grid_columnconfigure(0,weight=1)

	def interrorchange(self , message):
		self.intERROR.configure(text =message )

	def lenerrorchange(self , message):
		self.lenerror.configure(text =message )

def usergreeting():
	
	global username_information
	title = c.execute("SELECT title FROM login WHERE user = :user" , {'user' : str(username_information)}) 
	#grabbing the title of user and commiting it to 'total'
	for row in title:
		total= 'Welcome ' + str(row[0])

	last = c.execute("SELECT last FROM login WHERE user = :user" , {'user' : str(username_information)}) 
	#grabbing the last name and adding it after the user's title 
	for row2 in last:
		total += row2[0]
		

	account_type = c.execute("SELECT accounttype FROM login WHERE user = :user" , {'user' : str(username_information)}) 
	for row3 in account_type:
		total+= '   Account Type:' + str(row3[0])
		return total

def main():
	global sign_in_window , obj
	sign_in_window = tk.Tk()
	sign_in_window.iconbitmap('phantex.ico')
	obj = SignInGui(sign_in_window)
	sign_in_window.mainloop()
def mainpage(bool):
	global sign_in_window, mainpage_gui , mainpage_window
	if bool == True:
		sign_in_window.destroy()
		
		mainpage_window =tk.Tk() 
		mainpage_window.config(background = 'black')
		mainpage_window.title(string = 'Main Page')
		mainpage_gui = mainpagegui(mainpage_window)
	
def signin_check():
	global obj , username_information
	username_information = obj.username.get()
	password_information = obj.password.get()
	#checking the database to see if the info matches
	c.execute("SELECT * FROM login WHERE password =? and user = ?" ,  (str(password_information) , str(username_information)))
	if c.fetchall() == []:
		result=  False
		#update the user on the status of login
		obj.status_label.config(text = 'Incorrect password or username')
	else:
		result = True
	mainpage(result)
def signup_mthd():
	global  sign_up_window , sign_in_window ,signup_obj
	sign_in_window.destroy()
	sign_up_window = tk.Tk()
	sign_up_window.iconbitmap('phantex.ico')
	signup_obj = SignUp(sign_up_window )
def signupback_mthd():
	sign_up_window.destroy()
	main()
def mainpageback_mthd():
	global mainpage_window
	mainpage_window.destroy()
	main()
def combiner(category):
	global username_information
	placeholder = 0
	total = 0 
	#searching for the price of the user
	info = c2.execute("SELECT "+ category+ " FROM investments WHERE user = :user" , {'user' : str(username_information)})
	for row in info:
		#turning the row(tuple) , into a int
		placeholder = int(row[0])
		#adding all the results together
		total += placeholder
	return total


def advance_search_mthd(category , value):
	global username_information , information_box, search_box
	#removing whats currently in the box
	information_box.delete(0 , 'end')
	#searching for all investments
	results = c2.execute("SELECT * FROM investments WHERE "+str(category)+" = ?" , (value,))

	number_of_row = 0

	for row in results:
		number_of_row += 1

		information_box.insert(0 ,'#' + str(number_of_row)+ str(row) )
def single_search():
	advance_search_mthd('investment_id_number' , search_box.get())
def all_search():
	advance_search_mthd('user' , str(username_information))
def advanced_mthd():
	global information_box , search_box
	advanced_window = tk.Tk()
	advanced_window.iconbitmap('phantex.ico')
	advanced_window.config(background = 'black')
	advanced_window.title(string = 'Advance Statistics')
	

	#placement of window
	w = 1040
	h = 290
	ws = advanced_window.winfo_screenwidth()
	hs = advanced_window.winfo_screenheight()
	x = (ws/2) - (w/2)
	y =  (hs/2) - (h/2)
	advanced_window.geometry('%dx%d+%d+%d' % (w,h,x , y))
	#creation of labels 
	overal_price_invested = tk.Label(advanced_window , text = str('Total Spent On investments :' + ' ' +str(combiner('price'))),bg= 'black', fg ='white').grid(row = 2 , column = 0  , sticky= 'we')
	estimated_profit =tk.Label(advanced_window , text = str('Total Estimated_profit :' + ' ' +str(combiner('estimated_profit'))),bg= 'black', fg ='white').grid(row = 3 , column = 0  , sticky= 'we')
	amount_of_shares =tk.Label(advanced_window , text = str('Total Shares :' + ' ' +str(combiner('amount_of_shares'))),bg= 'black', fg ='white').grid(row = 4 , column = 0  , sticky= 'we')
	price_per_share =tk.Label(advanced_window , text = str('Total Estimated_profit :' + ' ' +str(combiner('price_per_share'))),bg= 'black', fg ='white').grid(row = 5 , column = 0  , sticky= 'we')
	passive_income =tk.Label(advanced_window , text = str('Combined Passive income :' + ' ' +str(combiner('passive_income'))),bg= 'black', fg ='white').grid(row = 6 , column = 0  , sticky= 'we')
	search_label = tk.Label(advanced_window , text = 'Search for investment using id number',bg= 'black', fg ='white').grid(row = 8 , column = 0 , sticky = 'we')
	header = tk.Label(advanced_window , text = 'Price , Date, Estimated profit , amount of shares , seller, buyer , price per share , user , location of property , dividend price rate , passive_income , id number',bg= 'black', fg ='white').grid(row = 0 , column = 1 , sticky = 'we')
	#creation of listbox

	information_box = tk.Listbox(advanced_window , width = 50)
	information_box.grid(row = 1 ,column =  1 ,rowspan = 6, sticky = 'we')
	#creation of Entrys
	search_box = ttk.Entry(advanced_window)
	search_box.grid(row = 9 , column = 0 , sticky = 'we')
	#creation of buttons
	submit_button = tk.Button(advanced_window , text = 'Submit' ,bg= 'black', fg ='white', command = single_search)
	submit_button.grid(row = 11 , column = 0 , sticky = 'we')	
	all_info_button = tk.Button(advanced_window,text = 'Import all investments',bg= 'black', fg ='white', command =all_search )
	all_info_button.grid(row = 12 ,column = 0 , sticky = 'we')
	

def remove_algo():
	global username_information , main_entry , error_msg
	#checking to see if the investment is in the database
	c2.execute("""SELECT * FROM investments WHERE user= ? and investment_id_number = ?""" ,  (username_information, main_entry.get()))
	if c2.fetchall() == []:
		#updating the user on the status of the request if there is no investment there
		error_msg.config(text = 'No Investment Under That ID number')
	else:
		error_msg.config(text = 'Investment Deleted')
		#updating the user on the status of the request if there is an investment there
		c2.execute("""DELETE  FROM investments WHERE user = ? and investment_id_number = ? """ , (username_information , main_entry.get()))
		conn2.commit()
def remove_inv_mthd():
	global main_entry ,error_msg
	#configuring window
	remove_window = tk.Tk()
	remove_window.title(string = 'Remove Window')
	remove_window.iconbitmap('phantex.ico')
	remove_window.config(background = 'black')
	w = 380
	h = 220
	ws = remove_window.winfo_screenwidth()
	hs = remove_window.winfo_screenheight()
	x = (ws/2) - (w/2)
	y =  (hs/2) - (h/2)
	remove_window.geometry('%dx%d+%d+%d' % (w,h,x , y))


	#widgets
	main_message = tk.Message(remove_window , text = 'Welcome To the Delete section , where you can remove an investment, Keep in mind once you remove an investment it cannot be recovered' , font = 'times 13 bold ',bg= 'black', fg ='white')
	main_message.grid(row = 1, column = 0 , sticky = 'we')
	note_message = tk.Label(remove_window, text= 'NOTE : ENTER THE Investment ID , CHECK HELP FOR MORE INFO',bg= 'black', fg ='white')
	note_message.grid(row = 2, column = 0 , sticky = 'we')
	main_entry = ttk.Entry(remove_window)
	main_entry.grid(row= 3  , column = 0 , sticky = 'we')
	delete_button = tk.Button(remove_window ,text='Remove**' ,  command = remove_algo,bg= 'black', fg ='white')
	delete_button.grid(row = 4 , column = 0  , sticky = 'we')
	error_msg = tk.Label(remove_window , text = None ,bg= 'black', fg ='red' )
	error_msg.grid(row = 5 , column = 0 , sticky = 'we')


def intcheck(value):
	try:
		int(value)
		return True
	except ValueError:
		return False


def save_inv_mthd():
	global username_information , mainpage_gui
	#storing the values in variables makes it a bit easier to read
	price_data = mainpage_gui.price_entry.get()
	date_data = mainpage_gui.date_entry.get()
	estimated_profit_data = mainpage_gui.estimatedprofit_entry.get()
	amount_of_shares_data = mainpage_gui.aos_entry.get()
	seller_data = mainpage_gui.seller_entry.get()
	buyer_data = mainpage_gui.buyer_entry.get()
	price_per_share_data = mainpage_gui.pps_entry.get()
	location_of_propery_data =mainpage_gui.Lop_entry.get()
	dividend_price_rate_data = mainpage_gui.dpr_entry.get()
	passive_income_data = mainpage_gui.PI_entry.get()
	investment_id_data = mainpage_gui.ID_entry.get()
	intcheck_results = True
	len_results = True

	if len(price_data) < 3 or len(date_data)<3 or len(passive_income_data) <3 or len(seller_data)<3 or len(buyer_data)<3 or len(estimated_profit_data) <3 :
		len_results = False
	if intcheck(price_data) == False or intcheck(estimated_profit_data) == False or intcheck(amount_of_shares_data)== False or intcheck(price_per_share_data)== False or intcheck(passive_income_data) == False:
		intcheck_results = False

	if intcheck_results == False:
		mainpage_gui.interrorchange('ERROR #1 :Price,estimated profit,amount of shares,price per share,passive income must be all numbers no letters')
	if len_results == False:
		mainpage_gui.lenerrorchange('ERROR #2 :Must have 3 or more characters in all boxes')

	else: 
		mainpage_gui.interrorchange (None)
		mainpage_gui.lenerrorchange('SUCCESSFULLY SAVED')
		c2.execute("INSERT INTO investments VALUES (?, ? , ?, ?, ? , ? , ?, ? , ? , ? , ? , ?)", 
		((price_data) , (date_data) , (estimated_profit_data) ,(amount_of_shares_data) ,  (seller_data) ,  (buyer_data) ,  (price_per_share_data) ,
		(username_information), (location_of_propery_data) , (dividend_price_rate_data)  , (passive_income_data), (investment_id_data) ))
		conn2.commit()


if __name__ == "__main__":
	main()

conn.close()
conn2.close()