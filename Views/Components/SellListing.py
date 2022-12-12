from tkinter import *
from tkinter import ttk

RIDGE_PAD = 2

class SellListing(ttk.Frame):
    def __init__(self, master):#, item_name, item_type, min_bid):
        #self.item_frm = ttk.Frame(master, width=900-(2*RIDGE_PAD), height=55, relief=RIDGE)
        #self.item_frm.propagate(0)
        ttk.Frame.__init__(self, master, width=900-(2*RIDGE_PAD), height=55, relief=RIDGE)
        """
        self.item_frm = ttk.Frame(master, width=900-(2*RIDGE_PAD), height=55, relief=RIDGE)
        self.item_frm.propagate(0)
        ttk.Label(self.item_frm, text=item_name).place(x=RIDGE_PAD, y=RIDGE_PAD)
        ttk.Label(self.item_frm, text=item_type).place(x=298+RIDGE_PAD, y=RIDGE_PAD)
        ttk.Label(self.item_frm, text="$" + str(min_bid)).place(x=(298*2)+RIDGE_PAD, y=RIDGE_PAD)"""

    def fill_labels(self, item_name, item_type, min_bid):
        ttk.Label(self, text=item_name).place(x=RIDGE_PAD, y=RIDGE_PAD)
        ttk.Label(self, text=item_type).place(x=298+RIDGE_PAD, y=RIDGE_PAD)
        ttk.Label(self, text="$" + str(min_bid)).place(x=(298*2)+RIDGE_PAD, y=RIDGE_PAD)