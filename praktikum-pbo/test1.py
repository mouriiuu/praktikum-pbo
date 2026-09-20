# class Nasabah:

#     def __init__(self, nama, saldo):
#         self.nama = nama
#         self.saldo = saldo

# # nama = input("Masukkan Nama: ")
# # saldo = input("Masukkan Saldo: ")

# # user = Nasabah(nama, saldo)

# # print(user.nama)
# # print(user.saldo)

# dapa = Nasabah("dapa", 5000)

# print(dapa.saldo)
# print(dapa.nama)


# class Karyawan:
#     def __init__(self, nama, gaji):
#         self.nama = nama
#         self._gaji = gaji # protected, hanya "disarankan" diakses dari dalam

# class Manager(Karyawan):
#     def tampilkan_gaji(self):
#     # subclass tetap bisa mengakses atribut protected milik parent
#         print(f"Gaji {self.nama}: {self._gaji}")


# manager = Manager("Daffa", 12000000)
# manager.tampilkan_gaji()
# print(manager._gaji)

class RekeningBank:

    def __init__(self, pemilik, saldo):
        self.pemilik = pemilik
        self.__saldo = saldo # private

    @property
    def saldo(self):
        return self.__saldo

    @saldo.setter
    def saldo(self, saldo_baru):
        if saldo_baru > 0:
            self.__saldo = saldo_baru

dapa = RekeningBank("Dapa", 100)
print(dapa.saldo)
dapa.saldo = 4000
print(dapa.saldo)


    # def get_saldo(self):
    #     return self.__saldo

    # def set_saldo(self, saldo_baru):
    #     if saldo_baru > 0:
        
    #         self.saldo = saldo_baru

# print(dapa.get_saldo())
# dapa.set_saldo(-50000)
# print(dapa.get_saldo())


#     def tarik_saldo(self, jumlah):
#         if jumlah > self.__saldo:
#             print("Saldo tidak cukup.")
#         elif jumlah <= 0:
#             print("Jumlah penarikan tidak valid.")
#         else:
#             self.__saldo -= jumlah
#             print(f"Berhasil menarik {jumlah}. Sisa saldo: {self.__saldo}")

#     def cek_saldo(self):
#         print(f"Saldo saat ini: {self.__saldo}")

# rekening = RekeningBank("Budi", 100000)
# rekening.tarik_saldo(30000)
# rekening.cek_saldo()
# # print(rekening.__saldo)

# print(rekening._RekeningBank__saldo) #Name mangling

