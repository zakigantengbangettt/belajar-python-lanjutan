print('=================================')
print('Selamat datang di Apliasi polling')
print('=================================')

survei =[
    {
        "pertanyaan": "apa bahasa pemegroman favorite anda:",
        "opsi" : ["Python","Javascrip","Java","C++"]

    },
    {
        "pertanyaan":"apa sistem yang kamu pake",
        "opsi" : {"windows","linux","macOS"}
        
    }
]

hasil_polling ={}
for item_survei in survei:
    for opsi in item_survei["opsi"]:
        hasil_polling[opsi] = 0

for item_survei in survei:
    print(f"\npertanyaan {item_survei["pertanyaan"]}")
    for i,opsi in enumerate(item_survei["opsi"]):
        print(f"-{opsi}")
    while True:
        input_user=input("jawaban anda").strip()
        if input_user in item_survei["opsi"]:
            print(f"{input_user},====terimaksih====")
        break
else:
    print(f"{input_user}")
    print("maaf tidak bisa")

print("======= hasil polling ========")
total_suara = sum(hasil_polling.values())
for opsi,jumlah_suara in hasil_polling.items():
    suara =(jumlah_suara/jumlah_suara)*100 if total_suara > 0 else 0
    print(f"{opsi} : {jumlah_suara} suara {suara:.2f}%\n")
print("="*44)

#with open("hasil_polling.txt") as file:




