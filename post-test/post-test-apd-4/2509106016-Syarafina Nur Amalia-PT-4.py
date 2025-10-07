import pwinput
from prettytable import PrettyTable
from colorama import Fore, Style
import os

os.system("cls")
nama = 'Fina'
sandi = '016'

while True:
    member = False
    totalAwal = 0
    belanjaSementara = ""

    print('='*55)
    print('|         Selamat Datang di Dealer Senku Jaya         |')
    print('='*55)
    
    member = str(input('\nApakah kamu adalah member? (yes/no) : ')).lower()
    if member == 'yes':
        percobaan = 3
        while percobaan > 0:
            loginNama = str(input('Masukkan nama Anda : '))
            loginSandi = pwinput.pwinput('Masukkan password Anda : ')
            if loginNama == nama and loginSandi == sandi:
                member = True
                print(f'\nSelamat, ', (nama) ,' berhasil login')
                break
            else:
                percobaan -= 1
                if percobaan > 0:
                    print(f'Login gagal, silakan coba lagi. Sisa percobaan {percobaan}')
                else:
                    print('Anda akan dialihkan sebagai non-member')
    elif member != 'no':
        print('Input tidak valid. Anda merupakan non-member')
            
    checkout = False
    while not checkout:
        if totalAwal > 0:
            print(f'Total sementara : Rp{totalAwal}')     
            
        tabel_menu = PrettyTable()
        tabel_menu.field_names = [Fore.GREEN + 'No', 'Nama Produk', 'Harga']
        tabel_menu.add_row(['1', 'Rolls Royce Phantom', 'Rp23.500.000'])
        tabel_menu.add_row(['2', 'Land Cruiser', 'Rp29.450.000'])
        tabel_menu.add_row(['3', 'Jeep Wrangler Rubicon', 'Rp32.890.000'])
        tabel_menu.add_row(['4', 'Ford Ranger', 'Rp37.770.000'])
        tabel_menu.add_row(['5', 'Mercedes Maybach S-Class', 'Rp40.650.000'])
        tabel_menu.add_row(['---', '-'*20, '-'*10])
        tabel_menu.add_row([f'{Fore.BLUE}6{Style.RESET_ALL}', f'{Fore.BLUE}Checkout{Style.RESET_ALL}', ""]) 
        print('\nSilakan pilih mobil yang ingin Anda beli')
        print(tabel_menu)
        pesanan = int(input('Pilih mobil idaman Anda (1-6) : '))

        if pesanan == 6:
            if totalAwal > 0:
                checkout = True
            else:
                print('Keranjang kosong. Pilih unit terlebih dahulu.')
        elif 1 <= pesanan <= 5: 
            mobil = ""
            harga = 0
            if pesanan == 1:
                mobil = 'Rolls Royce Phantom'
                harga = 23500000
                harga_str = 'Rp23.500.000'
            elif pesanan == 2:
                mobil = 'Land Cruiser'
                harga = 29450000
                harga_str = 'Rp29.450.000'
            elif pesanan == 3:
                mobil = 'Jeep Wrangler Rubicon'
                harga = 32890000
                harga_str = 'Rp32.890.000'
            elif pesanan == 4:
                mobil = 'Ford Ranger'
                harga = 37770000
                harga_str = '37.770.000'
            elif pesanan == 5:
                mobil = 'Mercedes Maybach S-Class'
                harga = 40650000
                harga_str = '40.650.000'

            totalAwal += harga
            if belanjaSementara == "":
                belanjaSementara = (f'{mobil}     | {harga_str}')
            else:
                belanjaSementara += (f'\n{mobil}    | {harga_str}')
                
            print(f'{mobil} telah masuk keranjang ✅')
        else:
                print('Perhatikan cara pengisian form')

    if member:
        diskon = int(totalAwal * 0.15)
        totalAkhir = totalAwal - diskon

        print('\nRincian pembelian Anda sebagai berikut')
        print('='*50)
        print(belanjaSementara)
        print('-'*50)

    if member:
        print(f'Total harga asli           : Rp{totalAwal}')
        print(f'Diskon member (15%)        : Rp{diskon}')
        print('='*50)
        print(f'Total akhir                : Rp{totalAkhir}')
    else:
            print(f'Total akhir            : Rp{totalAkhir}')
    
    while True:
        belanjaLagi = str(input('\nApakah ingin berbelanja lagi? (yes/no): ')).lower()
        if belanjaLagi == 'no':
            print('\nTerima kasih telah berbelanja di sini')
            exit()
        elif belanjaLagi == 'yes':
            print('\n' + '='*40)
            break
        else:
            print('Input tidak valid, gunakan (yes/no)')