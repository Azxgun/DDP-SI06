import math

# Menghitung luas dan keliling tabung
def luas_keliling_tabung(jari_jari, tinggi):
    luas = 2 * math.pi * jari_jari * (jari_jari + tinggi)
    keliling = 2 * math.pi * jari_jari
    return luas, keliling

jari_jari = float(input("Masukkan jari-jari tabung (cm): "))
tinggi = float(input("Masukkan tinggi tabung (cm): "))
luas, keliling = luas_keliling_tabung(jari_jari, tinggi)
print(f"Luas permukaan tabung: {luas} cm²")
print(f"Keliling alas tabung: {keliling} cm")