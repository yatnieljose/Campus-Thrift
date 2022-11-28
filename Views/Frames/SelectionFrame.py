"""Contrains the SelectionFrame class"""

from tkinter import ttk


class SelectionFrame(ttk.Frame):
    """Represents a SelectionFrame UI object to toggle between the MyListings view and the ListingsSearch view"""

    def __init__(self, master):
        ttk.Frame.__init__(self, master)

        self.btn_my_listings = ttk.Button(
            self, text="My Listings", command=master.show_my_listings)
        self.btn_listings_search = ttk.Button(
            self, text="Listings Search", command=master.show_listings_search)

        self.btn_my_listings.pack()
        self.btn_listings_search.pack()
