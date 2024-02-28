
class Player():
    def __init__(self, name, token, isVictorious):
        self._name = name
        self._token = token
        self._isVictorious = isVictorious
    
        
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    
    @property
    def token(self):
        return self._token

    @token.setter
    def token(self, value):
        self._token = value
        
    @property
    def isVictorious(self):
        return self._isVictorious

    @isVictorious.setter
    def isVictorious(self, value):
        self._isVictorious = value
    