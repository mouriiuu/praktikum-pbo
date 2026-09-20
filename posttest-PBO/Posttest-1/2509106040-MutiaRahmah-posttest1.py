class Kucing:
    nama_cafe = "Cat Space Princess"
    total_kucing = 0
    daftar_ras_valid = ["Anggora", "Persia", "Kampung", "Munchkin", "Sphynx"]

    def __init__(self, nama, ras, sifat, status_kesehatan):
        self.nama = nama
        self.ras = ras
        self.sifat = sifat
        self.__status_kesehatan = status_kesehatan
        Kucing.total_kucing += 1

    def cek_kondisi(self):
        print(f"{self.nama} | {self.ras} | {self.sifat} | Kesehatan: {self.__status_kesehatan}")

    @classmethod
    def ganti_nama_cafe(cls, nama_baru):
        cls.nama_cafe = nama_baru

    @staticmethod
    def validasi_ras(ras):
        return ras in Kucing.daftar_ras_valid

    @property
    def status_kesehatan(self):
        return self.__status_kesehatan

    @status_kesehatan.setter
    def status_kesehatan(self, status_baru):
        if status_baru not in ["Sehat", "Sakit", "Pemulihan"]:
            print("Gagal! Status tidak valid.")
        else:
            self.__status_kesehatan = status_baru


class Kunjungan:
    biaya_per_menit = 1000
    total_kunjungan = 0

    def __init__(self, nama_pengunjung, kucing, durasi_main):
        self.nama_pengunjung = nama_pengunjung
        self.kucing = kucing
        self.durasi_main = durasi_main
        self.__biaya = durasi_main * Kunjungan.biaya_per_menit
        Kunjungan.total_kunjungan += 1

    def buat_nota(self):
        print(f"Nota: {self.nama_pengunjung} main sama {self.kucing.nama} "
              f"selama {self.durasi_main} menit -> Rp{self.__biaya:,}")

    @classmethod
    def ubah_tarif(cls, tarif_baru):
        cls.biaya_per_menit = tarif_baru

    @staticmethod
    def validasi_durasi(durasi):
        return 5 <= durasi <= 120

    @property
    def biaya(self):
        return self.__biaya

    @biaya.setter
    def biaya(self, nilai_baru):
        if nilai_baru < 0:
            print("Gagal! Biaya tidak boleh negatif.")
        else:
            self.__biaya = nilai_baru


class CatCafe:
    nama_cafe = "Cat Space Princess"
    kapasitas_maksimal = 10

    def __init__(self, alamat):
        self.alamat = alamat
        self.koleksi_kucing = []
        self.__kas_cafe = 0

    def daftarkan_kucing_baru(self, kucing):
        if not Kucing.validasi_ras(kucing.ras):
            print("Gagal! Ras tidak dikenali.")
            return
        self.koleksi_kucing.append(kucing)
        print(f"{kucing.nama} berhasil didaftarkan.")

    def cek_kucing_tersedia(self):
        for k in self.koleksi_kucing:
            if k.status_kesehatan == "Sehat":
                print(f"- {k.nama} ({k.ras})")

    def tampilkan_semua_kucing(self):
        for k in self.koleksi_kucing:
            print(f"- {k.nama} ({k.ras}) - Status: {k.status_kesehatan}")

    def cari_kucing(self, nama):
        return next((k for k in self.koleksi_kucing if k.nama == nama), None)

    def update_status_kucing(self, nama, status_baru):
        kucing = self.cari_kucing(nama)
        if not kucing:
            print("Kucing tidak ditemukan.")
            return
        kucing.status_kesehatan = status_baru

    def hapus_kucing(self, nama):
        kucing = self.cari_kucing(nama)
        if not kucing:
            print("Kucing tidak ditemukan.")
            return
        self.koleksi_kucing.remove(kucing)
        print(f"{nama} berhasil dihapus dari cafe.")

    @classmethod
    def ubah_kapasitas(cls, kapasitas_baru):
        cls.kapasitas_maksimal = kapasitas_baru

    @staticmethod
    def validasi_alamat(alamat):
        return len(alamat.strip()) > 0

    @property
    def kas_cafe(self):
        return self.__kas_cafe

    @kas_cafe.setter
    def kas_cafe(self, nilai_baru):
        if nilai_baru < 0:
            print("Gagal! Kas tidak boleh negatif.")
        else:
            self.__kas_cafe = nilai_baru


cafe = CatCafe("Jl. Kucing Bahagia No.1")

while True:
    print("\n=== MENU CAT CAFE MEOW ===")
    print("1. Daftarkan kucing baru")
    print("2. Lihat kucing tersedia")
    print("3. Buat kunjungan")
    print("4. Lihat kas cafe")
    print("5. Update status kucing")
    print("6. Hapus data kucing")
    print("7. Keluar")
    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        nama = input("Nama kucing: ")
        ras = input("Ras kucing (Anggora/Persia/Kampung/Munchkin/Sphynx): ")
        sifat = input("Sifat kucing: ")
        kucing_baru = Kucing(nama, ras, sifat, "Sehat")
        cafe.daftarkan_kucing_baru(kucing_baru)

    elif pilihan == "2":
        cafe.cek_kucing_tersedia()
        if not cafe.koleksi_kucing:
            print("Belum ada kucing terdaftar.")

    elif pilihan == "3":
        if not cafe.koleksi_kucing:
            print("Belum ada kucing terdaftar.")
            continue
        nama_pengunjung = input("Nama pengunjung: ")
        cafe.cek_kucing_tersedia()
        nama_kucing = input("Pilih nama kucing: ")
        kucing_dipilih = next((k for k in cafe.koleksi_kucing if k.nama == nama_kucing), None)
        if not kucing_dipilih:
            print("Kucing tidak ditemukan.")
            continue
        durasi = int(input("Durasi main (menit): "))
        if not Kunjungan.validasi_durasi(durasi):
            print("Gagal! Durasi harus 5-120 menit.")
            continue
        kunjungan_baru = Kunjungan(nama_pengunjung, kucing_dipilih, durasi)
        kunjungan_baru.buat_nota()
        cafe.kas_cafe = cafe.kas_cafe + kunjungan_baru.biaya

    elif pilihan == "4":
        print(f"Kas cafe saat ini: Rp{cafe.kas_cafe:,}")

    elif pilihan == "5":
        if not cafe.koleksi_kucing:
            print("Belum ada kucing terdaftar.")
            continue
        cafe.tampilkan_semua_kucing()
        nama_kucing = input("Nama kucing yang mau diupdate: ")
        status_baru = input("Status baru (Sehat/Sakit/Pemulihan): ")
        cafe.update_status_kucing(nama_kucing, status_baru)

    elif pilihan == "6":
        if not cafe.koleksi_kucing:
            print("Belum ada kucing terdaftar.")
            continue
        cafe.tampilkan_semua_kucing()
        nama_kucing = input("Nama kucing yang mau dihapus: ")
        cafe.hapus_kucing(nama_kucing)

    elif pilihan == "7":
        print("Terima kasih sudah berkunjung ke Cat Space Princess!")
        break

    else:
        print("Pilihan tidak valid.")