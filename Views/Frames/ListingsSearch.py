# From Sequence Diagrams
# Shows Search Bar and a sorted list of populated Listings (most popular first if no search has been
# conducted)

from tkinter import *
from tkinter import ttk


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
