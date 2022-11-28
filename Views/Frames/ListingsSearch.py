"""Contains ListingsSearch class to show a search bar and a sorted list of populated listings"""

# From Sequence Diagrams
# Shows Search Bar and a sorted list of populated Listings (most popular first if no search has been
# conducted)

from tkinter import ttk, GROOVE


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
