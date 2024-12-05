import math

def luas_persegi(sisi):
    luas = sisi ** 2
    keliling = 4 * sisi
    print(f"Luas Persegi {sisi} x {sisi} = {luas}")
    print(f"Keliling Persegi adalah {keliling}")

def luas_persegi_panjang(panjang, lebar):
    luas = panjang * lebar
    keliling = 2 * (panjang + lebar)
    print(f"Luas Persegi Panjang {panjang} x {lebar} = {luas}")
    print(f"Keliling Persegi Panjang adalah {keliling}")

def luas_segitiga(alas, tinggi):
    luas = 0.5 * alas * tinggi
    print(f"Luas Segitiga 1/2 x {alas} x {tinggi} = {luas}")

def luas_lingkaran(jari1 , jari2):
   luas = 3.14 * jari1 * jari2
   print(f"Luas Lingkaran phi x {jari1} x {jari2} = {luas}")


def luas_jajar_genjang(alas, tinggi):
    luas = alas * tinggi
    print(f"Luas Jajar Genjang {alas} x {tinggi} = {luas}")

