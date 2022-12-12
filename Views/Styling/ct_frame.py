"""Contains CT_Frame class"""

#from tkinter import ttk

class CT_Frame:
    """Constructs a CT styled TKinter Frame"""

    master = None

    def __init__(self, frame):
        self.master = frame
        #self.master.style = ttk.Style()
        self.master.style.configure("TFrame", background="#041E42")
        self.master.style.configure("TButton", background="#041E42") 
        self.master.style.configure('TLabel', background='#041E42', font=('Arial', 11))