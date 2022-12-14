from db import DbMain
from uiDraw import uiDraw

class DbManagement:
    def __init__(self):
        self.db = DbMain()
        self.uiDraw = uiDraw()
        self.options = {
            1: "Save user data",
            2: "Save flight data",
            3: "View pending changes",
            4: "Unstage changes",
            5: "Back",
        }

        self.db.create_table()

    def saveToDb(self, allDataInput):
        allUserDataInput = allDataInput.dataInputPeople
        allFlightDataInput = allDataInput.dataInputFlights

        if bool(allUserDataInput.__dict__) or bool(allFlightDataInput.__dict__):
            while True:
                self.uiDraw.printOptions(self.options)
                self.option = int(input('Enter your choice: '))
                if self.option == 1:
                    self.saveUser(allUserDataInput)
                    return 0
                elif option == 2:
                    self.saveFlight(allFlightDataInput)
                    return 0
                elif option == 3:
                    self.viewChanges(allUserDataInput, allFlightDataInput)
                elif option == 4:
                    print("Currently not avaible")
                elif option == 5:
                    break
                else:
                    print("Incorrect input!")
                return

        print("\nEnter a record first.")

    def saveUser(self, allUserDataInput):
        self.db.insertUser((
            allUserDataInput.firstName, 
            allUserDataInput.surName ,
            allUserDataInput.idNumber ,
            allUserDataInput.birthDate ,
            allUserDataInput.postCode , 
            allUserDataInput.address ,
        ))
        print("Saved")

    def saveFlight(self, allFlightDataInput):
        self.db.insertFlight((
            allFlightDataInput.flightId ,
            allFlightDataInput.location1 ,
            allFlightDataInput.location2 ,
            allFlightDataInput.depTime ,
            allFlightDataInput.arrTime ,
        ))
        print("Saved")
        
    def viewChanges(self, allUserDataInput, allFlightDataInput):
        print(str(allUserDataInput.__dict__))
        print(str(allFlightDataInput.__dict__))