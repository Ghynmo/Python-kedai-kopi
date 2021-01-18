import sqlite3

conn = sqlite3.connect('kedaikopi.db') #Make or Connect to Database
c = conn.cursor() #Activate syntax of SQL

class Menu :
    def __init__(self, Nama, Kategori, Harga, Statusmenu):
        self.Nama = Nama
        self.Kategori = Kategori
        self.Harga = Harga
        self.Statusmenu = Statusmenu

    def infoDataMenu(self):
        print("Nama : {}, Kategori : {}, Harga : {}, Statusmenu : {}. ".format(
            self.Nama,
            self.Kategori.Kategori,
            self.Harga.Harga,
            self.Statusmenu.Statusmenu)
        )

    def insert_menu(self):
        with conn:
            c.execute ("INSERT INTO Menu VALUES (NULL, :Nama, :Kategori, :Harga, :Statusmenu)", 
            {'Nama':self.Nama, 'Kategori':self.Kategori, 'Harga':self.Harga, 'Statusmenu':self.Statusmenu})

    # def update_menu(self):
    #     with conn:
    #         c.execute ("UPDATE Menu SET Nama = :Nama WHERE IDmenu = :IDmenu ", 
    #         {'IDmenu':self.IDmenu, 'Nama':self.Nama, 'Kategori':self.Kategori, 'Harga':self.Harga, 'Statusmenu':self.Statusmenu})

    # def delete_menubyid(self):
    #     with conn:
    #         c.execute ("DELETE FROM Menu WHERE IDmenu = :IDmenu", {'IDmenu':self.IDmenu})

