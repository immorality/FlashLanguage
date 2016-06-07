import Tkinter as tk
import ttk as Ttk
import json
import tkFont
from addWordStage import addWordStage

class generalStage:
    def __init__(self, master):
        self.master = master
        self.master.iconbitmap('icons_7457.ico')
        self.master.title('FlashLanguage')
        self.width = 800#self.master.winfo_width()
        self.height = 600#self.master.winfo_height()
        self.x = (self.master.winfo_screenwidth() // 2) - (self.width // 2)
        self.y = (self.master.winfo_screenheight() // 2) - (self.height // 2)
        self.master.geometry('{}x{}+{}+{}'.format(self.width, self.height, self.x, self.y))
        self.frame = tk.Frame(self.master)
        self.customFont = tkFont.Font(family="Segoe UI Light", size=12)
        self.customFont1 = tkFont.Font(family="Harrington", size=35)
        self.labelFlash = tk.Label(self.frame, text="FlashLanguage ", font=self.customFont1)
        self.table = Ttk.Treeview(self.frame, show="headings", selectmode="browse", height=16)
        self.table["columns"] = ("one", "two", "tree")
        self.table.column("one", width=150)
        self.table.column("two", width=150)
        self.table.column("tree", width=250)
        self.table.heading("one", text="English")
        self.table.heading("two", text="Polish")
        self.table.heading("tree", text="Example")
        self.showButton = tk.Button(self.frame, text='Refresh vocabulary', width=25, command=self.refreshTable, font=self.customFont)
        self.button1 = tk.Button(self.frame, text = 'Add new word', width = 25, command=self.new_window, font=self.customFont)
        self.exitButton = tk.Button(self.frame, text='Exit', width=25, command=self.exit, font=self.customFont)
        self.labelFlash.pack()
        self.table.pack(pady=10)
        self.button1.pack()
        self.showButton.pack(pady=10)
        self.exitButton.pack()
        self.frame.pack()
    def new_window(self):
        self.newWindow = tk.Toplevel(self.master)
        self.app = addWordStage(self.newWindow)

    def showAllWords(self):
        self.file = open("data.json")
        self.dictionary = json.load(self.file)
        self.file.close()
        self.words=self.dictionary['words']
        for i in range(len(self.words)):
            self.table.insert("", tk.END, values=(self.words[i]['english'], self.words[i]['polish'], self.words[i]['example']))

    def refreshTable(self):
        self.clearTable()
        self.showAllWords()

    def clearTable(self):
        x = self.table.get_children()
        for item in x:
            self.table.delete(item)

    def exit(self):
        self.master.destroy()

#generalStage = Tk()
#generalStage.iconbitmap('icons_7457.ico')
#generalStage.title('FlashLanguage')
#generalStage.geometry('800x600+300+50')

#addButton = Button(text="Add new word", width=30)
#addButton.pack()
#addButton.bind("<Button-1>", create())

#tx = Text(font=('times', 12), width=50, height=15, wrap=WORD)
#tx.pack(expand=YES)
