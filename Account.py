class Account:
    def __init__(self, name, email, bio="NONE"):
            self._name = name
            self._email = email
            self._bio = bio
            completedTrans = []
            
    @property
    def name(self):
        return(self._name)
    def email(self):
        return(self._email)
    def bio(self):
        return(self._bio)
    
    @name.setter
    def name(self, newName):
        self._name = newName
    @email.setter
    def email(self, newEmail):
        self._email = newEmail
    @bio.setter
    def bio(self, newBio):
        self._bio = newBio
