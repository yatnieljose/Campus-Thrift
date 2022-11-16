from tkinter import *
from tkinter import ttk


class Listing(ttk.Frame):

    def __init__(self, master, name, price, loc_x, loc_y):
        ttk.Frame.__init__(self, master)

        ttk.Label(master, text=name).grid(
            row=loc_x, column=loc_y, padx=15, sticky='e')
        ttk.Label(master, text=price).grid(
            row=loc_x, column=loc_y + 1, padx=15, sticky='e')
        ttk.Button(master, text='Select').grid(
            row=loc_x, column=loc_y + 2, padx=15, sticky='e')
