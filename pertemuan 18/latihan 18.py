print("=======latihan 01======")
class kucing :
    def __init__(self,nama,warna):
        self.nama = nama
        self.warna = warna
       

    def bersuara (self):
        print("meowwwwwwww!!!!")

    def perkenalan_diri (self):
        print(f"Halo, saya kucing bernama {self.nama} dan warna saya {self.warna}")
kucing_1 = kucing("sule","hideng")
kucing_2 = kucing("alex","pirang")
kucing_1.perkenalan_diri()
kucing_1.bersuara()

kucing_2.perkenalan_diri()
kucing_2.bersuara()

print("=======latihan 02======")
class rekeningbank:
    def __init__(self,nomor_rekening,nama_pemilik):
        self.saldo = 0
        self.nama_pemilik = nama_pemilik
        self.nomor_rekening = nomor_rekening
    
    def lihat_saldo (self):
        print(f"saldo anda saat ini\nRP{self.saldo}")

    def setor(self,jumlah):
        self.saldo += jumlah
        print(f"sabar sebentar...\nberhasil setor {jumlah}.\nsaldo lw sisa {self.saldo}")

    def tarik(self,jumlah):
        self.saldo -= jumlah
        if jumlah > self.saldo:
            print(f"mampus !!!!!\nsaldo tidak mencukupi \nmakannya kerja lagi budi lihat ini lihat {jumlah} saldo mu udah kaya orang ngaggur")
        else:
            print(f"jumlah anda mencukupi {jumlah} walau saldo anda mencukupi tidak ada alesan untuk bekerja budii")
rekening_budi = rekeningbank("09747872","budi")
rekening_budi.lihat_saldo()
rekening_budi.setor(30)
rekening_budi.tarik(5200000)
rekening_budi.lihat_saldo()





        


        

