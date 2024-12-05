#Tugas5

#1
#membuat variabel list dengan value
kendaraan = ['Xsr', 'Sepeda Motor', 155,'Hitam', 2]
print ("kendaraan")

print(kendaraan)
print("")

#menambah list di belakang dengan value
kendaraan.append('Rp 38.380.000')
print(kendaraan)
print("")

kendaraan.append('Kopling')
print(kendaraan)
print("")

#menambah list setelah jenis kendaraan dengan value
kendaraan.insert(2, 'Yamaha')
print(kendaraan)
print("")

print("=====================================================================================")
print("")

#2
#membuat program python dengan match case untuk menghitung bangun datar
pilih =int(input("""selamat datang di aplikasi menhitung
                 1. untuk menghitung luas persegi
                 2. untuk menghitung luas linkaran
                 3. untuk  menghitung luas segitiga 
                 
                 Masukan pilihan mu\n"""))

match pilih:
    case 1 :
        print("kamu memilih 1 untuk menghitung luas persegi")
        sisi = int(input("masukan nilai sisi persegi: "))
        luasP = sisi * sisi
        print("luas persegi yang sisinya adalah", sisi, "adalah",  luasP)
    
    case 2 :
        print("kamu memilih 2 untuk menghitung luas lingkaran")
        jari2 = int(input("masukan nilai jari-jari lingkarang: "))
        luasL = 3.14 * jari2 * jari2
        print("luas lingkaran yang sisinya adalah", jari2, "adalah",  luasL)

    case 3 :
        print("kamu memilih 3 untuk menghitung luas segitiga")
        tinggi = int(input("masukan nilai tinggi sgitiga: "))
        alas = int(input("masukan nilai tinggi sgitiga: "))
        luasS = 0.5 * alas * tinggi
        print("luas lingkaran yang tingginya adalah", tinggi, "dan alasnya", alas, "adalah",  luasS)

    case _:
        print("data yang kamu masukan salah")