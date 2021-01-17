'''

Hello World

ok so since you have an Editor now i assume you know how to import python libraries...well import all which have been mentioned!
if you find any errors regarding problems in installing pyaudio, i would suggest to download the same using conda(Anaconda)
If you are still facing ANY kind of issues , kindly contact me at oyumgameo@gmail.com

Made by GameoPhileProductions
Open-Source Project
Front-end by Achyut Shukla
Back-end by Om Mukherjee


HOW IT WORKS:
for activating it , just go to your command prompt/terminal and go to the location you have this project, then type: python Jarv.py.
then it starts listening to the surrounding. It keeps beeping periodically for taking breaks...you have to call it by its name to activate it ! Make sure to call it just after your hear the BEEP sound
for playing any song/youtube video--> say Play [name of the song/video]
'''

import random
from os import system
from time import sleep  # this is for using delays in between the program is running
 # this is for the machine's text replies to be converted into speech
import speech_recognition  # this used by the machine to convert your voice into text in order to interpret the commands
from playsound import playsound  # this is  to play a 'beep' sound
from selenium import webdriver
import wikipedia
from tkinter import *
from datetime import datetime
import threading
import pyjokes

sr = speech_recognition.Recognizer()

root = Tk()
root.geometry("830x550")
root.resizable(False, False)
root.title("Virtual Machine")
root.configure(bg='black')

button_state = False
cmd = ""


botname = "Jarvis"  # This is the name of the bot.


def speak(str):
    print()

def user_reply(str):
    if len(str) > 0:
        screen.configure(state=NORMAL)
        screen.insert(END, "YOU: " + str + "\n")
        screen.configure(state=DISABLED)


def listen():
    try:
        with speech_recognition.Microphone() as source_1:
            sr.adjust_for_ambient_noise(source=source_1, duration=1)
            print("Listening")
            audio = sr.listen(source_1)

            Text = sr.recognize_google(audio, language='en-in')
            user_reply(Text)
            generate_reply(Text)


    except speech_recognition.RequestError as e:

        print(e)

    except Exception as e:
        print(e)
        print("Exception")


def user_reply(str):
    if len(str) > 0:
        screen.configure(state=NORMAL)
        screen.insert(END, "YOU: " + str + "\n")
        screen.configure(state=DISABLED)
    sleep(2)

def bot_reply(str):
    screen.configure(state=NORMAL)
    screen.insert(END, "BOT: " + str + "\n")
    screen.configure(state=DISABLED)

    # Here,Enable the button


'''
note : make both the userreply and botreply func s such that after you ve printed the same on the right/left 
 side accordingly, you could print the other message(the message to be displayed after it ) under it
'''

'''
def Accept_voice_command(event):           #Accept command and returns a string ...if command inappropriate returns error message

    #here,Disable the button
    listener = sr.Recognizer()
    playsound('audio.wav')
    command_listener = sr.Recognizer()
    r3 = sr.Recognizer()

    with sr.Microphone() as source:

        audio = r3.listen(source)
        try:
            command = command_listener.recognize_google(audio)

            cmd=command
        except:
            cmd='Im sorry!My listening skills are yet to be enhanced!For better results, you may type or try to speak again!'

    threading.Thread(target = lambda :bot_reply(cmd)).start()

    # dont forget to change value of choice_voice to false after 2-3 seconds...so that it can again be used after recieivng the reply of the bot...
'''
options = webdriver.ChromeOptions()
options.add_argument('headless')
driver = webdriver.Chrome(executable_path='/Users/ommukherjee/Documents/chromedriver', options=options)

def generate_reply(str):  # logical thinking (Back End)- Here, the bot will access the command and generate a proper reply accordingly

    str=str.lower()
    if 'what' in str and 'name' in str:

        str_2 = 'My Name is Jarvis!'
        screen.configure(state=NORMAL)
        screen.insert(END, "BOT: " + str_2 + "\n")
        screen.configure(state=DISABLED)

        print("Test Text")

    elif 'play' in str:
        ex = str.index('play') + 5
        ex2 = str[ex:]
        bot_reply('okay sir! opening on Youtube...')
        sleep(2)

        driver_head = webdriver.Chrome(executable_path='/Users/ommukherjee/Documents/chromedriver')  # your location[make sure your chromedriver is of the  version compatible to  that of your chrome]
        driver_head.get('https://www.youtube.com/results?search_query=' + ex2)
        driver_head.find_element_by_xpath('//*[@id="contents"]/ytd-video-renderer[1]').click()

    elif 'what' in str and 'time' in str:

        now = datetime.now()
        time = now.strftime("%H:%M:%S")
        bot_reply(time)  # if possible, only for this one , make the texts a bit bigger...this way, the time shown will look better

    elif ('who' in str or 'what' in str ) and 'is' in str:

        xo = str.index('is') + 3
        personalityname = str[xo:]
        personalityinfo = wikipedia.summary(personalityname)
        mi = personalityinfo.index('.') + 1
        threading.Thread(target=bot_reply(personalityinfo[:mi])).start()

    elif 'hello' in str :
        now = datetime.now()
        time = now.strftime("%H:%M:%S")
        hr=int(time[:2])
        if(hr>=4 and hr<12):
            bot_reply('Good morning sir!')

        elif(hr>=12 and hr<=16):
            bot_reply('Good Afternoon')
        else:
            bot_reply('Good evening sir ')

    elif 'music' in str:
        xo = str.index('music') + 6
        song = str[xo:]
        driver.get('https://gaana.com/search/' + song)
        driver.find_element_by_xpath('//*[@id="new-release-album"]/li[1]').click()
    elif 'joke' in str:
        bot_reply(pyjokes.get_joke())
    elif 'exit' in str or 'bye' in str:

        driver.quit()
        root.quit()
        sys.exit()
    elif 'stop' in str:
        driver.close()


def enter():
    global cmd
    cmd = command_enter.get()
    command_enter.delete(0, END)
    if len(cmd) > 0:
        screen.configure(state=NORMAL)
        screen.insert(END, "YOU: " + cmd + "\n")
        screen.configure(state=DISABLED)
        generate_reply(cmd)



my_frame = Frame(root)

scroll_bar = Scrollbar(my_frame, orient=VERTICAL)

screen = Text(my_frame, height=15, width=89, yscrollcommand=scroll_bar.set, font=("Times new roman", 14))
screen.configure(state=DISABLED)
screen.pack(side=LEFT)
my_frame.grid(row=0, column=0, padx=5, pady=5)

scroll_bar.configure(command=screen.yview)
scroll_bar.pack(side=RIGHT, fill=Y)

command_enter = Entry(root, width=60, font=("Times new roman", 14))
command_enter.grid(row=1, column=0, padx=5, pady=80, ipadx=3, ipady=10)

speak_icon = PhotoImage(file="speak.png").subsample(7, 9)

speak_button = Button(root, image=speak_icon, borderwidth=2, height=40, width=80, activebackground=None,
                      transition=None,command = listen, bg="white")
speak_button.place(x=47, y=409)
# speak_button.bind('<ButtonPress-1>', threading.Thread(target = lambda :listen( )))

enter_icon = PhotoImage(file="enter.png").subsample(2, 3)

button_enter = Button(root, image=enter_icon, borderwidth=2, height=40, width=80, activebackground=None,
                      transition=None, bg="white", command=enter)
button_enter.place(x=700, y=409)

root.mainloop()
