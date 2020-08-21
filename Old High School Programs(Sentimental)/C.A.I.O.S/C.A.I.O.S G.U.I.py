
#C.A.I.O.S CANVAS :)
#o u n u y
#m t p t s
#m o u p t
#a m t u e
#n a   t m
#d t
#  e
#  d


#Pha<n>tex™
#Caios™ Created by Ronald Colyar on 12/ 15 /17
#PERMISSION TO USE THIS CODE BY ANYMEANS , MAKE MODIFICATIONS


import pyttsx3
import os
from tkinter import *
from tkinter import ttk
import wikipedia

#main window 
root = Tk()
root.config(background = 'Black')
root.title('Caios Assistant Manager')
root.iconbitmap('Caios.ico')
root.resizable(height = False, width = False)

#initing our pyttsx3
engine = pyttsx3.init()

def talktome(text):
	engine.say(text)
	engine.runAndWait()

def restart():
	talktome('Restarting system Ronald ,sir')
	talktome('all systems will be rebooting , in less than one minute')
	os.system('shutdown -r')
def googlechrome():
	talktome('now opening google chrome for you ,sir')
	os.startfile('C:/Program Files (x86)/Google/Chrome/Application/chrome.exe')

def shutdown():
	talktome('system will now shutdown , sir')
	os.system('shutdown /p')


def status():
	
	talktome('system is online , waiting on your command ronald , sir ')

def sublime_text():
	talktome('starting sublime text for you , ronald ,sir')
	os.startfile('C:/Program Files/Sublime Text 3/sublime_text.exe')

def internet_explorer():
	talktome('starting Internet for you , ronald ,sir')
	os.startfile('C:/Program Files (x86)/Internet Explorer/iexplore.exe')

def codes():
	
	talktome('Opening main code folder , sir')
	os.startfile('C:/Users/Kxrk/Downloads/Codes')

def song():
	global Songbox
	
	song_window = Toplevel()
	song_window.title(string = 'Caios™ Music')
	song_window.config(background = 'black')
	song_window.iconbitmap('Caios.ico')
	song_window.resizable(height = False, width = False)


    #greeting message
	talktome('Please enter the song you would like to play.')

	#creation of Label
	song_Label = Label(song_window , text= 'Enter Song here',bg= 'black', fg ='white')

	#creation of Entry
	Songbox = ttk.Entry(song_window)

	#creation of button
	submit = Button(song_window , text = 'submit', command =playsong,bg= 'black', fg ='white' )

	#placement of widgets
	song_Label.grid(row = 1 , column = 0 , sticky = 'we')
	submit.grid(row= 2 , column = 1 , sticky = 'we')
	Songbox.grid(row = 2 , column = 0 , sticky = 'we')

def wikipedia_window():

	global result , wiki_sentenceAmount_entry , wiki_topic_search_entry,result

	wiki_window  = Toplevel()
	wiki_window.iconbitmap('Caios.ico')
	wiki_window.config(background = 'black')
	wiki_window.resizable(height = False, width = False)


	wiki_submit_button = Button(wiki_window , text= 'Search' , command = wikipedia_search,bg= 'black', fg ='white')
	wiki_submit_button.grid(row = 2,  column = 2,  sticky = 'we')

	result = Text(wiki_window)
	result.grid(row = 3 , column = 0 , columnspan = 3 , sticky = 'we')


	#creation of Labels
	wiki_intro_title = Label(wiki_window , text = 'wikipedia search' ,font ='times 14 bold',bg= 'black', fg ='white')
	wiki_topic_search = Label(wiki_window, text = 'Enter The Topic You Would Like to Search',bg= 'black', fg ='white')
	wiki_sentenceAmount = Label(wiki_window ,text = 'Enter The Amount of Information(sentences) Ex :2 or if you want all enter "ALL" ',bg= 'black', fg ='white')



	#placement of Labels
	wiki_intro_title.grid(row = 0 , column =0 ,columnspan = 2, sticky = 'we' )
	wiki_topic_search.grid(row = 1 , column = 0 , sticky = 'we')
	wiki_sentenceAmount.grid(row = 1, column = 1 , sticky = 'we', pady = 5 , padx = 5)



	#creation of entrys
	wiki_topic_search_entry = ttk.Entry(wiki_window)
	wiki_sentenceAmount_entry = ttk.Entry(wiki_window)

	#placement of entrys

	wiki_sentenceAmount_entry.grid(row = 2, column = 1 , sticky = 'we', pady = 5 , padx = 5)
	wiki_topic_search_entry.grid(row = 2 , column = 0 , sticky = 'we')


def error_test(Topic):
	global wiki_topic_search_entry , result
	try:	
			result.insert(1.0,wikipedia.summary(str(Topic) ) )
			return True
			#checking to see if the topic is valid also checking to see if the topic is too general
	except  (wikipedia.exceptions.DisambiguationError, wikipedia.exceptions.PageError) :
			return False


def wikipedia_search():

	global result , wiki_sentenceAmount_entry, wiki_topic_search_entry

	results_box = result
	#removing all contents
	results_box.delete(1.0 , 'end')
	#key information
	Sentences = wiki_sentenceAmount_entry.get()
	Topic = wiki_topic_search_entry.get()
	talktome('searching the wikipedia database')

	#default boolean
	error = True
	if error_test(Topic) == False:
		error  = False
	#updating user if exception is thrown
	if error == False:
		results_box.insert(1.0 , "Error1 : Your Topic may be too vague , meaning it has multiple results or Your Topic may not match any of the known topics")
	
	else:
		results_box.insert(1.0,wikipedia.summary(str(Topic) , sentences = Sentences) )




def open_windows_defender():
	talktome('opening windows defender for you sir')
	os.startfile('C:/Program Files/Windows Defender/MSASCui.exe')


def playsong():
	global Songbox
	
	os.startfile('C:/Users/Kxrk/Music/'+Songbox.get()+'.mp3')



#creation of the label
title_Label = Label(root, text = 'C.A.I.O.S Command Center',bg= 'black', fg ='white')


#placement of label
title_Label.grid(row = 1 , column = 0 , sticky = 'we')



#creation of buttons
restart_button = Button(root , text = 'restart system', command= restart,bg= 'black', fg ='white')
shutdown_button = Button(root , text = 'shutdown system',command=shutdown,bg= 'black', fg ='white')
codes_but  = Button(root , text = 'Codes Folder',command=codes,bg= 'black', fg ='white')
sublime_button = Button(root , text = 'Sublime text',command=sublime_text,bg= 'black', fg ='white')
internet_button = Button(root , text = 'internet Explorer',command=internet_explorer,bg= 'black', fg ='white')
songbutton = Button(root, text = 'song',command=song,bg= 'black', fg ='white')
statusbutton = Button(root , text = 'status',command= status,bg= 'black', fg ='white')
googlebutton = Button(root , text = 'Google Chrome',command=googlechrome,bg= 'black', fg ='white')
wikipediabutton = Button(root, text = 'wikipedia search', command  = wikipedia_window,bg= 'black', fg ='white')
windowsdefenderbutton = Button(root, text = 'Windows Defender' , command =open_windows_defender  , bg= 'black', fg ='white')


#placement of buttons
restart_button.grid(row = 5 , column = 0 , sticky = 'we')
shutdown_button.grid(row  = 6 , column = 0 , sticky = 'we')
codes_but.grid(row = 4 , column = 0 , sticky = 'we')
sublime_button.grid(row = 4 , column = 1 , sticky = 'we')
internet_button.grid(row = 5 , column = 1 , sticky = 'we')
songbutton.grid(row = 6 ,column = 1, sticky = 'we')
statusbutton.grid(row = 7 , column = 1 ,sticky = 'we')
googlebutton.grid(row = 7 , column = 0, sticky = 'we')
wikipediabutton.grid(row = 8 , column = 0 , sticky ='we')
windowsdefenderbutton.grid(row = 8 , column = 1, sticky= 'we')


root.mainloop()