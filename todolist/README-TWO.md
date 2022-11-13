 ***Jelaskan perbedaan antara asynchronous programming dengan synchronous programming.***

 Perbedaan antara asynchronous programming dengan synchronous programming adalah dalam synchronous programming, setiap perintah akan memblok eksekusi perintah selanjutnya hingga perintah yang sedang dieksekusi selesai se. Sedangkan pada asynchronous programming, proses jalannya program bisa dilakukan secara bersamaan tanpa harus menunggu proses antrian

 ***Dalam penerapan JavaScript dan AJAX, terdapat penerapan paradigma Event-Driven Programming. Jelaskan maksud dari paradigma tersebut dan sebutkan salah satu contoh penerapannya pada tugas ini.***
 Event-Driven Programming adalah sebuah paradigma pemrograman yang alur programnya ditentukan oleh suatu event / peristiwa yang merupakan keluaran atau tindakan pengguna. Pada tugas ini contohnya yaitu pada saat button Add Task diklik oleh user, maka akan menyebabkan sebuah event terjadi, yaitu akan muncul modal pada laman website untuk membuat task baru di todolist kita.

 ***Jelaskan penerapan asynchronous programming pada AJAX.***
 AJAX adalah sebuah teknik yang dapat membuat laman website ter-update secara asinkronus yang berarti browser tidak perlu reload seluruh laman website ketika ada perubahan data yang kecil. AJAX akan mengirimkan request ke server, dan melanjutkan eksekusi tanpa menunggu balasan dari server terlebih dahulu.

 ***Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.***
 1. Menambah 3 views dan path baru untuk mengembalikan data task dalam bentuk json, menambahkan data baru ke dalam database, dan pengambilan task dengan AJAX. 

![This is an image](/todolist/assets/path.png)
![This is an image](/todolist/assets/views.png)

 2. Membuat file todolix_ajax.html dimana isinya ada class untuk membuka sebuah modal dengan form untuk menambahkan task dan menutupnya jika sudah memencet tombol "Create"
 ```
 <div class="modal fade modal-dialog modal-dialog-centered" id="addTask" tabindex="-1" aria-labelledby="addTaskLabel" aria-hidden="true">
    <div class="modal-dialog">
      <div class="modal-content">
        <div class="modal-header">
          <h1 class="modal-title fs-5" id="exampleModalLabel">Add Task</h1>
        </div>
        <div class="modal-body">
          <form method="POST" action="" style="display: inline-block;">
            {% csrf_token %}
            <table>
              <tr>
                <label>Title</label>
                <input type="text" name="title" id="title">
              </tr><br>
              <tr>
                <label>Description</label>
                <input type="textarea" name="description" id="description">
              </tr>
                  <td colspan="2">
                    <input data-bs-dismiss="modal" style="width: 100%; margin-top: 20px; margin-bottom: 7px;" class="btn btn btn-dark" type="submit" name="submit" value="Create" id="create-button">
                  </td>
              </tr>
          </table>
        </form>
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
      </div>
    </div>
  </div>
```
