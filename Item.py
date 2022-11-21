"""Contains the Item class"""


class Item:
    """Represents an Item object created by a user to sell"""

    def __init__(self, item_id, seller, price, name, typ, listing):
        self._item_id = item_id
        self._seller = seller
        self._price = price
        self._name = name
        self._typ = typ
        self._listing = listing
        self._offers = []  # object Transaction? Bid?

    @property
    def get_item_id(self):
        """Gets the item ID associated with the current Item object"""
        return (self._item_id)

    @property
    def get_seller(self):
        """Gets the seller Account associated with the current Item object"""
        return (self._seller)

    @get_seller.setter
    def set_seller(self, seller):
        self._seller = seller

    @property
    def get_price(self):
        """Gets the price associated with the current Item object"""
        return (self._price)

    @get_price.setter
    def set_price(self, price):
        self._price = price

    @property
    def get_name(self):
        """Gets the name associated with the current Item object"""
        return (self._name)

    @get_name.setter
    def set_name(self, name):
        self._name = name

    @property
    def get_type(self):
        """Gets the type associated with the current Item object"""
        return (self._typ)

    @get_type.setter
    def set_type(self, typ):
        self._typ = typ

    @property
    def get_offers(self):  # data type discussion
        """Gets offers for the current Item object"""
        return (0)

    # createListing

    @property
    def get_listing(self):
        """Gets Listing UI object associated with the current Item object"""
        return (0)

    # createOffer
