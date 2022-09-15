from dataInputPeople import dataInputPeople
from dataInputFlights import dataInputFlights

options = {
    1: 'People',
    2: 'Flight',
    3: 'Continue',
    4: 'Exit',
}

dataInputPeople = dataInputPeople()
dataInputFlights = dataInputFlights()

def printOptions(optionDict):
    for key, value in optionDict.items():
        if key == 1:
            print("\n{}. - {}".format(key, value))
        else:
            print("{}. - {}".format(key, value))


def matchCaseOptionOne():
    dataInputPeople.getInputPeopleData()
def matchCaseOptionTwo():
    dataInputFlights.getInputFlightsData()

while True:
    printOptions(options)
    option = int(input('Enter your choice: '))
    if option == 1:
        matchCaseOptionOne()
    elif option == 2:
        matchCaseOptionTwo()
    elif option == 3:
        break
    elif option == 4:
        exit(0)
    else:
        print("Incorrect input!")