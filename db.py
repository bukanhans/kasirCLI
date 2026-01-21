import mysql.connector

db = mysql.connector.connect(
    host='',
    user='',
    password='',
    database='db_kasir'
)

def insert_item(kode_barang, nama_barang, stok_barang, harga_barang ) :
    cursor = db.cursor()
    cursor.execute("INSERT INTO tbl_barang (kode_barang, nama_barang, stok_barang, harga_barang) VALUES(%s,%s,%s,%s)",(kode_barang, nama_barang, stok_barang, harga_barang))
    db.commit()

    if cursor.rowcount > 0 :
        print("data berhasil di masukkan")
    else :
        print("data gagal di masukkan")

def find(kode_barang):
    cursor = db.cursor()
    cursor.execute("SELECT nama_barang, harga_barang FROM tbl_barang WHERE kode_barang = (%s)", ( kode_barang,))
    data = cursor.fetchone()
    return data

def fecthdata() :
    cursor = db.cursor()
    cursor.execute("SELECT * FROM tbl_barang")
    return cursor.fetchall()

def update_item_stock(stok_barang, kode_barang) :
    cursor = db.cursor()
    cursor.execute("UPDATE tbl_barang SET " \
    "stok_barang = (%s) WHERE kode_barang = (%s)",(stok_barang, kode_barang))
    db.commit()

    if cursor.rowcount > 0 :
        print("data berhasil di masukkan")
    else :
        print("data gagal di masukkan")

def delete_item(kode_barang) :
    cursor = db.cursor()
    cursor.execute("DELETE FROM tbl_barang WHERE kode_barang = (%s)",(kode_barang,))
    db.commit()
    if cursor.rowcount > 0 :
        print("data berhasil di hapus")
    else :
        print("data gagal di hapus")
    