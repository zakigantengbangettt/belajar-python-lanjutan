print("======latihan 1=====")
jadwal_senin =["sains","matematika","olahraga","sejarah"]
print("jadwal pelajaran pada hari senin adalah:")
for i in jadwal_senin:
    print(i)
print("jadwal mata pelajaran pertama pada hari senin")
print(jadwal_senin[0])
print("jadwal mata pelajaran terakhir pada hari senin adalah:")
print(jadwal_senin[-1])

print("======latihan 2=====")
print("pada minggu depan akan ada perubahan jadwal pelajaran:")
jadwal_senin [2] ='kimia'
print("ini adalah jadwal yang di ubah",jadwal_senin)

print("======latihan 3=====")
nilai_mentah =[55,63,72,81,90]
for i in range(len(nilai_mentah)):
    nilai_mentah[i] =+ 5
    print("nilai bonus dari nilai mentah adalah: ",nilai_mentah)

print("======latihan 4=====")
awal_minggu =["senin","selasa","rabu","kamis","jum'at"]
akhir_minggu =["sabtu","minggu"]
seminggu = awal_minggu + akhir_minggu
print("jadwal minggu ini adalah: ",seminggu)
waktu_kerja =seminggu[0:5]
print("waktu kerja adalah: ",waktu_kerja)