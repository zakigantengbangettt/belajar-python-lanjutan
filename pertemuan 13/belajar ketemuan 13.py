daftar_kota = ['jakarta','surabaya','bandung']
print("nama - nama kota besar")
for kota in daftar_kota:
    print(kota)

angka = ['1','2','3','4','5'] # loop dengen index
for i in range(len(angka)):
        print(f"mengubah index {i}")
        angka [i] = angka[i]*2
print("lsit setelah di kalikan dua",angka)

list_a =['1','2','3','4']
list_b = ['5','6','7','8']
list_c = list_a + list_b # begabungan /concetenation
print(list_c)   
print(list_a*4) # perulangan list /repetion
