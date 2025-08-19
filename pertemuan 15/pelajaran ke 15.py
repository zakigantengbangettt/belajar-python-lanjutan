siswa = {
    "nama" : "Budi",
    "umur" : 17,
    "kota" : "Jakarta",
    "lulus" : True,
    "nilai semester":None
}
nama_siswa = siswa['nama']
print(f"nama siswa nya:{nama_siswa}") # cara manggil nilai dari dictionary
umur_siswa = siswa["umur"]
print(f"umur siswa nya:{umur_siswa}") # cara manggil nilai dari
print(siswa)
print(type(siswa))
print("cara menggunkan dick[]")
kontak = ("nama","cella"),("kelas", 12),("tinggal","bandung")
kontak_juga = dict[kontak]
print(kontak_juga)

print("##### menggunkan kata git() ######")
karyawan ={
    "nama" : "faiz",
    "umur" : 12,
    "kota" : "bandung",
}
nama =karyawan.get("nama")
print(f"data:\t{nama}")
umur = karyawan.get("umur")
print(f"data:\t{umur}")
pekerjaan =karyawan.get("karyawan","siswa")
print(f"data:\t{pekerjaan}") # jika tidak ada maka akan mengambil nilai default

print("**** menambah pasangan key value ******")
data_pendaftaran ={
    "nama" : "cantika",
    "umur" : 20,
    "alumni":"SMA 02"
}
print(f"data awal {data_pendaftaran}")
data_pendaftaran["kelamin"] = "cewek"
data_pendaftaran["poin"]   = 100
print(f"setelah di tambah{data_pendaftaran}")



kota ={"jaktim":"jakarta timur"}
print(len(kota)) # mengambnilai dari dictionary
