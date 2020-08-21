from tkinter import *
from tkinter import ttk 



class Planets:
	#going back to the main window 
	def backtomainmenu(a):
		main_window.withdraw()
		mainmenu.deiconify()
	#the main gui 
	def __init__(self , master, title, mass,moons,distance, temp,record,Radius  , image_planet, width,height):
		self.master = master
		master.title(string= title) 
		master.configure(background = 'black')
		master.iconbitmap('Zairaam-Bumpy-Planets-01-sun.ico')
		#photos
		self.photo = PhotoImage(file = image_planet)
		#creation of Labels
		self.planet_photo = Label(master, image = self.photo, bg = 'black' , fg = 'white')
		self.planet_photo.image = self.photo
		self.Radius = Label(master, text = Radius, bg = 'black' , fg = 'white')
		self.mass = Label(master , text = mass, bg = 'black' , fg = 'white')
		self.moons = Label(master , text = moons, bg = 'black' , fg = 'white' )
		self.orbit_distance = Label(master, text = distance, bg = 'black' , fg = 'white')
		self.surface_temp = Label(master, text = temp, bg = 'black' , fg = 'white')
		self.first_record = Label(master, text = record, bg = 'black' , fg = 'white')
		#placement of Labels
		self.planet_photo.grid(row = 1 , column = 2 , sticky = 'we')
		self.Radius.grid(row = 3 , column = 2 , sticky = 'we')
		self.mass.grid(row = 4, column = 2 , sticky = 'we')
		self.moons.grid(row = 5 , column = 2 , sticky = 'we')
		self.orbit_distance.grid(row = 6 , column =2 , sticky = 'we')
		self.surface_temp.grid(row = 7 , column = 2 , sticky = 'we')
		self.first_record.grid(row = 8 ,column = 2 ,sticky ='we')
		#placing of the window on start up
		w = width
		h = height
		ws = master.winfo_screenwidth()
		hs = master.winfo_screenheight()
		x = (ws/2) - (w/2)
		y =  (hs/2) - (h/2)
		master.geometry('%dx%d+%d+%d' % (w,h,x , y))
		#button
		self.backbutton = Button(master, text = 'Back To Main Menu', bg = 'black' , fg = 'white' ,command = self.backtomainmenu)
		self.backbutton.grid(row = 9 , column = 2 , sticky = 'we')

def mercury_method():
	global main_window
	mainmenu.withdraw()
	main_window = Toplevel()
	mercuryobj = Planets(main_window, 'Mercury , The smallest planet', 'Mass :3.30 x 10^23 kg (5.5% Earth)' , 'Moons : None, ', 'Oribit distance :57,909,227 km (0.39 AU)' , 'Surface Temp :-173 to 427°C' , 'First Record :14th century BC','Radius :1,516 mi', 'mercury.png',220,330)
	main_window.mainloop()
def venus_method():
	global main_window
	mainmenu.withdraw()
	main_window = Toplevel()
	venusobj = Planets(main_window, 'Venus , the morning and Evening star', 'Mass :4.87 x 10^24 kg (81.5% Earth)' , 'Moons : None, ', 'Oribit distance :108,209,475 km (0.73 AU)' , 'Surface Temp :462 °C' , 'First Record :17th century BC','Radius :3,760 mi', 'venus.png',230,390)
def earth_method():
	global main_window
	mainmenu.withdraw()
	main_window = Toplevel()
	earthobj = Planets(main_window, 'Earth , home', 'Mass :5.97 x 10^24 kg' , 'Moons : 1, ', 'Oribit distance :149,598,262 km (1 AU)' , 'Surface Temp :-88 to 58°C' , 'First Record :14th century BC','Radius :3,959 mi', 'earth.png',230,330)
	main_window.mainloop()
def mars_method():
	global main_window
	mainmenu.withdraw()
	main_window = Toplevel()
	marsobj = Planets(main_window, 'Mars , the red planet', 'Mass :6.42 x 10^23 kg (10.7% Earth)' , 'Moons : 2 (Phobos & Deimos), ', 'Oribit distance :57,909,227 km (0.39 AU)' , 'Surface Temp :-153 to 20 °C' , 'First Record :2nd millennium BC','Radius :2,106 mi', 'mars.png',220,380)
def jupiter_method():
	global main_window
	mainmenu.withdraw()
	main_window= Toplevel()
	jupiterobj = Planets(main_window, 'jupiter, The gas giant planet', 'Mass :	1.90 × 10^27 kg (318 Earths)' , 'Moons : 67 (Io, Europa, Ganymede & Callisto), ', 'Oribit distance :778,340,821 km (5.20 AU)' , 'Surface Temp :-148 °C' , 'First Record :7th or 8th century BC','Radius :43,441 mi', 'jupiter.png',270,360)
def uranus_method():
	global main_window
	mainmenu.withdraw()
	main_window = Toplevel()
	uranusobj = Planets(main_window, 'uranus , the Georgian Planet', 'Mass :8.68 × 10^25 kg (15 Earths)' , 'Moons : 27 (Miranda, Titania, Ariel, Umbriel & Oberon), ', 'Oribit distance :2,870,658,186 km (19.19 AU)' , 'Surface Temp :-216 °C' , 'First Record :March 13th 1781','Radius :15,759 mi', 'uranus.png',310,410)
def saturn_method():
	global main_window
	mainmenu.withdraw()
	main_window = Toplevel()
	saturnobj = Planets(main_window, 'Saturn , the angle ', 'Mass :5.68 × 10^26 kg (95 Earths)' , 'Moons : 62 (Titan, Enceladus, Iapetus & Rhea), ', 'Oribit distance :1,426,666,422 km (9.54 AU)' , 'Surface Temp :-178 °C' , 'First Record :8th century BC','Radius :36,184 mi', 'saturn.png',300,330)
def neptune_method():
	global main_window 
	mainmenu.withdraw()
	main_window = Toplevel()
	neptuneobj = Planets(main_window, 'Neptune,The Last Of The Gas Giants. Oceanus', 'Mass :1.02 × 10^26 kg (17 Earths)' , 'Moons : 14 (Triton), ', 'Oribit distance :4,498,396,441 km (30.10 AU)' , 'Surface Temp :-214 °C' , 'First Record :September 23rd 1846','Radius :15,299 mi', 'neptune.png',250,330)
def pluto_method():
	global main_window 
	mainmenu.withdraw()
	main_window = Toplevel()
	plutoobj = Planets(main_window, 'pluto, the dwarf', 'Mass :1.31 × 10^22 kg (0.17 Moons)' , 'Moons : 5 (Charon), ', 'Oribit distance :5,874,000,000 km (39.26 AU)' , 'Surface Temp :-229°C' , 'First Record :February 18th 1930','Radius :738.4 mi', 'pluto.png',250,390)


class gui:
	

	def __init__(self, master):
		self.master = master
		#title
		master.title(string ='Solar System ')
		master.configure(background = 'black')
		master.iconbitmap('Zairaam-Bumpy-Planets-01-sun.ico')
		#photos
		self.photo = PhotoImage(file ='main menu for solar system.png' )
		#creation of labels
		self.intro = Label(master, text = 'Solar System' , bg = 'black' , fg = 'white',font = 'times 20 bold')
		self.mainsolarsystem = Label(master , image = self.photo, bg = 'black')
		self.mainsolarsystem.image = self.photo
		self.credit = Label(master, text = 'App Developer: Ronald Colyar' , bg = 'black' , fg = 'white')
		#placement of labels
		self.intro.grid(row = 1 , column = 2 , sticky = 'we')
		self.mainsolarsystem.grid(row  = 2 ,  column = 2 , sticky = 'we')
		self.credit.grid(row = 13, column = 2 , sticky = 'we')
		#creation of buttons
		self.mercury = Button(master, text = 'Mercury, The smallest planet', bg = 'black' , fg = 'white' ,command = mercury_method)
		self.venus = Button(master, text = 'Venus , The Morning and Evening star ', bg = 'brown' , fg = 'white',command = venus_method)
		self.earth = Button(master, text = 'Earth, Home', bg = 'blue' , fg = 'white' ,command = earth_method)
		self.mars = Button(master, text = 'Mars, the Red Planet', bg = 'red' , fg = 'white', command = mars_method)
		self.jupiter = Button(master, text = 'jupiter, The gas giant planet', bg = 'brown' , fg = 'white',command = jupiter_method)
		self.saturn = Button(master, text = 'Saturn , the angle ', bg = 'gold' , fg = 'white',command = saturn_method)
		self.uranus = Button(master, text = 'uranus , the Georgian Planet', bg = 'grey' , fg = 'white', command = uranus_method)
		self.neptune= Button(master, text = 'Neptune,The Last Of The Gas Giants. Oceanus', bg = 'light blue' , fg = 'white',command = neptune_method)
		self.pluto = Button(master, text = 'Pluto, the infamous Planet X', bg = 'dark blue' , fg = 'white', command = pluto_method)


		#placement of buttons
		self.mercury.grid(row = 4 , column =2 , sticky= 'we')
		self.venus.grid(row = 5 , column =2 , sticky= 'we')
		self.earth.grid(row = 6 , column =2 , sticky= 'we')
		self.mars.grid(row = 7 , column =2 , sticky= 'we')
		self.jupiter.grid(row = 8 , column =2 , sticky= 'we')
		self.saturn.grid(row = 9 , column =2 , sticky= 'we')
		self.uranus.grid(row = 10 , column =2 , sticky= 'we')
		self.neptune.grid(row = 11 , column =2 , sticky= 'we')
		self.pluto.grid(row = 12 , column =2 , sticky= 'we')

		#placing of the window on start up
		w = 610
		h = 650
		ws = master.winfo_screenwidth()
		hs = master.winfo_screenheight()
		x = (ws/2) - (w/2)
		y =  (hs/2) - (h/2)
		master.geometry('%dx%d+%d+%d' % (w,h,x , y))

mainmenu= Tk()
menu_gui = gui(mainmenu)
#constant loop
mainmenu.mainloop()