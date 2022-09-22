#### Raihan Kus Putranto
#### 2106703821

Link Heroku : https://tugasduapbpraihankusui.herokuapp.com/katalog/


## Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html
![528676](https://user-images.githubusercontent.com/86870718/190313538-a995bb4c-a993-472b-9079-da4ca3e0e36a.jpg)


## Jelaskan kenapa menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?
Sebelum kita mulai membuat aplikasi web berbasis Django, kita *harus* menggunakan virtual environment. Virtual environment mempunyai fungsi untuk memisahkan pengaturan dan package yang diinstal kepada projek-projek Django yang dibuat. Hal ini sangat penting agar perubahan-perubahan antarproyek bisa terpisah dan tidak mengganggu proyek lainnya. Tanpa virtual environment, proyek yang kita buat bisa bentrok satu sama lain. Kemungkinan bentroknya bisa di file "requirements".

## Jelaskan bagaimana cara kamu mengimplementasikan poin 1 sampai dengan 4 di atas.
#### Poin 1
Buka file `views.py` di folder `katalog`. Buatlah fungsi `show_katalog` dengan parameter `request`. Folder ini akan mereturn `data_barang_katalog` yang berisi `list_katalog` berupa objek-objek dari `CatalogItem`, `name`, dan `id`.
### Poin 2 
Buat routing di file `urls.py` di folder `katalog`. Caranya adalah dengan menambahkan `urlpattern` yang berisi `path('', show_katalog, name='show_katalog')`. Kemudian, pindahkan routingnya menuju website dengan menambahkan url ke daftar url project di folder project_django
### Poin 3
Buka file `katalog.html` di folder templates. Buat loop untuk mengiterasi data-data di `list_katalog`, lalu berikan outputnya.
### Poin 4
Buka Heroku dan buat new app. Ambil nama proyek serta API Key dan tambahkan ke dalam repositori dengan nama `HEROKU_APP_NAME` serta `HEROKU_API_KEY`. Hal ini akan menghubungkan Github ke Heroku. 
