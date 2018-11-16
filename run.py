from hash import Hash
from library import Library

master = Library()

client = Hash()
client.inputUsername()
client.inputPass()

master.add(client)

print("\n")
master.printLib()

check = Hash()
logUse = input("Log in username: ")
check.setUse(logUse)
logPass = input("Log in password: ")
foundAccount = master.findAndRetHashObj(logUse)
chkSalt = foundAccount.retSalt()
check.runHash(logPass, chkSalt)
print("\n")
print(foundAccount.retHash())
print(check.retHash())
