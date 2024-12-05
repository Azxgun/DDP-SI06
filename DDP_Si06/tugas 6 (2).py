print("\n============= No 2===============")
jumlah = 0 #untuk menampung hasil penjumlahan
string = "" #hasil jumlah dalam bentuk string
bilangan = 1

while bilangan <= 19:
    jumlah += bilangan
    string += str(bilangan)
    if bilangan < 19 :
       string += "+"
    bilangan += 2
print (f"{string} = {jumlah}")
