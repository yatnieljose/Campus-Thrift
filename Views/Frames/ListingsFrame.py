from tkinter import *
from tkinter import ttk
from Views.Frames.TopFrame import TopFrame
from Views.Frames.SelectionFrame import SelectionFrame
from Views.Frames.MyListings import MyListings
from Views.Frames.ListingsSearch import ListingsSearch
import ct_tk

# main frame for MyListings and ListingsSearch
# displays MyListings by default
# includes Buttons to switch from MyListings <--> ListingSearch


class ListingsFrame(ttk.Frame):
    """Represents a ListingFrame UI object"""

    def __init__(self, master):
        ttk.Frame.__init__(self, master)
        self.my_listings_shown = True

        self.init_top_frame()
        self.init_selection()
        self.init_my_listings()
        self.init_listings_search()
        self.frame_listings_search.destroy()

        self.my_listings_shown = True

    def init_selection(self):
        self.frame_selection = SelectionFrame(self)
        self.frame_selection.pack(side=TOP, pady=10)

    def init_top_frame(self):
        self.frame_top_frame = TopFrame(self)
        self.frame_top_frame.pack(side=TOP, pady=10, padx=10)

    def init_my_listings(self):
        self.frame_my_listings = MyListings(self)
        self.frame_my_listings.pack(side=TOP, pady=10, padx=10)

    def init_listings_search(self):
        self.frame_listings_search = ListingsSearch(self)
        self.frame_listings_search.pack(side=TOP, pady=10, padx=10)

    # we can call this from MyListings
    def show_listings_search(self):
        """Shows the ListingsSearch UI object"""
        # performed when "Search Listings" button is pressed inside of MyListings
        if self.my_listings_shown:
            self.frame_my_listings.destroy()
            self.init_listings_search()
            self.my_listings_shown = False

    # we can call this from ListingsSearch
    def show_my_listings(self):
        """Shows the MyListings UI object"""
        # performed when "Show My Listings" button is pressed inside of ListingsSearch
        if not self.my_listings_shown:
            self.frame_listings_search.destroy()
            self.init_my_listings()
            self.my_listings_shown = True


def main():
    root = Tk()
    ct_tk.CT_Tk(root, 'Campus Thrift')
    ListingsFrame(root).pack()
    root.mainloop()


if __name__ == "__main__":
    main()
