from prettytable import PrettyTable
import os
from data import users, buku_sementara, kategori_buku
from colorama import init, Fore, Style

role = None
no_buku_selanjutnya = max(buku_sementara.keys()) + 1 if buku_sementara else 1

def angka_positif(x):
    try:
        angka = int(x)
        return angka > 0
    except ValueError:
        return False

def angka_positif_stok(x):
    try:
        angka = int(x)
        return angka >= 0
    except ValueError:
        return False

def teks_tidak_kosong(x):
    return len(x.strip()) > 0

def kategori_buku_positif(x):
    if not angka_positif(x):
        return False
    pilihan = int(x)
    return 1 <= pilihan <= len(kategori_buku)

def konfirmasi_delete_buku(x):
    return x.lower() in ('y', 'n')

#PROSEDUR
def clear():
    os.system('cls || clear')

def daftar_buku(data_buku):
    tabel_buku = PrettyTable()
    tabel_buku.field_names = [Fore.CYAN + "NO", "Judul", "Penulis", "Harga (Rp)", "Stok", "Kategori" + Style.RESET_ALL]

    if not data_buku:
        print("Tidak ada data buku yang tersedia.")
        return

    if role == 'user':
        buku_tampil = {key: value for key, value in data_buku.items() if value['Stok'] > 0}
    else:
        buku_tampil = data_buku
    
    if not buku_tampil and role == 'user':
        print("Maaf, buku yang Anda cari tidak tersedia.")
        return

    for key, value in buku_tampil.items():
        format_harga = f"{value['Harga']:,}".replace(",", ".")
        tabel_buku.add_row([key, value['Judul'], value['Penulis'], format_harga, value['Stok'], value['Kategori']])

    tabel_buku.align["NO"] = "r"
    tabel_buku.align["Judul"] = "l"
    tabel_buku.align["Penulis"] = "l"
    tabel_buku.align["Harga (Rp)"] = "r"
    tabel_buku.align["Stok"] = "r"
    tabel_buku.align["Kategori"] = "l"

    print(tabel_buku)
    print(Fore.GREEN + "\nTekan enter untuk melanjutkan..." + Style.RESET_ALL)
    input()

#FUNGSI TANPA PARAMETER
def menu_utama_admin():
    tabel_menu = PrettyTable()
    tabel_menu.field_names = [Fore.YELLOW + "No", "Menu" + Style.RESET_ALL]
    tabel_menu.align = "l"
    
    tabel_menu.add_row(["1", "Login"])
    tabel_menu.add_row(["2", "Register"])
    tabel_menu.add_row(["3", "Logout"])
    
    print("\n=== SELAMAT DATANG DI TOKO BUKU SENKUMEDIA ===")
    print(tabel_menu)
    
    return input("Silakan pilih menu yang tersedia: ").strip()

def menu_admin_login():
    clear()
    tabel_admin = PrettyTable()
    tabel_admin.field_names = [Fore.BLUE + "NO", "Menu" + Style.RESET_ALL]
    tabel_admin.align = "l"
    tabel_admin.add_row(["1", "Lihat data buku (Read)"])
    tabel_admin.add_row(["2", "Tambah buku baru (Create)"])
    tabel_admin.add_row(["3", "Update data buku (Update)"])
    tabel_admin.add_row(["4", "Hapus data buku (Delete)"])
    tabel_admin.add_row(["5", "Logout"])
    print(f"\n=== MENU admin ===")
    print(tabel_admin)
    return input("Pilih menu admin: ")

#FUNGSI DENGAN PARAMETER
def input_valid(tampilan, validasi, pesan = "Input tidak valid, coba lagi dengan teliti."):
    input_nilai = input(tampilan).strip()
    if validasi(input_nilai):
        return input_nilai
    else:
        print(pesan) 
        return input_valid(tampilan, validasi, pesan)

def login(username, password):
    for key, value in users.items():
        if key == username and value['password'] == password:
            return (True, key, value['role'])
    return (False, None, None)

def tambah_buku():
    global no_buku_selanjutnya
    clear()
    print("\n--- TAMBAH BUKU BARU ---")
    
    judul_baru = input_valid("Judul: ", teks_tidak_kosong, "Judul tidak boleh kosong.")
    penulis_baru = input_valid("Penulis: ", teks_tidak_kosong, "Penulis tidak boleh kosong.")
    
    harga_teks = input_valid("Harga (contoh: 150000): ", angka_positif, "Input harga tidak valid. Isi dengan angka positif.")
    harga_baru = int(harga_teks)
    
    stok_teks = input_valid("Stok: ", angka_positif_stok, "Input stok tidak valid. Isi dengan angka positif atau nol.")
    stok_baru = int(stok_teks)
    
    #Kategori
    print("\n--- PILIH KATEGORI BUKU ---")
    tabel_kategori = PrettyTable()
    tabel_kategori.field_names = [Fore.RED+ "NO", "Kategori" + Style.RESET_ALL]
    for i, kategori in enumerate(kategori_buku):
        tabel_kategori.add_row([i+1, kategori])
    print(tabel_kategori)
    
    #Input kategori dengan nilai positif
    pilihan_kategori_teks = input_valid("Pilih kategori (nomor): ", kategori_buku_positif, "Pilihan kategori tidak valid.")
    pilihan_kategori = int(pilihan_kategori_teks)
    kategori_baru = kategori_buku[pilihan_kategori - 1]
    
    buku_sementara[no_buku_selanjutnya] = {
        'Judul': judul_baru,
        'Penulis': penulis_baru,
        'Harga': harga_baru,
        'Stok': stok_baru,
        'Kategori': kategori_baru
    }
    print(f"\nBuku '{judul_baru}' berhasil ditambahkan dengan NO {no_buku_selanjutnya}.")
    no_buku_selanjutnya += 1 
    input(Fore.GREEN + "Tekan enter untuk kembali..." + Style.RESET_ALL)

def update_buku():
    clear()
    print("\n--- UPDATE DATA BUKU ---")
    daftar_buku(buku_sementara)
    
    if not buku_sementara: 
        return

    buku_ditemukan = None
    while buku_ditemukan is None:
        no_update_buku = input_valid("\nMasukkan NO buku yang akan diubah: ", angka_positif, "Input NO tidak valid. Masukkan angka positif.")
        no_update = int(no_update_buku)
        
        try:
            buku_ditemukan = buku_sementara[no_update]
        except KeyError:
            print(f"Buku dengan NO {no_update} tidak ditemukan.")
            
    print("\n(Kosongkan jika tidak ada data yang ingin diubah)") 
    data_diubah = False

    #Update judul
    isi_judul_baru = input(f"Judul baru ({buku_ditemukan['Judul']}): ").strip()
    if teks_tidak_kosong(isi_judul_baru):
        buku_ditemukan['Judul'] = isi_judul_baru
        data_diubah = True
    
    #Update penulis
    isi_penulis_baru = input(f"Penulis baru ({buku_ditemukan['Penulis']}): ").strip()
    if teks_tidak_kosong(isi_penulis_baru):
        buku_ditemukan['Penulis'] = isi_penulis_baru
        data_diubah = True

    #Update harga
    while True:
        harga_lama = f"{buku_ditemukan['Harga']:,}".replace(",", ".") 
        harga_baru_teks = input(f"Harga baru ({harga_lama}): ").strip()
        if harga_baru_teks == "": 
            break 
        if angka_positif(harga_baru_teks):
            buku_ditemukan['Harga'] = int(harga_baru_teks)
            data_diubah = True
            break
        print("Masukkan angka positif.")

    #Update stok
    while True:
        stok_baru_teks = input(f"Stok baru ({buku_ditemukan['Stok']}): ").strip()
        if stok_baru_teks == "": 
            break 
        if angka_positif_stok(stok_baru_teks):
            buku_ditemukan['Stok'] = int(stok_baru_teks)
            data_diubah = True
            break
        print("Masukkan angka positif.")

    #Update kategori
    print("\n--- PILIH KATEGORI BARU ---")
    tabel_kategori = PrettyTable()
    tabel_kategori.field_names = [Fore.YELLOW + "NO", "Kategori" + Style.RESET_ALL]
    for i, kategori in enumerate(kategori_buku):
        tabel_kategori.add_row([i+1, kategori])
    print(tabel_kategori)
    
    pilihan_kategori_teks = input(f"Pilih nomor kategori baru ({buku_ditemukan['Kategori']}): ").strip()
    
    if pilihan_kategori_teks != "":
        if kategori_buku_positif(pilihan_kategori_teks):
            pilihan_kategori = int(pilihan_kategori_teks)
            buku_ditemukan['Kategori'] = kategori_buku[pilihan_kategori - 1]
            data_diubah = True
        else:
            print("Pilihan kategori tidak valid, kategori tidak diubah.")

    if data_diubah:
        print(f"{Fore.GREEN}\nBuku dengan NO {no_update} berhasil diperbarui.{Style.RESET_ALL}")
    else:
        print(f"\nTidak ada perubahan data untuk buku NO {no_update}.")
    input(Fore.GREEN + "Tekan enter untuk kembali..." + Style.RESET_ALL )

def hapus_buku():
    clear()
    print("\n--- HAPUS BUKU ---")
    daftar_buku(buku_sementara)
    
    if not buku_sementara: 
        return

    buku_dihapus = None
    indeks_hapus = -1
    
    while buku_dihapus is None:
        nomor_hapus_teks = input_valid("\nMasukkan NO buku yang akan dihapus: ", angka_positif, "Input NO tidak valid. Masukkan angka positif.")
        nomor_buku_dihapus = int(nomor_hapus_teks)
        
        try:
            buku_dihapus = buku_sementara[nomor_buku_dihapus]['Judul']
            indeks_hapus = nomor_buku_dihapus
        except KeyError:
            print(f"Buku {nomor_buku_dihapus} tidak ditemukan.")
            
    #konfirmasi buku dihapus
    konfirmasi = input_valid(f"Apakah yakin ingin menghapus buku '{buku_dihapus}' (y/n)? : ", konfirmasi_delete_buku, "Konfirmasi hanya 'y' atau 'n'.")
    
    if konfirmasi.lower() == 'y':
        try:
            buku_sementara.pop(indeks_hapus)
            print(f"\nBuku '{buku_dihapus}' berhasil dihapus.")
        except KeyError:
            print("Buku tidak ditemukan.")
    else:
        print("Penghapusan dibatalkan.")
    input(Fore.GREEN + "Tekan enter untuk kembali..." + Style.RESET_ALL)

def register():
    global users
    clear()
    print("\n--- REGISTER PENGGUNA BARU ---")
    
    while True:
        pengguna_baru = input("Nama pengguna baru: ").strip()
        if not teks_tidak_kosong(pengguna_baru):
            print("Nama pengguna tidak boleh kosong.")
        elif pengguna_baru in users:
            print("Nama pengguna sudah terdaftar. Gunakan nama lain yang unik.")
        else:
            break

    password_baru = input_valid("Password baru: ", teks_tidak_kosong, "Password tidak boleh kosong. Buatlah password yang kuat.")
    
    users[pengguna_baru] = {'password': password_baru, 'role': 'user'}
    print(f"{Fore.GREEN}Registrasi berhasil! Akun dengan nama '{pengguna_baru}' telah dibuat.{Style.RESET_ALL}")
    input(Fore.GREEN + "Tekan enter untuk kembali..." + Style.RESET_ALL)