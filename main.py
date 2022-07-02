from concurrent.futures import thread
from email.mime import audio
from tkinter import *
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os
import pyttsx3 as pp
import speech_recognition
import threading


engine = pp.init()
voices=engine.getProperty('voices')
print(voices)


# set the male voice
engine.setProperty('voices',voices[0].id)

def speak(word):
    engine.say(word)
    engine.runAndWait()




data_list=[ 
            'Hello',
            'hi there!',
            'What is your name?',
            'My name is Bot, i am created by Dipak and Mittal',
            'How are you?',
            'I am doing great this days',
            'Thank You',
            'In wich city you live',
            'I am live in Satara',
            'In which language you talk?',
            'I mostly talk in English',
            'What is the capital of India',
            'Delhi is the capital of India',
            'In which language you talk',
            'I mostly talk in english',
            'What you do in free time',
            'I memorize things in my free time',
            'Ok bye',
            'bye take care'

            ]

bot=ChatBot('Bot')
trainer=ListTrainer(bot)

# for files in os.listdir('data/french/'):
# data=open('data/french/'+files,'r',encoding='utf-8').readlines()

trainer.train(data_list)

def botReply():
    question=questionField.get()
    question=question.capitalize()
    answer=bot.get_response(question)
    textarea.insert(END,'You: '+question+'\n')
    textarea.insert(END,'Bot: '+str(answer)+'\n')
    speak(answer)
    questionField.delete(0,END)


def audioToText():
    while True:
            
        sr=speech_recognition.Recognizer()
        try:
            with speech_recognition.Microphone() as m:
                sr.adjust_for_ambient_noise(m, duration=0.3)
                audio=sr.listen(m)
                query=sr.recognize_google(audio)
                

                questionField.delete(0, END)
                questionField.insert(0, query)
                botReply()
            
        except Exception as e:
            print(e)
        

root=Tk()

root.geometry('500x550+850+30')
root.title('ChatBot')
root.config(bg='black')

logoPic=PhotoImage(file='download.png')

logoPicLabel=Label(root,image=logoPic,bg='black')
logoPicLabel.pack(pady=5)

centerFrame=Frame(root)
centerFrame.pack()

scrollbar=Scrollbar(centerFrame)
scrollbar.pack(side=RIGHT)

textarea=Text(centerFrame,font=('times new roman',15,'bold'),height=10,yscrollcommand=scrollbar.set
              ,wrap='word')
textarea.pack(side=LEFT)
scrollbar.config(command=textarea.yview)

questionField=Entry(root,font=('verdana',20,'bold'))
questionField.pack(pady=15,fill=X)

askPic=PhotoImage(file='enter.png')


askButton=Button(root,image=askPic,command=botReply)
askButton.pack()

def click(event):
    askButton.invoke()


root.bind('<Return>',click)

thread=threading.Thread(target=audioToText)
thread.setDaemon(True)
thread.start()

root.mainloop()