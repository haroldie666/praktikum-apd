import pwinput

nama = 'Syarafina Nur Amalia'
sandi = '016'

print('='*55)
print('|         Selamat Datang di Dealer Senku Jaya         |')
print('='*55)
member = str(input('\nApakah kamu adalah member? (yes/no) : ')).lower()
if member == 'yes':
    loginNama = str(input('Masukkan nama Anda : '))
    loginSandi = pwinput.pwinput('Masukkan password Anda : ')
    if loginNama == nama and loginSandi == sandi:
        print(f'\nSelamat, ', (nama) ,' berhasil login')
        print('\nSilakan pilih mobil yang ingin Anda beli')
        print('='*45)
        print(f'|1. Rolls Royce Phantom       Rp23.500.000  |')
        print(f'|2. Land Cruiser              Rp29.450.000  |')
        print(f'|3. Jeep Wrangler Rubicon     Rp32.890.000  |')
        print(f'|4. Ford Ranger               Rp37.770.000  |')
        print(f'|5. Mercedes Maybach S-Class  Rp40.650.000  |')
        print('='*45)
        pesanan = int(input('Pilih mobil idaman Anda (1-5) : '))

        if pesanan == 1:
            mobil = 'Rolls Royce Phantom'
            harga = 23500000
        elif pesanan == 2:
            mobil = 'Land Cruiser'
            harga = 29450000
        elif pesanan == 3:
            mobil = 'Jeep Wrangler Rubicon'
            harga = 32890000
        elif pesanan == 4:
            mobil = 'Ford Ranger'
            harga = 37770000
        elif pesanan == 5:
            mobil = 'Mercedes Maybach S-Class'
            harga = 40650000
        else:
            print('Perhatikan cara pengisian pada form')

        diskon = harga * 0.15
        bayar = harga - diskon

        print('='*45)
        print('\nRincian pembelian Anda sebagai berikut')
        print('-'*50)
        print(f'Produk yang Anda beli   : {mobil}')
        print(f'Harga mobil             : {harga}')
        print(f'Diskon member           : {diskon}')
        print(f'Jumlah bayar            : {bayar}')
        print(f'Silakan bayar dikasir')
        print('-'*50)
    else:
        print('Login gagal, silakan coba lagi')

elif member == 'no':
    print('\nSilakan pilih mobil yang ingin Anda beli')
    print('='*45)
    print(f'|1. Rolls Royce Phantom       Rp23.500.000  |')
    print(f'|2. Land Cruiser              Rp29.450.000  |')
    print(f'|3. Jeep Wrangler Rubicon     Rp32.890.000  |')
    print(f'|4. Ford Ranger               Rp37.770.000  |')
    print(f'|5. Mercedes Maybach S-Class  Rp40.650.000  |')
    print('='*45)
    pesanan = int(input('Pilih mobil idaman Anda (1-5) : '))

    if pesanan == 1:
        mobil = 'Rolls Royce Phantom'
        harga = 23500000
    elif pesanan == 2:
        mobil = 'Land Cruiser'
        harga = 29450000
    elif pesanan == 3:
        mobil = 'Jeep Wrangler Rubicon'
        harga = 32890000
    elif pesanan == 4:
        mobil = 'Ford Ranger'
        harga = 37770000
    elif pesanan == 5:
        mobil = 'Mercedes Maybach S-Class'
        harga = 40650000
    else:
        print('Perhatikan cara pengisian pada form')
    
    bayar = harga

    print('='*45)
    print('\nRincian pembelian Anda sebagai berikut')
    print('-'*50)
    print(f'Mobil yang Anda beli : {mobil}')
    print(f'Jumlah bayar         : {bayar}')
    print(f'Silakan bayar dikasir')
    print('-'*50)
else:
    print('Maaf, jawaban Anda tidak dapat diproses')

print('\nTerima kasih telah berkunjung')