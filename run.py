from hash import Hash
from library import Library

master = Library()

client = Hash()
client.inputUsername()
client.inputPass()

master.add(client.retUse(), client.retHash(), client.retSalt())

print("\n")
master.printLib()

check = Hash()
logUse = input("Log in username: ")
check.setUse(logUse)
logPass = input("Log in password: ")
check.runHash(logPass)

print(master.findAndRetHash(logUse))
print(check.retHash())
"""
if master.findAndRetHash(logUse) == check.retHash():
    print("login successful")
"""
