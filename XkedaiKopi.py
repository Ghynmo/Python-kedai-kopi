class prosesPemesanan :
    def __init__(self, IDpemesanan, IDpelanggan, IDpelayan, IDmeja, totalHarga, Diskon, 
    Tanggal, Status, nomorMeja, jumlahKursi, statusMeja, IDmenu, namaMenu, kategoriMenu, 
    hargaMenu, statusMenu ):
        self.IDpemesanan = IDpemesanan
        self.IDpelanggan = IDpelanggan
        self.IDpelayan = IDpelayan
        self.IDmeja = IDmeja
        self.totalHarga = totalHarga
        self.Diskon = Diskon
        self.Tanggal = Tanggal
        self.Status = Status
        self.nomorMeja = nomorMeja
        self.jumlahKursi = jumlahKursi
        self.statusMeja = statusMeja
        self.IDmenu = IDmenu
        self.namaMenu = namaMenu
        self.kategoriMenu = kategoriMenu
        self.hargaMenu = hargaMenu
        self.statusMenu = statusMenu

    def infoDataPelayan(self):
        print("ID pelayan :{}. ".format(
            self.IDpelayan
            )    
        )

    def infoDataPemesanan(self):
        print("ID Pemesanan : {}, ID Pelanggan : {}, IDpelayan : {}, IDmeja : {}, totalHarga : {}, Diskon : {}, Tanggal : {}, Status {}. ".format(
            self.IDpemesanan, 
            self.IDpelanggan, 
            self.IDpelayan, 
            self.IDmeja, 
            self.totalHarga, 
            self.Diskon,
            self.Tanggal,
            self.Status
            )
        )

    def infoDataMeja(self):
        print("ID Meja : {} dengan Nomor meja: {}, Jumlah kursi : {}, dan Status meja : {}. ".format(
            self.IDmeja, 
            self.nomorMeja, 
            self.jumlahKursi, 
            self.statusMeja
            )
        )

    def infoDetailPemesanan(self):
        print("ID Menu : {}, dan ID Pemesanan : {}. ".format(
            self.IDmenu, 
            self.IDpemesanan
            )
        )

    def infoDataMenu(self):
        print("ID Menu : {}, dengan Nama menu : {}, Kategori: {}, Harga : {}, StatusMenu : {}. ".format(
            self.IDmenu, 
            self.namaMenu, 
            self.kategoriMenu, 
            self.hargaMenu, 
            self.statusMenu
            )
        )

    def infoDataPelanggan(self):
        print("ID Pelanggan : {}. ".format(
            self.IDpelanggan
            )
        )


class dataPelayan(prosesPemesanan):
    def __init__(self, IDpemesanan):
        super().__init__(IDpemesanan, 1234, 1234, 1234, "Rp.20.000", "5%", "9/12/30", "Ready",
        "12", "3", "Ready", "1234", "Kopi Pahit", "Minuman", "Rp.20.000", "Ready")
        print("=====Data Pelayan=====")
        super().infoDataPelayan()

class dataPemesanan(prosesPemesanan):
    def __init__(self, IDpemesanan):
        super().__init__(IDpemesanan, 1234, 1234, 1234, "Rp.20.000", "5%", "9/12/30", "Ready",
        "12", "3", "Ready", "1234", "Kopi Pahit", "Minuman", "Rp.20.000", "Ready")
        print("=====Data Pemesanan=====")
        super().infoDataPemesanan()

class dataMeja(prosesPemesanan):
    def __init__(self, IDpemesanan):
        super().__init__(IDpemesanan, 1234, 1234, 1234, "Rp.20.000", "5%", "9/12/30", "Ready",
        "12", "3", "Ready", "1234", "Kopi Pahit", "Minuman", "Rp.20.000", "Ready")
        print("=====Data Meja=====")
        super().infoDataMeja()

class dataDetailPemesanan(prosesPemesanan):
    def __init__(self, IDpemesanan):
        super().__init__(IDpemesanan, 1234, 1234, 1234, "Rp.20.000", "5%", "9/12/30", "Ready",
        "12", "3", "Ready", "1234", "Kopi Pahit", "Minuman", "Rp.20.000", "Ready")
        print("=====Detail Pemesanan=====")
        super().infoDetailPemesanan()

class dataMenu(prosesPemesanan):
    def __init__(self, IDpemesanan):
        super().__init__(IDpemesanan, 1234, 1234, 1234, "Rp.20.000", "5%", "9/12/30", "Ready",
        "12", "3", "Ready", "1234", "Kopi Pahit", "Minuman", "Rp.20.000", "Ready")
        print("=====Data Menu=====")
        super().infoDataMenu()

class dataPelanggan(prosesPemesanan):
    def __init__(self, IDpemesanan):
        super().__init__(IDpemesanan, 1234, 1234, 1234, "Rp.20.000", "5%", "9/12/30", "Ready",
        "12", "3", "Ready", "1234", "Kopi Pahit", "Minuman", "Rp.20.000", "Ready")
        print("=====Data Pelanggan=====")
        super().infoDataPelanggan()

kelas1 = dataPelayan("3229") 
kelas2 = dataPemesanan ("3229")
kelas3 = dataMeja("3229")
kelas4 = dataDetailPemesanan("3229") 
kelas5 = dataMenu ("3229")
kelas6 = dataPelanggan("3229")
print("======Nama Pelanggan=====")
class orang :
    def __init__(self, namaOrang, Alamat, Telepon ):
        self.namaOrang = namaOrang
        self.Alamat = Alamat
        self.Telepon = Telepon
kelas7 = orang ("Rizqi Hidayat", "Desa Keniten", "082264693559")
print(kelas7.namaOrang)

