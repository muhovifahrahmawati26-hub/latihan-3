# Input tiga bilangan dari pengguna
a = int(input("Masukkan bilangan pertama:"))
b = int(input("Masukkan bilangan kedua:"))
c = int(input("Masukkan bilangan ketiga:"))

# Tentukan bilangan terbesar
if (a >= b) and (a >= c):
    terbesar = a
elif (b >= a) and (b >= c):
    terbesar = b
else:
    terbesar = c

# Tampilkan hasilnya
print("Bilangan terbesar adalah: {terbesar}")