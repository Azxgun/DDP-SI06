import math

def luas_tabung(jari_jari, tinggi):
    luas_permukaan = 2 * math.pi * jari_jari * (jari_jari + tinggi)
    print(f"Luas Permukaan Tabung dengan jari-jari {jari_jari} dan tinggi {tinggi} = {luas_permukaan}")

def luas_kerucut(jari_jari, tinggi):
    luas_alas = math.pi * jari_jari ** 2
    garis_pelukis = math.sqrt(jari_jari ** 2 + tinggi ** 2)
    luas_selimut = math.pi * jari_jari * garis_pelukis
    luas_total = luas_alas + luas_selimut
    print(f"Luas Alas Kerucut = {luas_alas}")
    print(f"Luas Selimut Kerucut = {luas_selimut}")
    print(f"Luas Total Kerucut = {luas_total}")

def luas_kubus(sisi):
    luas_permukaan = 6 * (sisi ** 2)
    print(f"Luas Permukaan Kubus dengan sisi {sisi} = {luas_permukaan}")

def luas_permukaan_balok(panjang, lebar, tinggi):
    luas_permukaan = 2 * (panjang * lebar + panjang * tinggi + lebar * tinggi)
    print(f"Luas Permukaan Balok {panjang} x {lebar} x {tinggi} = {luas_permukaan}")

def l_prisma(luas_alas, keliling_alas, tinggi) :
    luas = (2 * luas_alas) + (keliling_alas * tinggi)
    print(f'Luas Prisma {(2 * luas_alas)} + {(keliling_alas * tinggi)} = {luas}')