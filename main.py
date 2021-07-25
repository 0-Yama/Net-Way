from src.interface.menuCreator import MenuCreator as mc
from src.database.handler import Handler as testDB
import tkinter as tk




root = tk.Tk()
root.geometry('1080x720')
root.resizable(False, False)
root.config(background="#FFF")
root.title("Net-Way")
app = mc(master=root)
app.mainloop()

