




def mojody_store(products,id=str):
    
    product = products.get(id)
    
    if product:
        mojody=products[id]["mojody"]
        if mojody<50:
            print("bekhar")
        else:
            print("nakhar")
    else:
        print("product not found")