'''
This is an old old old script I wrote for my highschool , There are many ways to shorten this project , 
one of the reasons I choose to leave it alone and not make any changes is because , I always want that reminder
as to where I have come from as a programmer using procedural code and not standard OOP.

'''


#last edited  3/12/2017
from tkinter import *
# allowing us to use tkinter widgets
from tkinter import ttk
#Window 
intropage = Tk()
root = Toplevel()
root.iconbitmap('panther.ico')
root.withdraw()
#placing of the window
w = 680
h = 250
ws = root.winfo_screenwidth()
hs = root.winfo_screenheight()
x = (ws/2) - (w/2)
y =  (hs/2) - (h/2)
#The window configuration 
root.resizable(width = False , height = False)
root.title(string=  "Longwood Panther Math Game Main Menu")
root.geometry('%dx%d+%d+%d' % (w,h,x , y))
#level variable
level = 1
#number incorrect
wrongcounter = 0
#addition level answers
anwser_of_addition_levels = {          '1' : '1,000' ,
                                       '2' : '1,250' ,
                                       '3' : '2,900' ,
                                       '4' : '3,443' ,
                                       '5' : '5,324'  ,
                                       '6' : '6,625' ,
                                       '7' : '58,567' ,
                                       '8' : '79,917' ,
                                       '9' : '135,713' ,
                                      '10' : '146,466',
                                      '11' : '{Pha<n>tex}'
                                      }
question_of_addition_levels = {         '1' : 'Enter 500 + 500?' ,
                                        '2' : 'Enter 1000 + 250?' ,
                                        '3' : 'Enter 2000 + 900?' ,
                                        '4' : 'Enter 2434 + 1009?' ,
                                        '5' : 'Enter 3020 + 2304?' ,
                                        '6' : 'Enter 4291 + 2334?',
                                        '7' : 'Enter 56233 + 2334?' ,
                                        '8' : 'Enter 56243 + 23674?',
                                        '9' : 'Enter 53403 + 82310?',
                                        '10': 'Enter 56233 + 90233?',
                                        '11':'You Have Finished You Are a Genius Panther:)'

                                          }
anwser_of_multi_levels = {'1' :  '36' ,
                                       '2' : '120' ,
                                       '3' : '132' ,
                                       '4' : '234' ,
                                       '5' : '440'  ,
                                       '6' : '351' ,
                                       '7' : '495' ,
                                       '8' : '989' ,
                                       '9' : '1,188' ,
                                      '10' : '2,576',
                                      '11' : '{Pha<n>tex}'


                                      }
question_of_multi_levels = {            '1' : 'Enter is 6 * 6?' ,
                                        '2' : 'Enter 10 * 12?' ,
                                        '3' : 'Enter 12 * 11?' ,
                                        '4' : 'Enter 13 * 18?' ,
                                        '5' : 'Enter is 22 * 20?' ,
                                        '6' : 'Enter is 27 * 13',
                                        '7' : 'Enter is 33 * 15' ,
                                        '8' : 'Enter is 43 * 23',
                                        '9' : 'Enter is 54 * 22?',
                                        '10': 'Enter is 56 * 46?',
                                        '11':'You Have Finished You Are a Genius Panther:)'
                                          }
question_of_sub_levels = {              '1' : 'Enter 44 - 6?' ,
                                        '2' : 'Enter 83  -  32?' ,
                                        '3' : 'Enter 122 - 31?' ,
                                        '4' : 'Enter 149 - 55?' ,
                                        '5' : 'Enter 170 - 74?' ,
                                        '6' : 'Enter 240 - 213',
                                        '7' : 'Enter 320 - 115' ,
                                        '8' : 'Enter 430 - 230',
                                        '9' : 'Enter 620 - 325?',
                                        '10': 'Enter 773 - 426?',
                                        '11':'You Have Finished You Are a Genius Panther:)'
                                          }
anwser_of_sub_levels = {'1' :  '38' ,
                                       '2' : '51' ,
                                       '3' : '91' ,
                                       '4' : '94' ,
                                       '5' : '96'  ,
                                       '6' : '27' ,
                                       '7' : '205' ,
                                       '8' : '200' ,
                                       '9' : '295' ,
                                      '10' : '347',
                                      '11' : '{Pha<n>tex}'
                        }
question_of_div_levels = {              '1' : 'Enter  8 / 8?' ,
                                        '2' : 'Enter 9  /  3?' ,
                                        '3' : 'Enter 12 / 3?' ,
                                        '4' : 'Enter 20 / 5?' ,
                                        '5' : 'Enter 70 / 10?' ,
                                        '6' : 'Enter 320 / 20',
                                        '7' : 'Enter 510 / 22' ,
                                        '8' : 'Enter 435  / 30',
                                        '9' : 'Enter 1620 / 32?',
                                        '10': 'Enter 1773  / 32?',
                                        '11':'You Have Finished You Are a Genius Panther:)'
                                          }                        
anwser_of_div_levels = {               '1' : '1' ,
                                       '2' : '3' ,
                                       '3' : '4' ,
                                       '4' : '4' ,
                                       '5' : '7'  ,
                                       '6' : '16' ,
                                       '7' : '23.18' ,
                                       '8' : '14.5' ,
                                       '9' : '50.62' ,
                                      '10' : '55.40',
                                      '11' : '{Pha<n>tex}'
                                      }
question_of_alge_levels = {             '1' : 'Solve g - 8 = 16?' ,
                                        '2' : 'Solve x - 56 = 23?' ,
                                        '3' : 'Enter 3x / 3 = 3?' ,
                                        '4' : 'Enter 10x / 5 = 40?' ,
                                        '5' : 'Enter 70x + 100 = 240?' ,
                                        '6' : 'Enter 95x + 130 =320',
                                        '7' : 'Enter 4x + 32 + 52 = 163' ,
                                        '8' : 'Enter 4(2a+3)=-3(a-1)+31',
                                        '9' : 'Enter 5(7a+5)=-3(a-2)+42',
                                        '10': '12(9a+5)=-10(a-4)+48?',
                                        '11':'You Have Finished You Are a Genius Panther:)'
                                          }                        
anwser_of_alge_levels = {              '1' : '24' ,
                                       '2' : '79' ,
                                       '3' : '3' ,
                                       '4' : '20' ,
                                       '5' : '2'  ,
                                       '6' : '2' ,
                                       '7' : '19.75' ,
                                       '8' : '2' ,
                                       '9' : '0.60' ,
                                      '10' : '0.23',
                                      '11' : '{Pha<n>tex}'
                                      }
question_of_geometry_levels = {         '1' : 'Solve C of the right triangle:  if a = 2 and b = 3' ,
                                        '2' : 'Solve C of the right triangle:  if a = 20 and b = 12' ,
                                        '3' : 'Solve C of the right triangle:  if a = 45 and b = 24?' ,
                                        '4' : 'Solve C of the right triangle:  if a = 67 and b = 32',
                                        '5' : 'Solve C of the right triangle:  if a = 68 and b = 36' ,
                                        '6' : 'Solve for C of a triangle if a = 80 , b = 90',
                                        '7' : 'If Angle(\_ABC)is a equalatteral triangle what measurement is a'  ,
                                        '8' : 'Solve for C of a triangle if a = 140 , B = 20',
                                        '9' : 'Solve for C if a = 60 (a and c are vertical angles )',
                                        '10': 'Solve for B of if C= 90 (B and C are vertical angles )',
                                        '11':'You Have Finished You Are a Genius Panther:)'
                                          }                        
anwser_of_geometry_levels = {          '1' : '3.61' ,
                                       '2' : '23.32' ,
                                       '3' : '51' ,
                                       '4' : '74.25' ,
                                       '5' : '76.94'  ,
                                       '6' : '10' ,
                                       '7' : '60' ,
                                       '8' : '20' ,
                                       '9' : '60' ,
                                      '10' : '90',
                                      '11' : '{Pha<n>tex}'
                                      }                                               
question_of_eleme_levels = {           '1' : 'The large fan blew a cool breeze on us.' ,
                                        '2' : 'Bill Rode his yellow skateboard down the steep hill.' ,
                                        '3' : 'We like pink lemonade better than regular lemonade.' ,
                                        '4' : "I love my grandad's rocking chair.",
                                        '5' : 'My dog has plaid color with his name on it.' ,
                                        '6' : 'Grandpa swept the dirty porch',
                                        '7' : "my mother's pasta is white."  ,
                                        '8' : ' My skunks are black.',
                                        '9' : "The car's gas tank is empty.",
                                        '10': 'I have a pen with red ink.',
                                        '11':'My mom loves how peaceful the lake is.',
                                        '12': 'Fish can be red.',
                                        '13': 'NiceWork :) Grammar master'
                                          }                        
anwser_of_eleme_levels = {          '1' : 'large' ,
                                       '2' : 'yellow' ,
                                       '3' : 'pink' ,
                                       '4' : 'rocking' ,
                                       '5' : 'plaid'  ,
                                       '6' : 'dirty' ,
                                       '7' : 'white' ,
                                       '8' : 'black' ,
                                       '9' : 'empty' ,
                                      '10' : 'red',
                                      '11' : 'peaceful', 
                                      '12' : 'red',
                                      '13' : '{Pha<n>tex}'
                                      }
question_of_middle_levels = {           '1' : 'I am so excited to see my family for chrismas____' ,
                                        '2' : 'What day of the week is your favorite____' ,
                                        '3' : 'You need to do your homework right after dinner____' ,
                                        '4' : "Please Take out the trash when your get home_____",
                                        '5' : 'My favorite team won the game im am filled with joy____' ,
                                        '6' : 'my mother just fart___ .',
                                        '7' : "I am thinking about walk___ to the store."  ,
                                        '8' : 'I plan on walking to the store later  said Jack',
                                        '9' : "The car's gas tank is empty  said Lisa",
                                        '10': 'I have a pen with red ink aswell as one with blue in it said John',
                                        '11':'Today I turn twenty one years of age.',
                                        '12': 'Me and my mother made a bad entry , so we re presented ourself.',
                                        '13': 'Most people try to resolve there issues in life , I dont.',
                                        '14':'NiceWork :) grammar master'
                                          }  
anwser_of_middle_levels = {          '1' : 'Exclamation' ,
                                       '2' : 'Question' ,
                                       '3' : 'period' ,
                                       '4' : 'period' ,
                                       '5' : 'Exclamation'  ,
                                       '6' : 'ed' ,
                                       '7' : 'ing' ,
                                       '8' : 'A' ,
                                       '9' : 'C' ,
                                      '10' : 'B',
                                      '11' : 'A', 
                                      '12' : 'C',
                                      '13' : 'A'
                                      }
question_of_High_levels = {           '1' : "A subway system is expanded to provide service to a growing suburb. A bike-sharing program is adopted to encourage nonmotorized transportation. '1:' To alleviate rush hour traffic jams in a congested downtown area, stoplight timing is coordinated. When any one of these changes occur, it is likely the result of careful analysis conducted by transportation planners.The work of transportation planners generally includes evaluating current transportation needs, assessing the effectiveness of existing facilities, and improving those facilities or  they design new ones. " ,
                                        '2' : " To alleviate rush hour traffic jams in a congested downtown area, stoplight timing is coordinated. When any one of these changes '2:' occur, it is likely the result of careful analysis conducted by transportation planners.The work of transportation planners generally includes evaluating current transportation needs, assessing the effectiveness of existing facilities, and improving those facilities or  they design new ones. " ,
                                        '3' : " To alleviate rush hour traffic jams in a congested downtown area, stoplight timing is coordinated. When any one of these changes  occur, it is likely the result of careful analysis conducted by transportation planners The work of transportation planners generally includes evaluating current transportation needs, assessing the effectiveness of existing facilities, and improving those facilities or '3:' they design new ones. Most transportation planners work in or near cities,  but some are employed in rural areas. Say, for example, a large factory is built on the outskirts of a small town. " ,
                                        '4' : "When any one of these changes  occur, it is likely the result of careful analysis conducted by transportation planners.The work of transportation planners generally includes evaluating current transportation needs, assessing the effectiveness of existing facilities, and improving those facilities or  they design new ones. Most transportation planners work in or near cities, '4:' but some are employed in rural areas. Say, for example, a large factory is built on the outskirts of a small town. Traffic to and from that location would increase at the beginning and end of work shifts",
                                        '5' : "Most transportation planners work in or near cities,  but some are employed in rural areas. Say, for example, a large factory is built on the outskirts of a small town. Traffic to and from that location would increase at the beginning and end of work shifts. The transportation planner’s '5:'job, might involve conducting a traffic count to determine the daily number of vehicles traveling on the road to the new factory. If analysis of the traffic count indicates that there is more traffic than the  current road as it is designed at this time can efficiently accommodate, the transportation planner might recommend widening the road to add another lane." ,
                                        '6' : "The transportation  planner’s job, might involve conducting a traffic count to determine the daily number of vehicles traveling on the road to the new factory. If analysis of the traffic count indicates that there is more traffic than the '6:' current road as it is designed at this time can efficiently accommodate, the transportation planner might recommend widening the road to add another lane.Transportation planners work closely with a number of community stakeholders, such as government officials and other interested organizations and individuals.  Next, representatives from the local public health department might provide input in designing a network of trails and sidewalks to encourage people to walk more..",
                                        '7' : "If analysis of the traffic count indicates that there is more traffic than the  current road as it is designed at this time can efficiently accommodate, the transportation planner might recommend widening the road to add another lane.Transportation planners work closely with a number of community stakeholders, such as government officials and other interested organizations and individuals. '7:' Next, representatives from the local public health department might provide input in designing a network of trails and sidewalks to encourage people to walk more.  According to the American Heart Association, walking provides numerous benefits related to health and well-being. Members of the Chamber of Commerce might share suggestions about designing transportation and parking facilities to support local businesses."  ,
                                        '8' : "Transportation planners work closely with a number of community stakeholders, such as government officials and other interested organizations and individuals.  Next, representatives from the local public health department might provide input in designing a network of trails and sidewalks to encourage people to walk more. '8:' According to the American Heart Association, walking provides numerous benefits related to health and well-being. Members of the Chamber of Commerce might share suggestions about designing transportation and parking facilities to support local businesses. People who pursue careers in transportation planning have a wide variety of educational backgrounds. ",
                                        '9' : "According to the American Heart Association, walking provides numerous benefits related to health and well-being. Members of the Chamber of Commerce might share suggestions about designing transportation and parking facilities to support local businesses. '9:' People who pursue careers in transportation planning have a wide variety of educational backgrounds. A two-year degree in transportation technology may be sufficient for some entry-level jobs in the field. Most jobs, however, require at least a bachelor’s degree; majors of transportation planners are  varied, including fields such as urban studies, civil engineering, geography, or transportation and logistics management. For many positions in the field, a master’s degree is required.",
                                        '10': "People who pursue careers in transportation planning have a wide variety of educational backgrounds. A two-year degree in transportation technology may be sufficient for some entry-level jobs in the field. Most jobs, however, require at least a bachelor’s degree; majors of transportation planners are '10:' varied, including fields such as urban studies, civil engineering, geography, or transportation and logistics management. For many positions in the field, a master’s degree is required.Transportation planners perform critical work within the broader field of urban and regional planning.",
                                        '11':"Transportation planners perform critical work within the broader field of urban and regional planning. As of 2010, there were approximately 40,300 urban and regional planners employed in the United States. The United States Bureau of Labor Statistics forecasts steady job growth in this field, '11:' projecting that 16 percent of new jobs in all occupations will be related to urban and regional planning. Population growth and concerns about environmental sustainability are expected to spur the need for transportation planning professionals.",
                                        '12': "Nice work :)"
                                        
                                          }  
anwser_of_High_levels = {          '1' : 'C' ,
                                       '2' : 'D' ,
                                       '3' : 'C' ,
                                       '4' : 'A' ,
                                       '5' : 'B'  ,
                                       '6' : 'D' ,
                                       '7' : 'B' ,
                                       '8' : 'C' ,
                                       '9' : 'A' ,
                                      '10' : 'A',
                                      '11' : 'C'
                                     
                                      }
anwser_of_High_levels_CHOICES = {      '1' : "Go to the referred part in the passage '1'                     Which choice best maintains the sentence pattern already established in the paragraph                                                                    A :NO CHANGE                                                              B:Coordinating stoplight timing can help- alleviate rush hour traffic jams in a congested downtown area.                                                                                                                                                                             C: Stoplight timing is coordinated to alleviate rush hour traffic jams in a congested downtown area.                                                                                        D:In a congested downtown area, stoplight timing is coordinated to alleviate rush hour traffic jams." ,
                                       '2' : 'Go to the referred part in the passage                                                                                       A:NO CHANGE                                                                   B:occur, they are                                                                              C:occurs, they are                                                 D:occurs, it is' ,
                                       '3' : 'Go to the referred part in the passage                               A:NO CHANGE                                                                   B:to design                                                        C: designing                                                        D:design' ,
                                       '4' : 'Refering to line 4 , which choice results in the most effective transition to the information that follows in the paragraph? ,                                                                                                                                            A:NO CHANGE                                                   B:where job opportunities are more plentiful.                                                                                   C:and the majority are employed by government agencies.                                                          D:DELETE the underlined portion and end the sentence with a period.' ,
                                       '5' : 'Go to the referred part in the passage                                                                     A:NO CHANGE                                                                     B:planner’s job                                                                          C:planners job,                                                                                      D:planners job'  ,
                                       '6' : 'Go to the referred part in the passage                                           A:NO CHANGE                                                                                    B:current design of the road right now                                                              C:road as it is now currently designed                                                                    D:current design of the road' ,
                                       '7' : 'Go to the referred part in the passage                                                     A:NO CHANGE                                                  B:For instance,                                                            C:Furthermore,                                      D:Similarly,' ,
                                       '8' : '8.The writer is considering deleting the underlined sentence. Should the sentence be kept or deleted?                                                              A:Kept, because it provides supporting evidence about the benefits of walking.                                                     B:Kept, because it provides an additional example of a community stakeholder with whom transportation planners work.                                                                C:Deleted, because it blurs the paragraph’s focus on the community stakeholders with whom transportation planners work.                                                                            D:Deleted, because it doesn’t provide specific examples of what the numerous benefits of walking are.' ,
                                       '9' : 'Go to the referred part in the passage                                                           A:NO CHANGE                                                            B:People, who pursue careers in transportation planning,                                                       C:People who pursue careers, in transportation planning,                                                                 D:People who pursue careers in transportation planning,' ,
                                      '10' : 'Go to the referred part in the passage                                                                A:NO CHANGE                                                           B:varied, and including                                                           C:varied and which include                                                                      D:varied, which include',
                                      '11' : '.Which choice completes the sentence with accurate data based on the graph?                                                                   A:NO CHANGE                                                                 B:warning, however, that job growth in urban and regional planning will slow to 14 percent by 2020.                                                                         C:predicting that employment of urban and regional planners will increase 16 percent between 2010 and 2020.                                                                    D:indicating that 14 to 18 percent of urban and regional planning positions will remain unfilled.'
                                     
                                      }
def intropage_deiconify():
  root.deiconify() 
  intropage.withdraw()

#intropage
intropage.title(string = 'Main Menu')
photo = PhotoImage(file = 'Untitled-1.png')
image = Label(intropage , image = photo)
image.image = photo
image.grid(row = 2 , column = 0 , sticky  = 'we')
w = 500
h = 170
ws = intropage.winfo_screenwidth()
hs = intropage.winfo_screenheight()
x = (ws/2) - (w/2)
y =  (hs/2) - (h/2)
intropage.geometry('%dx%d+%d+%d' % (w,h,x , y))
#introduction
welcome = Message(intropage , text = "Welcome To  C.I.CS Longwood's  Academic Practice" , font = 'times 14 bold')
welcome.grid(row = 2 , column = 1 , sticky = 'we'  )
#created by
MainDeveloper = Message(intropage , text = 'App Developer : Ronald Colyar')
MainDeveloper.grid(row = 2 , column = 2 , sticky = 'we')
#start button
start  = ttk.Button(intropage , text = 'Begin :)',command = intropage_deiconify)
start.grid(row = 2 , column = 3 , sticky = 'we' )
#icon
intropage.iconbitmap('panther.ico')
#addition level method
def addition():
   global wrongcounter,level

   while True:
        if AnswerBox.get() != anwser_of_addition_levels[str(level)]:
          wrongcounter +=1
          NumberWrong.configure(text ='Number Incorrect: ' + str(wrongcounter))
        break
       
   while True :
        if AnswerBox.get() == anwser_of_addition_levels[str(level)]:
               level =level + 1
               Question.configure(text = question_of_addition_levels[str(level)])
               levellabel.configure(text = 'Level : '+ str(level))
               AnswerBox.delete(0 , 'end')
        break
     
   if level == 11 :
      root.geometry('615x250')

 #Multiplication level  method      
def Multiplicationlevel():
   global level,wrongcounter 
   while True:
        if AnswerBox.get() != anwser_of_multi_levels[str(level)]:
          wrongcounter +=1
          NumberWrong.configure(text ='Number Incorrect: ' + str(wrongcounter))
        break

   while True:

      if AnswerBox.get() == anwser_of_multi_levels[str(level)]:
             level =level + 1
             Question.configure(text = question_of_multi_levels[str(level)])
             levellabel.configure(text = 'Level : '  + str(level))
      break
    
   if level == 11 :
      root.geometry('615x250')
#subtraction level method
def subtractlevel():
   global level,wrongcounter                                                                                                             
   while True:
        if AnswerBox.get() != anwser_of_sub_levels[str(level)]:
          wrongcounter +=1
          NumberWrong.configure(text ='Number Incorrect: ' + str(wrongcounter))
        break
  
   while True:
      if AnswerBox.get() == anwser_of_sub_levels[str(level)]:
             level =level + 1
             Question.configure(text = question_of_sub_levels[str(level)])
             levellabel.configure(text = 'Level : '  + str(level))
      break
   if level == 11 :
      root.geometry('615x250')
#division level method
def divlevel():
   global level
   global wrongcounter                                                                                                                   
   while True:
        if AnswerBox.get() != anwser_of_div_levels[str(level)]:
          wrongcounter +=1
          NumberWrong.configure(text ='Number Incorrect: ' + str(wrongcounter))
        break
   while True:

      if AnswerBox.get() == anwser_of_div_levels[str(level)]:
             level =level + 1
             Question.configure(text = question_of_div_levels[str(level)])
             levellabel.configure(text = 'Level : '  + str(level))
      break
   if level == 11 :
      root.geometry('615x250')  
                #geometry section
def geometry():
  root.withdraw()
  global geometry_answerbox , geometry_Question , geometry_levellabel , geometry_window , geometry_NumberWrong,geometry_backwardsbutton, level
  level = 1
  geometry_window = Toplevel()
  #the window placement
  w = 390
  h = 270
  ws = geometry_window.winfo_screenwidth()
  hs = geometry_window.winfo_screenheight()
  x = (ws/2) - (w/2)
  y =  (hs/2) - (h/2)
  geometry_window.geometry('%dx%d+%d+%d' % (w,h,x , y))
  geometry_window.title(string = 'Panther Geometry')
  geometry_window.iconbitmap('panther.ico')
  #photos
  photo = PhotoImage(file = 'geometry.png')
  #creation of labels
  geometry_Question = ttk.Label(geometry_window , text = question_of_geometry_levels[str(level)], font = 'times 10 bold')
  geometry_NumberWrong = ttk.Label(geometry_window , text ='Number Incorrect : 0')
  geometry_levellabel = ttk.Label(geometry_window , text = 'Level : ' + str(level))
  image = Label(geometry_window , image = photo)
  image.image = photo
  #placement of labels
 
  geometry_Question.grid(row = 2, column = 0 , sticky = 'we')
  geometry_NumberWrong.grid(row = 0 , column = 1 ,sticky='we')
  geometry_levellabel.grid(row = 0 , column = 0 , sticky=  'we')
  image.grid(row= 4 , column = 0 , sticky = 'we')
  #creation of buttons and entrys
  geometry_answerbox = ttk.Entry(geometry_window)
  geometry_submit = ttk.Button(geometry_window  , text= 'Submit x', command = geometry_method)
  geometry_backwardsbutton = ttk.Button(geometry_window , text = '<-Back',command = geometry_deiconify)
  #placement of buttons and entrys
  geometry_answerbox.grid(row = 3 , column = 0 , sticky = 'we')
  geometry_submit.grid(row = 3, column = 1, sticky = 'we')
  geometry_backwardsbutton.grid(row  = 1, column = 0 , sticky = 'we')

def geometry_method():
   global geometry_answerbox,geometry_Question,geometry_NumberWrong , level,wrongcounter
   while True:
        if geometry_answerbox.get() != anwser_of_geometry_levels[str(level)]:
          wrongcounter +=1
          geometry_NumberWrong.configure(text ='Number Incorrect: ' + str(wrongcounter))
        break
       
   while True :
        if geometry_answerbox.get()  == anwser_of_geometry_levels[str(level)]:
               level =level + 1
               geometry_Question.configure(text = question_of_geometry_levels[str(level)])
               geometry_levellabel.configure(text = 'Level : '+ str(level))
               geometry_answerbox.delete(0 , 'end')
        break
   geometry_answerbox.delete(0 , 'end')
   if level == 11 :
      root.geometry('615x250')

def geometry_deiconify():
  global geometry_backwardsbutton,geometry_window
  geometry_window.withdraw()
  root.deiconify()

def algebra():
  global level
  level = 1
  global backwardsbutton , Alge_answerbox,Alge_Question,Alge_levellabel,alge_NumberWrong,algebra_window
  root.withdraw()
  #placement of window
  algebra_window = Toplevel()

  w = 400
  h =280
  ws =algebra_window.winfo_screenwidth()
  hs = algebra_window.winfo_screenheight()
  x = (ws/2) - (w/2)
  y =  (hs/2) - (h/2)
  algebra_window.geometry('%dx%d+%d+%d' % (w,h,x , y))
  algebra_window.resizable(width = False , height = False)
  algebra_window.title(string = 'Panther Algebra')
  algebra_window.iconbitmap('panther.ico')
  #photos
  photo = PhotoImage(file = 'Algebra.png')
  #creation of labels
  Alge_Question = ttk.Label(algebra_window , text = question_of_alge_levels[str(level)], font = 'times 10 bold')
  alge_NumberWrong = ttk.Label(algebra_window , text ='Number Incorrect : 0')
  Alge_levellabel = ttk.Label(algebra_window , text = 'Level : ' + str(level))
  image = Label(algebra_window , image = photo)
  image.image = photo
  #placement of labels
  Alge_Question.grid(row = 2, column = 0 , sticky = 'we')
  alge_NumberWrong.grid(row = 0 , column = 1 ,sticky='we')
  Alge_levellabel.grid(row = 0 , column = 0 , sticky=  'we')
  image.grid(row = 4 , column = 0 , sticky ='we')
  #creation of buttons
  alge_submit = ttk.Button(algebra_window  , text= 'Submit x', command = algebra_method)
  backwardsbutton = ttk.Button(algebra_window , text = '<-Back',command = algebra_deiconify)
  #placement of buttons
  backwardsbutton.grid(row  = 1, column = 0 , sticky = 'we')
  alge_submit.grid(row = 3, column = 1, sticky = 'we')
  #creation of entrys
  Alge_answerbox = ttk.Entry(algebra_window)
  #placement of entrys
  Alge_answerbox.grid(row = 3 , column = 0 , sticky = 'we')

def algebra_deiconify():
  global backwardsbutton,algebra_window
  algebra_window.withdraw()
  root.deiconify()

def algebra_method():
   global Alge_answerbox,Alge_Question,alge_NumberWrong,level,wrongcounter

   while True:
        if Alge_answerbox.get() != anwser_of_alge_levels[str(level)]:
          wrongcounter +=1
          alge_NumberWrong.configure(text ='Number Incorrect: ' + str(wrongcounter))
        break
      
   while True :
        if Alge_answerbox.get()  == anwser_of_alge_levels[str(level)]:
               level =level + 1
               Alge_Question.configure(text = question_of_alge_levels[str(level)])
               Alge_levellabel.configure(text = 'Level : '+ str(level))
               Alge_answerbox.delete(0 , 'end')
        break
   Alge_answerbox.delete(0 , 'end') 
   if level == 11 :
      root.geometry('615x250')
    
def language_Arts():
  global language_window, language_backwardsbutton
  root.withdraw()
  language_window = Toplevel()
  language_window.iconbitmap('panther.ico')
  #title
  language_window.title(string = 'Language Arts Main Menu')
  w = 620
  h = 390
  ws = language_window.winfo_screenwidth()
  hs = language_window.winfo_screenheight()
  x = (ws/2) - (w/2)
  y =  (hs/2) - (h/2)
  language_window.geometry('%dx%d+%d+%d' % (w,h,x , y))
  Greetings =Message(language_window , text = 'Welcome to The Language Arts Section!!, this is Where you Can Brush up on Your Grammar , and improve gramatical errors. With Multiple levels based on your skill level(grade classification)'  , font= 'times 10 bold')
  Greetings.grid(row = 1 , column = 1 , sticky = 'we') 

  elementary = ttk.Button(language_window , text = 'Elementary',command = elementary_method)
  elementary.grid(row  = 2 , column = 1 , sticky = 'we')

  middleschool = ttk.Button(language_window ,text = 'Middle School', command = Middleschool_method)
  middleschool.grid(row = 2 , column  = 2 , sticky = 'we')

  highschool = ttk.Button(language_window , text = 'High School', command = Highschool_method)
  highschool.grid(row = 2 , column = 3,  sticky = 'we')

  photo1 = PhotoImage(file = 'grammar-cartoon.png')
  photo2 = PhotoImage(file ='Matt1-240x300.png')
  photo3 = PhotoImage(file = 'th.png')

  image1 = Label(language_window , image = photo1)
  image1.image = photo1
  image1.grid(row = 3 , column = 1 , sticky = 'we')

  image2 = Label(language_window, image = photo2)
  image2.image= photo2
  image2.grid(row = 3 , column = 2 ,sticky= 'we')

  image3 = Label(language_window , image = photo3)
  image3.image = photo3
  image3.grid(row= 3, column = 3 , sticky = 'we')

  jump_in = ttk.Label(language_window , text = 'Jump on In You Got IT!! :)' ,font = 'times 15 bold')
  jump_in.grid(row = 1  , column = 2 , sticky = 'we' )

  language_backwardsbutton = ttk.Button(language_window , text = '<-Back') 
  language_backwardsbutton.grid(row = 0 , column = 1, sticky = 'we')
  language_backwardsbutton.bind('<Button-1>', language_arts_Deiconify)

def language_arts_Deiconify():
  global language_backwardsbutton, language_window
  language_backwardsbutton.bind(language_window.withdraw() , root.deiconify() )

def elementary_method():
  global language_window,elem_answerbox,elem_Question,elem_NumberWrong,elem_levellabel,elementary_backwardsbutton ,elementary_window
  language_window.withdraw()
  elementary_window = Toplevel()
  #icon
  elementary_window.iconbitmap('panther.ico')
  elementary_window.title(string = 'Elementary School Practice')
  #photos
  photo1 =  PhotoImage(file = 'grammar-cartoon.png')
  #creation of labels
  elem_Question = Label(elementary_window , text = 'Question: ' + question_of_eleme_levels[str(level)], font = 'times 16 bold')
  directions = ttk.Label(elementary_window , text = 'Directions : Enter The First adjective , And Only The first Adjective.' , font = 'times 10 bold')
  elem_levellabel = ttk.Label(elementary_window , text = 'Level : ' + str(level) , font= 'times 13 bold')
  image1 = Label( elementary_window , image = photo1)
  image1.image = photo1
  elem_NumberWrong = ttk.Label(elementary_window , text ='Number Incorrect : 0')
  #placement of labels
  elem_Question.grid(row = 2, column = 0 , sticky = 'we')
  directions.grid(row = 0 , column = 0 , sticky = 'we')
  elem_levellabel.grid(row = 1, column = 0 , sticky=  'we')
  image1.grid(row = 5  , column = 0 , sticky = 'we')
  elem_NumberWrong.grid(row = 3 , column = 0 ,sticky='we')
  #creation of entrys and buttons
  elem_answerbox = ttk.Entry( elementary_window)
  submit = ttk.Button(elementary_window , text = 'Submit',command = elementary_method_check)
  elementary_backwardsbutton = ttk.Button(elementary_window  , text = '<-Back', command = elementary_deiconify)
  #placement of entrys and buttons
  elem_answerbox.grid(row = 4 , column = 0 , sticky = 'we')
  submit.grid(row = 4 , column = 1 ,sticky = 'we')
  elementary_backwardsbutton.grid(row = 3 , column = 1 , sticky = 'we')

  w = 610
  h = 340
  ws = elementary_window.winfo_screenwidth()
  hs = elementary_window.winfo_screenheight()
  x = (ws/2) - (w/2)
  y =  (hs/2) - (h/2)
  elementary_window.geometry('%dx%d+%d+%d' % (w,h,x , y))

def elementary_method_check():
   global elem_answerbox,elem_Question,elem_NumberWrong,level,elem_levellabel,wrongcounter

   while True:
        if elem_answerbox.get() != anwser_of_eleme_levels[str(level)]:
          wrongcounter +=1
          elem_NumberWrong.configure(text ='Number Incorrect: ' + str(wrongcounter))
        break
      
   while True :
        if elem_answerbox.get()  == anwser_of_eleme_levels[str(level)]:
               level =level + 1
               elem_Question.configure(text = question_of_eleme_levels[str(level)])
               elem_levellabel.configure(text = 'Level : '+ str(level))
               elem_answerbox.delete(0 , 'end')
        break
   elem_answerbox.delete(0 , 'end') 

def elementary_deiconify():
  global  elementary_window , language_window
  elementary_window.withdraw() 
  language_window.deiconify() 

def Middleschool_method():
  global level , AnswerChoice , rules , language_window , Middleschool_window,Middleschool_answerbox,Middleschool_Question,Middleschool_NumberWrong,Middleschool_levellabel,Middleschool_backwardsbutton ,elementary_window
  level = 1
  language_window.withdraw()
  Middleschool_window = Toplevel()
  Middleschool_window.iconbitmap('panther.ico')
  Middleschool_window.title(string = 'Middle School Practice')
  #photos
  photo1 =  PhotoImage(file = 'Matt1-240x300.png')
  #creation of labels
  Middleschool_Question = Label(Middleschool_window , text = 'Question: ' + question_of_middle_levels[str(level)], font = 'times 16 bold')
  directions = ttk.Label(Middleschool_window , text = "Rules: Choose the ending punctuation 'Question' , 'period' , 'Exclamation'" , font = 'times 10 bold')
  Middleschool_levellabel = ttk.Label(Middleschool_window , text = 'Level : ' + str(level) , font= 'times 13 bold')
  image1 = Label( Middleschool_window , image = photo1)
  image1.image = photo1
  Middleschool_NumberWrong = ttk.Label(Middleschool_window , text ='Number Incorrect : 0')
  AnswerChoice = ttk.Label(Middleschool_window , text = None)

  #placement of labels
  Middleschool_Question.grid(row = 2, column = 0 , sticky = 'we')
  directions.grid(row = 0 , column = 0 , sticky = 'we')
  Middleschool_levellabel.grid(row = 1, column = 0 , sticky=  'we')
  image1.grid(row = 7 , column = 0 , sticky = 'we')
  Middleschool_NumberWrong.grid(row = 3 , column = 0 ,sticky='we')
  AnswerChoice.grid(row = 5 , column = 0 , sticky = 'we')

  #creation of buttons
  submit = ttk.Button(Middleschool_window , text = 'Submit', command = Middleschool_method_check)
  Middleschool_backwardsbutton = ttk.Button(Middleschool_window  , text = '<-Back',command = Middleschool_deiconify)

  #placement of buttons
  submit.grid(row = 6 , column = 1 ,sticky = 'we')
  Middleschool_backwardsbutton.grid(row = 3 , column = 1 , sticky = 'we')
  #creation of entrys
  Middleschool_answerbox = ttk.Entry( Middleschool_window)
  #placement of entrys
  Middleschool_answerbox.grid(row = 6 , column = 0 , sticky = 'we')
  #placement of windows
  w = 690
  h = 380
  ws = Middleschool_window.winfo_screenwidth()
  hs = Middleschool_window.winfo_screenheight()
  x = (ws/2) - (w/2)
  y =  (hs/2) - (h/2)
  Middleschool_window.geometry('%dx%d+%d+%d' % (w,h,x , y))

def Middleschool_method_check():
   global AnswerChoice , Middleschool_answerbox,Middleschool_Question,Middleschool_NumberWrong,level,Middleschool_levellabel,wrongcounter

   while True:
        if Middleschool_answerbox.get() != anwser_of_middle_levels[str(level)]:
          wrongcounter +=1
          Middleschool_NumberWrong.configure(text ='Number Incorrect: ' + str(wrongcounter))
        break
      
   while True :
        if Middleschool_answerbox.get()  == anwser_of_middle_levels[str(level)]:
               level =level + 1
               Middleschool_Question.configure(text = question_of_middle_levels[str(level)])
               Middleschool_levellabel.configure(text = 'Level : '+ str(level))
               Middleschool_answerbox.delete(0 , 'end')
        if level == 6  or  level == 7:
          rules.configure(text = "Enter The correct pre-fix 'ed' or 'ing' ")
        if level == 8:
          rules.configure(text = 'Choose the correct Quotation location')
          AnswerChoice.configure(text= "AnswerChoices = A.Before 'I' and after 'later , B. Before 'I' and after 'store' , C. before 'plan'  and after 'later'  ")
        if level == 9:
          AnswerChoice.configure(text = "AnswerChoices =C.Before 'The' and after 'empty' , B. Before 'car's and after 'empty' , A. before 'gas'  and after 'lisa'   ")
        if level == 10:
          AnswerChoice.configure(text = " AnswerChoices = C. Before 'red' and after 'blue' ,  B.Before 'I' and after 'It', A. before 'I'  and after 'John'   ")
        if level == 11:
          rules.configure(text = 'choose where the hyphen fit correctly')
          AnswerChoice.configure(text = " A.Between Twenty and one , B. Between Turn and twenty , C. None of the above")
        if level == 12:
          AnswerChoice.configure(text = "C.Between re and presented , B.Between bad and entry  , C. None of the above")
        if level == 13:
          AnswerChoice.configure(text = " A. None of the above  , B.between most and people , C. Between in and life ")  
        break

   Middleschool_answerbox.delete(0 , 'end') 

def Middleschool_deiconify():
   global  Middleschool_window , language_window
   Middleschool_window.withdraw() 
   language_window.deiconify() 
def change_to_addition():
  global level
  level = 1
  AnswerBox.delete(0  , 'end')
  submit.bind('<Button-1>' , addition)
  Question.configure(text =question_of_addition_levels[str(level)])
  levellabel.configure(text ='Level : '  + str(level)) 
  Rules.configure(text= 'Rules: Comma in 4+ Digit Numbers')

def Highschool_method():
  global AnswerChoice_multi,level , AnswerChoice , rules , language_window ,Highschool_window,Highschool_answerbox,Highschool_Question,Highschool_NumberWrong,Highschool_levellabel,Highschool_backwardsbutton 
  level = 1
  language_window.withdraw()
  Highschool_window = Toplevel()
  Highschool_window.iconbitmap('panther.ico')
  Highschool_window.title(string = 'Highschool SAT  Practice')
  #creation of labels and messages
  Highschool_Question = Message(Highschool_window , text = 'Question: ' + question_of_High_levels[str(level)], font = 'times 16 bold')
  directions = ttk.Label(Highschool_window , text = 'Directions : Enter in the correct letter ,number in Quotation is the "refferenced" number ', font = 'times 10 bold')
  Highschool_levellabel = ttk.Label(Highschool_window , text = 'Level : ' + str(level) , font= 'times 13 bold')

  Highschool_NumberWrong = ttk.Label(Highschool_window , text ='Number Incorrect : 0')
  AnswerChoice_multi  = Message(Highschool_window ,text = anwser_of_High_levels_CHOICES[str(level)], font = 'times 10 bold' )
  #extras for image
  photo1 =  PhotoImage(file = 'satpracticeimage.png')
  image1 = Label( Highschool_window , image = photo1)
  image1.image = photo1
  #placement of labels and messages
  Highschool_Question.grid(row = 2, column = 0 , sticky = 'we')
  directions.grid(row = 0 , column = 0 , sticky = 'we')
  Highschool_levellabel.grid(row = 1, column = 0 , sticky=  'we')
  image1.grid(row = 7 , column = 0 , sticky = 'we')
  Highschool_NumberWrong.grid(row = 3 , column = 0 ,sticky='we')
  AnswerChoice_multi.grid(row = 2 , column = 1 , sticky = 'we')
  #creation of entrys
  Highschool_answerbox = ttk.Entry( Highschool_window)
  #placement of entrys
  Highschool_answerbox.grid(row = 3 , column = 1 , sticky = 'we')
  #creation  of buttons
  submit = ttk.Button(Highschool_window , text = 'Submit',command= Highschool_method_check)
  Highschool_backwardsbutton = ttk.Button(Highschool_window  , text = '<-Back' , command = Highschool_deiconify)
  #placement of buttons
  submit.grid(row = 6 , column = 1 ,sticky = 'we')
  Highschool_backwardsbutton.grid(row = 0 , column = 1 , sticky = 'we')
  #placement of the window
  w = 790
  h = 650
  ws = Highschool_window.winfo_screenwidth()
  hs = Highschool_window.winfo_screenheight()
  x = (ws/2) - (w/2)
  y =  (hs/2) - (h/2)
  Highschool_window.geometry('%dx%d+%d+%d' % (w,h,x , y))

def Highschool_deiconify():
  global  Highschool_window , language_window
  Highschool_window.withdraw() 
  language_window.deiconify()

def Highschool_method_check():
   global AnswerChoice_multi, AnswerChoice , Highschool_answerbox,Highschool_Question,Highschool_NumberWrong,level,Highschool_levellabel,wrongcounter
   
   while True:
        if Highschool_answerbox.get() != anwser_of_High_levels[str(level)]:
          wrongcounter +=1
          Highschool_NumberWrong.configure(text ='Number Incorrect: ' + str(wrongcounter))
        break

   while True :
        if Highschool_answerbox.get()  == anwser_of_High_levels[str(level)]:
               level =level + 1
               Highschool_Question.configure(text = question_of_High_levels[str(level)])
               Highschool_levellabel.configure(text = 'Level : '+ str(level))
               Highschool_answerbox.delete(0 , 'end')
               AnswerChoice_multi.configure(text =anwser_of_High_levels_CHOICES[str(level)] )
        break
   Highschool_answerbox.delete(0 , 'end')

def change_to_multi():
  global level
  level = 1
  AnswerBox.delete(0  , 'end')
  submit.bind('<Button-1>' ,Multiplicationlevel)
  Question.configure(text =question_of_multi_levels[str(level)])
  levellabel.configure(text ='Level : '  + str(level)) 
  Rules.configure(text= 'Rules: Comma in 4+ Digit Numbers')

def change_to_sub():
  
  global level
  level = 1
  AnswerBox.delete(0  , 'end')
  submit.bind('<Button-1>' ,subtractlevel)
  Question.configure(text =question_of_sub_levels[str(level)])
  levellabel.configure(text ='Level : '  + str(level))
  Rules.configure(text= 'Rules: Whole Numbers only')

def change_to_division():
  #deleting the answer entry for more user friendly experience
  global level
  level = 1
  AnswerBox.delete(0  , 'end')
  submit.bind('<Button-1>' ,divlevel)
  Question.configure(text =question_of_div_levels[str(level)] )
  levellabel.configure(text ='Level : '  + str(level) )
  Rules.configure(text= 'Rules: 2 Digits behind decimals only')

#photos
photo = PhotoImage(file = 'Untitled-1.png')

#creation of the labels
Rules = ttk.Label(root, text =  'Rules:Comma in 4+ Digit Numbers' , font = 'times 10 bold ')
goodluck = ttk.Label(root, text= "You've Got it !! Panther!", font = 'times 14 bold')
levellabel = ttk.Label(root , text = 'Level : 1')
Question = ttk.Label(root , text = question_of_addition_levels[str(level)], font = 'times 10 bold')
pantherpicture = Label(root, image = photo)
ps = ttk.Label(root, text = 'P.s Take Your Time :)')
NumberWrong = ttk.Label(root , text = 'Number Incorrect: 0')

#placement of labels
Rules.grid(row = 2 , column  = 1 , sticky = 'we')
goodluck.grid(row = 4 , column = 1 , sticky = 'we')
levellabel.grid(row = 1 , column = 0  , sticky = 'we')
Question.grid(row = 2 , column = 0 , sticky = 'we')
pantherpicture.grid(row  = 4 , column= 0  , sticky = 'we')
NumberWrong.grid(row =1 ,column = 1 , sticky = 'we' )
ps.grid(row = 3 , column = 3  ,sticky = 'we')

#creation of entrys
AnswerBox = ttk.Entry(root)

#placement of entrys
AnswerBox.grid(row  = 3 , column = 0 , columnspan = 2 , sticky = 'we')

#creation of buttons
submit = ttk.Button(root, text = 'Submit' , command = addition)
Multibutton = ttk.Button(root , text = 'Multiplication', command = change_to_multi)
additionbutton = ttk.Button(root , text = 'Addition' ,command = change_to_addition)
subtractionButton = ttk.Button(root  , text = 'Subtraction',  command =change_to_sub)
divisionbutton = ttk.Button(root, text = 'Division' , command = change_to_division)
algebutton = ttk.Button(root, text = 'Algebra',command = algebra)
geometrybutton = ttk.Button(root , text= 'Geometry' , command = geometry)
LA_Button = ttk.Button(root , text= 'Language Arts',command =language_Arts )

#placement of buttons
submit.grid(row  = 3, column = 2  , sticky = 'we')
Multibutton.grid(row = 0 , column = 0 , sticky = 'we' )
additionbutton.grid(row = 0  , column = 1 , sticky = 'we')
subtractionButton.grid(row = 0 , column  = 2 , sticky = 'we')
divisionbutton.grid(row = 0 , column = 3 , sticky = 'we')
algebutton.grid(row = 4 , column = 2, sticky = 'we')
geometrybutton.grid(row = 4 , column = 3 , sticky = 'we')
LA_Button.grid(row = 4 , column = 4, sticky = 'we')

root.mainloop()