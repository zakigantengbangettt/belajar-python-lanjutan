print("======latihan 1 =======")
belanjaan =[]
belanjaan.append("telur")
belanjaan.append("susu")
belanjaan.append("roti")
print(f"setelah di tambah oleh append",belanjaan)
belanjaan.insert(1,"apel")
print(f"di tambah oleh insert",belanjaan)
belanjaan.remove("apel")
print(f"setelah di hapus oleh remove gara gara gak jadi beli",belanjaan)
print(f"jadi hasil list belanja",belanjaan)

print("========latihan 2 ======")
list_nilai =[98,76,88,100,54]
print(f"list nilai awal",list_nilai)
list_berubah = sorted(list_nilai)
print("list sudah di ubah",list_berubah)

print("========latihan 3 ======")
input_user = input("masukan apa ajaa:")
daftar_kata =input_user.split()
print(daftar_kata)
daftar_kata.sort()
print(daftar_kata)
print(len(daftar_kata))

print("========latihan 4 ======")
a = [1, 2, 3, 4, 5] 
b = a               
c = a.copy()        
b[1] = 20 
c[1] = 30 
print(f"a = {a}") 
print(f"b = {b}") 
print(f"c = {c}")
