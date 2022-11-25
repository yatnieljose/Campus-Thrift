from tkinter import *
from tkinter import ttk
import ct_tk


class Listing(ttk.Frame):
    """Represents a Listing UI object"""

    def __init__(self, master, name, price, type):
        ttk.Frame.__init__(self, master)

        self.name = name
        self.price = price
        self.type = type

        self.init_item_name()
        self.init_item_price()
        self.init_item_type()
        self.init_select()

    def init_item_name(self):
        """Initiates the name label for the listing"""
        self.lbl_item_name = ttk.Label(self, text=self.name)
        self.lbl_item_name.grid(row=0, column=0, padx=15, sticky="e")

    def init_item_price(self):
        """Initiates the price label for the listing"""
        self.lbl_item_price = ttk.Label(self, text=str(self.price))
        self.lbl_item_price.grid(row=0, column=1, padx=15, sticky="e")

    def init_item_type(self):
        """Initiates the type label for the listing"""
        self.lbl_item_type = ttk.Label(self, text=self.type)
        self.lbl_item_type.grid(row=0, column=2, padx=15, sticky="e")

    def init_select(self):
        """Initiates the Select button for the listing"""
        self.btn_select = ttk.Button(self, text="Select")
        self.btn_select.grid(row=0, column=3, padx=15, sticky="e")


def main():
    root = Tk()
    ct_tk.CT_Tk(root, 'Campus Thrift')
    Listing(root, "Math250 Textbook", 20, "textbook").grid()
    root.mainloop()


if __name__ == "__main__":
    main()
