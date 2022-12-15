from tkinter import *
from tkinter import ttk
from Views.Components.Listing import Listing

RIDGE_PAD = 2


class BuyListing(Listing):
    def __init__(self, master, traceback, item):
        super().__init__(master, traceback, item)

        self.frm_id.grid(row=0, column=0)
        self.frm_name.grid(row=0, column=1)
        self.frm_type.grid(row=0, column=2)
        self.frm_min_bid.grid(row=0, column=3)
        self.frm_highest_bid.grid(row=0, column=4)
        self.frm_select.grid(row=0, column=5)

        self.init_seller_id()
        self.init_select()

    def init_seller_id(self):
        """Initiates the seller ID label for the listing"""
        ttk.Label(self.frm_id, text="Seller ID").grid(row=0, column=0)
        ttk.Button(self.frm_id, text=self.seller_id,
                   command=self.display_account_info).grid(row=1, column=0)

    def init_select(self):
        """Initiates the Select button for the listing"""
        ttk.Button(self.frm_select, text="Raise Offer",
                   command=self.raise_offer).grid(row=0, column=0)
        ttk.Button(self.frm_select, text="Remove Offer",
                   command=self.remove_offer).grid(row=1, column=0)

    def display_account_info(self):
        """Requests the information from the seller account in the form of a popup window"""
        self.traceback.display_account_info(self.seller_id)

    def raise_offer(self):
        pass

    def remove_offer(self):
        pass
