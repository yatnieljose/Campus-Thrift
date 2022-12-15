# Frame that represents MyListing
# Separate tables for current user-made Listings (SellerListing)  and current Listings user has highest
# bid on (BuyerListing)

from tkinter import ttk, BOTH, LEFT, RIGHT, RIDGE
from Views.Frames.TopFrame import TopFrame
from Models.Item import Item
from Views.Components.SellListing import SellListing
from Views.Components.BuyListing import BuyListing


class MyListings(ttk.Frame):
    """Represents a MyListings UI object"""

    def __init__(self, master):
        ttk.Frame.__init__(self, master, relief=RIDGE)
        self.master = master
        self.sell_listings = []
        self.buy_listings = []

        self.frm_container = ttk.Frame(
            master=self)
        self.frm_container.grid(sticky="ns")
        self.frm_container.pack_propagate(0)

        # create frame, label, and button for Seller side
        self.frame_sell_listings = ttk.Frame(self.frm_container)
        ttk.Label(self.frame_sell_listings, text="Seller").pack(
            fill=BOTH, side=LEFT)
        self.btn_create_listing = ttk.Button(
            self.frame_sell_listings, text="+", command=self.display_create_listing_tk)
        self.btn_create_listing.pack(fill=BOTH, side=RIGHT)

        # self.frame_sell_listings.place(x=RIDGE_PAD*2, y=RIDGE_PAD*2)
        self.frame_sell_listings.grid(row=0, column=0)
        # create label for Buyer side
        ttk.Label(self.frm_container, text="Buyer").grid(row=0, column=1)
        self.display_sell_listings()
        self.display_buy_listings()

        # create series of SellListing -> BuyListing -> SellListing -> BuyListing -> SellListing -> ...
        # for loop to create pagination options for each side (each gets a frame, button, label, button)

    def display_create_listing_tk(self):
        """Calls function of ListingsFrame that creates a CreateListingTk popup window"""

        self.master.display_create_listing_tk()
        # return self.master.display_create_listing_tk()

    def display_sell_listings(self):
        """Displays the current user's item listings"""
        items = self.master.display_my_listings(True)

        for item in items:
            self.sell_listings.append(
                SellListing(self.frm_container, self, item))

        for i in range(len(self.sell_listings)):
            self.sell_listings[i].grid(row=i+1, column=0)

    def display_buy_listings(self):
        """Displays items the current user has the highest bid on"""

        items = self.master.display_my_listings(False)

        for item in items:
            self.buy_listings.append(BuyListing(
                self.frm_container, self, item))

        N = len(self.buy_listings) if len(self.buy_listings) < 9 else 9

        for i in range(N):
            # self.buy_listings.fill_labels()
            self.buy_listings[i].grid(row=i+1, column=1)

    def refresh_sell_listings(self):
        """Requests the View to re-gather sell listings"""
        # CreateAccountTk -> MainFrame -> ListingsFrame ->

        self.display_sell_listings()

    def display_account_info(self, account_id):
        """Requests the display of the account info associated with given account ID"""
        self.master.display_account_info(account_id)

    def accept_bid(self):
        pass

    def remove_listing(self):
        pass
