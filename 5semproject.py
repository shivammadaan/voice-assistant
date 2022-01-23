import speech_recognition as sr
from wikipedia import *
import pywhatkit
import sounddevice
from pyttsx3 import *
from tkinter import messagebox
from tkinter import *
import random
from tkinter import Entry
master=Tk()
#master.geometry("400x700")
def calc_wind():
    root=Toplevel(master)

    def kd():
        e1.delete(0, END)

    def click(num):
        current = e1.get()
        e1.delete(0, END)
        e1.insert(0, str(current) + str(num))

    def add():
        num1 = e1.get()
        global no1
        no1 = float(num1)
        global xx
        xx = "add"
        e1.delete(0, END)

    def sub():
        num1 = e1.get()
        global no1
        no1 = float(num1)
        global xx
        xx = "sub"
        e1.delete(0, END)

    def mul():
        num1 = e1.get()
        global no1
        no1 = float(num1)
        global xx
        xx = "mul"
        e1.delete(0, END)

    def div():
        num1 = e1.get()
        global no1
        no1 = float(num1)
        global xx
        xx = "div"
        e1.delete(0, END)

    def eq():
        num2 = e1.get()
        e1.delete(0, END)
        if xx == "add":
            e1.insert(0, float(num2) + no1)
        elif xx == "sub":
            e1.insert(0, no1 - float(num2))
        elif xx == "mul":
            e1.insert(0, no1 * float(num2))
        elif xx == "div":
            if float(num2) == 0:
                e1.insert(0, 'ERROR')
                messagebox.showerror('ERROR', 'Cannot Divide By Zero')
            elif num2 != 0:
                e1.insert(0, no1 / float(num2))
        else:
            e1.insert(0, 'error')

    def ext():
        response = messagebox.askyesno('exit', 'wanna exit')
        if response == 1:
            root.quit()

    e1 = Entry(root, width=20, bd=5)
    e1.grid(row=0, column=1, columnspan=3)

    b1 = Button(root, text="1", padx=30, pady=20,bg="yellow", command=lambda: click(1)).grid(row=1, column=1)
    b2 = Button(root, text="2", padx=30, pady=20,bg="yellow", command=lambda: click(2)).grid(row=1, column=2)
    b3 = Button(root, text="3", padx=30, pady=20,bg="yellow", command=lambda: click(3)).grid(row=1, column=3)
    b4 = Button(root, text="4", padx=30, pady=20,bg="yellow", command=lambda: click(4)).grid(row=2, column=1)
    b5 = Button(root, text="5", padx=30, pady=20,bg="yellow", command=lambda: click(5)).grid(row=2, column=2)
    b6 = Button(root, text="6", padx=30, pady=20,bg="yellow", command=lambda: click(6)).grid(row=2, column=3)
    b7 = Button(root, text="7", padx=30, pady=20,bg="yellow", command=lambda: click(7)).grid(row=3, column=1)
    b8 = Button(root, text="8", padx=30, pady=20,bg="yellow", command=lambda: click(8)).grid(row=3, column=2)
    b9 = Button(root, text="9", padx=30, pady=20,bg="yellow", command=lambda: click(9)).grid(row=3, column=3)
    badd = Button(root, text="+", padx=29, pady=20, command=add, bg="blue").grid(row=4, column=1)
    b0 = Button(root, text="0", padx=30, pady=20,bg="yellow", command=lambda: click(0)).grid(row=4, column=2)
    B = Button(root, text="C", padx=30, pady=20, command=kd, bg="red").grid(row=4, column=3)
    bsub = Button(root, text="-", padx=32, pady=20, command=sub, bg="blue").grid(row=5, column=1)
    bmul = Button(root, text="X", padx=30, pady=20, command=mul, bg="blue").grid(row=5, column=2)
    bdiv = Button(root, text="/", padx=32, pady=20, command=div, bg="blue").grid(row=5, column=3)
    bE = Button(root, text="=", padx=105, pady=20, command=eq, bg="green").grid(row=6, column=1, columnspan=3)
    bexit = Button(root, text="EXIT", padx=95, pady=20, command=ext, bg="red").grid(row=7, column=1, columnspan=3)
    root.resizable(False, False)
def assis():
    soot=Toplevel(master)
    soot.geometry("300x600")
    def kd():
        listen=sr.Recognizer()
        engine=init()
        rate = engine.getProperty('rate')
        engine.setProperty('rate', 130)

        def talk(text):
            engine.say(text)
            engine.runAndWait()
        with sr.Microphone() as source:
            print('bolo')
            voice=listen.listen(source)
            try:
                command=listen.recognize_google(voice)
                print(command)
                if "play" in command:
                    command=command.replace("play","")
                    talk("playing"+command)
                    pywhatkit.playonyt(command)
                elif "what" in command:
                    res=summary(command,sentences=1)
                    talk(res)
                elif "who" in command:
                    res=summary(command,sentences=1)
                    talk(res)
                else:
                    talk("how can i help you")

            except:
                nn=Label(soot,text="error").pack()
    ab1=Button(soot,text="TAP AND SPEAK",command=kd,bg="red")
    ab1.pack()
def game():
    zoot=Toplevel(master)
    options = ('r', 'p', 's')
    user = " "
    computer = random.choice(options)
    print(computer)
    def click(op):
        global user
        if op == 1:
            user = 'r'
        elif op == 2:
            user = 'p'
        elif op == 3:
            user = 's'
        if computer == user:
            tie = Label(f2, text='ITS A TIE').pack(padx=10)
            tie2 = Label(f2, text='COMPUTER').pack(padx=10)
            tie3 = Label(f2, text='CHOSE {}'.format(computer)).pack(padx=10)
        elif (computer == 'r' and user == 'p') or (computer == 'p' and user == 's') or (
                computer == 's' and user == 'r'):
            tie = Label(f2, text='YOU WIN').pack(padx=10)
            tie2 = Label(f2, text='COMPUTER').pack(padx=10)
            tie3 = Label(f2, text='CHOSE {}'.format(computer)).pack(padx=10)
        else:
            tie = Label(f2, text='YOU LOOSE').pack(padx=10)
            tie2 = Label(f2, text='COMPUTER').pack(padx=10)
            tie3 = Label(f2, text='CHOSE {}'.format(computer)).pack(padx=10)
    zoot.geometry("300x300")
    f1 = LabelFrame(zoot, width=150, height=300)
    stone = Button(f1, text="STONE", command=lambda: click(1))
    stone.grid(row=1, column=1, pady=34, padx=30)
    paper = Button(f1, text="PAPER", command=lambda: click(2))
    paper.grid(row=2, column=1, pady=30)
    sci = Button(f1, text="SCISSOR", command=lambda: click(3))
    sci.grid(row=3, column=1, pady=30)
    f2 = LabelFrame(zoot, width=150, height=300)
    f1.grid(row=1, column=1)
    f2.grid(row=1, column=2)
def notes():
    loot=Toplevel(master)
    loot.geometry("300x600")
    command=None
    def kdn():
        listen=sr.Recognizer()
        with sr.Microphone() as source:
            print('bolo')
            voice=listen.listen(source)
            try:
                global command
                command = listen.recognize_google(voice)
                en.delete(0, END)
                en.insert(0, str(command))
            except:
                print("error")
    ab1 = Button(loot, text="TAP AND SPEAK", command=kdn, bg="red")
    ab1.pack()
    en=Entry(loot,width=300,bd=10)
    en.pack(ipady=100)



b1=Button(master,text="CALCULATOR",command=calc_wind,bg="yellow")
b1.grid(row=1,column=1,columnspan=1,padx=100,pady=60)
b2=Button(master,text="ASSISTANT",command=assis,bg="pink")
b2.grid(row=2,column=1,columnspan=1,padx=100,pady=60)
b3=Button(master,text="GAME",bg="green",command=game)
b3.grid(row=3,column=1,columnspan=1,padx=100,pady=60)
b4=Button(master,text="VOICE NOTES",bg="brown",command=notes)
b4.grid(row=4,column=1,columnspan=1,padx=100,pady=60)
master.mainloop()
