import modul_homework as modul
while True:
    modul.tampilan()
    pilihan = int(input('Masukan Pilihan : '))

    if pilihan == 1:
        modul.insert()

    elif pilihan == 2:
        modul.edit()
    
    elif pilihan == 3:
        modul.delete()

    elif pilihan == 4:
        modul.cari()

    elif pilihan == 5:
        modul.Tampilan_data()

    elif pilihan == 6:
        modul.Jumlah_Data()

    elif pilihan == 7:
        print('~'*30)
        print('Terimakasih Atas Kunjungan Anda')
        print('~'*30)
        exit()

    else:
        print("Pilihan tidak valid, silakan coba lagi.")