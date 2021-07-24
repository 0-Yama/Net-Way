from src.interface.menuCreator import MenuCreator as mc
import tkinter as tk
import os

class Main:

    def __init__(self):
        pass


root = tk.Tk()
root.geometry('1080x720')
root.resizable(False, False)
root.config(background="#FFF")
root.title("Net-Way")
app = mc(master=root)
app.mainloop()