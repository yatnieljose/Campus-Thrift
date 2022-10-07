class Receipt:
    def __init__(self, item, buyer, seller, price):
        self._item = item
        self._buyer = buyer
        self._seller = seller
        self._price = price
        
    @property
    def getItem(self):
        return(self._item)
    @getItem.setter
    def setItem(self, item):
        self._item = item
        
    @property
    def getBuyer(self):
        return(self._buyer)
    @getBuyer.setter
    def setBuyer(self, buyer):
        self._buyer = buyer
        
    @property
    def getSeller(self):
        return(self._seller)
    @getSeller.setter
    def setSeller(self, seller):
        self._seller = seller
        
    @property
    def getPrice(self):
        return(self._price)
    @getPrice.setter
    def setPrice(self, price):
        self._price = price
