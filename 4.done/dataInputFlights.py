import re
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
        