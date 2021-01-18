import sqlite3
from Menu import Menu
from Orang import Orang
from Pesanan import Pesanan
from Struk import Pemesanan
import datetime

timedate = datetime.datetime.now()
conn = sqlite3.connect('kedaikopi.db') #Make or Connect to Database
c = conn.cursor() #Activate syntax of SQL

start =  input('Masuk sebagai [1.Admin] atau [2.Pembeli] : ')

if start == '1':
    admin = input('Pilih menu : [1. Input menu makanan/minuman baru] | [2.Keuntungan hari ini] : ')
    if admin == '1':
        o, p, q, r = input("\nMasukkan Nama menu, Kategori, Harga, dan Ketersediaan(0 atau 1) : ").split()
        print("Menu baru dengan nama {}, Kategori {}, Harga {}, Status {}".format(o, p, q, r))
        M1 = Menu(o, p, q, r)
        M1.insert_menu()
    else:
        b1 = Pesanan(1,1)
        untunghari = b1.keuntungan()
        print ('*****Keuntungan hari ini sebesar: Rp.', untunghari)

elif start == '2':
    pembeli = input('Pilih menu : [1.Memesan] [2.Lihat Menu] : ')
    if pembeli == '1':
        # Process 1 Intro [Input Orang]
        x, y, z = input("Masukkan Nama, Alamat, dan Nomor HP : ").split()
        print("Pelanggan atas Nama {}, Alamat di {}, dan Nomor HP {}".format(x, y, z))
        P1 = Orang(x,y,z)
        P1.insert_orang()
        
        #Process 1.1 [Struk]
        S1 = Pemesanan()
        S1.insert_pemesanan()

        #Process 2 Order [Pesanan]
        print("Pilih Menu : \n        1.Kopi[3K] | 2.Roti[5K] | 3.Chappucino[22K] | 4.Ice Coffee Latte[16K] | 5.Indomie[10K]")
        print("         6.Es Kopi Susu[18K] | 7.Nasi Goreng[20K] | 8.Ice Mocchacino[19K] | 9.Pisang Goreng[18K]")
        print("         10.Americano[13K] | 11.Pisang Bakar Mantap[18K] | 12.Coffee Latte[15K] | 13.Kue Manis[10K]")
        print("         14.Chocolate[15K] | 15.Kentang Goreng[10K] | 16.Roti Bakar[20K] | 17.Martabak[22K]\n")
        loops = True
        ygdipesan = []
        jumlahygdpsn = []
        counterr = 0

        while loops:
            nomenu, pesananqt = input("Masukkan nomor menu dan jumlahnya : ").split()
            print("Nomor Menu {}, Sebanyak {}".format(nomenu, pesananqt))
            Ps1 = Pesanan(nomenu, pesananqt)
            Ps1.insert_pesanan()

            b1 = Pesanan(1, 1)
            pesanapaaja = b1.pesanall()
            ygdipesan.append(pesanapaaja)
            jumlahygdpsn.append(pesananqt)

            loo = input("Pesan lagi?, | (1)Ya | (0)Tidak : ")
            if loo == "1":
                loops = True
            else:
                loops = False
        
        #Process 3 [Bayar]
        b1 = Pesanan(nomenu, pesananqt)
        tagihan = b1.Hargaall()
        print ('\nTotal tagihan : ',tagihan)
        bayar = int(input("Masukkan Jumlah uang :"))

        #Process 4 cetak Struk
        print('\n____Struk Pembayaranan____')
        print('____Pada tanggal : ', timedate)
        print('____Atas nama : ', x)
        print('____Menu yang dipesan : ')
        while counterr < (len(ygdipesan)):
            print('            ', ygdipesan[counterr], 'sebanyak ', jumlahygdpsn[counterr])
            counterr += 1
        print('____Total harga sebesar = ', tagihan)
        print('____Jumlah uang = ', bayar)
        print('____Jumlah kembalian :', bayar-tagihan)
        print('')
    
    else:
        print("\n 1.Kopi[3K] | 2.Roti[5K] | 3.Chappucino[22K] | 4.Ice Coffee Latte[16K] | 5.Indomie[10K]")
        print(" 6.Es Kopi Susu[18K] | 7.Nasi Goreng[20K] | 8.Ice Mocchacino[19K] | 9.Pisang Goreng[18K]")
        print(" 10.Americano[13K] | 11.Pisang Bakar Mantap[18K] | 12.Coffee Latte[15K] | 13.Kue Manis[10K]")
        print(" 14.Chocolate[15K] | 15.Kentang Goreng[10K] | 16.Roti Bakar[20K] | 17.Martabak[22K]")

else:
    print('Pilihan tidak tersedia')

conn.commit()

conn.close()
