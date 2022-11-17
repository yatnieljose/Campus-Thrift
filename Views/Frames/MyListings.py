# Frame that represents MyListing
# Separate tables for current user-made Listings (SellerListing)  and current Listings user has highest
# bid on (BuyerListing)

from tkinter import *
from tkinter import ttk
from Views.Frames.TopFrame import TopFrame


class MyListings(ttk.Frame):
    # attributes :
    # - Create a Listing button (opens popup window)
    # - Edit a Listing button (opens popup window)
    # - "Show Listing Search" button
    # - Paginated list of current SellListings to the left
    # - Paginated list of current BuyListings to the right

    def __init__(self, master):
        ttk.Frame.__init__(self, master)

        self.frm_dummy = ttk.Frame(
            master=self, width=900, height=600, relief=RIDGE)
        self.frm_dummy.pack()
        self.frm_dummy.pack_propagate(0)
