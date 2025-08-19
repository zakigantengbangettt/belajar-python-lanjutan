print("------latihan 01 -----")
biodata ={
    "nama" :'Muhammad Zaki NIF',
    "umur" : 18,
    "hobi" : ["bermain sepak bola","membaca buku"],
    "sudah menikah" : True

}
data_gabungan ="|".join(f'{k}:{v}' for k,v in biodata.items())
print(data_gabungan)
nama_biodata = biodata["nama"]
print(f"biodata saya:{biodata}")
print(f"nama biodata saya:{nama_biodata}")
hobi_biodata = biodata["hobi"][0]

print("------latihan 02 ------")
biodata["kota"] = ["jakarta"]
print(f"list sudah di ubah{biodata}")
biodata["umur"] = 19
print(f"list sudah di ubah{biodata}")

print("------latihan 03 ------")
# print(biodata["pekerjaan"]) eror karena tidak ada di dalam biodata
print(biodata.get("pekerjaan","pelajar")) # tidak ada di dalam biodata jadi akan out put nya None

print("------latihan 04 ------")
input_user =input("masukan sebuah kalimat bebas ajaa:")
menghitung_huruf={}
for huruf in input_user:
    if huruf not in menghitung_huruf:
        menghitung_huruf [huruf] = 1
    else:
        menghitung_huruf[huruf] += 1
print(menghitung_huruf)
