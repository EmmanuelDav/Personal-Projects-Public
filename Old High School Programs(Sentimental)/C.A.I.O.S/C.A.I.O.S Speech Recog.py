'''

caios:





command
automated
input 
output
system
'''


#Caios™ Created by Ronald Colyar on 12/ 15 /17
#PERMISSION TO USE THIS CODE BY ANYMEANS , MAKE MODIFICATIONS


#modules/librays for system
import speech_recognition as sr
import pyttsx3
import pocketsphinx
import pyaudio
import random
import os
import wikipedia







def restart():
    os.system('shutdown -r')



def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        a=r.listen(source)
        try:
            return r.recognize_sphinx(a)


        except sr.UnknownValueError:
            print('Cant Understand')
        except sr.RequestError as e:
            print('Recog Error: (0)'.format(e))


                                            
engine = pyttsx3.init() 





def talktome(text):
    engine.say(text)
    engine.runAndWait()


# start up
talktome('Caios is now online ronald,sir')
talktome('how can i assist you')


def mainfunction():
    a=r.listen(source)
    user= r.recognize_sphinx(a)
    print(user)
    
                       
                       #main commands

    numb_of_times = 0

    #greetings   


    if user == 'hello' or user  == 'wassup' or user == 'hi' or user == 'hows it going':
        numb_of_times +=1
        

        #adding a little personality to caios
        if numb_of_times > 2 :
            z='still here sir' , 'how many times are you going to greet me sir'
            n = random.choice(z)
            talktome(n)


        a = 'Hi ,Sir how are you doing today?' , 'how is it going ,sir'
        k = random.choice(a)
        
        talktome(k)




    #Unpleasant greetings 
    elif user == 'bitch' or user == 'whore' or user  == 'hoe' or user == 'slut' or user == 'pussy':
     k = 'just a tip , Caios doesnt respond to ignorace', 'thats not nice , do you talk to your parents with that tone'
     A= random.choice(k)
     talktome(A)




     #commands
    elif user == 'what can you do' or user == 'what can you do caios' or user == 'what is your functionality' or user == 'commands':
        talktome('I have a number of different functions , they will be listed onto terminal')
        print('codes folder')
        print('status')
        print('restart')
        print('shutdown')
        print('python')
        print('song')
        print('play video')
        print('open pictures/picture')
        print('internet explorer')
        print('sublime')
        print('creator')
        print('windows defender')
        print('wikipedia'  )
    
    elif user == 'five':
     talktome('if you meant hi , hello')

    elif user =='shut down'  or  user =='shutdown':
            print('shutting down system.....')
            talktome('shutting off system')
            os.system("shutdown /p")
    

    elif user == 'status'or user =='online' :
            print('status: online')
            talktome('Already online sir')
            talktome('what can i assist you with')


    elif user == 'windows defender' or user == 'defender':
        os.startfile('C:/Program Files/Windows Defender/MSASCui.exe')


    #Similar soundings for online
    elif user =='for mine' or user == 'for lime':
            print('nearest command for sublime text.....')
            talktome('did you mean online?')
            talktome('system is online and ready to compute')            
            
   

    elif user == 'python':
        talktome('as you wish, sir')
        talktome('opening python interpreter')
        os.startfile('C:/Users/Kxrk/AppData/Local/Programs/Python/Python36-32/python.exe')


    elif user == 'what language were you written in' or user == 'what programming language created you' or user == 'what programming language is the best':
        talktome('python created me ,therefore its the best language on earth ')



    #simmilar soundings for python
    elif user == 'by phone' or user == 'by dawn':
     print('nearest command python.....')
     talktome('did you mean open python interpreter?')
     talktome('opening nearest command , launching python interpreter')
     os.startfile('C:/Users/Kxrk/AppData/Local/Programs/Python/Python36-32/python.exe')
    


    elif user == 'what is your name':
        talktome('caios , short for , command operated input output system')
    


    elif user == 'restart':
        print('system restarting.....')
        talktome('shutting down system and restarting')
        restart()

    
    elif user == 'sublime' or user  == 'sub lime':

        talktome('Now opening sublime text')
        print(' C.A.I.O.S is now opening sublime text...........')
        os.startfile('C:/Program Files/Sublime Text 3/sublime_text.exe')
    


    elif user == 'internet explorer' or user == 'Internet explorer' or user == 'Internet' or user== 'internet':
        talktome('launching internet explorer')
        print('C.A.I.O.S  is now opening internet explorer.....')
        os.startfile('C:/Program Files (x86)/Internet Explorer/iexplore.exe')
   


    elif user == 'code one' or user== 'code two' or user == 'code three'or user == 'code 3' or user== 'code 2' or user == 'code 3':
        talktome('you are awesome')
    


    elif user == 'song':
        talktome('What would you like me to play ronald , sir')
        print('listening for song file name......')
        #listen to name of song and execute
        k = listen()
        print('listening....')
        os.startfile('C:/Users/Kxrk/Music/'+k+'.mp3')
   

   
    elif user == 'play video' or user == 'open video' or user =='start video':
        talktome('what video would you like me play for you ronald , sir ')
        print('listening.......')
        k = listen()
        os.startfile('C:/Users/Kxrk/Videos/'+k+'.mp4')
   


    elif user == 'open pictures' or user == 'picture' or user =='open picture':
        talktome('what picture do you want me to open ronald , sir ')
        print('listeing......')
        k = listen()
        os.startfile('C:/Users/Kxrk/Pictures/'+k+'.png')

  
    
    elif user == 'codes folder' or user  == 'codes' or user == 'open codes folder':
        talktome('Starting Main Code Folder , Ronald Sir')
        os.startfile('C:/Users/Kxrk/Downloads/Codes')
    



    elif user == 'whats your name' or user == 'what is your name ' or user == "what's your name":
        talktome('caios , short for ,command ,automated ,input ,output, system')



   

    elif user == 'end' or user == 'quit' or user == 'close':
        quit()

    
    elif user == 'creator' or user == 'who is your creator' or user =='who created you':
        talktome('Ronald colyar jr. , in december 15th 2017')


    
    elif user == 'what programming language were you built in':
        talktome('python , the best programming language')


    #wikipedia api search
    elif user == 'wikipedia' or user == 'wiki' or user == 'pedia':
        talktome('what would you like to search wikipedia for , sir')
        print('Listening.......')

        k = listen()
        print('              ')
        print('              ')
        print('              ')
        print('              ')

        b = input("how many lines of information from wiki do you want , for example 1 ,2 ,3 ,4 or info(entering 'info' will give you information from wikipedia) ")
        print('               ')
        print('               ')
        talktome('gathering information on' + str(k))
        talktome('here is the required amount of information asked for , sir')
        if b =='info' or b == 'INFO':
            print(wikipedia.summary(str(k)))

        
        
  
        else:
            print(wikipedia.summary(str(k) , sentences = int(b)))
    else:
        print('unknown command of C.A.I.O.S')
        print('                            ')


    

   
if __name__ == "__main__": 
    print('C.A.I.O.S')
    print('CREATOR: RONAlD COLYAR JR.')
    print('About me: I am a command automated input output system ')
    print("you can find my commands by saying  'commands' " )  


    r = sr.Recognizer()
    with sr.Microphone() as source:
        while 3:
            mainfunction()
            




