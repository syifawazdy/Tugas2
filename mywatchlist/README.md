## **README TUGAS 3 PBP**

### Link Heroku:

https://tugas-3-pbp-syifa.herokuapp.com/mywatchlist/
https://tugas-3-pbp-syifa.herokuapp.com/mywatchlist/html/
https://tugas-3-pbp-syifa.herokuapp.com/mywatchlist/xml/
https://tugas-3-pbp-syifa.herokuapp.com/mywatchlist/json/

### Screenshot Postman
![This is an image](/mywatchlist/asset/html.png)
![This is an image](/mywatchlist/asset/json.png)
![This is an image](/mywatchlist/asset/xml.png)

### **Jelaskan perbedaan antara JSON, XML, dan HTML!**

JSON:

JSON adalah singkatan dari JavaScript Object Notation. JSON didasarkan pada bahasa JavaScript dan merupakan cara untuk merepresentasikan objek. File JSON sangat mudah dibaca jika dibandingkan dengan XML. Namun, JSON kurang terjamin keamanannya dibandingkan XML dan tidak mendukung comments. 


XML:

XML adalah singkatan dari Extensible Markup Language. XML didasarkan dari bahasa XML dan merupakan bahasa markup yang menggunakan struktur tag untuk mewakili item data. XML digunakan untuk menyimpan data dan mampu membawa data ke dan dari database. Walau dokumennya relatif sulit untuk dibaca dan ditafsirkan, XML lebih aman daripada JSON.


HTML:

HTML adalah singkatan dari Hyper Text Markup Language. HTML merupakan bahasa markup dan digunakan untuk menampilkan data. HTML tidak membawa data dan hanya menampilkannya. HTML menggambarkan struktur halaman web secara semantik dan memiliki elemen HTML yang merupakan blok bangunan halaman HTML.


### **Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?**

Kita memerlukan data delivery untuk mengimplementasikan suatu platform dikarenakan dalam mengembangkan suatu platform, ada kalanya kita perlu mengirimkan data dari satu stack ke stack lainnya sehingga dibutuhkan data delivery yang sesuai dengan request.


### **Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.**

1. Membuat app mywatchlist dan menambahkannya di INSTALLED_APPS settings.py project_django. Lalu menambah class berisi data terkait mywatchlist di models.py di folder mywatchlist. Melakukan makemigrations dan migrate, lalu membuat berkas data tentang film bernama initial_mywatchlist_data.json di folder fixtures, akhirnya loaddata.

2. Membuat fungsi untuk mywatchlist, html, json, dan xml. Lalu, membuat data film dalam file mywatchlist.html di folder templates dan membuat routing dengan menambahkan path di urlpatterms di urls.py untuk semua data delivery yang digunakan

3. Menambah unit test di tests.py dengan membuat class MyWatchListTest dan membuat fungsi untuk mengetes html, xml, dan json

4. Membuat fitur pesan dengan menggunakan if else di fungsi show_mywatchlist dan show_html (isinya sama dikarenakan /mywatchlist isinya sama dengan /mywatchlist/html)

Sekian. Terima Kasih.
