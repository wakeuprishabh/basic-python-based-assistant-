import pyttsx3
import random
import pywhatkit
import datetime



#setting up the speech function 
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voice',voices[1].id)








#defines a speech function
def speech(text):
    engine.say(text)
    engine.runAndWait()

#wishes the user 
def wishme():
    y=(datetime.datetime.now().hour)
    z=(datetime.datetime.now().minute)
    speech("hello i am zira , what is your name ")
    b=str(input("what is your name ??"))
    speech("nice to meet you")
    speech(b)
    speech("the current time is ")
    speech(y)
    speech(z)



wishme()
     


# number guessing game 
def numberguessing():
    ra=random.randint(0,100)
    speech("Welcome to the number guessing game ")
    speech("guess a number from 0 to 100")
    x=int(input("guess a number from 0 to 100 "))
    if x==ra:
        speech("yay you won the game !!!")
    else:
        speech("oops    try    again")


# to open up a yt video 
def ytwatch():
    speech("what would you like to watch ")
    speech("enter a url or keywords that would describe your content the best")
    yt=str(input("enter a url or keywords that would describe your content the best : "))
    pywhatkit.playonyt(yt)




    

    


#main function menu 
speech("what would you like me to do ")

v=int(input("if you would like to play a game press 1 , if you would like to watch a video press 2 , , and 3 to exit(1,2,3,)"))
if v==1:
    numberguessing()
elif v==2:
    ytwatch()

else:
    quit()
