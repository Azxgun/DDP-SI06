print("==============================================================================================")
#Bilangan Genap atau Ganjil

angka = int(input("masukan nilai angka "))
ganjil = "Bilangan Ganjil"
genap = "Bilangan genap"
if angka % 2 == 0:
    print(genap)
elif angka % 2 != 0:
    print(ganjil)
else:
    print("input tidak valid")

print("==============================================================================================")
#Nilai Ujian

nu = int(input("masukan nilai ujian kamu "))
lulus = "kamu lulus"
tidak_lulus = "kamu tidak lulus"

if nu >= 75:
    print("kamu lulus")
else:
    print("kamu tidak lulus")

print("==============================================================================================")
#Cek Usia dan Status

usia = int(input("masukan usia kamu "))
anak = "status kamu anak-anak"
remaja = "status kamu remaja"
dewasa = "status kamu dewasa"
if usia >=18:
    print("status kamu Dewasa")
elif usia > 13 and usia < 18:
    print("status kamu Remaja")
else:
    print("status kamu Anak-Anak")

print("==============================================================================================")
#Cek Keangotaan

status_anggota = input("masukan status anggota (gold, silver, bronze): ").lower()

if status_anggota == "gold" or status_anggota == "silver":
    print("selamat kamu mendapat diskon")
else:
    print("maaf kamu tidak mendapatkan diskon, terimakasih sudah berpatisi")

print("==============================================================================================")
#Pembelian Diskon

jp = int(input("masukan jumlah pembelian: "))
harga_barang = 1000
harga_diskon = harga_barang * jp * (10/100)
harga_total = harga_barang * jp
total = harga_total - harga_diskon
print(f"kamu mendapat diskon 10%, harga per barang {harga_barang} jadi total yang harus dibayar oleh kamu adalah {total} ") if jp > 100 else print(f"Harga per barang {harga_barang}, jadi total yang harus kamu dibayar adalah {harga_total} ")