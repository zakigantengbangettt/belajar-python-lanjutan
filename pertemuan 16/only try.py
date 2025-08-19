print("\n----menggunakan .keys()-----\n")
data_nilai ={
    "budi" : 20,
    "caca" : 30,
    "dodi" : 50
}
print("interasi melalui keys")
for siswa in data_nilai:
    nilai =data_nilai[siswa]
    print(f"nilai{siswa} adalah {nilai}")
print("===data yang menngunakan kata keys")
keys = data_nilai.keys()
print("objeck keys",keys)
for nama in data_nilai.keys():
    print(nama)
    
print("\n--- Menggunakan .values() ---") 
semua_nilai = data_nilai.values() 
print("Objek values:", semua_nilai) # Output: dict_values() 
total_nilai = 0
for nilai in data_nilai.values(): 
    total_nilai += nilai 
print(f"Total semua nilai: {total_nilai}") 

print("\nmenggunkan kata items()\n")
pasangan =data_nilai.items()
print(f"objeck items(){pasangan}")
for nama,nilai in data_nilai.items():
    print(f"siswa bernanama {nama} dengan nilai {nilai}")

kontak = {'Andi': '08123', 'Budi': '08234', 'Citra': '08345'} 
nomor_budi = kontak.pop('Budi') 
print(f"Menghapus Budi, nomornya adalah: {nomor_budi}") 
print("Kontak sekarang:", kontak)

kontak.popitem() 
print("Setelah popitem:", kontak) # Akan menghapus Citra

del kontak['Andi'] 
print("Setelah del Andi:", kontak) 

database_siswa = { 
"siswa_001": { 
"nama": "Budi Santoso", 
"umur": 17, 
"nilai": { 
"matematika": 90, 
"fisika": 88, 
"bahasa": 85 
        } 
    }, 
"siswa_002": { 
"nama": "Ani Lestari", 
"umur": 16, 
"nilai": { 
"matematika": 95, 
"fisika": 91, 
"bahasa": 89 
        } 
    } 
} 
# Mengakses data nested
 # Mengambil seluruh data siswa_002 
data_ani = database_siswa["siswa_002"] 
print("Data Ani:", data_ani) 
# Mengakses nama Ani 
nama_ani = database_siswa["siswa_002"]["nama"] 
print("Nama Siswa 002:", nama_ani) 
# Mengakses nilai fisika Budi 
nilai_fisika_budi = database_siswa["siswa_001"]["nilai"]["fisika"] 
print("Nilai Fisika Budi:", nilai_fisika_budi) 
# Menambahkan data baru 
database_siswa["siswa_001"]["nilai"]["kimia"] = 82 
print("Nilai Budi setelah ditambah Kimia:", database_siswa["siswa_001"]
 ["nilai"]) 

print("==============")
 # Loop luar untuk setiap siswa (key: 'siswa_001', 'siswa_002')
for id_siswa, data in database_siswa.items(): 
    print(f"\n--- Menampilkan data untuk ID: {id_siswa} ---") 
    nama_siswa = data["nama"] 
    umur_siswa = data["umur"] 
    print(f"Nama: {nama_siswa}, Umur: {umur_siswa}") 
# Loop dalam untuk setiap nilai mata pelajaran 
    print("Nilai:") 
for mapel, nilai in data["nilai"].items(): 
        print(f"  - {mapel.capitalize()}: {nilai}") 
        
