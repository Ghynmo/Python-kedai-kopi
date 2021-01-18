import sqlite3

conn = sqlite3.connect('kedaikopi.db') #Make or Connect to Database
c = conn.cursor() #Activate syntax of SQL

def create_table():
    with conn:
        c.execute ("""CREATE TABLE Pelayan (IDpelayan text, Nama text, Gaji integer )""")

def last_IDorang():
    c.execute ("SELECT IDorang FROM Orang ORDER BY IDorang DESC LIMIT 1 ")
    lastIDorang = c.fetchall()
    return lastIDorang
    
class Orang :
    def __init__(self, Nama, Alamat, Telepon):
        self.Nama = Nama
        self.Alamat = Alamat
        self.Telepon = Telepon

    def infoDataorang(self):
        print("Nama : {}, Alamat : {}, Telepon : {} ".format(
            self.Nama,
            self.Alamat,
            self.Telepon)
        )

    def insert_orang(self):
        with conn:
            c.execute ("INSERT INTO Orang VALUES (NULL, :Nama, :Alamat, :Telepon)", 
            {'Nama':self.Nama, 'Alamat':self.Alamat, 'Telepon':self.Telepon})


    # def update_orang(self):
    #     with conn:
    #         c.execute ("UPDATE sqlite_sequence SET seq = 3 WHERE NAME = 'Orang'") 
    #         {'IDorang':self.IDorang, 'Nama':self.Nama, 'Alamat':self.Alamat, 'Telepon':self.Telepon})

    # def delete_orangbyid(self):
    #     with conn:
    #         c.execute ("DELETE FROM Orang WHERE IDorang = :IDorang", 
    #         {'IDorang':self.IDorang})

# P1 = Orang("Bill","Cyernobyl",909)
# P1.update_orang()
# c.execute ("SELECT * FROM Orang")
# conn.commit()

# conn.close()