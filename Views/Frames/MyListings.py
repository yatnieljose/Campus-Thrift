# Frame that represents MyListing
# Separate tables for current user-made Listings (SellerListing)  and current Listings user has highest
# bid on (BuyerListing)

from tkinter import ttk, BOTH, LEFT, RIGHT, RIDGE
from Views.Frames.TopFrame import TopFrame
from Models.Item import Item
from Views.Components.SellListing import SellListing

RIDGE_PAD = 2

class MyListings(ttk.Frame):
    """Represents a MyListings UI object"""

    def __init__(self, master):
        ttk.Frame.__init__(self, master)
        self.master = master

        self.frm_container = ttk.Frame(
            master=self, width=900, height=550, relief=RIDGE)
        self.frm_container.grid(sticky="ns")
        self.frm_container.pack_propagate(0)

        # create frame, label, and button for Seller side
        self.frame_sell_listings = ttk.Frame(self)
        ttk.Label(self.frame_sell_listings, text="Seller").pack(
            fill=BOTH, side=LEFT)
        self.btn_create_listing = ttk.Button(
            self.frame_sell_listings, text="+", command=self.display_create_listing_tk)
        self.btn_create_listing.pack(fill=BOTH, side=RIGHT)

        self.frame_sell_listings.place(x=RIDGE_PAD*2,y=RIDGE_PAD*2)
        self.display_users_listings(self.frm_container)

        # create label for Buyer side
        ttk.Label(self, text="Buyer").grid(row=0, column=1)

        # create series of SellListing -> BuyListing -> SellListing -> BuyListing -> SellListing -> ...
        # for loop to create pagination options for each side (each gets a frame, button, label, button)

    def display_create_listing_tk(self):
        """Calls function of ListingsFrame that creates a CreateListingTk popup window"""
        
        self.master.display_create_listing_tk()
        self.display_users_listings(self.frm_container)
        #return self.master.display_create_listing_tk()

    def display_users_listings(self, container):
        """Displays the current user's item listings"""
        items = self.master.display_users_listings()
        for i in range(len(items)):
            self.frame_sell_listings.place(x=RIDGE_PAD, y=55*(i+1)+RIDGE_PAD)
            listing = SellListing(container)#, items[i].get_name, items[i].get_type, items[i].get_minimum_bid).place(x=RIDGE_PAD, y=RIDGE_PAD+(i*55))
            listing.place(x=RIDGE_PAD, y=RIDGE_PAD+(i*55))
            # second index accesses the data points of the item
            # 0 - item name, 1 - item type, 2 - item min bid
            listing.fill_labels(items[i][0], items[i][1], items[i][2])
        