



from add_store import *
from find_store import *
from delet_store import *
from mojody_store import *


def store(products):

   

    while True:
        menu_name = input("\n1. Add product\n2. Find product\n3. delete \n4. mojody check  \n5. Exit\nChoose: ")

        match menu_name:

            case "1":
                id = input("id product: ")
                name= input("name mahsool: ")
                mojody= int(input("mojody: "))

                add_store(products,id=id,name=name,mojody=mojody)

                print(products)


            case "2":
                id = input("id vared kon: ")
                Find_store(products,id=id)  
                
            case "3":
                id=input("id:")
                delet_store(products,id)
               
            case "4":
                id=input("id mahsool mored nazar ra vared konid:")
                mojody_store(products,id)




