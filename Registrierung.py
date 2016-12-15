import os

class Register():

    def __init__(self, username, passwort):
        self.username = username
        self.passwort = passwort

    def write_registration(self):
        openFile = open("/root/users.txt", "a")
        openFile.write(self.username + ", " + self.passwort + " \n")
        openFile.close()

    def check_registration(self):
        open_file = open("/root/users.txt", "r")
        read_file = open_file.read()
        print(read_file)


username = input("Username\n")
passwort = input("Passwort\n")

r = Register(username, passwort)
r.write_registration()
r.check_registration()
