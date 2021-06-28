from src.interface.menuCreator import MenuCreator as mc
import tkinter as tk



root = tk.Tk()
app = mc(master=root)
app.mainloop()