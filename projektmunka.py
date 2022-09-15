lista = []
lista1 =[]

def ppl():
    lista.append(input("FirstName: "))
    lista.append(input("SurName: "))
    lista.append(int(input("IdNumber: ")))
    lista.append(input("BirthDate: "))
    lista.append(int(input("PostCode: ")))
    lista.append(input("Address: "))
ppl()


def flights():
    lista1.append(input("flightId: "))
    lista1.append(input("location1: "))
    lista1.append(input("location2: "))
    lista1.append(input("depTime: "))
    lista1.append(input("arrTime: "))
flights()

print(lista,lista1)