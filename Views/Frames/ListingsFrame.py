from tkinter import *
from tkinter import ttk
from TopFrame import TopFrame
from MyListings import MyListings
from ListingsSearch import ListingsSearch
import ct_tk

# main frame for MyListings and ListingsSearch
# displays MyListings by default
# includes Buttons to switch from MyListings <--> ListingSearch


class ListingsFrame(ttk.Frame):
    """Represents a ListingFrame UI object"""

    def __init__(self, master):
        ttk.Frame.__init__(self, master)

        # must declare all of these in constructor
        self.frame_top_frame = TopFrame(self)
        self.frame_my_listings = MyListings(self)
        self.frame_listings_search = ListingsSearch(self)

        self.frame_top_frame.pack(side=TOP)
        self.frame_my_listings.pack(side=TOP)

    # we can call this from MyListings
    def show_listings_search(self):
        """Shows the ListingsSearch UI object"""
        # performed when "Search Listings" button is pressed inside of MyListings
        self.frame_my_listings.destroy()
        self.frame_listings_search.pack(side=TOP)

    # we can call this from ListingsSearch
    def show_my_listings(self):
        """Shows the MyListings UI object"""
        # performed when "Show My Listings" button is pressed inside of ListingsSearch
        self.frame_listings_search.destroy()
        self.frame_my_listings.pack(side=TOP)


def main():
    root = Tk()
    ct_tk.CT_Tk(root, 'Campus Thrift')
    ListingsFrame(root).pack()
    root.mainloop()


if __name__ == "__main__":
    main()
