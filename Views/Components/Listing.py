from tkinter import *
from tkinter import ttk
from Models.Item import Item
from abc import ABC, abstractmethod


class Listing(ttk.Frame, ABC):
    """Represents a Listing UI object"""

    def __init__(self, master, traceback, item):
        ttk.Frame.__init__(self, master, relief=RIDGE)

        self.master = master
        self.traceback = traceback
        self.item = item

        for i in range(6):
            self.columnconfigure(i, weight=1, minsize=125)

        self.seller_id = self.item.get_seller_id
        self.name = self.item.get_name
        self.type = self.item.get_type
        self.min_bid = self.item.get_minimum_bid
        self.highest_bid = self.item.get_highest_bid if self.item.get_highest_bid is not None else 0
        self.buyer_id = self.item.get_buyer_id

        self.frm_id = ttk.Frame(self)
        self.frm_name = ttk.Frame(self)
        self.frm_type = ttk.Frame(self)
        self.frm_min_bid = ttk.Frame(self)
        self.frm_highest_bid = ttk.Frame(self)
        self.frm_select = ttk.Frame(self)

        self.init_item_name()
        self.init_item_type()
        self.init_min_bid()
        self.init_highest_bid()

    def init_item_name(self):
        """Initiates the name label for the listing"""
        ttk.Label(self.frm_name, text="Name").grid(row=0, column=0)
        ttk.Label(self.frm_name, text=self.name).grid(row=1, column=0)

    def init_item_type(self):
        """Initiates the type label for the listing"""
        ttk.Label(self.frm_type, text="Type").grid(row=0, column=0)
        ttk.Label(self.frm_type, text=self.type).grid(row=1, column=0)

    def init_min_bid(self):
        """Initiates the minimum bid label for the listing"""
        ttk.Label(self.frm_min_bid, text="Minimum Bid").grid(row=0, column=0)
        ttk.Label(self.frm_min_bid, text=self.min_bid).grid(row=1, column=0)

    def init_highest_bid(self):
        """Initiates the highest bid label for the listing"""
        ttk.Label(self.frm_highest_bid, text="Highest Bid").grid(
            row=0, column=0)
        ttk.Label(self.frm_highest_bid, text=self.highest_bid).grid(
            row=1, column=0)

    @abstractmethod
    def display_account_info(self):
        """Requests the display of the account information"""
        pass
