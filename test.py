"""
test.py
Test Object

"""
import hashlib
import uuid

class Test():
    """docstring for Test."""
    identifier = ""
    hashStr = ""
    strSalt = ""

    def __init__(self):
        super().__init__()
        self.identifier = str(uuid.uuid4())
        print("hello, test object created")

    def inputPass(self):
        password = input("Enter Password: ")
        self.runHash(password)

    def printHash(self):
        print("hash:", self.hashStr)
        print("salt:", self.identifier)

    def runHash(self, data):
        hash = hashlib.sha256(data.encode() + self.identifier.encode()).hexdigest()
        self.hashStr = hash

    def verifyHash(self, input):
        hash = hashlib.sha256(input.encode() + self.identifier.encode()).hexdigest()
        if hash == self.hashStr:
            print("correct password")
        else:
            print("incorrect password")
