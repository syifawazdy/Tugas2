## **README TUGAS 5 PBP**

**Apa perbedaan dari Inline, Internal, dan External CSS? Apa saja kelebihan dan kekurangan dari masing-masing style?**

1. Internal CSS adalah kode CSS yang ditulis di dalam tag style dan kode HTML dituliskan di bagian atas (header) file HTML. Kelebihan Internal CSS yaitu perubahan pada Internal CSS hanya berlaku pada satu halaman saja dan kita tidak perlu melakukan upload beberapa file karena HTML dan CSS berada dalam satu file. Kekurangan Internal CSS yaitu idak efisien apabila kita ingin menggunakan CSS yang sama dalam beberapa file.

2. Eksternal CSS adalah kode CSS yang ditulis terpisah dengan kode HTML Eksternal CSS ditulis di sebuah file khusus yang berekstensi .css. File eksternal CSS biasanya diletakkan setelah bagian head pada halaman. Kelebihan External CSS yaitu ukuran file HTML akan menjadi lebih kecil dan struktur dari kode HTML jadi lebih rapi dan file CSS dapat digunakan di beberapa halaman website sekaligus. Kekurangan External CSS yaitu halaman akan menjadi berantakan ketika file CSS gagal dipanggil oleh file HTML dan diprioritaskan paling akhir dibanding CSS lain.

3. Inline CSS adalah kode CSS yang ditulis langsung pada atribut elemen HTML. Setiap elemen HTML memiliki atribut style, dan disitulah inline CSS ditulis. Kelebihan Inline CSS yaitu sangat membantu ketika kita hanya ingin menguji dan melihat perubahan pada satu elemen dan berguna untuk memperbaiki kode dengan cepat. Kekurangan Inline CSS yaitu idak efisien karena Inline style CSS hanya bisa diterapkan pada satu elemen HTML.

**Jelaskan tag HTML5 yang kamu ketahui.**

```<a>``` mendefinisikan hyperlink.
```<b>``` membuat bold
```<body>``` mendefinisikan body 
```<br>``` single line break
```<button>``` membuat tombol
```<div>``` menunjukkan suatu divisi atau bagian
```<h1>``` ke ```<h6>``` heading HTML
```<img>``` representasi gambar
```<nav>``` bagian navigasi
```<p>``` mendefinisikan paragraf
```<style>``` menyisipkan informasi styling (currently dengan CSS)
```<table>``` mendefinisikan sel di tabel
```<textarea>``` multiline text input
```<th>``` sel header di tabel
```<tr>``` baris sel di tabel
```<ul>``` unordered list


**Jelaskan tipe-tipe CSS selector yang kamu ketahui.**

1. Element Selector: menggunakan tag HTML sebagai selector (without leading # or .)
2. ID Selector: menggunakan ID pada tag sebagai selector (with leading #)
3. Class Selector: menggunakan Class pada tag sebagai selector (with leading .)

**Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.**

- Kustomisasi templat untuk halaman login, register, dan create-task semenarik mungkin.
Kustomisasi menggunakan bootstrap dengan sumber dari https://getbootstrap.com/docs

- Kustomisasi halaman utama todo list menggunakan cards. (Satu card mengandung satu task).
Kustomisasi menggunakan cards dengan sumber dari https://getbootstrap.com/docs/4.2/components/card/

- Membuat keempat halaman yang dikustomisasi menjadi responsive.
"Bootstrap includes a responsive, mobile first fluid grid system that appropriately scales up to 12 columns as the device or viewport size increases" - getboostrap.com

**--------------------------------------------------------------------------------------------------------------------------------------------------**

## **README TUGAS 4 PBP**

### Link Heroku:
https://tugas2pbpsyifa.herokuapp.com/todolist/
https://tugas2pbpsyifa.herokuapp.com/todolist/register
https://tugas2pbpsyifa.herokuapp.com/todolist/login
https://tugas2pbpsyifa.herokuapp.com/todolist/create-task
https://tugas2pbpsyifa.herokuapp.com/todolist/logout

**Apa kegunaan {% csrf_token %} pada elemen form? Apa yang terjadi apabila tidak ada potongan kode tersebut pada elemen form?**

Keguanaan dari {% csrf_token %} adalah merender elemen tersembunyi dengan nilai yang disetel ke token CSRF (Cross Site Request Forgeries). Ketika server Django menerima permintaan formulir, Django akan memverifikasi bahwa token cocok dengan nilai yang diberikan dalam formulir. Ini diperlukan untuk memastikan bahwa POST permintaan (misalnya permintaan pengubah data) berasal dari sesi klien yang otentik. Yang terjadi jika tidak ada potongan kode tersebut pada elemen form adalah akan membuat web menjadi kurang aman dari serangan CSRF.


**Apakah kita dapat membuat elemen form secara manual (tanpa menggunakan generator seperti {{ form.as_table }})? Jelaskan secara gambaran besar bagaimana cara membuat form secara manual.**


Ya, kita tetap bisa membuat form secara manual tanpa menggunakan built-in dari Django. Gambaran besar cara membuatnya adalah dengan membuat form class lalu merender form menjadi view dan membuat instance dari form class dengan html (jika ingin mempercantik bisa menggunakan CSS). 
```
<form action=[URL DESTINATION] method=[METHOD]>
<input type=[INPUT TYPE] other attributes>
....
....
<input type=[INPUT TYPE] other attributes>
</form>

```

**Jelaskan proses alur data dari submisi yang dilakukan oleh pengguna melalui HTML form, penyimpanan data pada database, hingga munculnya data yang telah disimpan pada template HTML.**

Alur data dari submisi form yaitu 
- User type address http://host/path
Browser lalu browser generate HTTP Request ke http://host/path dan server menerima HTTP Request dan mencari views.py mana yang akan meng-handle path
- Views.py yang sesuai akan men-generate HTML FORM page dan akan menampilkan HTML layout ke user
- User akan insert form lalu browser akan menghasilkan HTTP Request, Method, dan arguments ke URL tujuan sesuai dengan HTML page FORM
- Server menerima HTTP Request dan mencari views.py mana yang akan meng-handle path. Lalu, setelah views.py melakukan apa yang harus dilakukan maka akan dihasilkan halaman HTML
- Browser akan menampilkan halaman HTML kepada user.

**Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.**

- Membuat aplikasi baru bernama todolist dengan startapp todolist

- Menambahkan aplikasi todolist ke dalam INSTALLED_APPS pada settings.py

- Membuat models.py dengan class Task berisi atribut user, date, title, dan description

- Membuat form.py untuk membuat class NewForm sebagai basis create_task.html agar dapat membuat task baru di dalam form

- Mengisi views.py dengan berbagai fungsi seperti show_todolist, create_todo, login_user, logout_user, dan register.

- Membuat file html untuk registrasi dan login agar dapat membuat akun untuk memakai app todolist

- Membuat file html todolist.html agar dapat menampilkan tabel todolist 

- Mengimpor semua fungsi yang dibuat ke urls.py dan menambahkan path url ke urlpatterns untuk mengakses fungsi yang tadi diimpor

- Add, commit, push, deploy, dan membuat 2 user & 3 dummy data 
