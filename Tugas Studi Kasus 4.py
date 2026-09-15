produk = {
    "nama" : "Indomie",
    "harga" : 3500,
    "stok" : 100
}

while True:
    print("="*40)
    print("MENU PENGELOLAAN DATA PRODUK TOKO DIMAS")
    print("="*40)
    print("\n1. Tampilkan data produk")
    print("2. Tambahkan kategori dari produk")
    print("3. ubah stock produk")
    print("4. ubah harga produk")
    print("5. hapus kategori produk")
    print("6. selesai\n")
    print("="*40)

    pilihan = input("Pilih menu (1-6): ")

    if pilihan == "1":
        print("DATA PRODUK ANDA SAAT INI: ", produk)

    elif pilihan == "2":
        kategori = input("Masukkan kategori dari produk: ")
        produk ["kategori"] = kategori
        print(f"kategori {kategori} berhasil ditambahkan!")

    elif pilihan == "3":
        try:
            stok_baru = int(input("Masukkan stok baru produk: "))
            produk["stok"] = stok_baru
            print("stok telah diperbarui!")
        except ValueError:
            print("XXX stok berupa angka, harap masukkan angka XXX")

    elif pilihan == "4":
        try:
            harga_baru = int(input("Masukkan harga baru produk: "))
            produk["harga"] = harga_baru
            print("Harga telah diperbarui!")
        except ValueError:
            print("XXX harga berupa angka, harap masukkan angka XXX")

    elif pilihan == "5":
        del kategori
        print("Kategori produk berhasil dihapus!")

    elif pilihan == "6":
        print("Sistem berhenti, terimakasih telah menggunakan sistem ini :)")
        break

    else:
        print("INPUT SALAH, harap masukkan angka (1-6) !!!!")
    