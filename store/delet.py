




def delet(id):

    products={}
    product = products.get(id)  
    if product:
        product.pop(id)
        print ("pak shod")
    else:
        print("product not found")