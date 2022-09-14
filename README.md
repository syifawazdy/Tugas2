# Template Proyek Django PBP

Pemrograman Berbasis Platform (CSGE602022) - diselenggarakan oleh Fakultas Ilmu Komputer Universitas Indonesia, Semester Ganjil 2022/2023

*Read this in other languages: [Indonesian](README.md), [English](README.en.md)*

## Pendahuluan

Repositori ini merupakan sebuah template yang dirancang untuk membantu mahasiswa yang sedang mengambil mata kuliah Pemrograman Berbasis Platform (CSGE602022) mengetahui struktur sebuah proyek aplikasi Django serta file dan konfigurasi yang penting dalam berjalannya aplikasi. Kamu dapat dengan bebas menyalin isi dari repositori ini atau memanfaatkan repositori ini sebagai pembelajaran sekaligus awalan dalam membuat sebuah proyek Django.

## Cara Menggunakan

Apabila kamu ingin menggunakan repositori ini sebagai repositori awalan yang nantinya akan kamu modifikasi:

1. Buka laman GitHub repositori templat kode, lalu klik tombol "**Use this template**"
   untuk membuat salinan repositori ke dalam akun GitHub milikmu.
2. Buka laman GitHub repositori yang dibuat dari templat, lalu gunakan perintah
   `git clone` untuk menyalin repositorinya ke suatu lokasi di dalam sistem
   berkas (_filesystem_) komputermu:

   ```shell
   git clone <URL ke repositori di GitHub> <path ke suatu lokasi di filesystem>
   ```
3. Masuk ke dalam repositori yang sudah di-_clone_ dan jalankan perintah berikut
   untuk menyalakan _virtual environment_:

   ```shell
   python -m venv env
   ```
4. Nyalakan environment dengan perintah berikut:

   ```shell
   # Windows
   .\env\Scripts\activate
   # Linux/Unix, e.g. Ubuntu, MacOS
   source env/bin/activate
   ```
5. Install dependencies yang dibutuhkan untuk menjalankan aplikasi dengan perintah berikut:

   ```shell
   pip install -r requirements.txt
   ```

6. Jalankan aplikasi Django menggunakan server pengembangan yang berjalan secara
   lokal:

   ```shell
   python manage.py runserver
   ```
7. Bukalah `http://localhost:8000` pada browser favoritmu untuk melihat apakah aplikasi sudah berjalan dengan benar.

## Contoh Deployment 

Pada template ini, deployment dilakukan dengan memanfaatkan GitHub Actions sebagai _runner_ dan Heroku sebagai platform Hosting aplikasi. 

Untuk melakukan deployment, kamu dapat melihat instruksi yang ada pada [Tutorial 0](https://pbp-fasilkom-ui.github.io/ganjil-2023/assignments/tutorial/tutorial-0).

Untuk contoh aplikasi Django yang sudah di deploy, dapat kamu akses di [https://django-pbp-template.herokuapp.com/](https://django-pbp-template.herokuapp.com/)

## Credits

Template ini dibuat berdasarkan [PBP Ganjil 2021](https://gitlab.com/PBP-2021/pbp-lab) yang ditulis oleh Tim Pengajar Pemrograman Berbasis Platform 2021 ([@prakashdivyy](https://gitlab.com/prakashdivyy)) dan [django-template-heroku](https://github.com/laymonage/django-template-heroku) yang ditulis oleh [@laymonage, et al.](https://github.com/laymonage). Template ini dirancang sedemikian rupa sehingga mahasiswa dapat menjadikan template ini sebagai awalan serta acuan dalam mengerjakan tugas maupun dalam berkarya.

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




