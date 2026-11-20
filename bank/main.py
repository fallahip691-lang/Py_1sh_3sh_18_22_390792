
from add import *
from find import *
from charge import *
from delete import *

bank={}


while True:
    menu = input("1.add 2.find 3.charge 4.delete 5.exit: ")

    match menu:
        case "1":
            name = input("name: ")
            shomare_hesab = input("shomare hesab: ")
            mojody = int(input("mojody: "))
            add(bank,name,shomare_hesab,mojody)

        case "2":
            kode_meli=input("kode meli:")
            find(bank,kode_meli)

        case "3":
            kode_meli=input("kode meli:")
            charge(bank,kode_meli)

        case "4":
            kode_meli=input("kode meli:")
            delete(bank,kode_meli)

        case "5":
            break
