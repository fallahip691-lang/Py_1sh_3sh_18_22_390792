




def Find_store(products,id):
    product = products.get(id)  
    if product:
        print("\nproductr found:")
        print("Name_product:", product["name_product"])
        print("mojody", product["mojody"])
    else:
        print("product not found!")