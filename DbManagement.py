from db import DbMain
from uiDraw import uiDraw

db = DbMain()
uiDraw = uiDraw()

options = {
    1: "Save user data",
    2: "Save flight data",
    3: "View pending changes",
    4: "Unstage changes",
    5: "Back",
}


class DbManagement:
    
    db.create_table()

    def saveToDb(self, allDataInput):
        allUserDataInput = allDataInput.dataInputPeople
        allFlightDataInput = allDataInput.dataInputFlights

        a = bool(allUserDataInput.__dict__)

        if not bool(allUserDataInput.__dict__) or not bool(allFlightDataInput.__dict__):
            print("\nEnter a record first.")
            return

        while True:
            uiDraw.printOptions(options)
            option = int(input('Enter your choice: '))
            if option == 1:
                self.saveUser(allUserDataInput)
                break
            elif option == 2:
                self.saveFlight(allFlightDataInput)
                break
            elif option == 3:
                self.viewChanges(allUserDataInput, allFlightDataInput)
            elif option == 4:
                print("Currently not avaible")
            elif option == 5:
                break
            else:
                print("Incorrect input!")

           
        
    def saveUser(self, allUserDataInput):
        db.insertUser((
            allUserDataInput.firstName, 
            allUserDataInput.surName ,
            allUserDataInput.idNumber ,
            allUserDataInput.birthDate ,
            allUserDataInput.postCode , 
            allUserDataInput.address ,
        ))
        print("Saved")

    def saveFlight(self, allFlightDataInput):
        db.insertFlight((
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