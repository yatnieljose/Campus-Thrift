class Item:
    def __init__(self, itemID, seller, price, name, typ, listing):
        self._itemID = itemID
        self._seller = seller
        self._price = price
        self._name = name
        self._typ = typ
        self._listing = listing
        self._offers = [] ### object Transaction? Bid?
    
    @property
    def getItemID(self):
        return(self._itemID)
    
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
        
    @property
    def getName(self):
        return(self._name)
    @getName.setter
    def setName(self, name):
        self._name = name
        
    @property
    def getType(self):
        return(self._typ)
    @getType.setter
    def setType(self, typ):
        self._typ = typ
        
    @property
    def getOffers(self): #data type discussion
        return(0)
    
    ### createListing
    
    @property
    def getListing(self):
        return(0)
    
    ### createOffer
    
