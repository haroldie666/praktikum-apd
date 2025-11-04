from prettytable import PrettyTable
from alur import *
from data import *
from pwinput import pwinput
from colorama import init, Fore, Style

#Main program
def main():
    init(autoreset=True)
    sudah_login = False
    user_saat_ini = None
    program_berjalan = True


    clear()
    while program_berjalan:

        if not sudah_login:
            menu_utama = menu_utama_admin()
            
            if menu_utama == '1':
                print("\n--- LOGIN ---")
                input_nama_pengguna = input("Nama pengguna: ").strip()
                input_password = pwinput("Password: ").strip()
                
                login_berhasil, user_id, user_role = login(input_nama_pengguna, input_password)
                
                if login_berhasil:
                    sudah_login = True
                    user_saat_ini = user_id
                    role = user_role
                    print(f"{Fore.GREEN}\nSelamat datang, {user_saat_ini}{Style.RESET_ALL}")
                else:
                    print(Fore.RED + "Nama pengguna atau password salah. Silakan coba lagi." + Style.RESET_ALL)
                    
            elif menu_utama == '2':
                register()
                
            elif menu_utama == '3': 
                print(f"{Fore.BLUE}\nTerima kasih telah mampir di sini. See you next time.{Style.RESET_ALL}")
                program_berjalan = False
                
            else:
                print("Pilihan tidak valid. Silakan pilih angkanya saja (1, 2, atau 3).")
        
        #Menu setelah login admin atau user
        elif sudah_login:
            if role == 'admin':
                pilihan_admin = menu_admin_login()
                
                if pilihan_admin == '1': #Read admin
                    print("\n--- DAFTAR BUKU SEKARANG ---")
                    daftar_buku(buku_sementara)
                elif pilihan_admin == '2': #Create admin
                    tambah_buku()
                elif pilihan_admin == '3': #Update admin
                    update_buku()
                elif pilihan_admin == '4': #Delete admin
                    hapus_buku()
                elif pilihan_admin == '5': #Logout admin
                    sudah_login = False
                    user_saat_ini = None
                    role = None
                    print(Fore.MAGENTA + "Anda berhasil logout." + Style.RESET_ALL)
                else:
                    print("Pilihan tidak valid.")
            
            elif role == 'user':
                clear()
                tabel_user = PrettyTable()
                tabel_user.field_names = [Fore.YELLOW + "No", "Menu" + Style.RESET_ALL]
                tabel_user.align = "l"
                tabel_user.add_row([Fore.GREEN + "1", "Lihat daftar buku tersedia (Read)" + Style.RESET_ALL])
                tabel_user.add_row([Fore.GREEN + "2", "Logout" + Style.RESET_ALL])
                print(f"\n=== MENU USER ===")
                print(tabel_user)
                pilihan_user = input("Pilih menu (nomor): ").strip()

                if pilihan_user == '1': # Read User
                    print("\n--- DAFTAR BUKU TERSEDIA ---")
                    daftar_buku(buku_sementara)
                elif pilihan_user == '2': # Logout User
                    sudah_login = False
                    user_saat_ini = None
                    role = None
                    print(Fore.MAGENTA + "Anda berhasil logout." + Style.RESET_ALL)
                else:
                    print("Pilihan tidak valid.")

if __name__ == "__main__":
    main()