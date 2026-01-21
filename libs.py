import db


def welcome(title) :
    garis = "=" * (len(title)+6)
    print(garis)
    print(f"== {title} ==")
    print(garis)
    
def ulang(title) :
        repeat = input(f"\n\napakah anda ingin lanjut {title} [y/n] \n")
        if repeat == "n" :
            print("\nhave a good day")
            exit()

def add() :
    while True :
        kode_barang = int(input("masukkan kode barang : "))
        nama_barang = input("masukkan nama barang : ")
        stok_barang = int(input("masukkan stok barang : "))
        harga_barang = int(input("masukkan harga barang : "))

        db.insert_item(kode_barang, nama_barang, stok_barang, harga_barang)
        repeat = input("apakah anda ingin menambah barang lagi? [y/n]")
        if repeat == "n" :
            return False

def read() :
        item= db.fecthdata()
        for item in item:
            kode_barang = item[4]
            nama_barang = item[1]
            harga_barang = item[3]
            stok_barang = item[2]
            print(f'''
        kode barang : {kode_barang}
        {nama_barang} | {harga_barang}
        Stok barang : {stok_barang}
                ''')
        
def update() :
     while True :
          kode_barang = int(input("masukkan kode barang : "))
          stok_barang = int(input("masukkan jumlah stok : "))
          db.update_item_stock(stok_barang, kode_barang)
          repeat = input("apakah anda ingin mengedit stok barang lagi? [y/n]")
          if repeat == "n" :
            return False
          
def delete() :
    while True:
        kode_barang = int(input("masukkan kode barang yang ingin di hapus : "))
        db.delete_item(kode_barang)
        repeat = input("apakah anda ingin menghapus stok barang lagi? [y/n]")
        if repeat == "n" :
            return False
        
def kasir():
    print("kasir")
    while True:
        kode_barang = int(input("masukkan kode barang : ").strip())
        barang =  db.find(kode_barang)
        if barang is None : 
                print("barang tidak ada di dalam stok")
                repeat = input("apakah anda ingin membeli barang lagi? [y/n]")
                if repeat == "n" :
                    return False
                else : continue
        else : nama_barang, harga = barang 
        print(f'''Barang : {nama_barang} | harga : {harga}''')
        jumlah = int(input("masukkan QTY : "))
        total_harga = jumlah * harga
        print(f"total harga yang harus anda bayar adalah :",total_harga)

        repeat = input("apakah anda ingin membeli barang lagi? [y/n]")
        if repeat == "n" :
            return False

def pilihan():
    pilih = int(input("\n\nMasukkan Pilihan anda : "))
    if pilih == 1 :
        kasir()
    elif pilih == 2 :
        print("Stok Barang")
        read()
    elif pilih == 3 :
        print("Tambah Barang")
        add()
    elif pilih == 4 :
        print("Update Stok Barang")
        read()
        print("\n Pilih kode barang yang ingin di Update : ")
        update()
    elif pilih == 5 :
        print("Delete Stok Barang")
        read()
        delete()
    else : 
        print("pilihan anda tidak ada")