"""Contains the CT_Style class"""

from tkinter import ttk

class CT_Style(ttk.Style):
    """Creates a styling module for Campus Thrift widgets"""

    def __init__(self):
        ttk.Style.__init__(self)

    def CT_Label(self):
        self.configure('TLabel', background="#041E42")