"""
library of hashed passwords and their accompanying usernames
"""


class Library():

    hashes = []

    def __init__(self):
        super().__init__()
        """print("hello, library object created")"""

    def add(self, hashObj):
        self.hashes.append(hashObj)
        """print("added")"""

    def printLib(self):
        for i in range(len(self.hashes)):
            print("username:", self.hashes[i].username)
            print("hash:", self.hashes[i].hashStr)

    def findAndRetHashObj(self, data):
        for i in range(len(self.hashes)):
            if data == self.hashes[i].username:
                print("found:", self.hashes[i].username)
                print("found hash:", self.hashes[i].hashStr)
                return self.hashes[i]
