products = {}

while True:
    menu_name = input("\n1. Add product\n2. Find product\n3. delete \n4. mojody check  \n5. Exit\nChoose: ")

    match menu_name:

        case "1":
            id = input("id product: ")
            name = input("name mahsool: ")
            mojody = int(input("mojody: "))

            products[id] = {
                "id product": id,
                "name_product": name,
                "mojody": mojody,
            }
            print("product added successfully!")
            print(products)
        case "2":
            id = input("id vared kon: ")  
            product = products.get(id)  
            if product:
                print("\nproductr found:")
                print("Name_product:", product["name_product"])
                print("mojody", product["mojody"])
            else:
                print("product not found!")
        case "3":
            id=input("id:")
            product = products.get(id)  
            if product:
                product.pop(id)
                print("pak shod")
                break
        case "4":
            id=input("id mahsool mored nazar ra vared konid:")
            product = products.get(id)
            if product:
                if mojody<50:
                    print("bekhar")
                else:
                    print("nakhar")
            break