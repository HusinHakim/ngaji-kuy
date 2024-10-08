# README
Nama : Husin Hidayatu Hakim

NPM : 2306162222

Kelas : PBP C



## Tugas 2
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




![Django Flow Chart](django_chart.png)


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


Nama : Husin Hidayatu Hakim

NPM : 2306152481

Kelas : PBP C

## Tugas 3

### 1. Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?

Data delivery telah menjadi tulang punggung yang dibutuhkan dalam pengimplementasian sebuah platform. Fungsinya sebagai penghubung yang memungkinkan berbagai komponen di dalam platform berinteraksi secara efisien dan harmonis, baik antara server dan klien maupun antar elemen seperti database dan user interface. Proses pengiriman data yang teratur, aman, dan tepat waktu menjamin kinerja platform berjalan sesuai harapan, menghindari isolasi antar elemen yang dapat mengganggu fungsionalitas. Selain itu, strategi data delivery yang tepat dapat meningkatkan skalabilitas platform, memungkinkannya untuk beradaptasi dengan perubahan kebutuhan dan mengatasi lonjakan beban data dengan cepat dan efisien.


### 2. Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?

- Lebih Ringkas: JSON menggunakan sintaks yang lebih sederhana dan lebih sedikit karakter dibandingkan XML, sehingga lebih cepat dikirim dan diproses.

- Mudah Diproses: JSON lebih mudah dipahami dan diurai oleh banyak bahasa pemrograman, terutama JavaScript.

- Struktur Sederhana: JSON hanya menggunakan pasangan kunci-nilai, sedangkan XML menggunakan tag yang lebih kompleks.

- Kinerja Lebih Efisien: JSON membutuhkan lebih sedikit sumber daya untuk parsing, sehingga lebih cepat dan efisien dibanding XML.

- Populer di API Modern: Banyak API dan aplikasi web serta mobile menggunakan JSON karena kompatibilitas dan kecepatan yang lebih baik.

### 3. Jelaskan fungsi dari method `is_valid()` pada form Django dan mengapa kita membutuhkan method tersebut


Method `is_valid()` sangat penting dalam proses validasi data yang dimasukkan oleh pengguna pada form Django. Fungsinya adalah untuk memeriksa apakah data yang dikirimkan melalui form sudah sesuai dengan aturan validasi yang telah ditentukan, seperti apakah semua field wajib telah diisi, apakah format data benar, atau apakah data memenuhi batasan tertentu. Jika semua data valid, method ini akan mengembalikan `True`, dan jika ada yang tidak valid, akan mengembalikan `False`. Selain itu, jika terjadi kegagalan validasi, Django akan secara otomatis mengisi dictionary form.errors dengan pesan kesalahan untuk setiap field yang bermasalah. Method ini juga berperan penting dalam mencegah masuknya data yang tidak valid atau berbahaya, melindungi aplikasi dari bug dan potensi ancaman keamanan.

### 4. Mengapa kita membutuhkan `csrf_token` saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan `csrf_token` pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?

CSRF token (Cross-Site Request Forgery token) diperlukan saat membuat form di Django untuk melindungi aplikasi dari serangan CSRF. CSRF adalah jenis serangan di mana penyerang mencoba mengirim permintaan yang tidak sah atas nama pengguna yang telah diautentikasi di situs web. Token ini memastikan bahwa setiap permintaan yang dikirimkan oleh pengguna melalui form memang berasal dari sumber yang sah (situs web itu sendiri) dan bukan dari pihak eksternal.

Jika kita tidak menambahkan csrf_token pada form, aplikasi menjadi rentan terhadap serangan CSRF. Penyerang dapat memanfaatkan celah ini dengan mengirimkan permintaan berbahaya atas nama pengguna yang telah login tanpa sepengetahuan mereka, seperti melakukan transaksi atau mengubah data penting. Contohnya, jika pengguna mengakses halaman berbahaya yang dibuat oleh penyerang, halaman tersebut bisa secara otomatis mengirimkan permintaan ke server yang mengakibatkan perubahan data di akun pengguna tanpa izin.

Dengan menambahkan csrf_token, Django memastikan bahwa setiap permintaan form hanya bisa dijalankan jika token tersebut valid, sehingga melindungi aplikasi dari serangan yang mencoba memanfaatkan CSRF.

### 5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

1. Membuat `base.html` untuk menjadi page utama dalam website
    ```python
    {% load static %}
    <!DOCTYPE html>
    <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            {% block meta %} {% endblock meta %}
        </head>
        <body>
            {% block content %} {% endblock content %}
        </body>
    </html>
    ```

    2. Menambahkan `BASE_DIR` pada `settings.py` agar project mengenali html yang akan menjadi template utama
    ```python
    'DIRS': [BASE_DIR / 'templates'],
    ```

    3. Menambahkan atribut `id` pada model product
    ```python
    from django.db import models
    import uuid

    class Quran(models.Model):
        id = models.UUIDField(primary_key=True,default=uuid.uuid4, editable=False)  
        name = models.CharField(max_length=255)
        price = models.IntegerField(default=0)
        description = models.TextField()    
        stock = models.IntegerField(default=2)
        publisher = models.CharField(max_length=255, default="No Publisher") # penerbit quran
        type = models.CharField(max_length=255, default="Tafsir") # jenis quran (quran tafsir atau quran terjemahan)
    

    @property
    def is_in_stock(self):
        return self.stock > 0
    ```

    4. Membuat `forms.py` untuk mendeklarasikan atribut-atribut dari model yang membutuhkan input dari user
    ```python
    from django.forms import ModelForm
    from main.models import Quran

    class QuranForm(ModelForm):
        class Meta:
            model = Quran
            fields = ["name", "price", "description", "publisher", "stock", "type"]
    ```

    5. Membuat method `create_name_entry` untuk mengambil input user sesuai dengan `forms.py`
    ```python
    def create_quran_entry(request):
        form = QuranForm(request.POST or None)

        if form.is_valid() and request.method == "POST":
            form.save()
            return redirect('main:show_main')

        context = {'form': form}
        return render(request, "create_quran_entry.html", context)
    ```

    6. Membuat method `show_main` untuk menampilkannya di `main.html`
    ```python
    def show_main(request):
    quran_entries = Quran.objects.all()
    context = {
        'Nama_Aplikasi' : "Ngaji Kuy",
        'Name' : "Husin Hidayatul Hakim",
        'Class' : "PBP C",
        'quran_entries': quran_entries
    }
    return render(request, "main.html", context)

    ```


    7. Membuat `show_xml`, `show_json`, `show_xml_by_id`, `show_json_by_id` untuk menampilkan response back dari input user
    ```python
    def show_xml(request):
        data = Quran.objects.all()
        return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")


    def show_json(request):
        data = Quran.objects.all()
        return HttpResponse(serializers.serialize("json", data), content_type="application/json")

    def show_xml_by_id(request, id):
        data = Quran.objects.filter(pk=id)
        return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

    def show_json_by_id(request, id):
        data = Quran.objects.filter(pk=id)
        return HttpResponse(serializers.serialize("json", data), content_type="application/json")
    ```

    8. Melakukan routing di dari method yang sudah dibuat di `urls.py`
    ```python
    from django.urls import path
    from main.views import show_main, create_quran_entry, show_xml, show_json, show_xml_by_id, show_json_by_id

    app_name = 'main'

    urlpatterns = [
        path('', show_main, name='show_main'),
        path('create-mood-entry', create_quran_entry, name='create_mood_entry'),
        path('xml/', show_xml, name='show_xml'),
        path('json/', show_json, name='show_json'),
        path('xml/<str:id>/', show_xml_by_id, name='show_xml_by_id'),
        path('json/<str:id>/', show_json_by_id, name='show_json_by_id'),
    ]
    ```

    9. Membuat `create_name_entry.html` untuk tampilan ketika web ingin meminta input dari pengguna
    ```python
    {% extends 'base.html' %} 
    {% block content %}
    <h1>Add Product Entry</h1>

    <form method="POST">
    {% csrf_token %}
    <table>
        {{ form.as_table }}
        <tr>
        <td></td>
        <td>
            <input type="submit" value="Add Product Entry" />
        </td>
        </tr>
    </table>
    </form>

    {% endblock %}
    ```
    
    10. Membuat `main.html` untuk menampilkan product dari hasil input pengguna
    ```python
    {% extends 'base.html' %}
    {% block content %}
    <h1>Ngaji Kuy</h1>

    <h5>Nama_Aplikasi: </h5>
    <p>{{ Nama_Aplikasi }}<p>

    <h5>Name:</h5>
    <p>{{ name }}</p>

    <h5>Class:</h5>
    <p>{{ class }}</p>

    {% if not quran_entries %}
    <p>Belum ada data pemesanan pada ngaji kuy.</p>
    {% else %}
    <table>
    <tr>
        <th>Nama Quran</th>
        <th>Price</th>
        <th>Description</th>
        <th>Publisher</th>
        <th>Stock</th>
        <th>Type</th>
    </tr>

    
    {% for quran_entry in quran_entries %}
    <tr>
        <td>{{quran_entry.name}}</td>
        <td>{{quran_entry.price}}</td>
        <td>{{quran_entry.description}}</td>
        <td>{{quran_entry.publisher}}</td>
        <td>{{quran_entry.stock}}</td>
        <td>{{quran_entry.type}}</td>
    </tr>
    {% endfor %}
    </table>
    {% endif %}

    <br />

    <a href="{% url 'main:create_mood_entry' %}">
    <button>Add New Mood Entry</button>
    </a>

    {% endblock content %}
    ```

### Screenshot Postman
#### JSON
<img src="https://i.ibb.co.com/6ms8MZ5/JSONID.png" alt="JSONID" border="0">

#### XML
<img src="https://i.ibb.co.com/HhXmr37/JSON.png" alt="JSON" border="0">

#### JSON with ID
<img src="https://i.ibb.co.com/LZYLWXn/XML.png" alt="XML" border="0">

#### XML with ID
<img src="https://i.ibb.co.com/ggBSRR7/XMLID.png" alt="XMLID" border="0">


Nama : Husin Hidayatul Hakim

NPM : 23016152481

Kelas : PBP D

## Tugas 4


### 1. Apa perbedaan antara HttpResponseRedirect() dan redirect()?
`HttpResponseRedirect()` membutuhkan URL lengkap sebagai argumen, sedangkan `redirect()` lebih fleksibel, bisa menerima nama view atau model dan otomatis mengarahkan ke URL yang benar.

### 2. Jelaskan cara kerja penghubungan model Product dengan User!
Model `Product` dihubungkan dengan `User` melalui `ForeignKey`. Hal ini memungkinkan setiap produk terkait dengan satu pengguna, dan produk dapat difilter berdasarkan pengguna yang sedang login.

### 3. Apa perbedaan antara authentication dan authorization?
`Authentication` memverifikasi identitas pengguna, sedangkan `authorization` menentukan apa yang diizinkan untuk dilakukan oleh pengguna tersebut. Django mengelola keduanya melalui modul `auth`, dengan `authentication` menggunakan `login()` dan `authorization` melalui sistem perizinan.

### 4. Bagaimana Django mengingat pengguna yang telah login?
Django menggunakan session untuk mengingat pengguna yang login. Informasi sesi disimpan di sisi server dan referensi sesi (ID sesi) disimpan di cookies pengguna. Cookies dapat digunakan untuk menyimpan informasi seperti waktu login terakhir.
## Checklist Implementasi

### 1. Membuat Fungsi Registrasi, Login, dan Logout
#### Registrasi
Fungsi registrasi menggunakan `UserCreationForm` dari Django yang sudah tersedia, untuk memudahkan pembuatan pengguna baru. Formulir ini akan divalidasi dan, jika berhasil, akun pengguna akan dibuat.

```python
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

```
Tampilan HTML `register.html` juga dibuat untuk mengakomodasi form pendaftaran.

#### Login
Fungsi login menggunakan `AuthenticationForm` dan `login()` untuk memvalidasi kredensial pengguna. Jika valid, pengguna akan diarahkan ke halaman utama.

```python
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm

def login_user(request):
   if request.method == 'POST':
      form = AuthenticationForm(data=request.POST)

      if form is_valid():
        user = form.get_user()
        login(request, user)
        response = HttpResponseRedirect(reverse("main:show_main"))
        response.set_cookie('last_login', str(datetime.datetime.now()))
        return response

   else:
      form = AuthenticationForm(request)
   context = {'form': form}
   return render(request, 'login.html', context)
```

#### Logout
Fungsi logout menggunakan `logout()` untuk mengakhiri sesi pengguna dan menghapus informasi `last_login` dari cookies.

```python
from django.contrib.auth import logout

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response
```

### 2. Menghubungkan Model `Product` dengan `User`
Untuk menghubungkan model `Product` dengan `User`, kita perlu menggunakan `ForeignKey` di model `Product`. Hal ini memungkinkan setiap produk terkait dengan satu pengguna.

```python
from django.contrib.auth.models import User
from django.db import models

class Quran(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)  
    name = models.CharField(max_length=255)
    price = models.IntegerField(default=0)
```

Setelah itu, `Product` bisa difilter berdasarkan pengguna yang login untuk menampilkan hanya produk yang mereka buat.

```python
def show_main(request):
    quran_entries = Quran.objects.filter(user=request.user)
    context = {
        'Nama_Aplikasi' : "Ngaji Kuy",
        'name': request.user.username,
        'Class' : "PBP C",
        'quran_entries': quran_entries,
        'last_login': request.COOKIES['last_login'],
    }

    return render(request, "main.html", context)
```

### 3. Menampilkan Detail Pengguna yang Sedang Login dan Menggunakan Cookies
Informasi login terakhir dapat disimpan dalam cookies dengan menambahkan `last_login` saat pengguna berhasil login. Pada halaman utama, kita bisa menampilkan waktu login terakhir tersebut.

```python
from django.utils import timezone
from django.http import HttpResponseRedirect

def login_user(request):
   if request.method == 'POST':
      form = AuthenticationForm(data=request.POST)

      if form.is_valid():
        user = form.get_user()
        login(request, user)
        response = HttpResponseRedirect(reverse("main:show_main"))
        response.set_cookie('last_login', str(datetime.datetime.now()))
        return response

   else:
      form = AuthenticationForm(request)
   context = {'form': form}
   return render(request, 'login.html', context)
```

Pada halaman utama (`main.html`), tambahkan kode berikut untuk menampilkan waktu login terakhir:
```html
<h5>Sesi terakhir login: {{ last_login }}</h5>
```

### 4. Deployment ke PWS
Setelah mengimplementasikan aplikasi Django, langkah selanjutnya adalah melakukan deployment ke Pacil Web Service (PWS). Pastikan konfigurasi di `settings.py` sudah benar, dan tambahkan host `localhost` serta URL PWS ke `ALLOWED_HOSTS`.

```python
ALLOWED_HOSTS = ['localhost', '127.0.0.1', 'husin-hidayatul-ngajikuy.pbp.cs.ui.ac.id']
```


## Tugas 5

### 1. Urutan Prioritas CSS Selector

Pada CSS, prioritas selector menentukan aturan mana yang diterapkan jika terdapat beberapa selector untuk elemen yang sama. Urutan prioritas dari yang terendah hingga tertinggi adalah:

1. **Selector Tag (Elemen HTML):** Contoh `h1`, `p`, `div`.
2. **Selector Class:** Contoh `.class-name`.
3. **Selector Attribute dan Pseudo-class:** Contoh `[type="text"]`, `:hover`.
4. **Selector ID:** Contoh `#id-name`.
5. **Inline Style:** Gaya yang ditulis langsung pada elemen HTML, misalnya `style="color: blue;"`.
6. **Aturan dengan `!important`:** Contoh `color: red !important;`, memiliki prioritas tertinggi dan mengesampingkan aturan lainnya.

Jika ada konflik, selector dengan prioritas lebih tinggi akan diterapkan. Jika prioritasnya sama, selector yang ditulis terakhir dalam CSS akan digunakan.

---

### 2. Pentingnya Responsive Design

**Responsive design** penting karena memungkinkan tampilan dan fungsi website beradaptasi dengan berbagai ukuran layar dan perangkat, seperti desktop, tablet, dan smartphone. Ini memastikan pengalaman pengguna yang optimal tanpa memerlukan zoom atau scroll berlebihan.

**Contoh aplikasi yang sudah menerapkan responsive design:**

- **Google**
- **Tokopedia**
- **Tiket.com**

**Contoh aplikasi yang belum menerapkan responsive design:**

- **SiakNG**
- **Beberapa situs web lama yang tidak dioptimalkan untuk perangkat mobile**

---

### 3. Perbedaan Margin, Border, dan Padding

- **Margin:** Ruang di luar elemen yang memisahkan elemen tersebut dengan elemen lain.
  - **Implementasi:** `margin: 20px;` (mengatur margin di semua sisi).
  
- **Border:** Garis yang mengelilingi elemen, berada di antara margin dan padding.
  - **Implementasi:** `border: 2px solid black;` (mengatur ketebalan, jenis garis, dan warna).
  
- **Padding:** Ruang di dalam elemen antara konten dan border.
  - **Implementasi:** `padding: 10px;` (mengatur padding di semua sisi).

---

### 4. Konsep Flexbox dan Grid Layout

- **Flexbox (Flexible Box):**
  - **Definisi:** Metode layout satu dimensi dalam CSS untuk mengatur elemen secara fleksibel dalam baris atau kolom.
  - **Kegunaan:**
    - Memudahkan penataan dan alignment elemen secara horizontal atau vertikal.
    - Mengatur spacing dan distribusi ruang antar elemen.
  - **Contoh Implementasi:**

    ```css
    .flex-container {
      display: flex;
      flex-direction: row; /* atau column */
      justify-content: space-between;
      align-items: center;
    }
    ```

- **Grid Layout:**
  - **Definisi:** Sistem layout dua dimensi dalam CSS yang memungkinkan pengaturan elemen dalam baris dan kolom.
  - **Kegunaan:**
    - Membuat tata letak halaman yang kompleks dan terstruktur.
    - Mengatur ukuran dan posisi elemen dengan presisi.
  - **Contoh Implementasi:**

    ```css
    .grid-container {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      grid-gap: 10px;
    }
    ```

    

---
## 5. Implementasi Checklist Secara Step-by-Step

### a. Implementasi Fungsi Hapus dan Edit Product

Untuk menambahkan fitur mengedit dan menghapus produk, langkah-langkahnya adalah sebagai berikut:

1. **Menambahkan Method pada `views.py`:** Saya membuat method `edit_product` dan `delete_product` di `views.py` untuk mengelola logika edit dan hapus produk.
2. **Menambahkan Path pada `urls.py`:** Saya kemudian menambahkan routing atau path yang sesuai di `urls.py`, sehingga request untuk mengedit dan menghapus produk bisa diarahkan ke method yang tepat.
3. **Membuat Template Edit:** Saya membuat file `edit_quran.html` di dalam folder `main/templates` untuk mengatur tampilan halaman pengeditan produk.

### b. Kustomisasi Halaman Login, Register, dan Tambah Produk

Untuk membuat halaman login, register, dan tambah produk lebih menarik:

1. **Menggunakan Tailwind CSS:** Saya memanfaatkan framework Tailwind CSS untuk memberikan gaya yang menarik dan responsif pada halaman login, register, dan halaman tambah produk (`create_quran_entry.html`).
2. **Kustomisasi UI:** Saya fokus pada penggunaan komponen Tailwind yang modern dan minimalis, memastikan elemen-elemen UI teratur dan nyaman dilihat.

### c. Menampilkan Gambar dan Pesan Ketika Tidak Ada Produk Terdaftar

Agar halaman menampilkan gambar dan pesan saat tidak ada produk yang terdaftar:

1. **Mengecek Daftar Produk:** Saya menambahkan pengecekan di dalam template untuk memeriksa apakah terdapat produk yang terdaftar melalui `Quran.objects.filter(user=request.user)`.
2. **Menampilkan Gambar Default:** Jika tidak ada produk, saya menampilkan gambar default yang diambil dari folder `static` beserta pesan "Belum ada produk terdaftar" sebagai pengganti daftar produk.

### d. Menampilkan Daftar Produk dalam Bentuk Card

Jika ada produk yang tersimpan, maka halaman produk akan menampilkan produk-produk tersebut dalam bentuk card:

1. **Mengecek Daftar Produk:** Sama seperti sebelumnya, saya mengecek apakah terdapat produk yang disimpan menggunakan query `Quran.objects.filter(user=request.user)`.
2. **Menampilkan Produk dengan Card:** Jika ada produk, saya menampilkan detail setiap produk dalam bentuk card menggunakan template `card_quran.html`, yang saya desain sendiri.

### e. Menambahkan Tombol Edit dan Hapus pada Setiap Card Produk

Untuk setiap produk yang ditampilkan dalam card, saya menambahkan dua tombol:

1. **Implementasi Tombol:** Saya menambahkan tombol untuk mengedit dan menghapus produk, yang masing-masing terhubung dengan fungsi `edit_product` dan `delete_product`.


### f. Membuat Navigation Bar yang Responsif

Untuk membuat navbar yang responsif terhadap berbagai ukuran perangkat, terutama mobile dan desktop:

1. **Membuat `navbar.html`:** Saya membuat file `navbar.html` untuk menampilkan fitur-fitur utama aplikasi, seperti home, daftar produk, dan logout.
2. **Responsivitas:** Saya menambahkan kelas-kelas Tailwind untuk menampilkan tampilan yang berbeda pada perangkat mobile dengan menggunakan `<div class="mobile-menu hidden ...>`. Ini memastikan navbar bisa berubah tampilan ketika dilihat dari perangkat mobile, sehingga tetap mudah digunakan di berbagai ukuran layar.

---



## Tugas 6: Menjawab Pertanyaan Seputar CSS dan Responsive Design

### 1. Jelaskan manfaat dari penggunaan JavaScript dalam pengembangan aplikasi web!



1. **Interaktivitas yang Meningkat:** JavaScript memungkinkan pengembang untuk menambah elemen interaktif seperti animasi, pop-up, validasi formulir, dan pembaruan halaman secara real-time. Hal ini meningkatkan pengalaman pengguna secara keseluruhan dengan memberikan respon yang lebih cepat dan lebih baik terhadap aksi pengguna.

2. **Penggunaan AJAX untuk Responsif yang Lebih Baik:** Dengan AJAX (Asynchronous JavaScript and XML), JavaScript memungkinkan pengiriman dan penerimaan data dari server tanpa perlu me-refresh halaman. Ini membuat aplikasi lebih responsif, karena pengguna dapat melihat perubahan langsung di halaman tanpa perlu menunggu reload penuh.

3. **Kemampuan Manipulasi DOM (Document Object Model):** JavaScript dapat mengakses dan memanipulasi elemen HTML pada halaman web, sehingga memungkinkan pengembang untuk menambahkan, mengubah, atau menghapus elemen secara dinamis. Ini sangat berguna untuk membuat konten yang dapat diperbarui secara real-time berdasarkan tindakan pengguna.

4. **Framework dan Library Modern:** JavaScript adalah dasar dari banyak framework modern seperti React, Angular, dan Vue, yang memungkinkan pengembangan aplikasi web yang lebih kompleks dengan struktur yang terorganisir. Framework ini menyediakan komponen siap pakai dan mempercepat pengembangan dengan fitur-fitur tambahan seperti routing, state management, dan integrasi API.

5. **Kompatibilitas Lintas Platform:** JavaScript dapat dijalankan di berbagai browser dan perangkat, termasuk desktop, tablet, dan ponsel. Ini memungkinkan aplikasi yang ditulis dalam JavaScript untuk bekerja secara konsisten di berbagai platform tanpa perlu penyesuaian khusus.

### 2. Jelaskan fungsi dari penggunaan `await` ketika kita menggunakan `fetch()`! Apa yang akan terjadi jika kita tidak menggunakan `await`?


`await` digunakan untuk menunggu penyelesaian dari sebuah Promise sebelum melanjutkan eksekusi kode. Ketika `await` digunakan bersama dengan `fetch()`, ini memastikan bahwa aplikasi menunggu hingga respons dari server selesai sebelum melanjutkan ke langkah berikutnya.

Jika kita tidak menggunakan `await`, `fetch()` akan mengembalikan Promise yang belum selesai, dan kode akan terus berjalan tanpa menunggu respons dari server. Ini dapat menyebabkan error, terutama jika ada bagian kode yang bergantung pada data yang diperoleh dari `fetch()`. Misalnya, mencoba mengakses data dari server yang belum tersedia bisa menyebabkan error karena objek tersebut masih kosong.


### 3. Mengapa kita perlu menggunakan decorator `csrf_exempt` pada view yang akan digunakan untuk AJAX POST?


Dalam Django, setiap permintaan POST membutuhkan CSRF token untuk mencegah serangan Cross-Site Request Forgery (CSRF). CSRF adalah serangan di mana pengguna yang sah dimanipulasi untuk mengirim permintaan ke server tanpa sepengetahuan mereka.

Ketika kita mengirimkan permintaan AJAX POST, Django biasanya memerlukan CSRF token yang akan diverifikasi oleh server. Namun, untuk mempermudah pengembangan atau pengujian, kita dapat menonaktifkan pemeriksaan CSRF menggunakan decorator `csrf_exempt`.

Decorator `csrf_exempt` memberi tahu Django untuk mengabaikan pemeriksaan CSRF pada view tertentu. Meski demikian, sangat disarankan untuk tetap menyertakan CSRF token dalam permintaan AJAX POST guna menjaga keamanan aplikasi. Pada aplikasi produksi, CSRF token biasanya ditambahkan dalam header permintaan secara manual.

### 4. Pada tutorial PBP minggu ini, pembersihan data input pengguna dilakukan di belakang (backend) juga. Mengapa hal tersebut tidak dilakukan di frontend saja?


Pembersihan data input pengguna di backend sangat penting untuk memastikan keamanan dan validitas data yang diterima. Meskipun validasi di frontend bermanfaat untuk memberikan umpan balik cepat kepada pengguna, validasi backend adalah keharusan karena:

1. **Keamanan Data:** Validasi di frontend dapat dengan mudah diabaikan atau dimodifikasi oleh pengguna yang jahat, sehingga data yang tidak aman dapat dikirim ke server. Validasi di backend melindungi aplikasi dari serangan injeksi (seperti XSS dan SQL Injection) dengan memastikan data yang diterima aman.

2. **Konsistensi Validasi:** Backend memiliki kontrol penuh atas semua data yang diterima oleh server, tanpa memperhatikan dari mana data tersebut dikirim. Validasi di backend memastikan bahwa aturan dan kebijakan validasi diterapkan secara seragam, baik data dikirim dari frontend atau sumber lain.

3. **Menjaga Integritas Data:** Backend bertanggung jawab atas integritas data di database. Validasi backend membantu memastikan bahwa hanya data yang valid yang disimpan, sehingga mengurangi risiko kerusakan atau inkonsistensi data di dalam aplikasi.

Karena alasan ini, validasi backend tetap diperlukan meskipun validasi frontend juga dilakukan.

### 5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)!


#### 1. Menambahkan View untuk Menangani AJAX POST Request
- **Fungsi `add_quran_entry_ajax` di `views.py`**: Menyimpan data Quran baru yang diterima dari permintaan POST dengan validasi.
  ```python
  @login_required
  @require_POST
  def add_quran_entry_ajax(request):
      form = QuranForm(request.POST)
      if form.is_valid():
          quran_entry = form.save(commit=False)
          quran_entry.user = request.user
          quran_entry.save()
          # Mengembalikan data dalam format JSON
          return JsonResponse({'status': 'success'}, status=201)
      else:
          return JsonResponse({'status': 'error', 'errors': form.errors}, status=400)
  ```

#### 2. Memodifikasi Template `main.html` untuk Menggunakan AJAX GET
- **Menghapus `quran_entries` dari Context**: Data tidak lagi dikirim dari server; AJAX GET akan digunakan untuk mengambil data.
- **Menambahkan Script JavaScript untuk Mendapatkan Data dan Memperbarui Tampilan**:
  ```javascript
  async function getQuranEntries() {
      const response = await fetch("{% url 'main:show_json' %}");
      return response.json();
  }
  async function refreshQuranEntries() {
      const data = await getQuranEntries();
      // Proses dan tampilkan data di halaman
  }
  ```

#### 3. Membuat Modal untuk Menambahkan Quran Baru dengan AJAX POST
- **Menambahkan Tombol Modal dan Script untuk Membuka Modal**:
  ```html
  <button onclick="showModal()">Tambah Quran Baru</button>
  <div id="crudModal" class="modal hidden">
      <form id="quranEntryForm">
          <!-- Form Inputs -->
          <button type="submit">Simpan</button>
      </form>
  </div>
  ```
  ```javascript
  function showModal() { document.getElementById('crudModal').classList.remove('hidden'); }
  function hideModal() { document.getElementById('crudModal').classList.add('hidden'); }
  ```

#### 4. Mengimplementasikan Fungsi untuk Menambahkan Quran Baru Menggunakan AJAX POST
- **Menambahkan Event Listener dan Fungsi untuk Submit Data**:
  ```javascript
  document.getElementById('quranEntryForm').addEventListener('submit', function(event) {
      event.preventDefault();
      addQuranEntry();
  });
  function addQuranEntry() {
      fetch("{% url 'main:add_quran_entry_ajax' %}", {
          method: 'POST',
          body: new FormData(document.getElementById('quranEntryForm'))
      })
      .then(response => response.json())
      .then(data => {
          if (data.status === 'success') { refreshQuranEntries(); hideModal(); }
          else { alert('Error: ' + data.errors); }
      });
  }
  ```

#### 5. Pembersihan Data di Backend
- **Menambahkan `strip_tags` di `forms.py` untuk Pembersihan Input**:
  ```python
  from django.utils.html import strip_tags
  class QuranForm(forms.ModelForm):
      def clean_name(self):
          return strip_tags(self.cleaned_data["name"])
  ```

Dengan langkah-langkah ini, saya berhasil menerapkan AJAX GET dan POST, menjaga keamanan input, serta mengintegrasikan data secara asinkron tanpa perlu reload halaman.
