nilai = 50

status = 'lulus' if nilai >= 60 else 'tidak lulus'
print(status)

if nilai > 75:
    print('Nilai A')
elif nilai > 65:
    print('Nilai B')
else:
    print('Nilai C')

suhu = 35
if suhu > 35:
    print('panas')
if suhu > 30:
    print('sauna')
elif suhu > 20:
    print('normal')
else:
    print('dingin')

umur = int(input("Masukkan umur Anda: "))
if umur < 13:
    kategori = "Anak-anak"
elif umur < 18:
    kategori = "Remaja"
elif umur < 60:
    kategori = "Dewasa"
else:
    kategori = "Lansia"
print("Umur:", umur, "Kategori:", kategori)

