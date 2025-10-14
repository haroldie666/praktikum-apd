from prettytable import PrettyTable
from data import users, buku_sementara
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
            for pengguna in users:
                if pengguna[0] == input_nama_pengguna and pengguna[1] == input_kata_sandi:
                    sudah_login = True
                    user_saat_ini = pengguna[0]
                    role = pengguna[2]
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
                    if pengguna[0] == nama_pengguna_baru:
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
            
            users.append([nama_pengguna_baru, kata_sandi_baru, 'user'])
            print(f"Registrasi berhasil! Akun dengan nama '{nama_pengguna_baru}' telah dibuat.")

        elif pilihan_menu_utama == '3':
            print("\nTerima kasih telah mampir di sini. See you next time.")
            program_berjalan = False
        
        else:
            print("Pilihan tidak valid. Silakan pilih angkanya saja.")

        #Menu setelah login
        #ADMIN
    elif sudah_login:
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
                
                for buku in buku_sementara:
                    format_harga = f"{buku[3]:,}".replace(",", ".")
                    tabel_buku.add_row([buku[0], buku[1], buku[2], format_harga, buku[4], buku[5]])

                tabel_buku.align["Judul"] = "l"
                tabel_buku.align["Penulis"] = "l"
                tabel_buku.align["Harga (Rp)"] = "r"
                tabel_buku.align["Stok"] = "r"
                print(tabel_buku)

            #Create admin
            elif pilihan_admin == '2':
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
                while True:
                    kategori_baru = input("Kategori: ").strip()
                    if valid_teks(kategori_baru): 
                        break
                    print("Kategori tidak boleh kosong.")

                #Memperbarui data buku
                buku_sementara.append([no_buku_selanjutnya, judul_baru, penulis_baru, harga_baru, stok_baru, kategori_baru])
                print(f"\nBuku '{judul_baru}' berhasil ditambahkan dengan NO {no_buku_selanjutnya}.")
                no_buku_selanjutnya += 1 

            #Update admin
            elif pilihan_admin == '3':
                print("\n--- UPDATE DATA BUKU ---")
                print("NO buku yang tersedia:", [buku[0] for buku in buku_sementara])
                
                #Cari NO buku yang akan diubah
                buku_ditemukan = None
                while True:
                    id_ubah_teks = input("Masukkan NO buku yang akan diubah: ").strip()
                    if not id_ubah_teks.isdigit():
                        print("Input NO tidak valid. Masukkan angka.")
                        continue
                    
                    id_ubah = int(id_ubah_teks)
                    
                    for buku in buku_sementara:
                        if buku[0] == id_ubah:
                            buku_ditemukan = buku
                            break
                    
                    if buku_ditemukan:
                        break 
                    else:
                        print(f"Buku dengan NO {id_ubah} tidak ditemukan.")
                
                #Update buku
                if buku_ditemukan:
                    print(f"\nData saat ini: Judul='{buku_ditemukan[1]}', Penulis='{buku_ditemukan[2]}', Harga='{buku_ditemukan[3]:,}', Stok='{buku_ditemukan[4]}', Kategori='{buku_ditemukan[5]}'")

                    #Ubah judul
                    judul_baru_input = input(f"Judul baru ({buku_ditemukan[1]}): ").strip()
                    if valid_teks(judul_baru_input):
                        buku_ditemukan[1] = judul_baru_input

                    #Ubah penulis
                    penulis_baru_input = input(f"Penulis baru ({buku_ditemukan[2]}): ").strip()
                    if valid_teks(penulis_baru_input):
                        buku_ditemukan[2] = penulis_baru_input

                    #Ubah harga
                    while True:
                        harga_baru_teks = input(f"Harga baru ({buku_ditemukan[3]}): ").strip()
                        if harga_baru_teks == "": 
                            break 
                        elif valid_angka_positif(harga_baru_teks):
                            buku_ditemukan[3] = int(harga_baru_teks)
                            break
                        print("Input harga tidak valid. Isi data dengan benar.")

                    #Ubah stok
                    while True:
                        stok_baru_teks = input(f"Stok baru ({buku_ditemukan[4]}): ").strip()
                        if stok_baru_teks == "":
                            break 
                        elif stok_baru_teks.isdigit() and int(stok_baru_teks) >= 0:
                            buku_ditemukan[4] = int(stok_baru_teks)
                            break
                        print("Input stok tidak valid. Isi data dengan benar.")
                        
                    #Ubah kategori
                    kategori_baru_input = input(f"Kategori baru ({buku_ditemukan[5]}): ").strip()
                    if valid_teks(kategori_baru_input):
                        buku_ditemukan[5] = kategori_baru_input

                    print(f"\nBuku dengan NO {id_ubah} berhasil diperbarui.")

            #DELETE ADMIN
            elif pilihan_admin == '4':
                print("\n--- HAPUS BUKU ---")
                print("NO buku yang tersedia:", [buku[0] for buku in buku_sementara])
                
                buku_dihapus = None
                indeks_hapus = -1
                while True:
                    id_hapus_teks = input("Masukkan NO buku yang akan dihapus: ").strip()
                    if not id_hapus_teks.isdigit():
                        print("Input NO tidak valid. Masukkan angka.")
                        continue
                    
                    id_hapus = int(id_hapus_teks)
                    
                    for i in range(len(buku_sementara)):
                        if buku_sementara[i][0] == id_hapus:
                            buku_dihapus = buku_sementara[i]
                            indeks_hapus = i
                            break
                    
                    if buku_dihapus:
                        break 
                    else:
                        print(f"Buku {id_hapus} tidak ditemukan.")
                
                #CONFIRM DELETE
                if buku_dihapus:
                    konfirmasi = input(f"Anda yakin ingin menghapus buku '{buku_dihapus[1]}' (y/n)? : ").lower()
                    if konfirmasi == 'y':
                        buku_sementara.pop(indeks_hapus)
                        print(f"\nBuku '{buku_dihapus[1]}' berhasil dihapus.")
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
                print("\n--- DAFTAR BUKU TERSEDIA ---")
                
                tabel_buku = PrettyTable()
                tabel_buku.field_names = ["NO", "Judul", "Penulis", "Harga (Rp)", "Stok", "Kategori"]
                
                ada_buku_tersedia = False
                for buku in buku_sementara:
                    if buku[4] > 0:
                        ada_buku_tersedia = True
                        format_harga = f"{buku[3]:,}".replace(",", ".")
                        tabel_buku.add_row([buku[0], buku[1], buku[2], format_harga, buku[4], buku[5]])
                
                if ada_buku_tersedia:
                    tabel_buku.align["Judul"] = "l"
                    tabel_buku.align["Penulis"] = "l"
                    tabel_buku.align["Harga (Rp)"] = "l"
                    tabel_buku.align["Stok"] = "l"
                    print(tabel_buku)
                else:
                    print("Maaf, buku yang Anda cari tidak tersedia")

            #LOGOUT USER
            elif pilihan_user == '2':
                sudah_login = False
                user_saat_ini = None
                role = None
                print("Anda berhasil logout.")
                
            else:
                print("Pilihan tidak valid.")