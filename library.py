"""
library of hashed passwords and their accompanying usernames
"""


class Library():

    usernames = []
    hashes = []
    salts = []

    def __init__(self):
        super().__init__()
        """print("hello, library object created")"""

    def add(self, use, hash, salt):
        self.usernames.append(use)
        self.hashes.append(hash)
        self.salts.append(salt)
        print("added")

    def printLib(self):
        for i in range(len(self.usernames)):
            print("username:", self.usernames[i])
            print("hash:", self.hashes[i])

    def findAndRetHash(self, data):
        for i in range(len(self.usernames)):
            if data == self.usernames[i]:
                print("found:", self.usernames[i])
                print("found hash:", self.hashes[i])
                return self.hashes[i]
