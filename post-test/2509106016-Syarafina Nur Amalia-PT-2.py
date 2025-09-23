'''Hasil Cek Berat Badan'''

from prettytable import PrettyTable
from colorama import Fore, Style

t = PrettyTable()
t.field_names = ['keterangan', 'Hasil']

nama = input('Masukkan nama Anda = ')
tinggiBadan = float(input('Masukkan tinggi badan Anda = '))
beratBadan = float(input('Masukkan berat badan Anda = '))

beratIdeal = (tinggiBadan - 100)
isKelebihan = beratBadan > beratIdeal

statusTubuh = ['Berat badan ideal', 'Kelebihan berat badan, perbanyak olahraga']
status = statusTubuh[int(isKelebihan)]

print(Fore.CYAN + '\n\n','='*8,'Status Kesehatan Anda','='*8)
t.add_row(['Nama', Fore.BLUE + nama])
t.add_row(['Tinggi Badan (cm)', tinggiBadan])
t.add_row(['Berat Badan (kg)', beratBadan])
t.add_row(['Status', status])
print(t)