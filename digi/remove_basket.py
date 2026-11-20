


def remove_basket(basket,id):
    basket_=basket.get(id)
    if basket_:
        basket.pop(id)
        print ("pak shod")       
    else:
        print("product not found")
