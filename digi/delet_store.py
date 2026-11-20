



def delet_store(products,id):
    products={}
    product = products.get(id)  
    if product in products:
        product.pop(id)
        print ("pak shod")
    else:
        print("product not found")