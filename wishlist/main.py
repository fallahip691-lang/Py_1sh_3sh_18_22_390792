


from add_wishlist import *
from find_wishlist import *
from delete_wishlist import *
from show_wishlist import *

def wishlist():
    wishlist={"1":{"name":"iphone","price":1000}}
    wishlist=[]
    while True:
        menu=input("1.add 2.find 3.delete from wish list 4.wishlist  5.exit  ")
        while True:
            match menu:
                case"1":
                    product_id=input("product id ro vared kon:")
                    name=input("namet ro vared kon:")

                    price=int(input("price:"))
                    add_wishlist(wishlist,name,product_id,price)
                    break

                case"2":
                    product_id=input("product id ro vared kon:")
                    find(wishlist,product_id)
                    break
                


                case "3":
                    product_id=input("product id:")
                    delete_wishlist(wishlist,product_id)

                case "4":
                    product_id=input("product id:")
                    show_wishlist(wishlist,product_id)

                    
                

        
                
            




wishlist()