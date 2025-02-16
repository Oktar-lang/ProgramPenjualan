from tabulate import tabulate
list_item = [
    {"kode": "s001", "nama": "Chitato BBQ", "kategori": "Snack", "stok": 50, "harga": 18000},
    {"kode": "d001", "nama": "Pocari Sweat", "kategori": "Minuman", "stok": 100, "harga": 10000},
    {"kode": "c001", "nama": "Serum Wajah", "kategori": "Skincare", "stok": 30, "harga": 120000},
    {"kode": "s002", "nama": "Taro Seaweed", "kategori": "Snack", "stok": 20, "harga": 15000},
    {"kode": "d002", "nama": "Teh Pucuk Harum", "kategori": "Minuman", "stok": 40, "harga": 6000},
    {"kode": "c002", "nama": "Toner Wajah", "kategori": "Skincare", "stok": 55, "harga": 75000},
    {"kode": "d003", "nama": "Ultra Milk Coklat", "kategori": "Minuman", "stok": 35, "harga": 9000},
    {"kode": "s003", "nama": "SilverQueen Almond", "kategori": "Snack", "stok": 25, "harga": 27000},
    {"kode": "c003", "nama": "Moisturizer", "kategori": "Skincare", "stok": 15, "harga": 95000},
    {"kode": "s004", "nama": "Good Time Cookies", "kategori": "Snack", "stok": 10, "harga": 12000},
    {"kode": "c004", "nama": "Facial Wash", "kategori": "Skincare", "stok": 20, "harga": 50000}
]

totalPenjualanHarian=[]
#===============================================================================================================

#FUNGSI UNTUK HANDLE EROR STRING
#JIKA ADA KELEBIHAN SPASI MAKA AKAN TERHAPUS OLEH STRIP()
#STRING YANG DIINPUT HANYA BOLEH ANGKA ATAU HURUF DENGAN KODE ISALNUM() 
#MENGGUNAKAN REPLACE AGAR ITEM YANG MENGHARUSKAN MENGGUNAKAN SPASI DAPAT MELEWATI ISALNUM()
def inputString(string):
    while True:
        object=(input(f'{string}')).strip()
        if object.replace(' ', '').isalnum():
            return object
        else:
            print('Data Yang dientry Tidak Valid !!!')

#===============================================================================================================

#FUNGSI UNTUK HANDLE EROR INT
#HANYA DAPAT DIINPUT INT, DAN ANGKA POSITIF
def inputAngka(promp):
    while True:
        try:
            angka=int(input(f'{promp}'))
            if angka<0:
                print('Angka yang diinput harus bernilai Positif')
            else:
                break
        except:
            print('Yang diinput harus angka')
    return angka

#===============================================================================================================

#FUNGSI PILIHAN KEMBALI KE MAIN MENU ATAU TIDAK
def kembali():  
    kembali=inputString('Kembali Ke Main Menu ?? (y/t) :  ').lower()
    if kembali=='y':
        print('Kembali Ke Main Menu')
        mainMenu()
    elif kembali=='t':
        print('Tetap Di Menu Saat Ini ')
        return
    else:
        print('Hanya dapat memilih y/t')

#===============================================================================================================
#MENU 1 MENAMPILKAN ITEM (READ)
def menu1():
    while True:
        print(''' 
    1. Tampilkan Semua data
    2. Tampilkan data per kategori
    3. Cari Item Dengan Kode/Nama 
    4. Kembali ke Menu
              ''')

        pilihan=inputAngka('Silahkan Masukan Angka : ')
        print()
        #PILIHAN 1 HANYA MENAMPILKAN TABEL
        if pilihan==1:
            if list_item==[]:
                print('Tidak Ada Data Untuk Ditampilkan !!')
            else:
                print('\t\t\tDaftar Item')
                print()
                print(tabulate(list_item, headers='keys', tablefmt=('fancy_outline')))

        #PILIHAN 2 MENAMPILKAN SEMUA ITEM BERDASARKAN KATEGORI
        elif pilihan==2:
            if list_item==[]:
                print('Tidak Ada Data Untuk Ditampilkan !!')
            else:
                temp=[]#UNTUK MEMBUAT TABEL
                print(''' 
                Kategori Yang tersedia :
                1. Snack
                2. Minuman
                3. Skincare''')
                kategori=inputAngka('Silahkan Pilih Kategori Yang Ingin Ditampilkan : ')
                if kategori==1:
                    for item in list_item:
                        if item['kategori'].lower()=='snack':
                            temp.append(item)

                elif kategori==2:
                    for item in list_item:
                        if item['kategori'].lower()=='minuman':
                            temp.append(item)

                elif kategori==3:
                    for item in list_item:
                        if item['kategori'].lower()=='skincare':
                            temp.append(item)
                else:
                    print('Pilihan Tidak Tersedia !!')

                #MENAMPILKAN TABEL
                if temp != []:
                    print('\t\t\tDaftar Item')
                    print(tabulate(temp, headers='keys', tablefmt=('fancy_outline')))


        #PILIHAN 3 DAPAT MENAMPILKAN ITEM SPESIFIK, DENGAN MENGINPUT KODE/NAMA ITEM
        elif pilihan==3:
            if list_item==[]:
                print('Tidak Ada Data Untuk Ditampilkan !!')
            else:            
                temp=[] #UNTUK MEMBUAT TABEL
                itemFound=False
                item=inputString('Silahkan Masukan Kode/Nama :')

                #MENCARI ITEM MENGGUNAKAN ITERASI FOR SEBANYAK LIST ITEM
                for dict in list_item:
                    if dict['nama'].lower()==item.lower() or dict['kode'].lower()==item.lower():
                        temp.append(dict)
                        itemFound=True

                #DIBUAT IF BARU AGAR ITEM YANG TIDAK DITEMUKAN HANYA MUNCUL 1 KALI PEMBERITAHUAN   
                if itemFound==False:
                    print('Item Tidak Ditemukan !!!')

                #TEMP YANG SUDAH DIISI AKAN DIBUAT BENTUK TABEL, AGAR DAPAT DILIHAT
                print(tabulate(temp, headers='keys', tablefmt=('fancy_outline')))

        #KEMBALI KE MAIN MENU
        elif pilihan==4:
            kembali()
 
        else:
            print('Pilihan yang tersedia hanya 1-3 !!')

#===============================================================================================================

#MENU 2 Menambah Item (CREATE)
def menu2():
    while True:
        print('''
    1. Menambahkan Item Baru 
    2. Kembali Ke Menu
                ''')
        itemFound=True
        pilihan2=inputAngka('Silahkan Masukan Pilihan : ')

        #PILIHAN 1 MENAMBAHKAN ITEM YANG DIINPUT
        #HANYA BOLEH MEMASUKAN KODE ITEM BARU
        if pilihan2==1 :
            kodeInput = inputString('Silahkan Masukan Kode:')

            #CEK APAKAH KODE SUDAH ADA DALAM LIST
            #HASIL DARI ANY() ADALAH TRUE/FALSE
            if any(item['kode'].lower() == kodeInput.lower() for item in list_item):
                print('Kode Tersebut Sudah ada !!')
                itemFound=False
            
            else:
                #PILIH KATEGORI
                print('''Kategori :
                    1. Snack
                    2. Minuman
                    3. Skincare''')
                add=inputAngka('Silahkan Masukan kategori :')
                if add==1:
                    tipeInput='Snack'
                elif add==2:
                    tipeInput='Minuman'
                elif add==3:
                    tipeInput='Skincare'
                else:
                    print('Kategori Tidak Ditemukan !!')

                #INPUT DATA LAINNYA
                namaInput=inputString('Silahkan Masukan Nama Item :')
                stokInput=inputAngka('Silahkan Masukan Stok : ')
                hargaInput=inputAngka('Silahkan Masukan Harga : ')

            #PILIHAN UNTUK MENYIMPAN DATA/TIDAK
            if itemFound==True:
                while True:
                    simpanData=inputString('Apakah Anda Ingin Menyimpan Data ??(y/t): ').lower()
                    if simpanData=='y':
                        list_item.append({'kode':kodeInput, 'nama': namaInput, 'kategori': tipeInput,'stok': stokInput, 'harga': hargaInput})
                        print('Data Berhasil Disimpan !!')
                        break
                    elif simpanData=='t':
                        print('Data Tidak tersimpan !!')
                        break
                    else:
                        print('Hanya dapat memilih y/t')

        #KEMBALI KE MAIN MENU
        elif pilihan2==2:
            kembali()

        #JIKA DIINPUT LEBIH DARI PILIHAN
        else:
            print('Pilihan Hanya 1-2 !!!')

#===============================================================================================================
def menu3():
    print(tabulate(list_item, headers='keys', tablefmt=('fancy_outline')))
    while True:
        print(''' 
    1. Edit Item
    2. Update Stok Barang Datang    
    3. Kembali''')
        tempEdit=[] #UNTUK MEMBUAT TABEL
        pilihan3=inputAngka('Silahkan Masukan Pilihan :')
    
        #PILIHAN 1 MENGEDIT ITEM
        if pilihan3==1:
            #HANYA DAPAT MEMASUKAN KODE
            kodeEdit=inputString('Silahkan Masukan Kode Item Yang Ingin di Edit :')
            found=False
            for item in list_item:
                if item['kode'].lower()==kodeEdit.lower():
                    tempEdit.append(item)
                    print('Data Ditemukan !!!')

                    #SETELAH DATA DITEMUKAN, DATA AKAN TAMPIL DALAM TABEL INDIVIDU
                    print(tabulate(tempEdit, headers='keys', tablefmt=('fancy_outline')))

                    #INPUT PERUBAHAN DATA
                    print('''
    Pilih Bagian Yang Ingin Diubah :
    1. Nama
    2. Stok
    3. Harga''')    

                    edit=inputAngka('Silahkan Masukan Pilihan : ')
                    if edit==1:
                        kolom='nama'
                        ubah=inputString('Silahkan Masukan Nama Baru :')
                    elif edit==2:
                        kolom='stok'
                        ubah=inputAngka('Silahkan Mengedit Stok:')
                    elif edit==3:
                        kolom='harga'
                        ubah=inputAngka('Silahkan Masukan Harga :')
                    else:
                        print('Pilihan Hanya 1-3 !!')
                    found=True  
                    break

            #JIKA KODE TIDAK DITEMUKAN
            if found==False:    
                print('Item Tidak Ditemukan !!')

            #PILIHAN MENYIMPAN DATA   
            elif found==True:
                simpanData=inputString('Apakah Anda Ingin Menyimpan Data ??(y/t): ').lower()
                if simpanData=='y':
                    item[kolom]=ubah
                    print('Data Berhasil Disimpan !!')
                elif simpanData=='t':
                    print('Data Tidak tersimpan !!')
                else:
                    print('Hanya dapat memilih y/t')
        
        #PILIHAN 2 UPDATE STOK BARANG
        elif pilihan3==2:
            temp=[] #UNTUK MEMBUAT TABEL
            itemFound=False
            kodeTambah=inputString('Silahkan Masukan Kode Item: ')
            for item in list_item:
                    if item['kode'].lower()==kodeTambah.lower():
                        temp.append(item)
                        print('Item Ditemukan !!')

                        #SETELAH DATA DITEMUKAN, DATA AKAN TAMPIL DALAM TABEL INDIVIDU
                        print(tabulate(temp, headers='keys', tablefmt=('fancy_outline')))
                        tambahStok=inputAngka('Input Jumlah Datang : ')

                        #MENAMBAH STOK DARI ITEM YANG SUDAH ADA
                        tambah=inputString('Simpan Data ??(y/t) : ').lower()
                        if tambah=='y':
                            item['stok']+=tambahStok
                            print('Data Tersimpan !!')
                        else:
                            print('Data Batal Disimpan !!')
                        itemFound=True
            
            #JIKA ITEM TIDAK DITEMUKAN
            if itemFound==False:
                print('Item Tidak Ditemukan !!')

        #PILIHAN BALIK KE MAIN MENU ATAU TIDAK        
        elif pilihan3==3:
            kembali()
        else:
            print('Pilihan Hanya 1-3 !!!')

                        
#===============================================================================================================
#MENU 4 MENGHAPUS ITEM (DELETE)
def menu4():
    print('\tDaftar Item')
    print()
    print(tabulate(list_item, headers='keys', tablefmt=('fancy_outline')))
    while True:
        print('''
        1. Hapus item Berdasarkan Kode
        2. Hapus Berdasarkan Nama
        3. Kembali Ke Main Menu''')
        pilihan4=inputAngka('Silahkan Masukan Pilihan :')
        itemFound=False

        #PILIHAN 1 HAPUS ITEM LANGSUNG DENGAN MEINGNPUT KODE
        if pilihan4==1:
            temp=[]
            hapusItem=inputString('Masukan Kode Item Yang Ingin Dihapus : ')

            #MENCARI ITEM YANG DIINPUT
            for item in list_item:
                if item['kode'].lower()==hapusItem.lower():
                    temp.append(item)
                    itemFound=True

                    #MENAMPILKAN TABEL SETELAH DATA SECARA INDIVIDU
                    print(tabulate(temp, headers='keys', tablefmt=('fancy_outline')))
                    break #KEUAR DARI FOR LOOP

            if itemFound==False:
                print('Item Tersebut tidak ditemukan !!')

            #PILIHAN SIMPAN PERUBAHAN ATAU TIDAK
            else:
                hapusFix=inputString('Apakah Anda Yakin ingin Menghapus Item Tersebut ?? (y/t) : ')
                if hapusFix=='y':
                    list_item.remove(item)
                    print('Data Telah Dihapus !!')
                elif hapusFix=='t':
                    print('Data Batal DihapUs !!')
                else:
                    print('Hanya dapat memilih y/t')

        #PILIHAN 2 CARI ITEMNYA TERLEBIH DAHULU
        elif pilihan4==2:
            temp=[]
            itemFound=False
            hapusItem=inputString('Silahkan Masukan Nama :')

            #MENCARI ITEM YANG DIINPUT
            for item in list_item:
                if item['nama'].lower()==hapusItem.lower():
                    temp.append(item)
                    
                    #MENAMPILKAN TABEL SETELAH DATA SECARA INDIVIDU
                    print(tabulate(temp, headers='keys', tablefmt=('fancy_outline')))
                    itemFound=True

            if itemFound==False:
                print('Item Tidak Ditemukan !!!')

            #PILIHAN MENYIMPAN PERUBAHAN ATAU TIDAK
            else:
                yakin=inputString('Apakah Anda Ingin Menghapus Item Ini y/t :').lower()
                if yakin=='y':                          
                    list_item.remove(item)
                    print('Item Telah Dihapus !!')
                elif yakin=='t':
                    print('Item Batal Dihapus !!')
                else:
                    print('Hanya dapat memilih y/t')

        #KEMBALI KE MAIN MENU
        elif pilihan4==3:
            kembali()

        else:
            print('Pilihan Hanya 1-3 !!')

#===============================================================================================================

#PEMBELIAN
def menu5():
    cart=[]
    print('\tDaftar Item')
    print()
    print(tabulate(list_item, headers='keys', tablefmt=('fancy_outline')))
    while True: #OUTER WHILE
        print('''
    1. Beli item
    2. Cari Item
    3. Pembayaran
    4. kembali''')


        #PILIHAN 1 LANGSUNG MENGINPUT KODE ITEM YANG INGIN DIBELI
        pilihan5=inputAngka('Silahkan Masukan Pilihan :')
        if pilihan5==1:
            itemFound=False
            showCart=False
            while True:
                kodeBeli=inputString('Silahkan Masukan Kode : ')
                for item in list_item:
                    if item['kode'].lower()==kodeBeli.lower():
                        jumlahBeli=inputAngka('Jumlah Yang Ingin Dibeli : ')
                        itemFound=True

                        if jumlahBeli<=item['stok'] :
                            totalHarga=jumlahBeli*item['harga']
                            cart.append({'kode':kodeBeli, 
                                         'nama':item['nama'],
                                         'kategori':item['kategori'], 
                                         'jumlah':jumlahBeli, 
                                         'harga':item['harga'], 
                                         'total':totalHarga})
                            # item['stok']-=jumlahBeli
                            showCart=True
                                   
                        else:
                            print(f'stok tidak cukup !! ')
                        break #KELUAR DARI INNER WHILE

                if itemFound==False:    
                    print('Maaf Kode Item Tersebut Tidak Ditemukan !!')

                #SETIAP ITEM YANG DIPILIH AKAN LANGSUNG MUNCUL TABEL TOTAL BELANJA
                if showCart==True:
                    print('\t\t\tTotal Belanja')
                    print(tabulate(cart, headers='keys', tablefmt='grid'))
                    print()

                    #PENOTALAN BELANJA
                    totalAll=0
                    for item in cart:
                        totalAll+=item['total']
                    print(f'Total yang harus dibayar sebesar :Rp. {(totalAll)}')
                    break #KELUAR DARI INNER WHILE

        elif pilihan5==2:
            temp=[]
            itemFound=False
            item=inputString('Silahkan Masukan Kode/Nama :')
            for dict in list_item:
                if dict['nama'].lower()==item.lower() or dict['kode'].lower()==item.lower():
                    temp.append(dict)
                    itemFound=True
            if itemFound==False:
                print('Item Tidak Ditemukan !!!')
            
            #MENAMPILKAN TABEL SETELAH DATA SECARA INDIVIDU
            print(tabulate(temp, headers='keys', tablefmt=('fancy_outline')))

        #PEMBAYARAN  
        elif pilihan5==3:
            while True:
                if cart==[]:
                    print('Belum Ada Item Yang Dipilih !!')
                    break
                else:
                    uang=inputAngka('Silahkan Masukan Uang Anda : ')

                    #UANG TIDAK CUKUP
                    if uang<totalAll:
                        print(f'''Transaksi Dibatalkan Uangnya Kurang Sebesar 
                            Rp.{totalAll-uang}''')
                        
                    #TRANSAKSI SUKSES
                    elif uang>totalAll:
                        print(f'''Terimakasih Uang Kembalian anda Sebesar
                            Rp. {uang-totalAll}''')
                        
                        #PENGURANGAN STOK SETIAP TRANSAKSI SUKSES
                        for item in list_item:
                            for item2 in cart:
                                if item['kode']==item2['kode']:
                                    item['stok']-=item2['jumlah']

                        #BELANJAAN MASUK KE TOTAL PENJUALAN HARIAN
                        totalPenjualanHarian.extend(cart)
                        cart=[]
                        break

                    #TRANSAKSI SUKSES
                    else:
                        print(f'Terimakasih')

                        #PENGURANGAN STOK DI LIST_ITEM
                        for item in list_item:
                            for item2 in cart:
                                if item['kode']==item2['kode']:
                                    item['stok']-=item2['jumlah']

                        #BELANJAAN MASUK KE TOTAL PENJUALAN HARIAN
                        totalPenjualanHarian.extend(cart)
                        cart=[]
                        break

        elif pilihan5==4:
            kembali()
        else:
            print('Pilihan Hanya Tersedia 1-4 !!')

#===============================================================================================================

#LAPORAN PENJUALAN        
def menu6():
    while True:
        print('''
        1. Tampilkan Semua Penjualan Hari Ini
        2. Tampilkan Per Kategori
        3. Kembali''')
        pilihan6=inputAngka('Silahkan Masukan Pilihan :')
        if pilihan6==1:
            if totalPenjualanHarian==[]:
                print('Belum ada transaksi penjualan.')
            else:
                print('\nLaporan Penjualan:')
                print(tabulate(totalPenjualanHarian, headers='keys', tablefmt='fancy_outline'))

                #PENOTALAN PENJUALAN
                total_penjualan = sum(item['total'] for item in totalPenjualanHarian)
                print(f'\nTotal Pendapatan: Rp. {total_penjualan}')

        elif pilihan6==2:
            if totalPenjualanHarian==[]:
                print('Belum ada transaksi penjualan.')
            else:
                print(''' 
                Kategori Yang tersedia :
                1. Snack
                2. Minuman
                3. Skincare''')
                temp=[]
                kategori=inputAngka('Silahkan Pilih Kategori Yang Ingin Ditampilkan : ')
                if kategori==1:
                    for item in totalPenjualanHarian:
                        if item['kategori'].lower()=='snack':
                            temp.append(item)
                elif kategori==2:
                    for item in totalPenjualanHarian:
                        if item['kategori'].lower()=='minuman':
                            temp.append(item)
                elif kategori==3:
                    for item in totalPenjualanHarian:
                        if item['kategori'].lower()=='skincare':
                            temp.append(item)
                else:
                    print('Pilihan Tidak Tersedia !!')

                #MENAMPILKAN TABEL
                print(tabulate(temp, headers='keys', tablefmt=('fancy_outline')))

                #PENOTALAN PENJUALAN
                total_penjualan = sum(item['total'] for item in temp)
                print(f'\nTotal Pendapatan: Rp. {total_penjualan}')
    
        elif pilihan6==3:
            kembali()

        else:
            print('Pilihan hanya 1-3')

#===============================================================================================================
#FUNGSI MAIN MENU
def  mainMenu():
    print('''Main Menu : 
    1. Menampilkan Daftar item
    2. Menambahkan Item
    3. Update Item
    4. Menghapus item
    5. Penjualan Item
    6. Laporan Penjualan
    7. Exit Program''')

    menu=inputAngka('Silahkan Pilih menu :')

    if menu==1:
        menu1()
        mainMenu()
    elif menu==2:
        menu2()
        mainMenu()
    elif menu==3:
        menu3()
        mainMenu()
    elif menu==4:
        menu4()
        mainMenu()
    elif menu==5:
        menu5()
        mainMenu()
    elif menu==6:
        menu6()
        mainMenu()
    elif menu==7:
        kembali=inputString('Apakah anda ingin keluar dari program ?? (y/t) :  ').lower()
        if kembali=='y':
            print('Terimakasih')
            exit()
        elif kembali=='t':
            print('Tetap Di Menu Saat Ini ')
            mainMenu()
        else:
            print('Hanya dapat memilih y/t')
    else:
        print('input tidak valid')

mainMenu()