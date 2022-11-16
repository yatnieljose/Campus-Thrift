from tkinter import *
from tkinter import ttk


class CT_Tk:

    master = None

    def __init__(self, component, title):
        self.master = component
        self.master.title(title)
        self.master.resizable(False, False)
        self.master.configure(background='#041E42')

        self.master.style = ttk.Style()
        self.master.style.configure('TFrame', background='#041E42')
        self.master.style.configure('TButton', background='#041E42')
        self.master.style.configure(
            'TLabel', background='#041E42', font=('Arial', 11))
        self.master.style.configure(
            'Header.TLabel', font=('Arial', 18, 'bold'))
