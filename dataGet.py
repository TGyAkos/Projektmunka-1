import re
from datetime import datetime
from uiDraw import uiDraw

class dataGet:
    def __init__(self):
        self.dataInputPeople = dataInputPeople()
        self.dataInputFlights = dataInputFlights()
        self.uiDraw = uiDraw()
        self.options = {
            1: 'People',
            2: 'Flight',
            3: 'Back',
        } 

    def dataInput(self):
        #do it with async
        #uiDraw.printOptions(self.options,self.dataInputPeople.getInputPeopleData(), self.dataInputFlights.getInputFlightsData())            
        while True:
            self.uiDraw.printOptions(self.options)
            option = int(input('Enter your choice: '))
            if option == 1:
                self.dataInputPeople.getInputPeopleData()
            elif option == 2:
                self.dataInputFlights.getInputFlightsData()
            elif option == 3:
                break
            else:
                print("Incorrect input!")

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
        while not re.match("[A-Za-zzáéúőóüöí]", self.firstName):
            self.firstName = input("Incorrect first name, type in again!\n")

        self.surName = input("Type in your surame!\n")
        while not re.match("[A-Za-zzáéúőóüöí]", self.surName):
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

        self.address = input("Type in your address!\n") 
        while not re.match("^\w{1,}$", self.address):
            self.address = input("Incorrect address, type in again!\n")

class dataInputFlights:
    def __init__(self):
        self.flightId: str
        self.location1: str
        self.location2: str
        self.depTime: str
        self.arrTime: str
    def getInputFlightsData(self):
        self.flightId = input("Type in the flight ID\n")
        while not re.match("^\d{8}$", self.flightId):
            self.flightId = input("Incrorrect flight ID, type in again!\n")

        self.location1 = input("Type in the departure place!\n")
        while not re.match("^\w{1,} \w{1,}$", self.location1):
            self.location1 = input("Incrorrect departure place, type in again!\n")

        self.location2 = input("Type in the arrival place!\n")
        while not re.match("^\w{1,} \w{1,}$", self.location2):
            self.location2 = input("Incrorrect arrival place, type in again!\n")

        self.depTime = input("Type in the departure time!\n")
        while not re.match("^\d{2}:\d{2}$", self.depTime):
            self.depTime = input("Incrorrect departure time, type in again\n")

        self.arrTime = input("Type in the arrival time!\n")
        while not re.match("^\d{2}:\d{2}$", self.arrTime):
            self.arrTime = input("Incorrect arrival time, type in again!")