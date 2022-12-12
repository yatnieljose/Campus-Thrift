# Frame that represents MyListing
# Separate tables for current user-made Listings (SellerListing)  and current Listings user has highest
# bid on (BuyerListing)

from tkinter import ttk, BOTH, LEFT, RIGHT, RIDGE
from Views.Frames.TopFrame import TopFrame


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

        self.frame_sell_listings.grid(row=0, column=0)

        # create label for Buyer side
        ttk.Label(self, text="Buyer").grid(row=0, column=1)

        # create series of SellListing -> BuyListing -> SellListing -> BuyListing -> SellListing -> ...
        # for loop to create pagination options for each side (each gets a frame, button, label, button)

    def display_create_listing_tk(self):
        """Calls function of ListingsFrame that creates a CreateListingTk popup window"""

        return self.master.display_create_listing_tk()
