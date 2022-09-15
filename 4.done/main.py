from datetime import datetime
from db import DbMain

db = DbMain()

'''
emberek adatai és típusai:

fistName TEXT,
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