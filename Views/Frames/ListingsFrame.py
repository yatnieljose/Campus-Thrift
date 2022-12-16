"""Contains ListingsFrame class for toggling between MyListings and ListingsSearch"""

from tkinter import ttk, TOP, messagebox
from Views.Frames.TopFrame import TopFrame
from Views.Frames.SelectionFrame import SelectionFrame
from Views.Frames.MyListings import MyListings
from Views.Frames.ListingsSearch import ListingsSearch

# main frame for MyListings and ListingsSearch
# displays MyListings by default
# includes Buttons to switch from MyListings <--> ListingSearch


class ListingsFrame(ttk.Frame):
    """Represents a ListingFrame UI object"""
    # Main -> MainFrame

    def __init__(self, master):
        ttk.Frame.__init__(self, master)
        self.my_listings_shown = True
        self.logout_option = False

        self.init_top_frame()
        self.init_selection()
        self.init_my_listings()
        self.init_listings_search()
        self.frame_listings_search.destroy()

        self.my_listings_shown = True

    def init_selection(self):
        """Initializes a SelectionFrame object and packs it into this frame"""
        self.frame_selection = SelectionFrame(self)
        self.frame_selection.pack(side=TOP, pady=10)

    def init_top_frame(self):
        """Initializes a TopFrame object and packs it into this frame"""
        self.frame_top_frame = TopFrame(self)
        self.frame_top_frame.pack(side=TOP, pady=10, padx=10)

    def init_my_listings(self):
        """Initializes a MyListings object and packs it into this frame"""
        self.frame_my_listings = MyListings(self)
        self.frame_my_listings.pack(side=TOP, pady=10, padx=10)

    def init_listings_search(self):
        """Initializes a ListingsSearch object and packs it into this frame"""
        self.frame_listings_search = ListingsSearch(self)
        self.frame_listings_search.pack(side=TOP, pady=10, padx=10)

    def show_listings_search(self):
        """Shows the ListingsSearch UI object"""
        # performed when "Search Listings" button is pressed inside of MyListings
        if self.my_listings_shown:
            self.frame_my_listings.destroy()
            self.init_listings_search()
            self.my_listings_shown = False

    def show_my_listings(self):
        """Shows the MyListings UI object"""
        # performed when "Show My Listings" button is pressed inside of ListingsSearch
        if not self.my_listings_shown:
            self.frame_listings_search.destroy()
            self.init_my_listings()
            self.my_listings_shown = True

    def display_manage_account_tk(self):
        """Displays the Manage Account window when called"""
        # TopFrame ->

        self.master.display_manage_account_tk()

    def display_my_listings(self, seller):
        """Displays the listings of the current user"""
        # MyListings ->
        return self.master.get_items(seller)

    def display_all_listings(self):
        """Displays the listings of items available for sale"""
        # ListingsSearch ->
        return self.master.get_all_items()

    def refresh_sell_listings(self):
        """Refreshes sell listings after a new item is created by the user. Can only be called when 
        MyListings is in control"""
        # CreateAccountTk -> MainFrame ->

        self.frame_my_listings.refresh_sell_listings()

    def logout(self):
        self.master.logout()

    def display_create_listing_tk(self):
        """Calls this method in MainFrame to create a CreateListingTk popup window"""
        # MyListings ->

        self.master.display_create_listing_tk()

    def get_rank(self):
        return self.master.get_rank()

    def get_completed_transactions(self):
        return self.master.get_completed_transactions()

    def set_highest_bid(self, item_id, offer):
        """Requests an update to the highest bid on specified item"""
        # GenericListing -> ListingsSearch ->

        self.master.set_highest_bid(item_id, offer)

    def display_account_info(self, account_id):
        """Requests the display of the account info associated with given account ID"""
        self.master.display_account_info(account_id)

    def accept_bid(self, sold_item):
        # SellListing -> MyListings ->
        self.master.accept_bid(sold_item)

    def delete_item(self, item):
        # SellListing -> MyListings
        """Deletes the item"""
        self.master.delete_item(item)