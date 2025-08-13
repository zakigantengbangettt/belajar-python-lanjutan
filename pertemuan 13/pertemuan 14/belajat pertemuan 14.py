nama_nama_buah = ['magga','apel','durian']
print("list awal",nama_nama_buah)
nama_nama_buah.append("rambutan")
print(nama_nama_buah)
nama_nama_buah.append("alpukat")
print(nama_nama_buah)

list_b = [1,2,3,4,5]  # menggunakam extend supaya tidak ngaco
list_a = [6,7,8,9,10]
list_b.extend(list_a)
print(list_b)

huruf = ['a','b','d','e']  # insert di gunakan untuk menambah kan data di tengah list atau di mana pun sesuai index kita
print("sebelum di insert",huruf)
huruf.insert(2,'c')
print("setelah di insert",huruf)

i = ['a','b','c','d'] # del untuk menghapus data list
del i[1:3]
print(i)

nilai = [1,2,3,4,5]
nilai_yg_dihapus= nilai.pop(2) # pop untuk menghapus data list dan mengembalikan data yang di hapus
print("nilai yang dihapus",nilai_yg_dihapus)
print("nilai setelah dihapus",nilai)

hewan =['kucing','pemadam','singa','buaya']
hewan.remove("pemadam")  #remove buat menghapus data list tanpa index
print(hewan)

j =[50,10,30,20,40,60,80,70] # untuk mengurutkan angka dan string
j.sort()
print(j)

j =[50,10,30,20,40,60,80,70] # reverse untuk mengembalikan urutan list jadi kebalik
j.reverse()
print(j)


list_asli = [1,2,3,4,5,6]
list_alias = list_asli [:] # atau list_asli.copy()
print(f"list asli sebelum di ubah{list_asli}")
print(f"list alias sebelum di ubah{list_alias}")
list_asli.append(7)
print(f"list sesudah di ubah{list_asli}")
print(f"list alias sesudah di ubah{list_alias}") # list alias tidak ber



