# ProgramPenjualan

Program ini merupakan sebuah aplikasi sederhana dengan fitur-fitur yang dapat membantu dalam manajemen penjualan.
Adapun 6 fitur utama yang terdapat di program ini meliputi:
  1. Menampilkan Daftar item
  2. Menambahkan Item
  3. Update Item
  4. Menghapus item
  5. Penjualan Item
  6. Laporan Penjualan

Note  : Untuk kelancaran program ini pengguna diharapkan untuk melakukan instalasi tabulate terlebih dahulu,
        agar tabel-tabel yang tersedia pada program ini dapat ditampilkan.

1. Menampilkan Daftar Item
   Pada menu ini pengguna dapat menampilkan seluruh data yang tersedia. Apabila pengguna belum memiliki data (masih kosong),
   akan muncul pemberitahuan bahwa dataset anda masih kosong.
   Adapun sub menu yang tersedia yaitu :
   1. Menampilkan data secara keseluruhan
      Apabila menu ini dipilih maka seluruh data akan muncul dalam satu tabel
      
   2. Menampilkan data per kategori
      Pada menu ini pengguna dapat menampilkan item berdasarkan kategorinya, dimana pada saat ini kategori yang tersedia adalah:
      1. Snack
      2. Minuman
      3. Skincare
      Pada saat ini hanya terdapat 3 kategori, maka dari itu pengguna hanya dapat memilih pilihan 1-3.

   3. Cari item berdasarkan kode/nama
      pada menu ini pengguna dapat mencari item berdasarkan kode atau menu. ketika menu ini dipilih maka pengguna dapat menginput nama/kode,
      apabila nama/kode tersedia maka akan muncul tabel individu yang berisi seluruh data dari item yang diinput.


2. Menambahkan item
   Fitur ini digunakan untuk menambahkan sebuah item baru. Untuk menambahkan item baru pengguna diharuskan menginput sebuah kode (primary key) baru.
   Apabila kode tersebut sudah tersedia (duplicate) maka akan muncul pemberitahuan bahwa kode tersebut telah digunakan.
   Namun jika tidak maka pengguna dapat menginput data lainnya.

3. Update item
   Pada menu ini pengguna dapat memperbaharui seluruh data kecuali kodenya dan kategorinya. Adapun sub menu yang tersedia pada menu ini:
   1. Edit Item
      pada menu ini pengguna akan memasukan code dari item yang ingin diedit datanya.
      Apabila data ditemukan maka akan lanjut memilih bagian mana yang ingin di edit.
      Bagian yang bisa diedit diantaranya adalah nama, stok, dan harga.
      
   2. Update stok barang datang
      Menu ini memungkinkan pengguna menambahkan stok dari item yang tersedia.
      Pengguna akan memasukan kode dari item yang ingin ditambah stoknya,
      apabila data ditemukan maka pengguna dapat menginput berapa stok yang ingin ditambahkan.

4. Menghapus item
   Pada menu ini pengguna dapat menghapus item-item yang diinginkan, adapun sub menu yang tersedia:
   1. Hapus berdasarkan kode
      pada menu ini pengguna akan memasukan kode dari item yang ingin dihapus.
      Apabila ditemukan akan memuncul tabel individu yang berisikan data lengkap dari item yang ingin dihapus.
      Kemudian akan muncul pertanyaan ya/tidak, item akan terhapus jika pengguna memilih ya.
      
   2. Hapus berdasarkan nama
      Pada menu ini pengguna akan memasukan nama dari item yang ingin dihapus.
      Nama yang diinput dapat menggunakan huruf besar atau kecil, namun harus sesuai dengan nama yang ada pada dataset.
      Apabila ditemukan akan memuncul tabel individu yang berisikan data lengkap dari item yang ingin dihapus.
      Kemudian akan muncul pertanyaan ya/tidak, item akan terhapus jika pengguna memilih ya.
      
5. Penjualan Item
   pada menu ini pengguna dapat melakukan proses penjualan layaknya program kasir.
   Adapun sub menu yang tersedia pada program ini diantaranya :
   1. Beli item
      pada menu ini pengguna dapat memasukan kode dari item yang ingin di beli dan banyaknya.
      setiap pemilihan item berhasil akan muncul sebua tabel yang akan menampilkan data yang dipilih beserta total harganya.
      
   3. Cari Item
      Jika tidak mengetahui kode, atau hanya ingin melihat data dari item pengguna dapat menggunakan menu ini.
      pada menu ini pengguna dapat mencari item dengan memasukan nama atau kode dari item tersebut.
      setelah berhasil maka akan muncul tabel indivdu yang menampilkan dara lengkap dari item yang dipilih
      
   5. Pembayaran
      pada menu ini pengguna dapat melakukan proses pembayaran dengan memasukan jumlah uang lebih dari atau sama dengan total belanja.
      stok dari item akan berkurang setiap transaksi yang dilakukan di menu ini berhasil.

6. Laporan Penjualan
   Menu ini akan merekap semua item yang terjual beserta total penjualannya, kemudian akan di tampilkan dalam bentuk tabel.
   pengguna juga dapat memilih untuk menampilkan item yang terjual berdasarkan kategori item.
   
