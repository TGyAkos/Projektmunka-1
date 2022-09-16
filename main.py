from db import DbMain
from dataGet import dataGet
from uiDraw import uiDraw 
from DbManagement import DbManagement

class Main:
    def __init__(self):
        self.db = DbMain()
        self.uiDraw = uiDraw()
        self.data = dataGet()
        self.DbManagement = DbManagement()
        self.options = {
            1: "Add a record",
            2: "Save a record",
            3: "View user records",
            4: "View flight records",
            5: "Exit",
        }

    def main():
        while True:
            uiDraw.printOptions(self.options)
            self.option = int(input('Enter your choice: ')) #Should only appear when it's needed, oh well
            if self.option == 1:
                self.data.dataInput()
            elif self.option == 2:
                if self.DbManagement.saveToDb(self.data) == 0:
                    del self.data
                    self.data = dataGet()
            elif self.option == 3:
                print(self.db.getAllUser())#Refactor this it looks like shit
            elif self.option == 4:
                print(self.db.getAllFlight())#Refactor this it looks like shit
            elif self.option == 5:
                break
            else:
                print("Incorrect input!")

    if __name__ == "__main__":
        main()



'''
emberek adatai és típusai:qq`

firstName TEXT,
surName TEXT,
idNumber INT,
birthDate DATE,
postCode INT,
address TEXT

egy object-re példa

user = (
    'Adrian',
    'Huszka',
    '123456',
    'YYYY-mm-dd',
    1234,
    'Szentes xy utca 1.'
)

repülő adatai és típusai:

flightId TEXT,      // repülési azonosító
location1 TEXT,     // indulási hely
location2 TEXT,     // érkezési hely
depTime TEXT,       // indulási idő
arrTime TEXT        // érkezési idő

egy object-re példa

flight = (
    65465454,
    'ország1 város',
    'ország2 város',
    '1234',
    '1234'
)

self.db.insertUser(user)
self.db.insertFlight(flight)

for item in self.db.getAllUser():
    print(item)
    print(item[2])

for item in self.db.getAllFlight():
    print(item)
'''
