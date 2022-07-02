from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from tkinter import *
import pyttsx3 as pp
import speech_recognition as s
import threading

#initialize the voice

engine = pp.init()
voices=engine.getProperty('voices')
print(voices)


# set the male voice
engine.setProperty('voices',voices[0].id)

def speak(word):
    engine.say(word)
    engine.runAndWait()

bot = ChatBot("My Bot")

convo = [
    'Hello',
    'hi there!',
    'What is your name?',
    'My name is Bot, i am created by Dipak and Mittal',
    'How are you?',
    'I am doing great this days',
    'Thank You',
    'In wich city you live',
    'I am live in Satara',
    'In which language you talk?'
    'I mostly talk in English'
]

trainer = ListTrainer(bot)

# Now training the bot with the help of trainer

trainer.train(convo)

# answer = bot.get_response("What is your name?")
# print(answer)

# print("Tals to bot")

# while True:
#     query = input()
#     if query=='exit':
#         break
#     answer = bot.get_response(query)
#     print("bot : ",answer)

# Creating Photo Label Image

main = Tk()
main.geometry("500x650")
main.title("My Chat Bot")

img = PhotoImage(file = 'bot1.png')
photoL = Label(main, image= img)

photoL.pack(pady=5)


# Take query: It takes audio as input from user and convert into string..

def takeQuery():
    sr=s.Recognizer
    sr.pause_threshold=1
    print("Your bot is listening try to speak")
    with s.Microphone() as m:
        try:
            audio=sr.listen(m)
            query=sr.recognize_google(audio, language='eng-in')
            print(query)
            textF.delete(0, END)
            textF.insert(0, query)
            ask_from_bot()
        except Exception as e:
            print(e)
            print("Not Recognize")
        


def ask_from_bot():
    query=textF.get()
    answer_from_bot = bot.get_response(query)
    msgs.insert(END, "you: " + query)
    msgs.insert(END, "Bot: " + str(answer_from_bot))
    speak(answer_from_bot)
    textF.delete(0, END)
    msgs.yview(END)
    
    

# Creating Frame

frame = Frame(main)
sc = Scrollbar(frame)
msgs=Listbox(frame,width=80,height=20)

frame.pack()

sc.pack(side=RIGHT, fill=Y)
msgs.pack(side=LEFT, fill=BOTH, pady=10)



# Creating TextField

textF= Entry(main, font=("Verdana", 20))
textF.pack(fill=X, pady=10)

# Creating Buttons
btn = Button(main, text="Ask from bot", font=("Verdana", 20), command=ask_from_bot)
btn.pack()


# Creating Function
def enter_function(event):
    btn.invoke()
    
#Going to bind main window with entr key
main.bind('<Return>', enter_function)

def repeatL():
    while True:
        takeQuery()

t=threading.Thread(target=repeatL)
t.start()


main.mainloop()