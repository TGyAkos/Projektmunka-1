def printOptions(optionDict):
    for key, value in optionDict.items():
        if key == 1:
            print("\n{}. - {}".format(key, value))
        else:
            print("{}. - {}".format(key, value))

def matchCaseOptionOne():
    print("matchCaseOptionOne")
def matchCaseOptionTwo():
    print("matchCaseOptionTwo")
def matchCaseOptionThree():
    print("matchCaseOptionThree")

options = {
    1: 'Ember',
    2: 'Jarat',
    3: 'Tovabb',
    4: 'Kilepes',
}

x = True
while x == True:
    printOptions(options)
    option = int(input('Enter your choice: '))
    if option == 1:
        matchCaseOptionOne()
    elif option == 2:
        matchCaseOptionTwo()
    elif option == 3:
        matchCaseOptionThree()
    elif option == 4:
        exit(0)
    else:
        print("Nem jo input")
