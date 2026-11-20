




def add_wishlist(products,wishlist,product_id:str,name:str,price:int):
    while True:
        if product_id in products:
            wishlist[product_id]={"name":name,"price":price}
            return(wishlist)
        else:
            print("product not found!")
        