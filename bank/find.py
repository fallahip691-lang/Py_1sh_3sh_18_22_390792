





def find(bank,kode_meli):
    bank_ = bank.get(kode_meli)

    if bank_:
        print(bank_)
    else:
        print("not found")
        