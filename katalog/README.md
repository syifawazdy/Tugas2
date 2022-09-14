## Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html;
![This is an image](/katalog/asset/urls.py.png)

Ketika ada http requests dari klien, dia akan diterima oleh urls.py. Dari urls .py akan ada jalur-jalur (path) tertentu (exp: /login, /home) dan ditangani oleh views tersendiri. Oleh urls.py akan dicek http request ini akan ke path yang mana, maka urls akan memforward request ke views.py yang akan menangani context yang sesuai sehingga masing2 path akan mempunyai views.py tersendiri. Jika requestnya membutuhkan read/write data pada database, views.py akan berhubungan dengan models.py. Models.py disini berperan sebagai manager dari data user. Dikarenakan data perlu ditunjukkan ke user, maka views.py akan mengambil template yang sesuai untuk membuat halaman context yang utuh di html. Halaman html yang utuh tersebut yang akan menjadi response untuk dikirim ke klien. 

## Jelaskan kenapa menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?

Kita menggunakan virtual environment untuk mengisolasi package serta dependencies dari aplikasi sehingga tidak bertabrakan dengan versi lain yang ada pada komputer. Walau sangat direkomendasikan untuk menggunakan virtual environment, kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment. Tanpa virtual environment, semua proyek kita akan menggunakan installed packages yang sama. Jika hanya menjalankan skrip kecil untuk memeriksa algoritma kita mungkin tidak memerlukan virtual environment (walau tetap sangat direkomendasikan menggunakannya)

## Jelaskan bagaimana cara kamu mengimplementasikan poin 1 sampai dengan 4 di atas.

Berikut cara saya mengimplementasikan poin 1 sampai 4:
- Membuat fungsi show_katalog di views.py yang dapat melakukan pengambilan data dari model dan dikembalikan ke dalam HTML.

- Mengisi urls.py di aplikasi katalog untuk melakukan routing terhadap fungsi views yang telah dibuat sehingga nantinya halaman HTML dapat ditampilkan lewat browser dan mendaftarkan aplikasi katalog pada variabel urlpatterns di urls.py pada folder project_django 

- Mengimpor models di dalam file views.py dan menggunakan class tersebut untuk melakukan pengambilan data dari database dengan import render dan CatalogItem. Lalu memanggil fungsi query ke model database dan menyimpan hasil query ke dalam variabel nama dan id

- Menambahkan context pada pengembalian fungsi render di fungsi show_katalog agar data didalamnya dapat di-render oleh Django sehingga muncul di halaman HTML.

- Menggunakan sintaks {{data}} untuk melakukan mapping terhadap data yang telah ikut di-render pada fungsi views untuk dapat memunculkannya di HTML. Untuk menampilkan daftar katalog, perlu dilakukan iterasi terhadap variabel list_barang yang telah ikut render ke dalam HTML

- Sebelum deploy, mempersiapkan migrasi skema model ke dalam databese Django lokal, menerapkan skema model yang telah dibuat, dan memasukka data ke databese Django lokal. Lalu, menambahkan variabel repository secret baru untuk melakukan deployment. Deployment dilakukan melalui aplikasi Heroku dengan menambah app baru dan menyambungkannya dengan GitHub.