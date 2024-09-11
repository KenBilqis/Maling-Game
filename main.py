import random

welcome_message = "Welcome To Maling Games!"
maling_position = random.randint(1, 5)

print("****************************")
print(f"* {welcome_message} *")
print("****************************")

nama_user = input("Silahkan masukkan nama kamu: ")

bentuk_tong = "|_|"
tong = [bentuk_tong] * 5

tong_maling = tong.copy()
tong_maling[maling_position - 1] = "|-_-|"

tong = ' '.join(tong)
tong_maling = ' '.join(tong_maling)

print(f'''
Halo {nama_user}!
Coba lihat tong di bawah ini
{tong}
''')

pilihan_user = int(input("Menurut kamu di nomor berapa Maling bersembunyi? [1 / 2 / 3 / 4 / 5]: "))

konfirmasi_pilihan = input(f"apakah kamu yakin jawabannya adalah {pilihan_user}[y/n]? ")

if konfirmasi_pilihan == "y":
    if pilihan_user == maling_position:
        print(f'''
Selamat {nama_user} kamu berhasil menangkap maling tersebut!🙌
{tong_maling}
dia bersembunyi di tong nomor {maling_position}
''')
    else:
        print(f'''
Yahhh pilihan kamu salah sehingga maling berhasil kabur😖
{tong_maling} 
ternyata dia bersembunyi di tong nomor {maling_position} sedangkan kamu memilih tong nomor {pilihan_user}
''')
elif konfirmasi_pilihan == "n":
    print("GA USAH MAIN BLOK")
    exit()
else:
    print("PILIH YG BENER COG!")
    
