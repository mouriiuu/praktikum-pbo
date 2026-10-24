from abc import ABC, abstractmethod


def baca_angka(pesan):
    while True:
        try:
            return int(input(pesan))
        except ValueError:
            print("Input harus angka.")


def cetak_ringkasan(objek):
    print(objek.ringkasan())


class Kucing(ABC):
    nama_cafe = "Cat Space Princess"
    total_kucing = 0
    tarif_per_menit = 1000
    daftar_ras_valid = ["Anggora", "Persia", "Kampung", "Munchkin", "Sphynx"]

    def __init__(self, nama, ras, sifat, status_kesehatan):
        self.nama = nama
        self.ras = ras
        self.sifat = sifat
        self._status_kesehatan = status_kesehatan
        self.__kode_internal = f"KCG-{Kucing.total_kucing + 1:04d}"
        Kucing.total_kucing += 1

    @abstractmethod
    def hitung_tarif(self, durasi):
        pass

    @abstractmethod
    def aturan_main(self):
        pass

    def cek_kondisi(self):
        print(f"{self} | {self.sifat} | Kesehatan: {self._status_kesehatan} | {self.aturan_main()}")

    def __str__(self):
        return f"[{self.__kode_internal}] {self.nama} ({self.ras})"

    @classmethod
    def ganti_nama_cafe(cls, nama_baru):
        cls.nama_cafe = nama_baru

    @classmethod
    def ubah_tarif(cls, tarif_baru):
        cls.tarif_per_menit = tarif_baru

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
            print(f"Status {self.nama} diperbarui jadi {status_baru}.")


class AnakKucing(Kucing):
    biaya_pendampingan = 5000

    def __init__(self, nama, ras, sifat, status_kesehatan, durasi_maksimal_main):
        super().__init__(nama, ras, sifat, status_kesehatan)
        self.durasi_maksimal_main = durasi_maksimal_main

    @classmethod
    def dari_input(cls, nama, ras, sifat):
        durasi_maks = baca_angka("Durasi maksimal main (menit): ")
        return cls(nama, ras, sifat, "Sehat", durasi_maks)

    def hitung_tarif(self, durasi):
        return durasi * self.tarif_per_menit + AnakKucing.biaya_pendampingan

    def aturan_main(self):
        izin = "boleh main" if self._status_kesehatan == "Sehat" else "harus istirahat"
        return f"Anak kucing, maks {self.durasi_maksimal_main} menit, {izin}"


class KucingDewasa(Kucing):
    def __init__(self, nama, ras, sifat, status_kesehatan, tingkat_kemandirian):
        super().__init__(nama, ras, sifat, status_kesehatan)
        self.tingkat_kemandirian = tingkat_kemandirian

    @classmethod
    def dari_input(cls, nama, ras, sifat):
        tingkat = input("Tingkat kemandirian (Rendah/Sedang/Tinggi): ")
        return cls(nama, ras, sifat, "Sehat", tingkat)

    def hitung_tarif(self, durasi):
        return durasi * self.tarif_per_menit

    def aturan_main(self):
        izin = "bebas main" if self._status_kesehatan == "Sehat" else "sedang istirahat"
        return f"Kucing dewasa, kemandirian {self.tingkat_kemandirian}, {izin}"


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

    def ringkasan(self):
        return f"Kas cafe saat ini Rp{self.__saldo:,}"


class Kunjungan:
    total_kunjungan = 0

    def __init__(self, nama_pengunjung, durasi_main):
        self.nama_pengunjung = nama_pengunjung
        self.durasi_main = durasi_main
        self.nama_kucing = "-"
        self.__biaya = 0
        Kunjungan.total_kunjungan += 1

    def hitung_biaya(self, kucing):
        self.nama_kucing = kucing.nama
        self.__biaya = kucing.hitung_tarif(self.durasi_main)

    def buat_nota(self):
        print(f"Nota: {self.ringkasan()}")

    def ringkasan(self):
        return (f"{self.nama_pengunjung} main sama {self.nama_kucing} "
                f"selama {self.durasi_main} menit -> Rp{self.__biaya:,}")

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

    def __len__(self):
        return len(self.koleksi_kucing)

    def daftarkan_kucing_baru(self, kucing):
        if not Kucing.validasi_ras(kucing.ras):
            print("Gagal! Ras tidak dikenali.")
            return
        if len(self) >= CatCafe.kapasitas_maksimal:
            print("Gagal! Kapasitas cafe penuh.")
            return
        self.koleksi_kucing.append(kucing)
        print(f"{kucing.nama} berhasil didaftarkan.")

    def cek_kucing_tersedia(self):
        tersedia = [k for k in self.koleksi_kucing if k.status_kesehatan == "Sehat"]
        if not tersedia:
            print("Belum ada kucing yang tersedia.")
        for k in tersedia:
            print(f"- {k}")

    def tampilkan_semua_kucing(self):
        if len(self) == 0:
            print("Belum ada kucing terdaftar.")
            return
        print(f"Total kucing: {len(self)}")
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

    def catat_kunjungan(self, nama_pengunjung, kucing, durasi):
        kunjungan = Kunjungan(nama_pengunjung, durasi)
        kunjungan.hitung_biaya(kucing)
        kunjungan.buat_nota()
        self.log_kunjungan.append(kunjungan)
        self.kas.tambah_saldo(kunjungan.biaya)

    def simulasi_biaya(self, durasi):
        if len(self) == 0:
            print("Belum ada kucing terdaftar.")
            return
        for k in self.koleksi_kucing:
            print(f"{k} -> Rp{k.hitung_tarif(durasi):,}")

    def laporan(self):
        for objek in [self.kas, *self.log_kunjungan]:
            cetak_ringkasan(objek)

    @classmethod
    def ubah_kapasitas(cls, kapasitas_baru):
        cls.kapasitas_maksimal = kapasitas_baru

    @staticmethod
    def validasi_alamat(alamat):
        return len(alamat.strip()) > 0


JENIS_KUCING = {"1": AnakKucing, "2": KucingDewasa}

DAFTAR_MENU = [
    "1. Daftarkan kucing baru",
    "2. Lihat kucing tersedia",
    "3. Tampilkan semua kucing",
    "4. Buat kunjungan",
    "5. Lihat kas cafe",
    "6. Update status kucing",
    "7. Keluarkan kucing",
    "8. Laporan ringkasan",
    "9. Simulasi biaya semua kucing",
    "10. Bukti abstraksi",
    "11. Keluar",
]


def menu_daftar(cafe):
    nama = input("Nama kucing: ")
    ras = input("Ras kucing (Anggora/Persia/Kampung/Munchkin/Sphynx): ")
    sifat = input("Sifat kucing: ")
    kelas = JENIS_KUCING.get(input("Tipe kucing (1 = Anak Kucing, 2 = Kucing Dewasa): "))
    if kelas is None:
        print("Tipe kucing tidak valid.")
        return
    cafe.daftarkan_kucing_baru(kelas.dari_input(nama, ras, sifat))


def menu_kunjungan(cafe):
    if len(cafe) == 0:
        print("Belum ada kucing terdaftar.")
        return
    nama_pengunjung = input("Nama pengunjung: ")
    cafe.cek_kucing_tersedia()
    kucing = cafe.cari_kucing(input("Pilih nama kucing: "))
    if kucing is None:
        print("Kucing tidak ditemukan.")
        return
    if kucing.status_kesehatan != "Sehat":
        print("Gagal! Kucing sedang tidak sehat.")
        return
    durasi = baca_angka("Durasi main (menit): ")
    if not Kunjungan.validasi_durasi(durasi):
        print("Gagal! Durasi harus 5-120 menit.")
        return
    if isinstance(kucing, AnakKucing) and durasi > kucing.durasi_maksimal_main:
        print(f"Gagal! {kucing.nama} hanya boleh bermain maksimal "
            f"{kucing.durasi_maksimal_main} menit.")
        return
    cafe.catat_kunjungan(nama_pengunjung, kucing, durasi)



def menu_update(cafe):
    if len(cafe) == 0:
        print("Belum ada kucing terdaftar.")
        return
    cafe.tampilkan_semua_kucing()
    nama = input("Nama kucing yang mau diupdate: ")
    status = input("Status baru (Sehat/Sakit/Pemulihan): ")
    cafe.update_status_kucing(nama, status)


def menu_keluarkan(cafe):
    if len(cafe) == 0:
        print("Belum ada kucing terdaftar.")
        return
    cafe.tampilkan_semua_kucing()
    cafe.keluarkan_kucing(input("Nama kucing yang mau dikeluarkan: "))


def menu_simulasi(cafe):
    cafe.simulasi_biaya(baca_angka("Durasi simulasi (menit): "))


def bukti_abstraksi():
    try:
        Kucing("Percobaan", "Anggora", "Jinak", "Sehat")
    except TypeError as error:
        print(f"TypeError: {error}")


def main():
    cafe = CatCafe("Jl. Kucing Bahagia No.1")
    aksi_menu = {
        "1": lambda: menu_daftar(cafe),
        "2": cafe.cek_kucing_tersedia,
        "3": cafe.tampilkan_semua_kucing,
        "4": lambda: menu_kunjungan(cafe),
        "5": lambda: cetak_ringkasan(cafe.kas),
        "6": lambda: menu_update(cafe),
        "7": lambda: menu_keluarkan(cafe),
        "8": cafe.laporan,
        "9": lambda: menu_simulasi(cafe),
        "10": bukti_abstraksi,
    }
    while True:
        print("\n=== MENU PURRBOOK - CAT SPACE PRINCESS ===")
        for baris in DAFTAR_MENU:
            print(baris)
        pilihan = input("Pilih menu: ")
        if pilihan == "11":
            print("Terima kasih sudah berkunjung ke Cat Space Princess!")
            break
        aksi = aksi_menu.get(pilihan)
        if aksi is None:
            print("Pilihan tidak valid.")
        else:
            aksi()


if __name__ == "__main__":
    main()