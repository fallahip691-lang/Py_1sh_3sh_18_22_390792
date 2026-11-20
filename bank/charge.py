








def charge(bank,kode_meli):
    bank_ = bank.get(kode_meli)

    if bank_:
        sharj = int(input("sharj: "))
        if sharj > 0:
            bank_["mojody"] += sharj
            print(bank_["mojody"])
        else:
            print("invalid amount")
    else:
        print("not found")