"""
test.py
Test Object

"""
import hashlib
import uuid


class Hash():
    """docstring for Test."""
    identifier = ""
    hashStr = ""
    strSalt = ""
    username = ""

    def __init__(self):
        super().__init__()
        self.identifier = str(uuid.uuid4())
        """print("hello, test object created")"""

    def inputPass(self):
        password = input("Enter Password: ")
        self.runHash(password)

    def inputUsername(self):
        use = input("Enter Username: ")
        self.username = use

    def printHash(self):
        print("username:", self.username)
        print("hash:", self.hashStr)
        print("salt:", self.identifier)

    def retUse(self):
        return self.username

    def setUse(self, data):
        self.username = data

    def retHash(self):
        return self.hashStr

    def retSalt(self):
        return self.identifier

    def runHash(self, data):
        dataString = data.encode() + self.identifier.encode()
        hash = hashlib.sha256(dataString).hexdigest()
        self.hashStr = hash

    def verifyHash(self, input):
        dataString = input.encode() + self.identifier.encode()
        hash = hashlib.sha256(dataString).hexdigest()
        if hash == self.hashStr:
            print("correct password")
        else:
            print("incorrect password")
