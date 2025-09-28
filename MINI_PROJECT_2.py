# MINI PROJECT 2
# NABILA VIVIANA ASRI
# NIM: 2509116098
rute =["jakarta", "surabaya", "bandung", "jogja"]
harga_tiket = [100000, 150000, 200000, 1250000]
list_rute ={"jakarta":100000,
            "surabaya":150000,
            "bandung":200000,
            "jogja":1250000}
owner ={"NABILA":"27"}
karyawan ={"RAFFI":"123"}
def menu_owner():
        while True:
               print("====== MENU OWNER ======")
               print("1.LIHAT RUTE & HARGA TIKET")
               print("2.TAMBAH RUTE")
               print("3.UBAH RUTE")
               print("4.HAPUS RUTE")
               print("5.LOGOUT")
            
               pilih_opsi =input("PILIH OPSI 1-5: " )
               if pilih_opsi =="1":
                print("= = = = = =  R U T E = = = = = =")
                for rute, harga in list_rute.items():
                    print(f"{rute:<20} Rp{harga}")
                print()
                
               elif pilih_opsi =="2":
                nama_menu=input("masukkan nama rute baru: ").lower()
                if nama_menu in list_rute:
                    print("RUTE SUDAH TERDAFTAR")
                else:
                    try:
                          price = int(input("masukkan harga tiket : "))
                          list_rute[nama_menu] = price                          
                          print(f"menu {nama_menu} berhasil ditambahkan.")
                    except ValueError:
                          print("harga harus berupa angka")
               elif pilih_opsi =="3":
                rute_menu=input("masukkan rute yang ingin anda rubah: ").lower()
                if rute_menu in list_rute:
                    rute_baru=input("masukkan nama rute baru: ").lower()
                    try:
                        harga_new =int(input("masukkan harga rute baru: "))                                            
                        del list_rute[rute_menu]
                        list_rute[rute_baru]=harga_new
                        print(f"Menu {rute_menu} berhasil dirubah ke{rute_baru}.")
                    except ValueError:
                          print("harga harus berupa angka")
                else:
                     print("RUTE TIDAK TERSEDIA")

               elif pilih_opsi =="4":
                hapus =input("masukkan rute yang ingin dihapus: ").lower()
                if hapus in list_rute:
                    del list_rute[hapus]
                    print(f"Rute {hapus} berhasil dihapus")

                else:
                     print("RUTE YANG INGIN ANDA HAPUS TIDAK TERSEDIA")

               elif pilih_opsi== "5":
                print("GOOD BYE OWNER")
                exit()
               else:
                   print("OPSI TIDAK ADA")

def menu_karyawan():
    masukkan =input("pilih menu: (lihat rute/pesan tiket): ")
    if masukkan =="lihat rute":
                  print("========= LIST RUTE ===========")
                  print("JAKARTA")
                  print("SURABAYA")
                  print("BANDUNG")
                  print("YOGYAKARTA")
                  print("===============================")
                  lanjut =input("apakah anda ingin melanjutkan untuk pemesanan tiket (ya/tidak)?:")
                  if lanjut=="ya":
                      masukkan = "pesan tiket"
                  else:
                    print("terimakasih")
                    return
    if masukkan =="pesan tiket":
                  a = (input("pilih tujuan anda (jakarta/surabaya/bandung/jogja)?:"))
                  if a == "jakarta":
                    nama =input("masukkan nama anda:")
                    print(rute[0], "=Rp",harga_tiket[0])
                    harga_pilihan = harga_tiket[0]
                    tujuan = rute[0]
                  elif a == "surabaya":
                        nama =input("masukkan nama anda:")
                        print(rute[1], "=Rp", harga_tiket[1])
                        harga_pilihan = harga_tiket[1]
                        tujuan = rute[1]
                  elif a == "bandung":
                        nama =input("masukkan nama anda:")
                        print(rute[2], "=Rp", harga_tiket[2])
                        harga_pilihan = harga_tiket[2]
                        tujuan =rute[2]
                  elif a == "jogja":
                        nama =input("masukkan nama anda:")
                        print(rute[3], "=Rp", harga_tiket[3])
                        harga_pilihan = harga_tiket[3]
                        tujuan =rute[3]
                  else:
                       print("rute tidak tersedia")
                       return
                  try:
                            berapa_tiket = int(input("berapa tiket?: "))
                            total = harga_pilihan * berapa_tiket
                            print("TOTAL TIKET YANG ANDA PESAN:","Rp",total)
                            detail=input("apakah anda ingin melihat detail tiket anda? (ya/tidak):")
                            if detail == "ya":
                                print("======= DETAIL TIKET =======")
                                print("NAMA:",nama)
                                print("TUJUAN :",tujuan)
                                print("JUMLAH TIKET:",berapa_tiket)
                                print("HARGA TIKET:Rp.",harga_pilihan)
                                print("TOTAL PEMBAYARAN:Rp.",total)
                                print("===========================")
                                print("TERIMAKASIH SELAMAT MENIKMATI PERJALANAN")
                            elif detail == "tidak":
                                print("TRANSAKSI SELESAI HATI HATI DI JALAN")
                            else :                    
                                 print("TERIMAKASIH SELAMAT MENIKMATI PERJALANAN")
                  except ValueError:
                            print("jumlah tiket harus berupa angka")
                            exit()

def login():
     print("======= LOGIN =======")
     print("1.OWNER")
     print("2.KARYAWAN")
     pilih =input("LOGIN SEBAGAI (1/2):")
     if pilih =="1":
         username =input("masukkan username anda: ")
         password =input("masukkan password anda: ")
         if username in owner and owner [username] == password:
             print("WELCOME OWNER")
             menu_owner()
         else:
              print("USERNAME & PASSWORD OWNER SALAH")

     elif pilih =="2":
         username =input("masukkan username anda: ")
         password =input("masukkan password anda: ")
         if username in karyawan and karyawan [username] == password:
             print("WELCOME")
             menu_karyawan()
     else:
          print("USERNAME & PASSWORD ANDA SALAH")
login()