[Heroku Link](https://tugasduapbpraihankusui.herokuapp.com/mywatchlist/)

# Perbedaan JSON, XML, dan HTML
### JSON
JSON adalah format yang digunakan untuk menukar informasi dari web server sehingga dapat dibaca oleh para pengguna. Elemen yang disimpan dengan JSON akan lebih efisien tetapi tidak rapi ketika dilihat.

### XML
XML adalah format yang digunakan untuk menyederhanakan proses pertukaran dan penyimpanan data. XML menyimpan data dengan format yang lebih sederhana tetapi kurang efisien.

### HTML
HTML adalah sebuah markup language yang digunakan untuk merepresentasikan data dalam element tree. Kemudian data tersebut ditampilkan dalam bentuk suatu web page yang bisa dikustomisasi.

# Mengapa diperlukan data delivery
Data delivery diperlukan untuk untuk memfasilitasi pengiriman serta pertukaran data antara user dengan server. Dengan data delivery, maka pengiriman data tersebut dapat menjadi lebih efisien dan mudah.

# Implementasi
### Poin 1
Menjalankan perintah `python manage.py startapp mywatchlist` pada projek Django

### Poin 2
Menambahkan `mywatchlist` ke dalam `urls.py` pada folder `project_django`

### Poin 3
Membuat model pada `models.py` bernama `MyWatchList` yang memiliki attribut `watched`, `title`, `rating`, `release_date`, dan `review`.

### Poin 4
Membuat initial data pada folder `fixtures` bernama `initial_movie_data.json` yang berisi 10 data film. Kemudian melakukan migrasi dengan `python manage.py makemigrations` dan `python manage.py migrate`. Setelah itu melakukan load initial data dengan `python manage.py loaddata initial_movie_data.json`

### Poin 5
Menambahkan method untuk menampilkan data dengan format HTML, XML, dan JSON pada file `views.py`.

### Poin 6 
Menambahkan routing untuk mengakses `mywatchlist` dalam format HTML, XML, dan JSON pada `urls.py` di dalam aplikasi `mywatchlist`.

# Postman

### HTML

### XML

### JSON
