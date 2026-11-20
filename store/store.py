



from add import *
from find import *
from delet import *
from mojody import *


def store():

    products = {}

    while True:
        menu_name = input("\n1. Add product\n2. Find product\n3. delete \n4. mojody check  \n5. Exit\nChoose: ")

        match menu_name:

            case "1":
                id = input("id product: ")
                name= input("name mahsool: ")
                mojody= int(input("mojody: "))

                add(id=id,name=name,mojody=mojody)

                print(products)


            case "2":
                id = input("id vared kon: ")
                Find(id=id)  
                
            case "3":
                id=input("id:")
                delet(id)
               
            case "4":
                id=input("id mahsool mored nazar ra vared konid:")
                mojody(id)
                


store()