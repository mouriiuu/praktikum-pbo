# class Animal:
#     def __init__(self, nama, umur, warna_bulu, berbisa):
#         self.nama = nama
#         self.umur = umur
#         self.warna_bulu = warna_bulu
#         self.berbisa = berbisa

#     def makan(self):
#         print(f"{self.nama} sedang makan")

# kucing = Animal("oren", 2, "Orange", None)
# ular = Animal("kobraw", 2, None, True)

class Animal:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur

class Mamalia(Animal):
    def __init__(self, nama, umur, warna_bulu):
        self.warna_bulu = warna_bulu

class Reptile(Animal):

    def __init__(self, nama, umur, berbisa):
        self.berbisa = berbisa

kucing = Mamalia("oren", 2, "orange")
print(kucing.nama)