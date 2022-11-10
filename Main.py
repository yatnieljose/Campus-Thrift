import tkinter as tk
from tkinter import ttk
import Views.Frames.TopFrame as vf


window = tk.Tk()
window.title("Campus Thrift")
window.resizable(width=False, height=False)
window.rowconfigure([0, 1, 2], minsize=200)
window.columnconfigure(0, minsize=1000)

frm_top = vf.TopFrame(window)


frm_choice = tk.Frame(master=window)
frm_bot = tk.Frame(master=window)

frm_top.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
frm_choice.grid(row=1, column=0, padx=25)
frm_bot.grid(row=2, column=0, padx=10)


window.mainloop()
