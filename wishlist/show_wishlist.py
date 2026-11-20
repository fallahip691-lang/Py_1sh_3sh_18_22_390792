


def show_wishlist(wishlit,product_id):
    wishlit_=wishlit.get(product_id)
    if wishlit_:  
        return(wishlit[product_id])
    else:
        return("not found")