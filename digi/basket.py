

from add_basket import *
from remove_basket import *
def basket(products):
    basket=[]
    product={}
    while True:
        while True:
            menu="1.addto basket 2.remove from basket 3.exit"
            match menu:
                case"1":
                    id = input("id product: ")
                    name= input("name mahsool: ")
                    add_basket(product,products,basket,name,id)
                case"2":
                    id = input("id product: ")
                    remove_basket(basket,id)
                case "3":
                    break

                

    