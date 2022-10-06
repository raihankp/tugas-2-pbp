[Heroku Link](https://tugasduapbpraihankusui.herokuapp.com/todolist/)

# TUGAS 04

## Apa kegunaan {% csrf_token %} pada elemen <form>? Apa yang terjadi apabila tidak ada potongan kode tersebut pada elemen <form>?
CSRF token merupakan suatu angka unik yang sangat panjang dan tidak mungkin bisa ditebak. Setiap user yang mengakses suatu website mempunyai CSRF token sendiri-sendiri. 
Ketika terdapat suatu _request_ dari user, server akan memastikan bahwa CSRF token yang dimiliki user sesuai dengan token yang diharapkan oleh server. Apabila berbeda, maka server akan menolak _request_ dari user.
CSRF tokens bisa menghindari CSRF attacks dari pihak lain karena CSRF tokens nya tidak bisa diketahui.
  
## Apakah kita dapat membuat elemen <form> secara manual (tanpa menggunakan generator seperti {{ form.as_table }})? Jelaskan secara gambaran besar bagaimana cara membuat <form> secara manual.
Ya, bisa. Caranya adalah dengan menampilkan setiap parameter secara manual. Contohnya adalah, apabila kita ingin menampilkan username, maka kita bisa menggunakan kode {{form.username}}. Begitu pula untuk parameter lainnya.

## Jelaskan proses alur data dari submisi yang dilakukan oleh pengguna melalui HTML form, penyimpanan data pada database, hingga munculnya data yang telah disimpan pada template HTML.
Setelah kita melakukan submisi pada form, data-data yang telah diisi akan dipanggil melalui fungsi-fungsi yang terdapat di views. Setelah itu, data-data tersebut akan dibuat objeknya di models dan dimasukkan ke dalam database Django.

## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
1. Membuat app baru bernama `todolist` dengan `perintah python manage.py startapp todolist`
2. Melakukan routing app dengan cara menambah path todolist ke urls.py yang terdapat di project_django dengan perintah `path('todolist/', include('todolist.urls')),`
3. Membuat models.py dengan objek-objek yang diminta
4. Membuat fungsi login, register, dan logout di `views.py` dan halaman html sesuai dengan tutorial Lab3
5. Membuat fungsi show_todolist di `views.py`
6. Membuat file `forms.py` dengan isi menggunakan `modelform` dan memiliki 2 fields yaitu title dan description
7. Membuat fungsi add_task untuk menambah task, fungsi update_task untuk mengupdate is_finished, fungsi delete_task untuk menghapus task yang telah dibuat.
8. Menambahkan routing page di `urls.py` pada folder `todolist` sesuai dengan fungsi-fungsi yang ada di `views.py`
9. Melakukan push kepada git dan deploy melalui heroku
10. Membuat dua akun pengguna dan tiga dummy data di heroku


# TUGAS 05

## Apa perbedaan dari Inline, Internal, dan External CSS? Apa saja kelebihan dan kekurangan dari masing-masing style?
| | Inline | Internal | External |
|-|--|--|--|
|Perbedaan|Style berada di satu elemen saja|CSS berada di file yang sama|CSS berada di file sendiri|
|Kelebihan|Membantu ketika ingin menguji style pada satu elemen, mempercepat perbaikan, dan load halaman lebih cepat|Berlaku pada satu halaman saja|Tidak perlu membuat banyak file CSS karena berada dalam satu file yang sama dengan HTML|CSS bisa diberlakukan pada beberapa file HTML, ukuran HTML juga lebih kecil|
|Kekurangan|Tidak efisien karena hanya digunakan pada satu elemen saja|Tidak efisien ketika ingin menggunakan style yang sama di beberapa file|Memperbanyak file dan satu halaman HTML akan berantakan ketika CSS gagal dipanggil|


## Jelaskan tag HTML5 yang kamu ketahui.
'<html>' Tag untuk membuat dokumen HTML
'<title>' Tag untuk menentukan judul dari suatu halaman
'<body>' Tag untuk membuat tubuh dari suatu halaman
'<h1> - <h6>' Tag untuk membuat header
'<p>' Tag untuk membuat suatu paragraf
'<a>' Tag untuk membuat hyperlink
'<br>' Tag untuk memberikan satu baris kosong
'<b>' Tag untuk membuat suatu kata tercetak tebal
'<table>' Tag untuk membuat table
'<th>' Tag untuk membuat caption pada table
'<tr>' Tag untuk membuat baris pada table
'<td>' Tag untuk membuat sel pada table
'<form>' Tag untuk membuat form untuk input user
'<input>' Tag untuk membuat suatu input
'<button>' Tag untuk membuat suatu tombol yang bisa diklik
'<label>' Tag untuk membuat label
'<img>' Tag untuk memasukkan gambar

## Jelaskan tipe-tipe CSS selector yang kamu ketahui.
1. Selektor Tag, akan memilih elemen yang sesuai dengan tag
2. Selektor Class (didahului .), akan memilih elemen berdasarkan class yang dipilih
3. Selektor ID (didahului #), akan memilih elemen berdasarkan ID dan bersifat unik (hanya boleh digunakan satu elemen)
4. Selektor Universal (*), akan memilih semua elemen pada scope tertentu

## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
1. Masukkan <link >bootstrap kepada base.html
2. Menerapkan style dan bootstrap kepada halaman login, register, create-task, dan todolist
3. Membuat keempat halaman responsif dengan memasukkan media query pada base.html
4. Melakukan push dan deploy kepada heroku


