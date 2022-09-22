[Heroku Link](https://tugasduapbpraihankusui.herokuapp.com/mywatchlist/)

# Perbedaan JSON, XML, dan HTML
### JSON
JSON adalah format untuk menukar informasi yang berasal dari web server, sehingga dapat dibaca oleh para pengguna. Elemen yang disimpan akan lebih efisien, tetapi tidak rapi apabila kita lihat.

### XML
XML adalah format untuk menyederhanakan proses pertukaran dan penyimpanan data. XML menyimpan data dengan format yang lebih sederhana, tetapi kurang efisien.

### HTML
HTML adalah markup language yang digunakan untuk merepresentasikan data dalam elemen tree. Data tersebut akan ditampilkan dalam bentuk web page yang bisa dikustomisasi.

# Mengapa diperlukan data delivery
Data delivery diperlukan untuk memfasilitasi pengiriman dan pertukaran data antara user dna server. Dengan data delivery, pengiriman data dapat menjadi lebih efisien.

# Implementasi
### Poin 1
Jalankan perintah `python manage.py startapp mywatchlist` pada projek Django untuk membuat app baru bernama mywatchlist

### Poin 2
Tambahkan `mywatchlist` ke dalam `urls.py` pada folder `project_django`

### Poin 3
Buat model pada `models.py` bernama `MyWatchList` dengan attribut `watched`, `title`, `rating`, `release_date`, dan `review`.

### Poin 4
Initial data di folder `fixtures` bernama `initial_movie_data.json` yang berisi 10 data film. Lakukan migrasi dengan `python manage.py makemigrations` dan `python manage.py migrate`. Lalu, load initial data dengan `python manage.py loaddata initial_movie_data.json`

### Poin 5
Tambahkan method untuk menampilkan data dengan format HTML, XML, dan JSON pada file `views.py`.

### Poin 6 
Menambahkan routing untuk mengakses `mywatchlist` dalam format HTML, XML, dan JSON pada `urls.py` di dalam aplikasi `mywatchlist`.

# Postman

### HTML
![image](https://user-images.githubusercontent.com/86870718/191658959-d3b07a4f-3b68-4592-a287-7521f09d9823.png)

### XML
![image](https://user-images.githubusercontent.com/86870718/191658997-f620baef-638d-4bdf-a30a-0a4fcabf3a5f.png)

### JSON
![image](https://user-images.githubusercontent.com/86870718/191659022-4cc32801-6514-479d-ac46-2727407cac6c.png)
