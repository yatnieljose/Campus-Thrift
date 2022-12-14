from Views.Components.Listing import Listing
from tkinter import ttk
import Models.Validator as Validator


class GenericListing(Listing):
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
                   command=self.get_seller_account_info).grid(row=1, column=0)

    def init_select(self):
        """Initiates the Select button for the listing"""
        self.entry_offer = ttk.Entry(self.frm_select)
        self.entry_offer.grid(row=0, column=0)
        ttk.Button(self.frm_select, text="Make Offer",
                   command=self.make_offer).grid(row=1, column=0)

    def get_seller_account_info(self):
        pass

    def make_offer(self):
        offer = self.entry_offer.get()
        if Validator.validate_offer(self.min_bid, self.highest_bid, offer):
            self.traceback.set_highest_bid(self.item.get_item_id, offer)
            self.traceback.refresh_listings()
