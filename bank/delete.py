







def delete(bank,kode_meli):
    if kode_meli in bank:
        del bank[kode_meli]
        print("deleted")
    else:
        print("not found")