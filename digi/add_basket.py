



def add_basket(product,products,basket,name,id):
            product[id] = {
                        "id product": id,
                        "name_product": name,
                                    }
            print(product)
            if product in products:
                basket.append(product)