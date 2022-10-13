[Heroku Link](https://tugasduapbpraihankusui.herokuapp.com/todolist/)

# TUGAS 06

### Jelaskan perbedaan antara asynchronous programming dengan synchronous programming.
Synchronous Programming adalah program yang berjalan secara sekuensial. Program dieksekusi baris per baris secara hierarki dan harus menunggu proses antrian untuk menjalankan kode selanjutnya. Proses ini cenderung lebih lambat. Sedangkan, Asynchronous Programming adalah program yang bisa berjalan secara bersamaan tanpa menunggu proses antrian. Proses ini memiliki waktu eksekusi yang lebih singkat dan cepat.

### Dalam penerapan JavaScript dan AJAX, terdapat penerapan paradigma Event-Driven Programming. Jelaskan maksud dari paradigma tersebut dan sebutkan salah satu contoh penerapannya pada tugas ini.
Event-Driven Programming merupakan suatu paradigma pemrograman yang alurnya ditentukan dari tindakan user berupa suatu event. Event merupakan sebuah aksi yang muncul karena dipicu berbagai hal. Misalnya adalah ketika suatu button di klik.
Contoh penerapannya pada tugas ini adalah mengirimkan data task baru ketika button diklik.

### Jelaskan penerapan asynchronous programming pada AJAX.
Penerapan Asynchronous Programming pada AJAX terjadi ketika event dilakukan, contohnya ketika suatu button di klik, maka program akan segera mengeksekusi suatu proses tanpa menunggu proses antrian hierarki kode selanjutnya. Misalkan button yang diklik akan mengembalikan data task, maka AJAX GET akan digunakan. Bila button yang diklik akan menambah task baru, maka AJAX POST akan digunakan.

### Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
1. Membuat fungsi bernama `show_json` dan `add_task` di views dengan menerapkan asynchronous programming
2. Melakukan routing `show_json` dan add_task di `urls.py`
3. Membuat <script> di `todolist.html` untuk membuat card lalu mengarahkannya ke fungsi `add_task` untuk membuat object task baru dan mereturn hasil POST
4. Melakukan request GET ke `todolist/json` lalu map ke data. Setiap iterasi akan menambahkan card sehingga dapat muncul pada halaman
5. Membuat modal untuk membuat card baru dan membuat fungsi POST yang akan berjalan saat button `Tambah Task` diklik. Apabila POST sukses, data akan ditambah dengan card yang baru dibuat.
