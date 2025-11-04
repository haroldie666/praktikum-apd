from prettytable import PrettyTable
from data import users, buku_sementara, kategori_buku
import os

os.system("cls || clear")
sudah_login = False
user_saat_ini = None
role = None
program_berjalan = True
no_buku_selanjutnya = 5 
valid_angka_positif = lambda x: x.isdigit() and int(x) > 0
valid_teks = lambda x: len(x.strip()) > 0

while program_berjalan:
    if not sudah_login:
        tabel_menu = PrettyTable()
        tabel_menu.field_names = ["No", "Menu"]
        tabel_menu.align = "l"
        
        tabel_menu.add_row(["1", "Login"])
        tabel_menu.add_row(["2", "Register"])
        tabel_menu.add_row(["3", "Logout"])
        
        print("\n=== SELAMAT DATANG DI TOKO BUKU SENKUMEDIA ===")
        print(tabel_menu)
        
        pilihan_menu_utama = input("Silakan pilih menu yang tersedia: ").strip()
        if pilihan_menu_utama == '1':

            print("\n--- LOGIN ---")
            input_nama_pengguna = input("Nama pengguna: ").strip()
            input_kata_sandi = input("Password: ").strip()
            
            login_berhasil = False
            for key, value in users.items():
                if key == input_nama_pengguna and value['password'] == input_kata_sandi:
                    sudah_login = True
                    user_saat_ini = key
                    role = value['role']
                    print(f"\nSelamat datang, {user_saat_ini}")
                    login_berhasil = True
                    break
            
            if not login_berhasil:
                print("Nama pengguna atau password salah. Silakan coba lagi.")

        elif pilihan_menu_utama == '2':
            print("\n--- REGISTER PENGGUNA BARU ---")
            while True:
                nama_pengguna_baru = input("Nama pengguna baru: ").strip()
                nama_sudah_ada = False
                for pengguna in users:
                    if pengguna == nama_pengguna_baru:
                        nama_sudah_ada = True
                        break
                
                if not valid_teks(nama_pengguna_baru):
                    print("Nama pengguna tidak boleh kosong.")
                elif nama_sudah_ada:
                    print("Nama pengguna sudah terdaftar. Gunakan nama lain yang unik.")
                else:
                    break 
            
            while True:
                kata_sandi_baru = input("Password baru: ").strip()
                if not valid_teks(kata_sandi_baru):
                    print("Password tidak boleh kosong. Buatlah password yang kuat.")
                else:
                    break

            users.update({nama_pengguna_baru: {'password': kata_sandi_baru, 'role': 'user'}})
            print(f"Registrasi berhasil! Akun dengan nama '{nama_pengguna_baru}' telah dibuat.")

        elif pilihan_menu_utama == '3':
            print("\nTerima kasih telah mampir di sini. See you next time.")
            program_berjalan = False
        
        else:
            print("Pilihan tidak valid. Silakan pilih angkanya saja.")
        
    #Menu setelah login
    elif sudah_login:
        os.system("cls || clear")
        if role == 'admin':
            tabel_admin = PrettyTable()
            tabel_admin.field_names = ["NO", "Menu"]
            tabel_admin.align = "l"
            tabel_admin.add_row(["1", "Lihat data buku (Read)"])
            tabel_admin.add_row(["2", "Tambah buku baru (Create)"])
            tabel_admin.add_row(["3", "Update data buku (Update)"])
            tabel_admin.add_row(["4", "Hapus data buku (Delete)"])
            tabel_admin.add_row(["5", "Logout"])
            print(f"\n=== MENU {role.upper()} ===")
            print(tabel_admin)
            pilihan_admin = input("Pilih menu Admin: ").strip()
            
            #READ
            if pilihan_admin == '1':
                print("\n--- DAFTAR BUKU SEKARANG ---")
                
                tabel_buku = PrettyTable()
                tabel_buku.field_names = ["NO", "Judul", "Penulis", "Harga (Rp)", "Stok", "Kategori"]
                
                if not buku_sementara:
                    print("Tidak ada data buku yang tersedia.")
                else:
                    for key, value in buku_sementara.items():
                        format_harga = (f"{value['Harga']:,}".replace(",", "."))
                        tabel_buku.add_row([key, value['Judul'], value['Penulis'], format_harga, value['Stok'], value['Kategori']])

                        tabel_buku.align["NO"] = "r"
                        tabel_buku.align["Judul"] = "l"
                        tabel_buku.align["Penulis"] = "l"
                        tabel_buku.align["Harga (Rp)"] = "r"
                        tabel_buku.align["Stok"] = "r"
                        tabel_buku.align["Kategori"] = "l"
                    print(tabel_buku)
                input("Tekan enter untuk kembali ke menu Admin...")

            #Create admin
            elif pilihan_admin == '2':
                os.system("cls || clear")
                print("\n--- TAMBAH BUKU BARU ---")
                
                #Memasukkan judul baru
                while True:
                    judul_baru = input("Judul: ").strip()
                    if valid_teks(judul_baru): 
                        break
                    print("Judul tidak boleh kosong.")

                #Memasukkan nama penulis
                while True:
                    penulis_baru = input("Penulis: ").strip()
                    if valid_teks(penulis_baru): 
                        break
                    print("Penulis tidak boleh kosong.")

                #Memasukkan harga
                while True:
                    harga_teks = input("Harga (contoh: 150000): ").strip()
                    if valid_angka_positif(harga_teks):
                        harga_baru = int(harga_teks)
                        break
                    print("Input harga tidak valid. Isi dengan benar.")

                #Memasukkan stok
                while True:
                    stok_teks = input("Stok: ").strip()
                    if stok_teks.isdigit() and int(stok_teks) >= 0:
                        stok_baru = int(stok_teks)
                        break
                    print("Input stok tidak valid. Isi dengan benar.")
                    
                #Memasukkan kategori
                print("\n--- PILIH KATEGORI BUKU ---")
                tabel_kategori = PrettyTable()
                tabel_kategori.field_names = ["NO", "Kategori"]
                for i, kategori in enumerate(kategori_buku):
                    tabel_kategori.add_row([i+1, kategori])

                print(tabel_kategori)

                while True:
                    pilihan_kategori = input("Pilih kategori (nomor): ").strip()
                    if pilihan_kategori.isdigit():
                        pilihan_kategori = int(pilihan_kategori)
                        if 1 <= pilihan_kategori <= len(kategori_buku):
                            kategori_baru = kategori_buku[pilihan_kategori - 1]
                            break
                    print("Pilihan kategori tidak valid.")

                #Memperbarui data buku
                buku_sementara[no_buku_selanjutnya] = {
                    'Judul': judul_baru,
                    'Penulis': penulis_baru,
                    'Harga': harga_baru,
                    'Stok': stok_baru,
                    'Kategori': kategori_baru
                }
                print(f"\nBuku '{judul_baru}' berhasil ditambahkan dengan NO {no_buku_selanjutnya}.")
                no_buku_selanjutnya += 1 

            #Update admin
            elif pilihan_admin == '3':
                os.system("cls || clear")
                print("\n--- UPDATE DATA BUKU ---")
                
                tabel_buku = PrettyTable()
                tabel_buku.field_names = ["NO", "Judul", "Penulis", "Harga (Rp)", "Stok", "Kategori"]
                
                if not buku_sementara:
                    print("Tidak ada data buku yang tersedia. Kembali ke menu utama.")
                    continue

                for key, value in buku_sementara.items():
                    format_harga = f"{value['Harga']:,}".replace(",", ".")
                    tabel_buku.add_row([key, value['Judul'], value['Penulis'], format_harga, value['Stok'], value['Kategori']])
                    tabel_buku.align["NO"] = "r"
                    tabel_buku.align["Judul"] = "l"
                    tabel_buku.align["Penulis"] = "l"
                    tabel_buku.align["Harga (Rp)"] = "r"
                    tabel_buku.align["Stok"] = "r"
                    tabel_buku.align["Kategori"] = "l"
                print(tabel_buku)
                
                #Cari NO buku yang akan diubah
                buku_ditemukan = None
                while True:
                    id_ubah_teks = input("\nMasukkan NO buku yang akan diubah: ").strip()
                    if not id_ubah_teks.isdigit():
                        print("Input NO tidak valid. Masukkan angka.")
                        continue
                    
                    id_ubah = int(id_ubah_teks)
                    #Cari buku berdasarkan NO
                    for key in buku_sementara.keys():
                        if key == id_ubah:
                            buku_ditemukan = buku_sementara[key]
                            break
                    
                    if buku_ditemukan:
                        break 
                    else:
                        print(f"Buku dengan NO {id_ubah} tidak ditemukan.")
                
                #Update buku
                if buku_ditemukan:
                    harga_saat_ini_format = f"{buku_ditemukan['Harga']:,}".replace(",", ".")

                    print("\n(Kosongkan jika tidak ada data yang ingin diubah)") 
                    data_diubah = False

                    #Ubah judul
                    judul_baru_input = input(f"Judul baru ({buku_ditemukan['Judul']}): ").strip()
                    if judul_baru_input != "":
                        if valid_teks(judul_baru_input):
                            buku_ditemukan['Judul'] = judul_baru_input
                            data_diubah = True
                        else:
                            print("Judul tidak diubah.")

                    #Ubah penulis
                    penulis_baru_input = input(f"Penulis baru ({buku_ditemukan['Penulis']}): ").strip()
                    if penulis_baru_input != "":
                        if valid_teks(penulis_baru_input):
                            buku_ditemukan['Penulis'] = penulis_baru_input
                            data_diubah = True
                        else:
                            print("Penulis tidak diubah.")

                    #Ubah harga
                    while True:
                        harga_lama_display = f"{buku_ditemukan['Harga']:,}".replace(",", ".") 
                        harga_baru_teks = input(f"Harga baru ({harga_lama_display}): ").strip()
                        if harga_baru_teks == "": 
                            break 
                        elif valid_angka_positif(harga_baru_teks):
                            buku_ditemukan['Harga'] = int(harga_baru_teks)
                            data_diubah = True
                            break
                        print("Masukkan angka positif.")

                    # Ubah stok
                    while True:
                        stok_baru_teks = input(f"Stok baru ({buku_ditemukan['Stok']}): ").strip()
                        if stok_baru_teks == "":
                            break 
                        elif stok_baru_teks.isdigit() and int(stok_baru_teks) >= 0:
                            buku_ditemukan['Stok'] = int(stok_baru_teks)
                            data_diubah = True
                            break
                        print("Masukkan angka positif atau nol.")
                        
                    #Mengubah kategori dengan menu
                    print("\n--- PILIH KATEGORI BARU ---")
                    tabel_kategori = PrettyTable()
                    tabel_kategori.field_names = ["NO", "Kategori"]
                    for i, kategori in enumerate(kategori_buku):
                    
                        tabel_kategori.add_row([i+1, kategori])

                    print(tabel_kategori)
                    
                    while True:
                        pilihan_kategori_teks = input("Pilih nomor kategori baru (1-6): ").strip()
                        if pilihan_kategori_teks != "":
                            if valid_teks(pilihan_kategori_teks):
                                pilihan_kategori = int(pilihan_kategori_teks)
                                if 1 <= pilihan_kategori <= len(kategori_buku):
                                    buku_ditemukan['Kategori'] = kategori_buku[pilihan_kategori - 1]
                                    data_diubah = True
                                    break
                        else:
                            print("Kategori tidak diubah.")
                            break
                    if data_diubah:
                        print(f"\nBuku dengan NO {id_ubah} berhasil diperbarui.")
                    else:
                        print(f"\nTidak ada perubahan data untuk buku NO {id_ubah}.")

            #DELETE ADMIN
            elif pilihan_admin == '4':
                os.system("cls || clear")
                print("\n--- HAPUS BUKU ---")

                tabel_buku = PrettyTable()
                tabel_buku.field_names = ["NO", "Judul", "Penulis", "Harga (Rp)", "Stok", "Kategori"]
                
                if not buku_sementara:
                    print("Tidak ada data buku yang tersedia.")
                else:
                    for key, value in buku_sementara.items():
                        format_harga = f"{value['Harga']:,}".replace(",", ".")
                        tabel_buku.add_row([key, value['Judul'], value['Penulis'], format_harga, value['Stok'], value['Kategori']])
                        tabel_buku.align["NO"] = "r"
                        tabel_buku.align["Judul"] = "l"
                        tabel_buku.align["Penulis"] = "l"
                        tabel_buku.align["Harga (Rp)"] = "r"
                        tabel_buku.align["Stok"] = "r"
                        tabel_buku.align["Kategori"] = "l"
                    print(tabel_buku)

                buku_dihapus = None
                indeks_hapus = -1
                
                while True:
                    id_hapus_teks = input("\nMasukkan NO buku yang akan dihapus: ").strip()
                    if not id_hapus_teks.isdigit():
                        print("Input NO tidak valid. Masukkan angka.")
                        continue
                    
                    id_hapus = int(id_hapus_teks)
                    
                    for key in buku_sementara.keys():
                        if key == id_hapus:
                            buku_dihapus = buku_sementara[key]['Judul']
                            indeks_hapus = key
                            break
                    
                    if buku_dihapus:
                        break 
                    else:
                        print(f"Buku {id_hapus} tidak ditemukan.")
                
                #CONFIRM DELETE
                if buku_dihapus:
                    konfirmasi = input(f"Anda yakin ingin menghapus buku '{buku_dihapus}' (y/n)? : ").lower()
                    if konfirmasi == 'y':
                        buku_sementara.pop(indeks_hapus)
                        print(f"\nBuku '{buku_dihapus}' berhasil dihapus.")
                    else:
                        print("Penghapusan dibatalkan.")

            #LOGOUT ADMIN
            elif pilihan_admin == '5':
                sudah_login = False
                user_saat_ini = None
                role = None
                print("Anda berhasil logout.")

            else:
                print("Pilihan tidak valid.")

        #Menu user
        elif role == 'user':
            os.system("cls || clear")
            tabel_user = PrettyTable()
            tabel_user.field_names = ["No", "Menu"]
            tabel_user.align = "l"
            tabel_user.add_row(["1", "Lihat daftar buku tersedia (Read)"])
            tabel_user.add_row(["2", "Logout"])
            print(f"\n=== MENU {role.upper()} ===")
            print(tabel_user)
            pilihan_user = input("Pilih menu Pengguna: ").strip()

            #READ USER
            if pilihan_user == '1':
                os.system("cls || clear")
                print("\n--- DAFTAR BUKU TERSEDIA ---")
                
                tabel_buku = PrettyTable()
                tabel_buku.field_names = ["NO", "Judul", "Penulis", "Harga (Rp)", "Stok", "Kategori"]
                
                ada_buku_tersedia = False
                for key, value in buku_sementara.items():
                    if value['Stok'] > 0:
                        ada_buku_tersedia = True
                        format_harga = f"{value['Harga']:,}".replace(",", ".")
                        tabel_buku.add_row([key, value['Judul'], value['Penulis'], format_harga, value['Stok'], value['Kategori']])

                if ada_buku_tersedia:
                    tabel_buku.align["Judul"] = "l"
                    tabel_buku.align["Penulis"] = "l"
                    tabel_buku.align["Harga (Rp)"] = "r"
                    tabel_buku.align["Stok"] = "r"
                    print(tabel_buku)
                else:
                    print("Maaf, buku yang Anda cari tidak tersedia")

                input("Tekan enter untuk kembali ke menu User...")

            #LOGOUT USER
            elif pilihan_user == '2':
                sudah_login = False
                user_saat_ini = None
                role = None
                print("Anda berhasil logout.")
                
            else:
                print("Pilihan tidak valid.")