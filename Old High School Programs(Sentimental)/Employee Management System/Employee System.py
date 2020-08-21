'''
Employee System 

By Ronald Colyar : 1/2/2018


'''
#our modules for this project
import csv
from tkinter import *
from tkinter import ttk



#main class gui
class employee_gui :
	
	def __init__(self , master):
		
		self.master = master

		master.resizable(height = False , width = False)
		#the lists for days months and years
		self.dayoptions = ['1', '2' , '3' , '4' , '5' , '6' , '7' , '8' , '9', '10' , '11' , '12' , '13' , '14' , '15' , '16' , '17' , '18' , '19', '20' , '21' , '22' , '23' , '24' , '25' , '26' , '27' , '28' , '29' , '30' , '31']
		self.monthoptions = ['1' , '2' , '3' , '4' , '5' , '6' , '7' , '8' , '9' , '10' , '11' , '12']
		self.years_unsplit='2029 - 2028 - 2027 - 2026 - 2025 - 2024 - 2023 - 2022 - 2021 -2020 - 2019 - 2018 - 2017 - 2016 - 2015 - 2014 - 2013 - 2012 - 2011 -2010 - 2009 - 2008 - 2007 - 2006 - 2005 - 2004 - 2003 - 2002 - 2001 -2000 - 1999 - 1998 - 1997 - 1996 - 1995 - 1994 - 1993 - 1992 - 1991 - 1990 - 1989 - 1988 - 1987 - 1986 - 1985 - 1984 - 1983 - 1982 - 1981 -1980 - 1979 - 1978 - 1977 - 1976 - 1975 - 1974 - 1973 - 1972 - 1971 -1970 - 1969 - 1968 - 1967 - 1966 - 1965 - 1964 - 1963 - 1962 - 1961 -1960 - 1959 - 1958 - 1957 - 1956 - 1955 - 1954 - 1953 - 1952 - 1951 -1950 - 1949 - 1948 - 1947 - 1946 - 1945 - 1944 - 1943 - 1942 - 1941 -1940 - 1939 - 1938 - 1937 - 1936 - 1935 - 1934 - 1933 - 1932 - 1931 -1930 - 1929 - 1928 - 1927 - 1926 - 1925 - 1924 - 1923 - 1922 - 1921'
		self.yearoptions2 = self.years_unsplit.split('-')


		#creation of the optionmenus with  there variables
		self.dayvar= StringVar()
		self.dropdown_day = ttk.OptionMenu(master,self.dayvar , *self.dayoptions)
		self.monthvar = StringVar()
		self.dropdown_month = ttk.OptionMenu(master, self.monthvar , *self.monthoptions)
		self.yearvar = StringVar()
		self.dropdown_year = ttk.OptionMenu(master , self.yearvar , *self.yearoptions2)

		#placement of optionmenus
		self.dropdown_day.grid(row = 6 , column = 0 , sticky= 'we')
		self.dropdown_month.grid(row = 6 , column = 1 , sticky = 'we',padx=5, pady=5)
		self.dropdown_year.grid(row = 6 ,column = 2 , sticky = 'we')

		#creation of labels
		self.firstname_label = Label(master, text = 'Employee First Name ***' ,bg= 'black', fg ='white')
		self.lastname_label = Label(master, text = 'Employee last Name ***',bg= 'black', fg ='white')
		self.employee_email_label = Label(master, text = 'Employee Email ***',bg= 'black', fg ='white')
		self.DAY_label= Label(master, text = 'Day**',bg= 'black', fg ='white')
		self.month_label= Label(master, text = 'month**',bg= 'black', fg ='white')
		self.year_label = Label(master, text = 'Year**' ,bg= 'black', fg ='white')
		self.Address_label = Label(master ,text = 'Address(optional)*** Example: 110 s. grove street',bg= 'black', fg ='white')
		self.Position_label= Label(master , text= 'Position/Occupation***' , bg= 'black', fg ='white')
		self.salary_label = Label(master , text = 'Employee Salary***',bg= 'black', fg ='white')
		self.employee_id_label = Label(master, text = 'Employee Id **VERY IMPORTANT**',bg= 'black', fg ='white')

		#creation of entrys
		self.first_name_entry = ttk.Entry(master)
		self.last_name_entry = ttk.Entry(master)
		self.employee_email_entry = ttk.Entry(master)
		self.Address_entry = ttk.Entry(master)
		self.Position_entry = ttk.Entry(master)
		self.salary_entry = ttk.Entry(master)
		self.employee_id_entry = ttk.Entry(master)
		
		
		#Placement of label widgets
		self.firstname_label.grid(row = 1 , column = 0 , sticky ='we', padx=5, pady=5)
		self.lastname_label.grid(row = 1 , column = 1 , sticky ='we',padx=5, pady=5)
		self.employee_email_label.grid(row = 3 , column  = 0 , columnspan = 2 , sticky = 'we')
		self.DAY_label.grid(row = 5 , column = 0 , sticky = 'we',padx=5, pady=5)
		self.month_label.grid(row = 5 , column = 1 , sticky = 'we',padx=5, pady=5)
		self.year_label.grid(row = 5 , column = 2, sticky = 'we', padx=5, pady=5)
		self.Address_label.grid(row = 7 , column = 0 ,sticky = 'we',padx=5, pady=5)
		self.Position_label.grid(row = 9 , column = 0 , sticky = 'we',padx=5, pady=5)
		self.salary_label.grid(row = 11 , column = 0 , sticky = 'we',padx=5, pady=5)
		self.employee_id_label.grid(row = 13 , column = 0 , sticky = 'we',padx=5, pady=5)


		#placement of entry widgets
		self.first_name_entry.grid(row = 2 ,column  = 0 , sticky = 'we',padx=5, pady=5 )
		self.last_name_entry.grid(row = 2 ,column  = 1 , sticky = 'we',padx=5, pady=5)
		self.employee_email_entry.grid(row = 4  , column = 0 , columnspan = 3 , sticky = 'we', padx=5, pady=5)
		self.Address_entry.grid(row = 8 , column = 0 , columnspan = 3, sticky = 'we',padx=5, pady=5)
		self.Position_entry.grid(row = 10 , column = 0 ,columnspan = 3, sticky = 'we',padx=5, pady=5)
		self.salary_entry.grid(row = 12 , column = 0 , sticky = 'we',padx=5, pady=5)
		self.employee_id_entry.grid(row = 14 , column = 0 , sticky = 'we' ,padx=5, pady=5 )


		#the main menu bar
		self.titlebaroptions = Menu(master)
		self.filesystem = Menu(master,tearoff=False)
		self.filesystem.add_command(label = 'Display Employee Information'  , command =display_information_window)
		self.savesystem = Menu(master,tearoff=False)
		self.savesystem.add_command(label= 'Save Employee File' , command=save_information_mthd)
		self.deletesystem =Menu(master,tearoff=False)
		self.deletesystem.add_command(label = 'Delete Employee' , command = delete_information_window)
		self.help = Menu(master, tearoff = False)
		self.help.add_command(label= 'Help' , command = help_window)


		#adding the sections  to the main menu bar
		self.titlebaroptions.add_cascade(label = 'Open' , menu = self.filesystem)
		self.titlebaroptions.add_cascade(label = 'Save' , menu = self.savesystem)
		self.titlebaroptions.add_cascade(label = 'Remove Employee' , menu =self.deletesystem)
		self.titlebaroptions.add_cascade(label = 'Help' ,  menu = self.help)
		

		# adding features and aesthetics to our main window 
		master.config(menu = self.titlebaroptions)
		master.iconbitmap('employeeicon.ico')
		master.title(string = 'Phantex Employee Management System')
		master.configure(background = 'black')

		#logos
		self.photo = PhotoImage(file = 'phantexlogo.png')
		self.phantexlogo = Label(master, image = self.photo, bg= 'black', fg ='white')
		self.phantexlogo.image = self.photo
		self.phantexlogo.grid(row = 15 , column = 0 , sticky = 'we')

		self.photo2 = PhotoImage(file = 'phantexlogo.png')
		self.phantexlogo2 = Label(master, image = self.photo, bg= 'black', fg ='white')
		self.phantexlogo2.image = self.photo
		self.phantexlogo2.grid(row = 15 , column = 1 , sticky = 'we')



def delete_information_method():
    #a tkinter entry
    global delete_entry, csv_writer1
    #opening csv in read
    with open('employees.csv' , 'r', newline='') as emp_read:
        #creating our dictreader
        csv_dictreader = csv.DictReader(emp_read)
        fieldnames = csv_dictreader.fieldnames
        contents = [line for line in csv_dictreader]
    #opening csv file in write mode
    with open ('employees.csv' , 'w', newline='') as emp_write:
        #creating our writer
        csv_writer1 = csv.DictWriter(emp_write, fieldnames=fieldnames)
        csv_writer1.writeheader()
        #our loop to check each line inside of our csv file is not equal to what is inside the delete entry
        for line in contents:
            if line['employee id'] != str(delete_entry.get()):
                csv_writer1.writerow(line)

     #grabbing all the employee data and inserting it inside of the listbox
def all_emp_search():
	global information_box
	#deleting data out of the listbox , that was previously there
	information_box.delete(0 , 'end')
	#our read file
	with open ('employees.csv' , 'r') as employee_read_file:
		#inserting all information inside of the csv file into the listbox
		for line in employee_read_file:
			information_box.insert(END , line)
	#grabbing a single employee data and inserting it inside the listbox
def single_emp_search():

	global search_label_entry,information_box
	#deleting data out of the listbox , that was previously there
	information_box.delete(0 , END)
	#our read file
	with open ('employees.csv' , 'r') as employee_read_file:
	
	#searching the contents of the csv file for what is inside of the entry and if matches , insert that line(content) inside of the listbox
		for line in employee_read_file:
			if line.find(str(search_label_entry.get())) > -1:
				information_box.insert(END , line)



def delete_information_window():
	global delete_entry
	delete_frame = Toplevel()

	delete_frame.resizable(height = False , width = False)
	delete_frame.config(background = 'black')
	delete_frame.iconbitmap('employeeicon.ico')
	
	delete_intro_header = Label(delete_frame , text = 'Welcome to the Delete section' , font = 'times 14 bold',bg= 'black', fg ='white')
	delete_intro_header.grid(row  = 2 , column = 0 , sticky = 'we')

	
	delete_entry_header = Message(delete_frame , text = 'Enter in the employee ID , you would like to remove , if you dont recall , you can access the employee information , by going to Mainpage/Open/Display Employee Information, here you can search for an employee name , and all the information including the ID will be present',bg= 'black', fg ='white')
	delete_entry_header.grid(row = 3, column = 0 , sticky= 'we')
	
	delete_note_header = Label(delete_frame , text = 'Note: Once You Delete An Employee There is no recovery , be careful with this process',bg= 'black', fg ='white')
	delete_note_header.grid(row = 4, column = 0 , sticky = 'we')
	
	delete_entry = ttk.Entry(delete_frame )
	delete_entry.grid(row = 5, column = 0 , sticky  = 'we')

	delete_button = Button(delete_frame , text = 'Delete Employee' ,  fg = 'white', bg = 'black',command = delete_information_method)
	delete_button.grid(row = 5 , column = 1, sticky = 'we')


#the information display 

def display_information_window():
	global search_label_entry,information_box
	display_frame = Toplevel()

	display_frame.config(background = 'black')
	display_frame.resizable(height = False , width = False)
	display_frame.iconbitmap('employeeicon.ico')


	intro_message = Label(display_frame, text = 'Welcome to the Display section' , font = 'times 14 bold',bg= 'black', fg ='white')

	search_label = Label(display_frame , text = 'Search for one Employee information',bg= 'black', fg ='white')
	search_label.grid(row = 3 , column = 0 , sticky = 'we')
	
	search_label_entry = ttk.Entry(display_frame)
	search_label_entry.grid(row = 4, column = 0 , sticky = 'we')



	all_information_label = Label(display_frame , text = 'All employee information',bg= 'black', fg ='white')
	all_information_label.grid(row = 3 , column =2 , sticky = 'we')

	information_box = Listbox(display_frame, bd = 0 , width = 70)
	information_box.grid(row  = 6 , column = 0, sticky= 'we')

	all_information_button = Button(display_frame , text = 'All Information',bg = 'black' , fg = 'white',  command = all_emp_search)
	all_information_button.grid(row = 4 , column = 2 , sticky = 'we')

	search_single_emp = Button(display_frame , text  = 'Search Single Employee', command  = single_emp_search,bg = 'black' , fg = 'white' )
	search_single_emp.grid(row = 5 , column = 2 , sticky = 'we')


def help_window():
	help_frame = Toplevel()

	help_frame.configure(background = 'black')
	help_frame.resizable(height = False , width = False)
	help_frame.iconbitmap('employeeicon.ico')


	intro_message = Label(help_frame, text = 'Welcome to the help section' , font = 'times 14 bold',bg = 'black' , fg = 'white')
	intro_message.grid(row = 3  , column = 0 , sticky = 'we')

	mainmessage = Message(help_frame, text = 'The way this program works , is it allows you to  store your employee information , and go back and later access it , using the employee ID feature. The Employee ID makes accessing your information more smooth and manageable , feel free to use this program for your buisnesses and ect. Try to keep the employee IDs different for management purposes',bg = 'black' , fg = 'white')
	mainmessage.grid(row = 4 , column = 0 , sticky  ='we')

	help_frame.iconbitmap('employeeicon.ico')



def save_information_mthd():
	global csvwriter
	#grabbing all the information from our entrys
	first_info = mainmenu_submit.first_name_entry.get()
	last_info = mainmenu_submit.last_name_entry.get()
	email_info = mainmenu_submit.employee_email_entry.get()
	day_info = mainmenu_submit.dayvar.get()
	month_info = mainmenu_submit.monthvar.get()
	year_info = mainmenu_submit.yearvar.get()
	position_info = mainmenu_submit.Position_entry.get()
	employee_salary_info = mainmenu_submit.salary_entry.get()
	employee_id_info = mainmenu_submit.employee_id_entry.get()
	adress_info = mainmenu_submit.Address_entry.get()

	fieldnames_list = ['first name' , 'last name' , 'email' , 'DOB' ,'adress' ,'position' , 'employee salary' , 'employee id'  ]
	#putting our information into a list of strings , 
	whole_information = [str(first_info) , str(last_info) , str(email_info) , str(month_info + '-' +day_info +'-' + year_info ) ,str(adress_info),  str(position_info) , str(employee_salary_info) , str(employee_id_info) ]
	#creating our dictonary , using the fieldnames as the key and the whole information as the value of the dictionary
	my_whole_info_dict = dict(zip(fieldnames_list , whole_information))
	
	#opening our csv file in write mode and adding the data from the entrys
	with open('employees.csv', 'a' ,newline = "") as employee_file:
					csvwriter = csv.DictWriter(employee_file, fieldnames = fieldnames_list , delimiter = ',')
			
		

					csvwriter.writeheader()
					

				
					csvwriter.writerow(my_whole_info_dict)



					

					

				
				


if __name__ == "__main__":
    #main window
    root = Tk()

        
    mainmenu_submit = employee_gui(root)

    
    root.mainloop()


	
