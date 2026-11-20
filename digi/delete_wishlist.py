



def delete_wishlist(wishlist,product_id):
    wishlist_=wishlist.get(product_id)
    if wishlist_:
        wishlist.pop(product_id)
    else:
        print("not found")



