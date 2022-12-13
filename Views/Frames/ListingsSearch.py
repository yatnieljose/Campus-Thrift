"""Contains ListingsSearch class to show a search bar and a sorted list of populated listings"""

# From Sequence Diagrams
# Shows Search Bar and a sorted list of populated Listings (most popular first if no search has been
# conducted)

from tkinter import ttk, GROOVE
from Views.Components.BuyListing import BuyListing

RIDGE_PAD = 2

class ListingsSearch(ttk.Frame):
    """Represents a ListingsSearch UI object"""
    # attributes :
    # - Search Bar to type keywords into
    # - "Search" button
    # - "Show My Listings" button
    # - Paginated list of presorted Listings (10 per page or whatever looks cool)
    # - Next page, previous page buttons (think about how Google does pagination)
    # - Side bar with various sorting options (radio boxes?), like type, price highest to lowest, etc

    def __init__(self, master):
        ttk.Frame.__init__(self, master)

        self.frm_container = ttk.Frame(
            master=self, width=1400, height=550, relief=GROOVE)
        self.frm_container.grid(sticky="ns")
        self.frm_container.pack_propagate(0)

        self.display_item_listings(self.frm_container)

    def display_item_listings(self, container):
        """Displays the listings of items available for sale"""
        items = self.master.display_item_listings()
        for i in range(len(items)):
            listing = BuyListing(container)
            listing.place(x=RIDGE_PAD, y=RIDGE_PAD+(i*55))
            listing.fill_labels(items[i][0], items[i][1], items[i][2])