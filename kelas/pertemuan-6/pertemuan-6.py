# Membuat set
# buah = {"apel", "jeruk", "mangga", "apel"}
# suka= set(["apel", "jeruk", "mangga", "apel"])
# print(buah)
# print(suka)

# angka = [1, 1, 2, 2, 3, 4, 5, 6, 7]
# unik = set(angka)
# print(unik)

# angka_ganjil = {1, 3, 5, 7, 9}
# for angka in angka_ganjil:
#     print(angka, end=" ")

# angka_ganjil = {1, 3, 5, 7, 9}
# angka_genap = {2, 4, 6, 8, 10}
# union = angka_ganjil | angka_genap
# print(union)

# angka_ganjil = {1, 3, 5, 7, 9}
# angka_genap = {2, 4, 6, 8, 10, 12, 14, 16}
# update = angka_ganjil.union(angka_genap)
# print(update)

# buah = {'mangga', 'jeruk', 'manggis', 'aprikot', 'semangka'}
# tropis = {'piasang', 'mengkudu', 'nanas', 'kelapa', 'semangka'}
# intersect = buah.intersection(tropis)
# print(intersect)

# obat = {'paracetamol', 'ibuprofen', 'amoxilin', 'antimo'}
# obat1 = {'paracetamol', 'antangin', 'amoxilin', 'antimo'}
# difference = obat1.difference(obat)
# print(difference)

# Daftar_buku = {
# "Buku1" : "Bumi Manusia",
# "Buku2" : "Laut Bercerita"
# }
# print(Daftar_buku["Buku1"]) #cara akses pertama, menggunakan key
# print(Daftar_buku) #cara akses kedua, menampilkan semua isi dictionary

# Biodata = {
# "Nama" : "Ananda Daffa Harahap",
# "NIM" : 2409106050,
# "KRS" : ["Pemrograman Web", "Struktur Data", "Basis Data"],
# "Mahasiswa_Aktif" : True,
# "Social Media" : {
#     "Instagram" : "daffahrhap"
#     }
# }
# for i, j in Biodata.items():
#     print(i)
#     print(j)
# for i in Biodata:
#     print(i, ":", Biodata[i])

# List_game = dict(GTA_5 = "Open World", Valorant = "FPS", Honkai_Star_Rail = "RPG")
# print(List_game)

# print(f"nama saya adalah {Biodata["Nama"]}")
# print(f"Instagram : {Biodata['Social Media']['Instagram']}")

# print(f"nama saya adalah {Biodata.get('Nama')}")
# print(Biodata.get("Nama"))

# print(Biodata.get("Nama"))
# print(Biodata.get("Alamat"))
# print(Biodata.get("Alamat", "Key tersebut tidak ada"))

# Nilai = {
# "Matematika": 80,
# "B. Indonesia": 90,
# "B. Inggris": 81,
# "Kimia": 78,
# "Fisika": 80
# }
# # Tanpa menggunakan items()
# for i in Nilai:
#     print(i)
# print("") # pemisah

# # Menggunakan items()
# for i, j in Nilai.items():
#     print(f"Nilai {i} anda adalah {j}")

# Film = {
# "Avenger Endgame" : "Action",
# "Sherlock Holmes" : "Mystery",
# "The Conjuring" : "Horror"
# }
# print(Film)

# Film["Zombieland"] = "Comedy" #menambah item biasa
# Film.update({"Hours" : "Thriller"}) #mengubah item dengan update
# #Setelah Ditambah
# print(Film)

# Film = {
# "Avenger Endgame" : "Action",
# "Sherlock Holmes" : "Mystery",
# "The Conjuring" : "Horror"
# }
# #Sebelum Diubah
# print(Film)
# Film["Sherlock Holmes"] = "Action"
# Film.update({"The Conjuring" : "Tragedy"})
# print(Film)

# data = {
# "Nama" : "Daffa",
# "Umur" : 19,
# "Jurusan" : "Informatika"
# }
# print(data)

# #setelah dihapus
# del data["Nama"]
# print(data)

# data = {
# "Nama" : "Daffa",
# "Umur" : 19,
# "Jurusan" : "Informatika"
# }
# #Sebelum Dihapus
# print(data)
# cache = data.pop("Nama")
# #Setelah dihapus
# print(data)
# #memanggil data yang telah dihapus pada dictionary
# print(data.get("Nama"))
# #memanggil data yang telah dihapus pada variabel cache
# print(cache)

# data = {
# "Nama" : "Daffa",
# "Umur" : 19,
# "Jurusan" : "Informatika"
# }
# #Sebelum Dihapus
# print(data)
# data.clear()
# #Setelah dihapus
# print(data)

# data = {
# "Nama" : "Daffa",
# "Umur" : 19,
# "Jurusan" : "Informatika"
# }
# print("Jumlah Data = ", len(data))

# buku = {
# "Buku1" : "Bumi Manusia",
# "Buku2" : "Laut Bercerita"
# }
# pinjam = buku.copy()
# print("Dictionary yang telah disalin : ", pinjam)

# key = "apel", "jeruk", "mangga"
# value = 1
# buah = dict.fromkeys(key, value)
# print(buah)

# Nilai = {
# "Matematika" : 80,
# "B. Indonesia" : 90,
# "B. Inggris" : 81,
# "Kimia" : 78,
# "Fisika" : 80
# }
# #menggunakan keys
# for i in Nilai.keys():
#     print(i)
# print("")
# #menggunakan value
# for i in Nilai.values():
#     print(i)

Nilai = {
"Matematika" : 80,
"B. Indonesia" : 90,
"B. Inggris" : 81
}
#sebelum Setdefault
print(Nilai)
print("")
#menggunakan setdefault
print("Nilai : ", Nilai.setdefault("Kimia", 70))
print("")
#setelah menggunakan setdefault
print(Nilai)

# Musik = {
# "The Chainsmoker" : ["All we Know", "The Paris"],
# "Alan Walker" : ["Alone", "Lily"],
# "Neffex" : ["Best of Me", "Memories"]
# }
# for i, j in Musik.items():
#     print(f"Musik milik {i} adalah : ")
#     for song in j:
#         print(song)
# print("")

# Musik = {
#     "The Chainsmoker": ["All we Know", "The Paris"],
#     "Alan Walker": ["Alone", "Lily"],
#     "Neffex": ["Best of Me",['tes','halo'], "Memories"],
#     'Paramore' : ["Misery Business", "Ain't It Fun", 
#                 ['All We Know Is Falling',['Here We Go Again', 'My Heart']],'This Is Why' ]
# }

# print(Musik['Paramore'][2][1][0])

# angka = {}
# unik = set(angka)
# print(type(unik))

# a = {1,2,3}
# b = {11,2,8}
# c = a|b
# print(c)

# mahasiswa = {
#     '2509106016' : {'Nama' : 'Syarafina Nur Amalia', 'kelas' : 'A25', 'IPK' : '4.00'},
#     '2609106055' : {'Nama' : 'Ishigami Senku', 'kelas' : 'A26', 'IPK' : '5.00'},
# }

# for i, j in mahasiswa.items():
#     print(f'\nNIM : {i}')
#     for key, value in j.items():
#         print(f'{key} : {value}')