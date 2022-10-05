class Account:
    def __init__(self, name, email, bio="NONE"):
            self._name = name         #str
            self._email = email       #str
            self._bio = bio           #str
            self._rank = 1            #int
            self._profilePicture = "" #str of the picture path, default needed
            self._numRejected = 0     #int
            self._completedTrans = [] #list
            self._listedItems = []    #list
            
    @property
    def getName(self):
        return(self._name)
    @getName.setter
    def setName(self, newName):
        self._name = newName
        
    @property
    def getEmail(self):
        return(self._email)
    @getEmail.setter
    def setEmail(self, newEmail):
        self._email = newEmail
        
    @property
    def getBio(self):
        return(self._bio)
    @getBio.setter
    def setBio(self, newBio):
        self._bio = newBio
        
    @property
    def getRank(self):
        return(self._rank)
    @getRank.setter
    def setRank(self, newRank):
        self._rank = newRank
        
    @property
    def getProfilePicture(self):
        return(self._profilePicture)
    @getProfilePicture.setter
    def setProfilePicture(self, newPicture):
        self._profilePicture = newPicture
        
    @property
    def numOfRejected(self):
        return(self._numRejected)
    def incNumOfRejected(self):
        self._numRejected += 1
    def decNumOfRejected(self):
        if self._numRejected != 0:
            self._numRejected -= 1
            
    @property
    def numOfCompleted(self):
        return(len(self._completedTrans))
    def addItem(self, item):
        self._completedTrans.append(item)
