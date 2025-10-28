#mengggunakan fungsi agar code block lebih rapi dan mudah dibaca

#def tanpa parameter
# def perkenalan():
#     print("Mata kuliah")
#     print("Kalkulus")
#     input("Tekan enter untuk melanjutkan...")
# perkenalan()

# def perkalian():
#     x = 5*5
#     print(x)
# perkalian()

# def perkenalan(nama):
#     print(f'Halo, {nama} selamat berbelanja')
# perkenalan('fina')

# def salam():
#     print("Halo, Ridho")
# def kali():
#     x = 5*5
#     print(x)
# salam()
# salam()
# salam()
# kali()
# kali()
# kali()

#def dengan parameter, yanga ada dalam kurung adalah parameter
# def luas_persegi_panjang(panjang, lebar):
#     luas = panjang * lebar
#     print("luas persegi panjang adalah ", luas)

# #Pemanggilan Fungsi luas_persegi_panjang
# luas_persegi_panjang(4, 5)

#Fungsi yang tidak mengembalikan nilai biasanya disebut dengan prosedur.
#pengembalian nilai dengan return   
# def luas_persegi(sisi):
#     luas = sisi * sisi
#     return luas
# # pemanggilan fungsi luas persegi
# print("Luas persegi :", luas_persegi(8))

# def luas_persegi(sisi):
#     luas = sisi * sisi
#     return luas
# def volume_persegi(sisi):
#     volume = luas_persegi(sisi) * sisi
#     print("Volume Persegi = ", volume)
# # pemanggilan Fungsi
# luas_persegi(4)
# volume_persegi(8)

#urutan pengaksesan variabel (scope) dikenal dengan sebutan 
# LGB (Local, Global, dan Build-in).
#Variabel Build-in adalah variabel yang sudah ada di dalam Python.

# membuat variabel global, di luar fungsi
# Nama = "Hambali"
# Mata_Kuliah = "Algoritma dan Pemrograman Dasar"

# #variabel lokal, di dalam fungsi
# def info():
#     Prodi = "Informatika"
#     Mata_Kuliah = "Logika Informatika"
#     # mengakses variabel lokal
#     print("Prodi:", Prodi)
#     print("Mata Kuliah:", Mata_Kuliah)

# # mengakses variabel global
# print("Nama:", Nama)
# print("Mata Kuliah:", Mata_Kuliah)

# # memanggil fungsi info
# info()

# def faktorial(n):
# # Basis (Base Case): Kondisi berhenti, nilai paling kecil
#     if n == 1 or n == 0:
#         return 1
# # Rekursi (Recursive Case): Fungsi memanggil dirinya sendiri
#     else:
#         return n * faktorial(n - 1)
# # Memanggil fungsi
# hasil = faktorial(7)
# print(f"Hasil dari 7! adalah: {hasil}")

# Film = []
# def show_data():
#     if len(Film) <= 0:
#         print("Belum Ada data")
#     else:
#         print("ID | Judul Film")
#         for indeks in range(len(Film)):
#             print(indeks, "|", Film[indeks])

# def insert_data():
#     Film_baru = input("Judul Film: ")
#     Film.append(Film_baru)
#     print("Film berhasil ditambahkan!")

# def edit_data():
#     show_data()
#     indeks = int(input("Inputkan ID Film: "))
#     if indeks >= len(Film) or indeks < 0:
#         print("ID salah")
#     else:
#         judul_baru = input("Judul baru: ")
#         Film[indeks] = judul_baru
#         print("Film berhasil diupdate!")

# def delete_data():
#     show_data()
#     indeks = int(input("Inputkan ID Film: "))
#     if indeks >= len(Film) or indeks < 0:
#         print("ID salah")
#     else:
#         Film.remove(Film[indeks])
#         print("Film berhasil dihapus!")

# def show_menu():
#     print("=== Data Film ===")
#     print("[1] Show Data")
#     print("[2] Insert Data")
#     print("[3] Edit Data")
#     print("[4] Delete Data")
#     print("[5] Exit")
#     menu = input("PILIH MENU> ")
#     print ("\n")

#     if menu == "1":
#         show_data()
#     elif menu == "2":
#         insert_data()
#     elif menu == "3":
#         edit_data()
#     elif menu == "4":
#         delete_data()
#     elif menu == "5":
#         exit()
#     else:
#         print ("Salah pilih!")

# while(True):
#     show_menu()

# angka = int(input('masukkan harga : '))
# print(angka)

# try:
#     angka = int(input('Masukkan Angka : '))
# except ValueError:
#     print('input yang anda masukkan bukan Integer (angka)')
# else:
#     print(angka)
# finally:
#     print('zidan')

try:
    usn = input('Username yang diinginkan : ')
    if len(usn) < 8:
        raise ValueError('Nama Minimal Memiliki 8 karakter')
    if not usn.isdigit():
        raise ValueError('Username harus ada angka')
except ValueError as e:
    print(e)
else:
    print(usn)