
from basket import *
from wishlist import *

def wish_and_basket(product):
    while True:
        menu=input("1.basket 2. wishlist 3. exit")
        match menu:
            case "1":
                basket(product)
            case "2":
                wishlist(product)
            









