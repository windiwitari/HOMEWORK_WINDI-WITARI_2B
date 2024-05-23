def tampilan():
    print ('-MANAJEMEN STOK BARANG-')
    print('='*25)
    print ('1. Tambah Data Barang')
    print ('2. Edit Data')
    print ('3. Hapus Data Barang')
    print ('4. Cari Data')
    print ('5. Tampilkan Data Barang')
    print ('6. Tampilkan Jumlah Data')
    print ('7. Keluar')
    print('='*25)

barang_list = []

def insert():
    nama = str(input('Masukan Nama Barang : '))
    stok = str(input('Masukan Stok Barang : '))
    data_new = {'nama barang':nama,'stok':stok}
    barang_list.append(data_new)
    print("Data Berhasil di Tambahkan")

def edit():
    try:
        hapus = int(input('Hapus data index ke: '))
        if hapus < 0 or hapus >= len(barang_list):
            print("Indeks tidak valid!")
            return
        
        new = input('Masukkan Nama: ')
        stok_edit = int(input('Masukkan Stok: '))
        barang_list[hapus] = (new, stok_edit)
        print("Data barang berhasil diubah!")
    except ValueError:
        print("Input tidak valid! Pastikan Anda memasukkan data dengan benar")

def delete():
    hapus = int(input('Hapus Data Index Ke : '))
    del barang_list[hapus]
    print("Data barang berhasil diubah!")
  
def cari():
    if barang_list:
        nama = input("Cari Nama Barang: ")
        ditemukan = False
        for a in barang_list:
            if nama.lower() in a['nama barang'].lower():
                print("=== HASIL PENCARIAN ===")
                print(f"- {a['nama barang']} stock {a['stok']}")
                ditemukan = True
            if not ditemukan:
                print("Barang tidak ditemukan!!")       

def Tampilan_data():
    print('Toko Elektronik'.upper())
    for a in barang_list:
        print(a['nama barang'],':',a['stok'])
        
def Jumlah_Data():
    print(f"Jumlah data barang: {len(barang_list)}")