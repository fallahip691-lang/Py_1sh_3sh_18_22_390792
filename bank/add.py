






def add(bank,name,shomare_hesab,mojody):
    kode_meli = input("kode meli: ")

    if kode_meli not in bank:
    
        bank[kode_meli] = {
            "name": name,
            "shomare hesab": shomare_hesab,
            "mojody": mojody
        }
        print("added")
        print(bank[kode_meli])
    else:
        print("already exists")