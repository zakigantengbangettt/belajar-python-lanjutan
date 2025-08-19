print("======latihan 1======")
harga_buah =  {"apel": 5000, "jeruk": 8500, "mangga":
 7800, "pisang": 3000}
pasangan = harga_buah.items()
print(pasangan)
for buah in harga_buah:
    harga = harga_buah[buah]
    print(f"harga 1 kg {buah} adalah {harga} rupiah")

print("=====latihan 2========")
kontak ={
    "ibu" : "085123456789",
    "bapak" : "081234567890",
    "teman" : "082345678901"
}
kontak["ibu"] = "087777766556"
kontak.pop("teman")
print("sudah di ubah",kontak)

print("=====latihan 3========")
id_produck ={
    "PROD001":{
        "nama" : "samsung",
        "harga" : 1000000,
        "stok" : 100
        
    },
    "PROD002":{
        "nama" : "sony", 
        "harga" : 2000000,
        "stok" : 50
        },
}   

print(f"nama produck PROD001 adalah {id_produck['PROD001']['nama']}")
print(f"harga produck PROD002 adalah {id_produck['PROD002']['harga']}")

print("=====latihan 4=====")
input_user =input("masukan file disini:")
try:
    with open(input_user, 'r') as file:
        penghitung_kata ={}
        for baris in flle:
            
