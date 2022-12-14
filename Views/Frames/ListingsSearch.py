"""Contains ListingsSearch class to show a search bar and a sorted list of populated listings"""

# From Sequence Diagrams
# Shows Search Bar and a sorted list of populated Listings (most popular first if no search has been
# conducted)

from tkinter import ttk, RIDGE, IntVar
from Views.Components.GenericListing import GenericListing
import Models.TypeOptions as TypeOptions


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
        ttk.Frame.__init__(self, master, relief=RIDGE)

        self.all_listings = []

        # A top frame for search bar and button
        self.frm_search = ttk.Frame(self, relief=RIDGE)
        self.frm_search.grid(row=0, column=0, columnspan=2)
        self.search_bar = None

        # a left-side frame for choosing sort and filters
        self.frm_filters = ttk.Frame(self, relief=RIDGE)
        self.frm_filters.grid(row=1, column=0)
        self.sort_var = IntVar()
        self.filter_var = []
        for i in range(len(TypeOptions.type_options)):
            self.filter_var.append(IntVar())

        # a right-side frame showing all relevant listings
        self.frm_listings = ttk.Frame(self, relief=RIDGE)
        self.frm_listings.grid(row=1, column=1)

        # fill each
        self.fill_search()
        self.fill_filters()
        self.display_all_listings()

    def fill_search(self):
        """Fills the top frame with a search bar and button"""

        self.search_bar = ttk.Entry(self.frm_search).grid(row=0, column=0)
        ttk.Button(self.frm_search, text="Search",
                   command=self.search).grid(row=0, column=1)

    def fill_filters(self):
        """Fills the bottom-left frame with various sorting and filtering options"""

        # sort price from highest <--> lowest (can only pick one)
        ttk.Radiobutton(self.frm_filters, text="Sort by Price (Lowest to Highest)",
                        variable=self.sort_var, value=1, command=self.chosen_sort).grid(row=0, column=0)
        ttk.Radiobutton(self.frm_filters, text="Sort by Price (Highest to Lowest)",
                        variable=self.sort_var, value=2, command=self.chosen_sort).grid(row=1, column=0)

        # create a checkbox for every type_option. Can choose as many or as few
        for i in range(len(TypeOptions.type_options)):
            ttk.Checkbutton(self.frm_filters, text=f"{TypeOptions.type_options[i]}", variable=self.filter_var[i],
                            onvalue=1, offvalue=0, command=self.chosen_filter).grid(row=2+i, column=0)

    def display_all_listings(self):
        """Displays the listings of items available for sale"""

        items = self.master.display_all_listings()

        for item in items:
            self.all_listings.append(
                GenericListing(self.frm_listings, self, item))

        for i in range(len(self.all_listings)):
            self.all_listings[i].grid(row=i, column=0)

    def chosen_sort(self):
        pass

    def chosen_filter(self):
        pass

    def search(self):
        pass

    def set_highest_bid(self, item_id, offer):
        """Requests the highest bid of a specific item be updated"""
        # GenericListing ->

        self.master.set_highest_bid(item_id, offer)

    def refresh_listings(self):
        """Re-loads fresh items from database"""

        self.all_listings = []

        for widget in self.frm_listings.winfo_children():
            widget.destroy()

        self.display_all_listings()
