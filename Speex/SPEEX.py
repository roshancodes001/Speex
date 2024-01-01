from tkinter import *
from gtts import gTTS
from playsound import playsound
import os
import random

def Text_to_speech():
    Message = entry_field.get()
    speech = gTTS(text = Message)
    speech.save('Speech.mp3')
    #playsound('Speech.mp3')
    os.system('Speech.mp3')
def Exit():
    tk.destroy()
def Reset():
    Txt.set("")
def Help():
    Hlp=random.choice(HlpLst)
    Txt.set(Hlp)
        

tk = Tk()
tk.geometry('1920x1080')
tk.resizable(0,0)
bg=PhotoImage(file="TTS1.png")
bgr=Label(tk,image=bg)
bgr.place(x=0,y=0)
tk.title('Speex')
playsound("intro.mp3")
Label(tk, text ='Enter Text:', font ='impact 40',fg='teal').place(x=200,y=300)
Txt = StringVar()
entry_field = Entry(tk,textvariable =Txt, width ='50' ,font= 'impact 24' )
entry_field.place(x=200 , y=390)
HlpLst=["Welcome to Speex","Enjoy your Life",'Welcome to cit','You are not brave you have merely forgetten the fear of death','Tatake tatake','you cannot do it is the best motivation','Keep learning because life never stops teaching','if you want to fly give up everything that weighs you down','life has no ctrl+z','sometimes you win sometimes you learn']
Button(tk, text = "Play" , font = 'impact 24', command = Text_to_speech,bg='lightcyan').place(x=300, y=450)
Button(tk, text = 'Clear', font='impact 24', command = Reset,bg='lightcyan').place(x=750 , y =450)
Button(tk,text = 'Close Application',font = 'impact 24' , command = Exit, bg = 'lightcyan').place(x=20,y=950)
Button(tk,text = 'Generate Random',font = 'impact 24' , command = Help, bg = 'lightcyan').place(x=437,y=550)

tk.mainloop()

