import asyncio

class uiDraw:
    def printOptions(self, optionDict):
        for key, value in optionDict.items():
            if key == 1:
                print("\n{}. - {}".format(key, value))
            else:
                print("{}. - {}".format(key, value))
    def printResponses(self, optionDict, firstResponseFunction, secondResponseFunction):
        """Not Operational / Do async"""
        while True:
                self.printOptions(optionDict)
                option = int(input('Enter your choice: '))
                if option == 1:
                    firstResponseFunction()
                elif option == 2:
                    secondResponseFunction()
                elif option == 3:
                    break
                elif option == 4:
                    exit(0)
                else:
                    print("Incorrect input!")