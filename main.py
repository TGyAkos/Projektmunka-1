
from db import DbMain #Refactor this it looks like shit
from dataGet import dataGet
from uiDraw import uiDraw 
from DbManagement import DbManagement

db = DbMain()
uiDraw = uiDraw()
data = dataGet()
DbManagement = DbManagement()

options = {
    1: "Add a record",
    2: "Save a record",
    3: "View user records",
    4: "View flight records",
    5: "Exit",
}

while True:
    uiDraw.printOptions(options)
    option = int(input('Enter your choice: ')) #Should only appear when it's needed, oh well
    if option == 1:
        data.dataInput()
    elif option == 2:
        DbManagement.saveToDb(data)
    elif option == 3:
        print(db.getAllUser())
    elif option == 4:
        print(db.getAllFlight())
    elif option == 5:
        break
    else:
        print("Incorrect input!")

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

db.insertUser(user)
db.insertFlight(flight)

for item in db.getAllUser():
    print(item)
    print(item[2])

for item in db.getAllFlight():
    print(item)
'''