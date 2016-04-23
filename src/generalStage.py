from Tkinter import *
from ttk import *
from ConnectDB import *


def showUsers():
     for x in getUsers():
        tx.insert(2.0, x + " ")


generalStage = Tk()
generalStage.iconbitmap('icons_7457.ico')
generalStage.title('FlashLanguage')
generalStage.geometry('800x600+300+50')

tx = Text(font=('times', 12), width=50, height=15, wrap=WORD)
tx.pack(expand=YES)

butt = Button(text="Hei!", width=30, command=showUsers)
butt.pack()
