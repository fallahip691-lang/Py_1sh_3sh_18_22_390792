
bank = {}

while True:
    menu = input("1.add 2.find 3.charge 4.delete 5.exit: ")

    match menu:
        case "1":
            kode_meli = input("kode meli ro vared kon: ")

            if kode_meli not in bank:
                name = input("namet ro vared kon: ")
                shomare_hesab = input("shomare hesab bede: ")
                mojody = int(input("mojody: "))

                bank[kode_meli] = {
                    "name": name,
                    "shomare hesab": shomare_hesab,
                    "mojody": mojody
                }

                print("account added")
            else:
                print("account already exists")

        case "2":
            kode_meli = input("kode meli ro vared kon: ")
            bank_ = bank.get(kode_meli)

            if bank_:
                print("name:", bank_["name"])
                print("shomare hesab:", bank_["shomare hesab"])
                print("mojody:", bank_["mojody"])
            else:
                print("not found")

        case "3":
            kode_meli = input("kode meli ro vared kon: ")
            bank_ = bank.get(kode_meli)

            if bank_:
                sharj = int(input("sharj: "))
                if sharj > 0:
                    bank_["mojody"] += sharj
                    print("new mojody:", bank_["mojody"])
                else:
                    print("invalid amount")
            else:
                print("not found")

        case "4":
            kode_meli = input("kode meli ro vared kon: ")

            if kode_meli in bank:
                del bank[kode_meli]
                print("account deleted")
            else:
                print("not found")

        case "5":
            break
