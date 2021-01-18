import sqlite3
from Orang import last_IDorang

conn = sqlite3.connect('kedaikopi.db') #Make or Connect to Database
c = conn.cursor() #Activate syntax of SQL

L_ID_Orang= last_IDorang()

def last_IDpemesanan():
    c.execute ("SELECT IDpemesanan FROM Pemesanan ORDER BY IDpemesanan DESC LIMIT 1 ")
    lastIDpemesanan = c.fetchall()
    return lastIDpemesanan

class Pemesanan:
    def __init__(self):
        self.ps = L_ID_Orang[0][0]+1
        # self.pm = L_ID_Struk[0][0]

    def insert_pemesanan(self):
        with conn:
            c.execute ("INSERT INTO Pemesanan VALUES (NULL, :LIDorang, DATE('now'))", 
            {'LIDorang':self.ps})

    # def update_pemesanan(self):
    #     with conn:
    #         c.execute ("UPDATE Pemesanan SET Diskon = :Diskon WHERE IDpemesanan = :IDpemesanan ", 
    #         {'IDpemesanan':self.IDpemesanan, 'Diskon':self.Diskon, 'Tanggal':self.Tanggal, 'Totalharga':self.Totalharga, 'Statuspemesanan':self.Statuspemesanan})

    # def delete_pemesananbyid(self):
    #     with conn:
    #         c.execute ("DELETE FROM Pemesanan WHERE IDpemesanan = :IDpemesanan", 
    #         {'IDpemesanan':self.IDpemesanan})
