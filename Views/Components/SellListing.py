from tkinter import *
from tkinter import ttk
from Views.Components.Listing import Listing

RIDGE_PAD = 2


class SellListing(Listing):
    def __init__(self, master, traceback, item):
        super().__init__(master, traceback, item)

        self.frm_name.grid(row=0, column=0)
        self.frm_type.grid(row=0, column=1)
        self.frm_min_bid.grid(row=0, column=2)
        self.frm_highest_bid.grid(row=0, column=3)
        self.frm_id.grid(row=0, column=4)
        self.frm_select.grid(row=0, column=5)

        self.init_buyer_id()
        self.init_select()

    def init_buyer_id(self):
        """Initiates the buyer ID of highest bidder label for the listing"""
        ttk.Label(self.frm_id, text="Buyer ID").grid(row=0, column=0)
        ttk.Button(self.frm_id, text=self.buyer_id,
                   command=self.display_account_info).grid(row=1, column=0)

    def init_select(self):
        """Initiates the Select button for the listing"""
        ttk.Button(self.frm_select, text="Accept Offer",
                   command=self.accept_offer).grid(row=0, column=0)
        ttk.Button(self.frm_select, text="Remove Listing",
                   command=self.remove_listing).grid(row=1, column=0)

    def display_account_info(self):
        """Requests the information from the buyer account in the form of a popup window"""
        self.traceback.display_account_info(self.buyer_id)

    def accept_offer(self):
        pass

    def remove_listing(self):
        pass
