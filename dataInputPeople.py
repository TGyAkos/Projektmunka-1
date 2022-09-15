class dataInputPeople:
    def __init__(self):
        self.firstName: str
        self.surName: str
        self.idNumber: int
        self.birthDate: str
        self.postCode: int
        self.address: str
        self.checkInputPeopleData()
    def getInputPeopleData(self):
        self.firstName = input("firstName\n")
        self.surName = input("surName\n")
        self.idNumber = input("idNumber\n")
        self.birthDate = input("birthDate\n")
        self.postCode = input("postCode\n")
        self.address = input("address\n")
    def checkInputPeopleData(self):
