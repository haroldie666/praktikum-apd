data = {
"Nama" : "Daffa",
"Umur" : 19,
"Jurusan" : "Informatika"
}
#Sebelum Dihapus
print(data)
cache = data.pop("Nama")
#Setelah dihapus
print(data)
#memanggil data yang telah dihapus pada dictionary
print(data.get("Nama"))
#memanggil data yang telah dihapus pada variabel cache
print(cache)