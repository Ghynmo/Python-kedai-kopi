import sqlite3
from Menu import Menu
from Struk import last_IDpemesanan

conn = sqlite3.connect('kedaikopi.db') #Make or Connect to Database
c = conn.cursor() #Activate syntax of SQL

L_ID_Struk= last_IDpemesanan()

class Pesanan :
    def __init__(self, IDmenu, Jumlah):
        self.pm = L_ID_Struk[0][0]+1
        self.lastidpesan = L_ID_Struk[0][0]+1
        self.IDmenu = IDmenu
        self.Jumlah = Jumlah
        self.haoa = self.Totalharga()

    def Hargaall(self):
        c.execute ("SELECT SUM(Harga) FROM Pesanan WHERE IDpemesanan = :LID_ps GROUP BY IDpemesanan", 
        {'LID_ps':self.pm})
        hasilall = c.fetchall()
        self.uwu = hasilall[0][0]
        return int(self.uwu)
    
    def pesanall(self):
        c.execute ("SELECT Nama FROM Menu Join Pesanan ON Menu.IDmenu = Pesanan.IDmenu WHERE IDpemesanan = :LID_ps ORDER BY Waktu DESC", {'LID_ps':self.lastidpesan})
        etdah = c.fetchall()
        self.susah = etdah[0][0]
        return str(self.susah)

    def keuntungan(self):
        c.execute ("SELECT SUM(Harga) FROM Pesanan Join Pemesanan ON Pesanan.IDpemesanan = Pemesanan.IDpemesanan WHERE Tanggal = DATE('now') GROUP BY Tanggal")
        keuntungan = c.fetchall()
        self.untung = keuntungan[0][0]
        return int(self.untung)
    
    def Totalharga(self):
        c.execute ("SELECT Harga*:Jumlah FROM Menu WHERE IDmenu = :IDmenu", 
        {'IDmenu':self.IDmenu, 'Jumlah':self.Jumlah})
        hasil = c.fetchall()
        self.haa = hasil[0][0]
        return int(self.haa)

    def insert_pesanan(self):
        with conn:
            c.execute ("INSERT INTO Pesanan VALUES (:LIDpm, :IDmenu, :Jumlah, :Harga, DATETIME('now'))", 
            {'LIDpm':self.pm, 'IDmenu':self.IDmenu, 'Jumlah':self.Jumlah, 'Harga':self.haoa})

    # def update_pesanan(self):
    #     with conn:
    #         c.execute ("UPDATE Pesanan SET Jumlah = :Jumlah WHERE IDpesanan = :IDpesanan ", 
    #         {'IDpesanan':self.IDpesanan, 'Jumlah':self.Jumlah, 'IDmenu':self.IDmenu})

    # def delete_pesananbyid(self):
    #     with conn:
    #         c.execute ("DELETE FROM Pesanan WHERE IDpesanan = :IDpesanan", 
    #         {'IDpesanan':self.IDpesanan})


# b1 = Pesanan(2, 4)
# print(b1.keuntungan())