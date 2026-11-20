



def find(wishlist,product_id)->dict:
    while True:
        store={"1":{"name":"iphone","price":1000}}
        wishlist=[]
        store_=store.get(product_id)
        if store_:
            return store[product_id]

        else:
            return "not found"
        