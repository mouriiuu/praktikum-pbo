class Kucing:
    nama_cafe = "Cat Space Princess"
    total_kucing = 0
    daftar_ras_valid = ["Anggora", "Persia", "Kampung", "Munchkin", "Sphynx"]

    def __init__(self, nama, ras, sifat, status_kesehatan):
        self.nama = nama
        self.ras = ras
        self.sifat = sifat
        self._status_kesehatan = status_kesehatan
        self.__kode_internal = f"KCG-{Kucing.total_kucing + 1:04d}"
        Kucing.total_kucing += 1

    def cek_kondisi(self):
        print(f"{self.nama} | {self.ras} | {self.sifat} | Kesehatan: {self._status_kesehatan}")

    @classmethod
    def ganti_nama_cafe(cls, nama_baru):
        cls.nama_cafe = nama_baru

    @staticmethod
    def validasi_ras(ras):
        return ras in Kucing.daftar_ras_valid

    @property
    def status_kesehatan(self):
        return self._status_kesehatan

    @status_kesehatan.setter
    def status_kesehatan(self, status_baru):
        if status_baru not in ["Sehat", "Sakit", "Pemulihan"]:
            print("Gagal! Status tidak valid.")
        else:
            self._status_kesehatan = status_baru


class AnakKucing(Kucing):
    def __init__(self, nama, ras, sifat, status_kesehatan, durasi_maksimal_main):
        super().__init__(nama, ras, sifat, status_kesehatan)
        self.durasi_maksimal_main = durasi_maksimal_main

    def cek_kondisi(self):
        print(f"{self.nama} (Anak Kucing) | {self.ras} | {self.sifat} | "
              f"Kesehatan: {self._status_kesehatan} | Maks main: {self.durasi_maksimal_main} menit "
              f"(butuh pendampingan ekstra)")


class KucingDewasa(Kucing):
    def __init__(self, nama, ras, sifat, status_kesehatan, tingkat_kemandirian):
        super().__init__(nama, ras, sifat, status_kesehatan)
        self.tingkat_kemandirian = tingkat_kemandirian


class KasCafe:
    def __init__(self):
        self.__saldo = 0

    def tambah_saldo(self, nominal):
        if nominal < 0:
            print("Gagal! Nominal tidak boleh negatif.")
        else:
            self.__saldo += nominal

    @property
    def saldo(self):
        return self.__saldo


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


class CatCafe:
    nama_cafe = "Cat Space Princess"
    kapasitas_maksimal = 10

    def __init__(self, alamat):
        self.alamat = alamat
        self.koleksi_kucing = []
        self.log_kunjungan = []
        self.kas = KasCafe()

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
            k.cek_kondisi()

    def cari_kucing(self, nama):
        return next((k for k in self.koleksi_kucing if k.nama == nama), None)

    def update_status_kucing(self, nama, status_baru):
        kucing = self.cari_kucing(nama)
        if not kucing:
            print("Kucing tidak ditemukan.")
            return
        kucing.status_kesehatan = status_baru

    def keluarkan_kucing(self, nama):
        kucing = self.cari_kucing(nama)
        if not kucing:
            print("Kucing tidak ditemukan.")
            return
        self.koleksi_kucing.remove(kucing)
        print(f"{nama} berhasil dikeluarkan dari cafe.")

    def catat_kunjungan(self, kunjungan):
        kunjungan.buat_nota()
        self.log_kunjungan.append(kunjungan)
        self.kas.tambah_saldo(kunjungan.biaya)

    @classmethod
    def ubah_kapasitas(cls, kapasitas_baru):
        cls.kapasitas_maksimal = kapasitas_baru

    @staticmethod
    def validasi_alamat(alamat):
        return len(alamat.strip()) > 0


cafe = CatCafe("Jl. Kucing Bahagia No.1")

while True:
    print("\n=== MENU CAT SPACE PRINCESS ===")
    print("1. Daftarkan kucing baru")
    print("2. Lihat kucing tersedia")
    print("3. Tampilkan semua kucing")
    print("4. Buat kunjungan")
    print("5. Lihat kas cafe")
    print("6. Update status kucing")
    print("7. Keluarkan kucing")
    print("8. Keluar")
    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        nama = input("Nama kucing: ")
        ras = input("Ras kucing (Anggora/Persia/Kampung/Munchkin/Sphynx): ")
        sifat = input("Sifat kucing: ")
        tipe = input("Tipe kucing (1=Anak Kucing, 2=Kucing Dewasa): ")
        if tipe == "1":
            durasi_maks = int(input("Durasi maksimal main (menit): "))
            kucing_baru = AnakKucing(nama, ras, sifat, "Sehat", durasi_maks)
        else:
            tingkat = input("Tingkat kemandirian (Rendah/Sedang/Tinggi): ")
            kucing_baru = KucingDewasa(nama, ras, sifat, "Sehat", tingkat)
        cafe.daftarkan_kucing_baru(kucing_baru)

    elif pilihan == "2":
        cafe.cek_kucing_tersedia()
        if not cafe.koleksi_kucing:
            print("Belum ada kucing terdaftar.")

    elif pilihan == "3":
        if not cafe.koleksi_kucing:
            print("Belum ada kucing terdaftar.")
            continue
        cafe.tampilkan_semua_kucing()

    elif pilihan == "4":
        if not cafe.koleksi_kucing:
            print("Belum ada kucing terdaftar.")
            continue
        nama_pengunjung = input("Nama pengunjung: ")
        cafe.cek_kucing_tersedia()
        nama_kucing = input("Pilih nama kucing: ")
        kucing_dipilih = cafe.cari_kucing(nama_kucing)
        if not kucing_dipilih:
            print("Kucing tidak ditemukan.")
            continue
        durasi = int(input("Durasi main (menit): "))
        if not Kunjungan.validasi_durasi(durasi):
            print("Gagal! Durasi harus 5-120 menit.")
            continue
        kunjungan_baru = Kunjungan(nama_pengunjung, kucing_dipilih, durasi)
        cafe.catat_kunjungan(kunjungan_baru)

    elif pilihan == "5":
        print(f"Kas cafe saat ini: Rp{cafe.kas.saldo:,}")

    elif pilihan == "6":
        if not cafe.koleksi_kucing:
            print("Belum ada kucing terdaftar.")
            continue
        cafe.tampilkan_semua_kucing()
        nama_kucing = input("Nama kucing yang mau diupdate: ")
        status_baru = input("Status baru (Sehat/Sakit/Pemulihan): ")
        cafe.update_status_kucing(nama_kucing, status_baru)

    elif pilihan == "7":
        if not cafe.koleksi_kucing:
            print("Belum ada kucing terdaftar.")
            continue
        cafe.tampilkan_semua_kucing()
        nama_kucing = input("Nama kucing yang mau dikeluarkan: ")
        cafe.keluarkan_kucing(nama_kucing)

    elif pilihan == "8":
        print("Terima kasih sudah berkunjung ke Cat Space Princess!")
        break

    else:
        print("Pilihan tidak valid.")