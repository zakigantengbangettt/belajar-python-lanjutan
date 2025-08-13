try:
    with open("transaksi_kotor.txt") as file_input:
        with open("transaksi_kotor.txt", "w") as file_output:
            file_output.write("=======================\n")
            file_output.write("laporan transaksi\n")
            file_output.write("=======================\n")
            grand_total = 0
            for baris in file_input:
                baris = baris.strip()

                if not baris:
                    continue
                data_potongan = baris.split(",")
                id_bersih =data_potongan[0].strip().upper()
                nama_bersih =data_potongan[1].strip().title()
                jumlah_bersih = int(data_potongan[2].strip())
                harga_bersih = int(data_potongan[3].strip())
                total_harga =jumlah_bersih*harga_bersih
                grand_total += total_harga

                file_output.write(
                    f"ID: {id_bersih} | Produk: {nama_bersih} | Jumlah: {jumlah_bersih} | Total Harga: Rp {total_harga}\n"
                )
                file_output.write(f"\ndata sedang diproses...\n")
                file_output.write(f"=======================\n")
                print("data sudah di bersihkan ngappp tinggal liat ajaaaa...")
except FileNotFoundError:
    print("file tidak di temukan")
    


                   


