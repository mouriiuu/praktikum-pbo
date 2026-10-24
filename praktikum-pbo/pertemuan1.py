# class Product:
#     merk = "Lenovo"


#     def __init__(self, mark):    
#             self.mark = mark

#     def change_price(self, new_price):
#         self.price = new_price
#         pass

# class ProductDetail:
#     pass
# class product_detail:
#     pass

# product = Product("Lenovo")
# product1 = Product("HP")

# print(product.merk) # untuk memanggil atribut
# print(product1.merk)

class Tim:
    def __init__(self, nama, ceo):
        self.nama = nama
        self.ceo = ceo

rrq = Tim("RRQ Hoshi", "Pak AP")
evos = Tim("Evos Legends", "Hartman Harris")
print(rrq.nama) # RRQ Hoshi
print(evos.nama)

class Tim:
    nama_liga = "MPL Indonesia"

    def __init__(self, nama, ceo):
        self.nama = nama
        self.ceo = ceo

rrq = Tim("RRQ", "Pak AP")
evos = Tim("Evos Legends", "Hartman Harris")
print(rrq.nama_liga) # MPL Indonesia
print(evos.nama_liga) # MPL Indonesia

Tim.nama_liga = "MPL Indonesia Season 15"
print(rrq.nama_liga) # MPL Indonesia Season 15
print(evos.nama_liga) # MPL Indonesia Season 15