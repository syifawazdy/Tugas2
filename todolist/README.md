## **README TUGAS 3 PBP**

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
