# README
Nama : Husin Hidayatu Hakim

NPM : 2306162222

Kelas : PBP C



## Questions
### Step by step pembuatan Ngaji Kuy

1. Membuat direktori baru dengan nama `ngaji-kuy`.

2. Membuat dan mengaktifkan virtual environment pada direktori tersebut dengan:
    ```
    python -m venv env
    env\Scripts\activate
    ```

3. Membuat berkas reqirements berisikan :
    ```
    django
    gunicorn
    whitenoise
    psycopg2-binary
    requests
    urllib3
    ```
    dan menginstal dependencies tersebut dengan perintah `pip install -r requirements.txt`
4. Menginisiasi proyek django baru dengan perintah
`django-admin startproject ngaji-kuy .`

5. Membuat aplikasi baru bernama main dengan perintah
`python manage.py startapp main`

6. Membuat berkas template dalam main dan mengisinya dengan 
    ```
    <h1>Ngaji Kuy</h1>
    <h5>NPM: </h5>
    <p>{{ npm }}<p>
    <h5>Name: </h5>
    <p>{{ name }}<p>
    <h5>Class: </h5>
    <p>{{ class }}<p>
    ```
7. Membuat model product dengan memodifikasi berkas models.py dengan 
    ```
    from django.db import models

    class Quran(models.Model):
        name = models.CharField(max_length=255)
        price = models.IntegerField(default=0)
        description = models.TextField()
        stock = models.IntegerField(default=0) # stock quran yang tersedia
        publisher = models.CharField(max_length=255) # penerbit quran
        type = models.CharField(max_length=255) # jenis quran (quran tafsir atau quran terjemahan)
        discount = models.DecimalField(max_digits=5, decimal_places=2, default=0.00) # diskon quran
    ```
8. Menambahkan routing untuk menghubungkan `views.py` di `main` pada `urls.py`:
    ```python
    from django.urls import path
    from main.views import show_main

    app_name = 'main'

    urlpatterns = [ path('', show_main, name='show_main'),]
    ```
9. Mengkofigurasi routing url proyek dengan memodifikasi berkas urls.py dalam direktori ngaji_kuy dengan :
    ```
    urlpatterns = [
    ...
    path('', include('main.urls')),
    ...
    ]
    ```
10. Melakukan deployment pada PWS (Pacil Web Service).




![Django Flow Chart](Django_Chart.jpg)


### Fungsi git dalam pengembangan perangkat lunak
1. MMemungkinkan anggota tim bekerja pada proyek yang sama secara bersamaan tanpa saling mengganggu hasil kerja satu sama lain.

2. Melacak semua perubahan yang terjadi pada kode, termasuk detail seperti waktu perubahan dan identitas pengubahnya.

3. Menjadi tempat penyimpanan file atau product management, memudahkan penggunaan backup file.

4. Memudahkan deployment dengan adanya fungsi pull serta push.


### Alasan Django dijadikan sebagai framework pembelajaran
1. Menyediakan banyak fitur bawaan yang memudahkan pengembangan aplikasi web.
2. Menerapkan MVT (Model-View-Template) yang membantu pengembangan web yang terstruktur dan terorganisir.
3. Memiliki sistem keamanan yang solid untuk mengamankan aplikasi web. 

### Alasan model Django disebut sebagai ORM
Model di Django disebut ORM (Object-Relational Mapping) karena berperan sebagai perantara antara model objek di kode Python dan database relasional. Dengan ORM, aplikasi menjadi lebih portabel serta mendukung berbagai jenis relasi antar tabel di dalam database.
