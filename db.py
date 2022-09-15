import sqlite3

class DbMain:
    def __init__(self):
        self.con = sqlite3.connect('fel1.db')
        self.cur = self.con.cursor()
        self.create_table()

    def create_table(self):
        self.cur.execute("""CREATE TABLE IF NOT EXISTS userData(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            fistName TEXT,
            surName TEXT,
            idNumber TEXT,
            birthDate DATE,
            postCode INTEGER,
            address TEXT
        )""")
        self.cur.execute("""CREATE TABLE IF NOT EXISTS flight(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            flightId TEXT,
            location1 TEXT,
            location2 TEXT,
            depTime TEXT,
            arrTime TEXT
        )""")

    def insertUser(self, item):
        self.cur.execute("""
            INSERT OR IGNORE INTO userData(
                fistName,
                surName,
                idNumber,
                birthDate,
                postCode,
                address
            ) VALUES (?,?,?,?,?,?)
        """, item)
        self.con.commit()

    def insertFlight(self, item):
        self.cur.execute("""
            INSERT OR IGNORE INTO flight(
                flightId,
                location1,
                location2,
                depTime,
                arrTime
            ) VALUES (?,?,?,?,?)
        """, item)
        self.con.commit()

    def getAllUser(self):
        self.cur.execute("""SELECT * FROM userData""")
        rows = self.cur.fetchall()
        return rows

    def getAllFlight(self):
        self.cur.execute("""SELECT * FROM flight""")
        rows = self.cur.fetchall()
        return rows

    def getUserByfistName(self, fistName):
        self.cur.execute("""SELECT * FROM user WHERE fistName = ?""", fistName)
        rows = self.cur.fetchall()
        return rows