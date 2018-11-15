from test import Test

password = Test()
password.inputPass()
password.printHash()


checkPassword = input("Check Password: ")
password.verifyHash(checkPassword)
