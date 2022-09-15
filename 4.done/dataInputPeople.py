import re
from datetime import datetime
class dataInputPeople:
    def __init__(self):
        self.firstName: str
        self.surName: str
        self.idNumber: int
        self.birthDate: str
        self.postCode: int
        self.address: str
    def getInputPeopleData(self):
        self.firstName = input("Type in your first name!\n")
        while not re.match("[A-Za-zzáéúőóüö]", self.firstName):
            self.firstName = input("Incorrect first name, type in again!\n")

        self.surName = input("Type in your surame!\n")
        while not re.match("[A-Za-zzáéúőóüö]", self.surName):
            self.surName = input("Incorrect surname, type in again!\n")

        self.idNumber = input("Type in your ID number!\n")
        while not re.match("^\d{6}$", self.idNumber):
            self.idNumber = input("Incorrect ID number, type in again!\n")

        self.birthDate = input("Type in your birth date!\n")
        while True:
            try:
                self.birthDate = datetime.strptime(self.birthDate,"%Y-%m-%d")
                break
            except ValueError:
                self.birthDate = input(" Incorrect birth date, type in again!\n")

        self.postCode = input("Type in your postcode!\n")
        while not re.match("^\d{4}$", self.postCode):
            self.postCode = input("Incorrect postcode, type in again!\n")

        self.address = input("Type in your adress!\n")
