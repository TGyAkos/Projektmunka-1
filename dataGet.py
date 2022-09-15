from dataInputPeople import dataInputPeople

options = {
    1: 'Ember',
    2: 'Jarat',
    3: 'Tovabb',
    4: 'Kilepes',
}
dataInputPeople = dataInputPeople()
lista = []
lista1 = []

def printOptions(optionDict):
    for key, value in optionDict.items():
        if key == 1:
            print("\n{}. - {}".format(key, value))
        else:
            print("{}. - {}".format(key, value))


def matchCaseOptionOne():
    print("matchCaseOptionOne")
    try:
        dataInputPeople.getInputPeopleData()
    except:
        print('nem jo')
        matchCaseOptionOne()
    print(dataInputPeople)
def matchCaseOptionTwo():
    print("matchCaseOptionTwo")
def matchCaseOptionThree():
    print("matchCaseOptionThree")

while True:
    printOptions(options)
    option = int(input('Enter your choice: '))
    if option == 1:
        matchCaseOptionOne()
    elif option == 2:
        matchCaseOptionTwo()
    elif option == 3:
        matchCaseOptionThree()
        break
    elif option == 4:
        exit(0)
    else:
        print("Nem jo input")