
print('=======latihan 01======')

import re
data =  "Pendapatan bulan ini adalah Rp 1,500,000, sedangkan  pengeluaran sebesar Rp 850,000."
semua_angka = re.findall(r'\d+', data)
print(f"outputnya: {semua_angka}")

print('=======latihan 02 =====')
import re
input_user = input("masukan nomor telepon\nkamu yang jelek ituu:")

if re.search(r'^\d+$',input_user):
    print("loadinggg....")
    print("nomor anda",input_user)
    if 10 <= len(input_user)<=13:
        print("nomor jelek vilid")
    else:
        print("kepanjangan pinterrrr")
else:
    print("nomor kocak bukan angka")

print('=======latihan 03 =====')
import re
kata ="python adalah bahasa yang menyenangkan, python mudah dipelajari."
pola_anka = r'\w+'
terserah = re.search(pola_anka,kata)
if terserah:
    print("hasil ketemu",terserah.group())

else:
    print("tidak ketemu")

j = re.findall(r'\w+',kata)
print('yang peke findall',j)

print('=======latihan 04 =====')
import re
l ="Kucing, anjing, dan burung adalah hewan peliharaan."
print(re.findall(r'Kucing|anjing|burung',l))
 

