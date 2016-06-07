import json
import Tkinter as tk
import tkFont
from words import Words
from autocompleteEntry import AutocompleteEntry


class addWordStage:
    def __init__(self, master):
        self.master = master
        self.master.iconbitmap('icons_7457.ico')
        self.master.title('FlashLanguage')
        self.width = 600  # self.master.winfo_width()
        self.height = 350  # self.master.winfo_height()
        self.x = (self.master.winfo_screenwidth() // 2) - (self.width // 2)
        self.y = (self.master.winfo_screenheight() // 2) - (self.height // 2)
        self.master.geometry('{}x{}+{}+{}'.format(self.width, self.height, self.x, self.y))
        self.lista = ["aab", "auto", "bar", "bubble"]
        self.frame = tk.Frame(self.master)
        self.customFont = tkFont.Font(family="Segoe UI Light", size=12)
        self.customFont1 = tkFont.Font(family="Harrington", size=35)
        self.labelFlash = tk.Label(self.frame, text="FlashLanguage ", font=self.customFont1)
        self.labelEnglish = tk.Label(self.frame, text="English word: ", font=self.customFont)
        self.labelPolish = tk.Label(self.frame, text="Polish word: ", font=self.customFont)
        self.labelExample = tk.Label(self.frame, text="Example: ", font=self.customFont)
        #self.testEntry = AutocompleteEntry(self.master, self.lista, self.frame, width=30, font=self.customFont)
        self.textBoxEnglish = AutocompleteEntry(self.master, self.lista, self.frame, width=30, font=self.customFont)
        self.textBoxEnglish.focus()
        self.textBoxPolish = AutocompleteEntry(self.master, self.lista, self.frame, width=30, font=self.customFont)
        self.textBoxExample = tk.Entry(self.frame, width=30, font=self.customFont)
        self.quitButton = tk.Button(self.frame, text = 'Close', width = 25, command = self.close_windows, font=self.customFont)
        self.addButton = tk.Button(self.frame, text='Add', width=25, command = self.addNewWord, font=self.customFont)
        self.labelFlash.pack(side="top")
        #self.testEntry.pack(side="top")
        self.labelEnglish.pack(side="top")
        self.textBoxEnglish.pack(side="top")
        self.labelPolish.pack(side="top")
        self.textBoxPolish.pack(side="top")
        self.labelExample.pack(side="top")
        self.textBoxExample.pack(side="top")
        self.addButton.pack(side="left", padx=10, pady=30)
        self.quitButton.pack(side="left", padx=10)
        self.frame.pack()

    def addWordToDictionary(self, word):
        self.file = open("data.json")
        self.dictionary = json.load(self.file)
        self.file.close()

        self.dictionary['words'].append(vars(word))
        self.file = open("data.json", "w")
        json.dump(self.dictionary, self.file, indent=1)
        self.file.close()

    def getNewWords(self, english, polish, example):
        self.english = english
        self.polish = polish
        self.example = example
        return Words(self.english, self.polish, self.example)

    def addNewWord(self):
        self.newWord = self.getNewWords(self.textBoxEnglish.get(), self.textBoxPolish.get(), self.textBoxExample.get())
        self.addWordToDictionary(self.newWord)

    def close_windows(self):
        self.master.destroy()



