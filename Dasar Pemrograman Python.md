# Dasar Pemrograman Python

Penyusun **Rudy Eko Prasetya, S.Kom** - Blog [https://rudyekoprasetya.wordpress.com](https://rudyekoprasetya.wordpress.com)

![logo python](https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/200px-Python-logo-notext.svg.png)

Modul ini disusun untuk mempelajari bahasa pemrograman python secara mendasar serta mengenal algoritma dan pemrograman yang ditujukan bagi siswa atau mahasiswa informatika atau siapapun yang ingin belajar pemrograman

Modul ini dibuat menggunakan versi **python 3.9x** berdasarkan dokumentasi resmi python [https://docs.python.org/3/](https://docs.python.org/3/) yang dipersingkat agar mudah untuk dipraktekkan dan dipahami Silahkan menyesuaikan bila ada update mengenai versi terbaru.

Modul ini menggunakan lisensi [Creative Common](https://creativecommons.org/about/cclicenses/) dengan atribut NonKomersial-BerbagiRupa dimana Lisensi ini mengizinkan setiap orang untuk menggubah, memperbaiki, dan membuat ciptaan turunan bukan untuk kepentingan komersial, selama mereka mencantumkan kredit dan melisensikan ciptaan turunan dengan syarat yang serupa dengan ciptaan asli.

Modul ini dibuat dengan menggunakan [**Markdown**](https://www.markdownguide.org/basic-syntax/) dan akan terus di update seiring dengan pengalaman belajar dan mengajar penyusun. History perubahan atau pull request bisa di akses pada [https://github.com/rudyekoprasetya/belajar-python](https://github.com/rudyekoprasetya/belajar-python)

## Daftar Isi

- [Pengenalan](#pengenalan-bahasa-python)
- [Persiapan IDE (Integrated Development Environment)](#persiapan-ide)
- [Cara Penulisan Bahasa Python](#cara-penulisan-bahasa-python)
- [Variabel dan Tipe Data di Python](#variabel-dan-tipe-data)
- [Macam-macam Operator](#operator-di-python)
- [Mengenal Percabangan](#mengenal-percabangan)
- [Mengenal Perulangan](#mengenal-perulangan)
- [Mengenal Array](#mengenal-array)
- [Mengenal Function](#mengenal-function)
- [Mengenal Object Oriented Programming](#object-oriented-programming)
- [Daftar Referensi](#referensi)
- [Tentang Penyusun](#tentang)

## Pengenalan Bahasa Python

**Python** adalah bahasa pemrograman tingkat tinggi. Dibuat oleh Guido van Rossum dan pertama kali dirilis pada tahun 1991.

![Guido van Rossum](https://upload.wikimedia.org/wikipedia/commons/thumb/d/da/Guido-portrait-2014.jpg/290px-Guido-portrait-2014.jpg)

Python banyak digunakan untuk membuat berbagai macam program, seperti: program CLI, Program GUI (desktop), Aplikasi Mobile, Web, IoT, Game, Program untuk Hacking, dsb.

Python juga dikenal dengan bahasa pemrograman yang mudah dipelajari, karena struktur sintaknya rapi dan mudah dipahami. Sehingga cocok dipelajari bagi pemula yang belum pernah kenal coding.

Python memang sangat sederhana dibandingkan bahasa yang lainnya. Tidak perlu ini dan itu untuk membuat program memunculkan tulisan **Hello World!**. Coba bandingkan coding dibawah ini

ini adalah C++
```c++
#include<iostream>

main() {
	cout<<"Hello World!";
}
```

ini adalah Java
```java
class Hello{
	public static void main(String[] args) {
		System.out.println("Hello World!");
	}
}
```

Sedangkan ini adalah Python
```python
print("Hello World!")
```

Bahkan tagline di websitenya menjelaskan, kalau python akan membuat kita bekerja lebih cepat dan efektif.

> *Python is a programming language that lets you work quickly and integrate systems more effectively.*


## Persiapan IDE

Hal-hal yang harus dipersiapkan sebelum belajar Bahasa Pemrograman Python adalah

1. Install Python, silahkan download di [https://www.python.org/downloads/](https://www.python.org/downloads/) dan lakukan installasi pada sistem operasi anda
2. Install Code Editor bisa [Sublime-text](https://www.sublimetext.com/download) atau [VS Code](https://code.visualstudio.com/download)
3. Paham perintah dasar console / terminal / cmd. Silahkan merujuk [kesini](https://dev.to/kymiddleton/reference-guide-common-commands-for-terminal-6no)
4. Semangat Belajar Tinggi

Setelah itu untuk memulai menggunakan laravel. Buatlah suatu folder kerja, semisal **Documents/Belajar-python** dimana nantinya akan kita gunakan sebagai workspace atau letak semua file kita. 

Untuk cek apakah python sudah terinstall anda bisa membuka terminal, kemudian ketikan perintah

untuk windows
```console
$ py --version
```

untuk MacOS atau linux perintahnya 

```console
$ python --version
```

jika muncul versi python maka installasi sudah berhasil.

Didalam python terdapat **Mode interaktif** yang merupakan fasilitas/fitur yang disediakan oleh Python sebagai tempat menulis kode secara interaktif. Fitur ini dikenal juga dengan istilah *Shell, Console, REPL (Read–Eval–Print Loop) atau interpreter*.

Cara membuka mode interaktif adalah dengan mengetik perintah py pada terminal windows.

```console
$ py
Python 3.9.6 (tags/v3.9.6:db3ff76, Jun 28 2021, 15:26:21) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>>_
```

untuk linux/MacOS
```console
$ python
Python 3.9.6 (tags/v3.9.6:db3ff76, Jun 28 2021, 15:26:21) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>>_
```

Tanda `>>>`, artinya python siap menerima perintah. Cobalah tulis **print("Hello World")** kemudian tekan Enter. 

Untuk keluar dari mode interaktif tekan **Ctrl+C** atau ketik perintah **exit()**.

## Cara Penulisan Bahasa Python

Setiap bahasa pemrograman memiliki struktur penulisan yang berbeda-beda, begitu pula dengan python. **“Bagaimana kalau tidak dipathui?”** Resikonya bisa terjadi error.

Baik untuk praktek silahkan buat folder dengan nama **1-intro** dalam folder kerja yang sudah disiapkan. Kemudian buka folder tersebut dalam code editor anda. 

Selanjutnya buatlah file baru dengan nama **Main.py** dengan isi sebagai berikut

```python
#ini adalah komentar yang tidak ditampilkan saat eksekusi
print('Perkenalkan nama ku Python')
print('salam kenal')

print("meski ditulis lurus"); print("maka tulisan ini kan dibawah")
```

buka folder kerja anda didalam terminal atau console. Kemudian masuk kedalam folder *1 intro* dengan perintah

```console
$ cd 1-intro
```

kemudian kita jalankan perintah

```console
$ py Main.py
```

untuk linux/MacOS

```console
$ python Main.py
```

*Apakah yang akan Muncul??*

Penulisan satu statement dalam python tidak diakhiri dengan tanda titik-koma. Sedangkan, bila kita ingin menulis lebih dari satu statement dalam satu baris, maka kita harus memisahnya dengan titik-koma. 

*String* dalam pemrograman biasanya ditulis dengan dibungkus menggunakan tanda petik. Bisa menggunakan **tanda petik tunggal(' ') maupun ganda(" ")**.

Komentar merupakan baris kode yang tidak akan dieksekusi. Komentar digunakan untuk memberikan informasi tambahan dan untuk menonaktifkan kode. Ada beberapa cara menulis komentar pada pemrograman Python. Cara pertama menggunakan *tanda pagar (#)*. Cara ini paling sering digunakan. Selain untuk mengapit teks (string), tanda petik juga dapat digunakan untuk membuat komentar.

```python
#komentar satu barus dengan pagar

`Komentar banyak baris yang diapit dengan tanda petik`
```

Selanjutnya coba lakukan perubahan pada code Main.py seperti dibawah ini

```python
print('Perkenalkan nama ku Python')
print('salam kenal')

print('meski ditulis lurus');print('maka tulisan ini kan dibawah')

#Variable yang nilainya di inputkan user
nama = input('Masukan Nama Anda ')

print('Hello ',nama,' Selamat Belajar')
```

jalankan ulang code diatas dengan perintah

```console
$ py Main.py
```

untuk linux/MacOS

```console
$ python Main.py
```

Coba amatilah apa yang muncul.

code `nama` adalah variable(akan dibahas pada bab berikutnya) yang digunakan untuk menampung data input dari user, dimana code `input()` berfungsi untuk menangkap semua ketikan keyboard user.

### Latihan

1. Cobalah buat Program Python dengan nama file **biodata.py** Untuk menampilkan Biodata Anda dengan tampilan sebagai berikut

```console
+-------------------------------------+
|   Nama      |  Gender |    Alamat   |
+-------------------------------------+
|  Budi       |    L    |    Kediri   |
+-------------------------------------+
|  Susi       |    P    |    Malang   |
+-------------------------------------+
|  Rani       |    P    |    Yogya    |
+-------------------------------------+
|  Dodi       |    L    |    Nganjuk  |
+-------------------------------------+
```

2. Buatlah program untuk Kartu Ucapan Selamat Hari raya dengan nama file **ucapan.py** dimana nama akan di inputkan sendiri oleh user

berikut adalah contoh tampilannya

```console
Masukan Nama Anda : _Rudy Eko Prasetya_

+-------------------------------------+
|         Selamat Hari raya           |
|     Kepada Rudy Eko Prasetya        |
|     Mohon Maaf Lahir dan Batin      |
+-------------------------------------+
```

## Variabel dan Tipe Data

*Kamu pernah dengan istilah variabel??? mungkin kayak di matematika seperti ini*

> 5 + x = 10 berapakah nilai x?

x disitu adalah suatu variabel. Variabel merupakan suatu nilai yang isinya bisa berubah-ubah. kenapa koq berubah?? coba kasus diatas kita ubah menjadi berikut ini

> 6 + x = 10 berapakah nilai x?

*apakah nilai x masih 5???* **Variabel** adalah tempat kita menyimpan nilai sementara. Variabel akan ada selama program dijalankan. Namun kita juga bisa menghapusnya dari memori.

Aturan untuk penulisan variabel adalah
1. Nama variabel boleh diawali menggunakan huruf atau garis bawah (_), contoh: nama, _nama, namaKu, nama_variabel.
2. Tidak boleh ada spasi
3. Tidak boleh menggunakan karakter-karakter 
```console
! @ # $ % ^ & * ( ) +  - = { } [  ] : " ; ' < > ? , . / |
```
4. Tidak boleh menggunakan reserved words yang ada dalam python seperti *if, while, else, for, class* dst.

Coba buat folder baru dengan nama **2 Variable** didalamnya kita buat file **Main.py** berikut codenya

```python
#menuliskan variable dan operator di python
a = 20
b = 10
nama = "Rudy"

print('Nilai a =',a)
print('Nilai b =',b)
print('Nilai nama =',nama)
```

Buka console kemudian kita jalankan perintah

```console
$ cd 2 Variable
$ py Main.py
```

untuk linux/MacOS

```console
$ cd 2 Variable
$ python Main.py
```

*Apakah yang akan muncul??*

Coba ubah code diatas menjadi

```python
#menuliskan variable dan operator di python
a = 20
a = 5
b = 10
nama = "Rudy"

print('Nilai a =',a)
print('Nilai b =',b)
print('Nilai nama =',nama)
```

Coba jalankan ulang, apakah ada perubahan???

Setiap variabel memiliki **tipe data**, apakah merupakan angka bulat, angka pecahan, atau berupa karakter, dan sebagainya. Jadi, tipe data adalah pengelompokan data berdasarkan isi dan sifatnya. 

Tipe data dalam python bersifat *dynamic typing*. dimana kita tidak perlu mendefinisikan sebelumnya apakah tipe data yang akan digunakan. seperti halnya bahasa pemrograman C++ dimana kita harus mendefisikan dahulu tipe datanya.

tambahkan code berikut pada file **Main.py** di baris paling bawah

```python
a = 20
b = 10
nama = "Rudy"

print('Nilai a =',a)
print('Nilai b =',b)
print('Nilai nama =',nama)

#untuk mengetahui tipe data variabel a
print(type(a));
#untuk mengetahui tipe data variabel nama
print(type(nama));
```

dengan coding `type()` kita bisa mengetahui tipe data yang ada dalam suatu variable.

Secara umum, tipe data primitif dalam python dibagi menjadi tiga jenis:

1. **Tipe data angka**
   - `int`: bilangan bulat, contoh 32, 22, 12, 10, dst
   - `float`: bilangan pecahan, contoh 1.3, 4.2, 22.3 dst
2. **Tipe data teks/string**
   - `Char`: Karakter, contoh 'R'.
   - `String`: Kumpulan karakter, contoh "Rudy Eko Prasetya".
3. **Tipe data boolean**
   - hanya memiliki dua nilai yaitu **True** dan **False** atau **0 dan 1**. Penulisan True dan False, huruf pertamnya harus kapital dan tanpa tanda petik.

Meskipun Python telah otomatis mendeteksi tipe data yang tersimpan dalam variabel, tapi ada kalanya kita perlu melakukan konversi tipe data.

Untuk ujicoba silahkan buat file baru dengan nama **konversi.py**

```python
a = 5
b = 2
c = a / b

print(c)
```

Coba jalankan coding diatas dan amatilah.

Pembagian nilai a dan b menghasilkan 3 (integer/bulat). *Mengapa demikian?* Karena nilai a dan b bertipe integer, maka hasilnya pun berupa integer.

*Bagaimana agar hasilnya ada komanya?*

silahkan ubah code menjadi berikut

```python
a = 10
b = 3
c = float(a) / float(b)

print(c)
```

Coba jalankan dan perhatikan hasilnya

### Fungsi-fungsi untuk merubah tipe data
1. `int()` untuk mengubah menjadi integer;
2. `long()` untuk mengubah menjadi integer panjang;
3. `float()` untuk mengubah menjadi float;
4. `bool()` untuk mengubah menjadi boolean;
5. `chr()` untuk mengubah menjadi karakter;
6. `str()` untuk mengubah menjadi string.
7. `bin()` untuk mengubah menjadi bilangan Biner.
8. `hex()` untuk mengubah menjadi bilangan Heksadesimal.
9. `oct()` untuk mengubah menjadi bilangan okta.


## Operator di Python

Dalam Pemrograman tidak bisa terpisahkan dari matematika. *kenapa??* karena memang dasar ilmu komputer adalah matematika. Salah satunya adalah ilmu tentang operasi bilangan dan logika. Pada pemrograman, ini kita kenal dengan Operator. 

**Operator** adalah simbol-simbol yang digunakan untuk melakukan operasi terhadap suatu nilai dan variabel. Ada beberapa operator yang ada pada bahasa python.

Untuk praktek silahkan buat folder **3 Operator** kemudian buat file **Main.py**

```python
a = 20
b = 10

#Operator Aritmatika
print('a + b = ',a+b)
print('a - b = ',a-b)
print('a x b = ',a*b)
print('a : b = ',a/b)
print('a modulo b = ',a%b)
```

Coba jalankan dan amatilah. 

```console
$ cd 3 Operator
$ py Main.py
```

untuk linux/MacOS

```console
$ cd 3 Operator
$ python Main.py
```

**Operator aritmatika** merupakan operator untuk melakukan operasi aritmatika seperti penjumlahan, pengurangan, perkalian dan pembagian.

Operator berikutnya yang harus kamu ketahi adalah **operator penugasan atau assignment**. Operator ini adalah operator untuk memberikan tugas kepada variabel biasanya digunakan untuk mengisi nilai.

Coba buat coding dibawah dan jalankan

```python
a = 10

#operator Assignment
a += 5
a -= 5
a *= 5
a /= 5
print(a)
```

**Operator pembanding** adalah operator untuk membandingkan dua buah nilai. Hasil operasi dari operator ini akan menghasilkan nilai dengan tipe data boolean, yaitu *true (benar) dan false (salah)*. Berikut untuk prakteknya.

```python
a = 20
b = 10

#operator Pembanding hasilnya true and false atau 0 dan 1
print('a sama dengan b hasilnya ' , a == b);
print('a tidak sama dengan b hasilnya ' ,a != b);
print('a lebih dari b hasilnya ' ,a > b);
print('a kurang dari b hasilnya ' ,a < b);
print('a lebih dari sama dengan b hasilnya ' ,a >= b);
print('a kurang dari sama dengan b hasilnya ' ,a <= b);
```

**Operator logika** adalah operator untuk melakukan operasi logika seperti AND, OR, dan NOT ini akan menghasilkan nilai dengan tipe data boolean, yaitu *true (benar) dan false (salah)*. Berikut adalah contohnya

```python
a = 0
b = 1

#operator Logika
print('a AND b hasilnya ',a & b)
print('a OR b hasilnya ',a | b)
print('NOT b hasilnya ',not b)
```

**Operator ternary** juga dikenal dengan operator kondisi, karena digunakan untuk membuat sebuah ekspresi kondisi

> Kamu suka aku ? Ya : Tidak

Contohnya

```python
aku = (umur < 10) ? "bocah" : "dewasa"
print(aku)
```

Coba jalankan code diatas, *tulisan apakah yang muncul bocah atau dewasa?*

### Latihan

1. Buatlah program pyhton dengan nama file **latihanop1.py** dimana bisa perhitungan otomatis dengan python untuk mencari (pilih salah satu)
   - Volume Tabung
   - Volume Balok
   - Luas Kerucut
dimana nilai nilai input berasal dari user, berikut contohnya

```console
Masukan Panjangnya(cm) = _2_
Masukan Lebarnya(cm) = _3_
Masukan Tingginya(cm) = _1_

Maka Volume balok tersebut adalah 6  
```

2. Buatlah program python dengan nama file *latihanop2.py* untuk menentukan kelulusan suatu siswa dengan memasukan nilainya, dengan ketentuan lulus adalah lebih dari 70, berikut adalah contoh tampilannya

```console
Masukan nama Anda = _Rudy_
Masukan nilai Anda = _78_

Selamat Rudy Nilai anda masuk dalam kriteria LULUS
```

## Mengenal Percabangan

Kadangkala terdapat suatu kejadian yang baru akan dikerjakan jika suatu kondisi tertentu telah terpenuhi. Pemilihan yaitu instruksi yang dikerjakan dengan kondisi tertentu. 

**Percabangan** adalah Satu atau beberapa instruksi hanya dilaksanakan apabila kondisi bernilai benar, sebaliknya apabila salah maka instruksi tidak akan dilaksanakan. Contoh Algoritma percabangan adalah 

> Jika nilai diatas 75 maka dinyatakan Lulus Selain itu Remidi

Buatlah folder kerja dengan nama **3 Percabangan**, kemudian buat file dengan nama **Main.py** berikut codingnya

```python
nilai = input('Masukan Nilai Anda ')

if float(nilai) >= 75:
	print('Selamat Anda Lulus')
```

Penulisan blok program harus **ditambahkan indentasi (tab atau spasi 2x/4x)**.

Coba jalankan dan masukan nilai 80, amatilah apa yang keluar

Selanjutnya coba jalankan dan masukan nilai 60, *tulisan apakah yang muncul?*

Coba kita ubah codingnya menjadi

```python
nilai = input('Masukan Nilai Anda ')

if float(nilai) >= 75:
	print('Selamat Anda Lulus')
else:
	print('Maaf Anda Harus Remidi')
```

Coba jalankan lagi dan masukan nilai 60, amatilah hasilnya

Sekarang kita ubah code nya menjadi berikut

```python
nilai = input('Masukan nilai ')

if float(nilai) > 85:
	print('Nilai Anda A')
elif float(nilai) >= 75:
	print('Nilai Anda B')
else:
	print('Nilai Anda C')
```

Coba jalankan dan masukan nilai 80, *tulisan apa yang akan muncul?*

### Latihan

1. Buatlah program untuk menentukan nama nama hari berdasarkan angka yang di inputkan oleh user, contoh

```console
PROGRAM NAMA HARI

Pilihan 
1 = Senin
2 = Selasa
3 = Rabu
4 = Kamis
5 = Jumat
6 = Sabtu
7 = Minggu

Masukan pilihan [1 s/d 7] = __
```

2. Buatlah program untuk mencari diskon dari suatu pembelian barang dengan kondisi
   - Jika Pembelian diatas 100.000 dapat diskon 10%
   - Jika Pembelian diatas 50.000 diskon 5%
   - Selain itu tidak dapat diskon

Contoh

```console
Masukan Total Pembelian = _200000_
Diskon Anda = 20000
Total Bayar Anda = 180000
```

## Mengenal Perulangan

Pernahkah anda dihukum guru anda untuk menuliskan sebuah kalimat perjanjian tidak akan mengulangi perbuatan tidak baik sampai papan tulis tersebut penuh? Misalnya menulis:

```console
Saya Tidak akan datang terlambat lagi
Saya Tidak akan datang terlambat lagi
Saya Tidak akan datang terlambat lagi
Saya Tidak akan datang terlambat lagi
Saya Tidak akan datang terlambat lagi
....
....dst
```

Seperti yang bisa anda lihat diatas, kita diminta untuk menulis kalimat yang sama sebanyak (contoh: 100 kali). Tentunya hal ini menjadi pekerjaan yang melelahkan.

Kabar baiknya, kita bisa menggunakan fungsi perulangan atau looping. **Looping atau perulangan** adalah fungsi pada bahasa pemrograman untuk menjalankan baris kode secara berulang-ulang selama kondisi masih terpenuhi.

Terdapat dua jenis perualangan dalam bahasa pemrograman python, yaitu perulangan dengan **for dan while**.

### Perulangan FOR

Perulangan for disebut *counted loop (perulangan yang terhitung)*. perulangan for biasanya digunakan untuk mengulangi kode yang sudah diketahui banyak perulangannya.

Untuk uji coba Buatlah folder **4 Perulangan** didalamnya ada file **for.py**

```python
# perulangan for

for i in range(0,10):
	print("Saya Tidak akan datang terlambat lagi");
```

Coba jalankan coding diatas, *Tulisan apa yang muncul??*

variable `i` digunakan untuk menampung indeks, fungsi `range()`berfungsi untuk membuat list dengan range dari 0-10

Sekarang cobalah ubah coding menjadi dibawah ini

```python
# perulangan for

for i in range(0,10):
	print("Angka Ke - ", i);
```

Jika dijalankan, *tulisan apa yang akan muncul??*

### Perulangan WHILE

sementara perulangan while disebut *uncounted loop (perulangan yang tak terhitung)*. Perbedaannya dengan for yaitu while perulangan yang memiliki syarat dan tidak tentu berapa banyak perulangannya.

Masih dalam folder kerja yang sama buatlah file **while.py** dengan isi sebagai berikut

```python
# perulangan WHILE
jawab = 'ya'
hitung = 0

while(jawab == 'ya'):
    hitung += 1
    jawab = input("Ulang lagi ya/tidak? ")

print ("Total perulangan = ", hitung)
```

Coba jalankan coding diatas, perulangan akan terus dilakukan jika kita menjawab **ya**, dan akan berhenti dijawab selain itu.

Perulangan while bisa jua digunakan untuk membuat deret angka, semisal angka 1 s/d 10. Codingnya sebagai berikut

```python
angka = 0

while (angka <10):
	angka+=1
	print("Angka ke - ",angka)
```

### Latihan

1. Dengan menggunakan perulangan WHILE buatlah deret angka dari 10 s/d 1
2. Buatlah program dengan menggunakan perulangan FOR, untuk menampilkan deret angka genap dari 1 s/d 10
3. Buatlah program untuk mencari jumlah dari suatu deret angka bulat dimana batasnya ditentukan oleh user, berikut adalah contoh tampilannya

```console
Masukan Batas = _5_

Jumlah deret angka 1 s/d 5 adalah 15
```


## Mengenal Array

**Array** adalah salah satu struktur data yang berisi sekumpulan data dan memiliki indeks. Indeks digunakan untuk mengakses nilai array dan selalu dimulai dari *nol (0)*. Didalam python Array disebut sebagai **List**.

![ilustrasi list](https://rudyekoprasetya.files.wordpress.com/2020/03/array1.jpg?w=616)

Diatas adalah contoh data array. Jika kita ingin menampilkan data “Ani” maka kita akan memanggil indeks 0. 

Silahkan buat folder baru dengan nama **5 List** yang didalamnya ada file **Main.py**

```python
#membuat list
siswa = ['ani', 'budi', 'dodi', 'rudy']

# menampilkan list
print('array ke -0 adalah', siswa[0])

#menampilkan semua data list
for i in siswa:
	print ("Nama Siswa ", i)
```

Coba jalankan dan amati hasilnya

untuk menanipulasi elemen list coba tambahkan code berikut dibari bawah

```python
#membuat list
siswa = ['ani', 'budi', 'dodi', 'rudy']

# menampilkan list
print('array ke -0 adalah', siswa[0])

#menampilkan semua data list
for i in siswa:
	print ("Nama Siswa ", i)

# merubah data budi menjadi anton 
siswa[1] = "Anton"

for i in siswa:
	print ("Nama Siswa ", i)
```

Jalankan dan amati perbedaanya. Coding `siswa[1]` disini adalah menandakan list siswa pada indeks ke-1.

Kita bisa menambahkan elemen baru kedalam suatu array dengan coding `append(item)` 

Berikut adalah contohnya

```python
#membuat list
siswa = ['ani', 'budi', 'dodi', 'rudy']

baru = input('Masukan data siswa baru = ')

# menambah data di list
siswa.append(baru)

for i in siswa:
	print ("Nama Siswa ", i)
``` 

atau kita bisa menyisipkan data pada element tertentu dengan coding `inser(index,item)`

berikut contohnya

```python
#membuat list
siswa = ['ani', 'budi', 'dodi', 'rudy']

baru = input('Masukan data siswa baru = ')

# menambah data di list
siswa.append(baru)

for i in siswa:
	print ("Nama Siswa ", i)

# menambah data joni di index ke 2
siswa.insert(2, 'joni')

for i in siswa:
	print ("Nama Siswa ", i)
``` 

Coba jalankan dan amatilah perbedaanya

untuk menghapus elemen suatu list kita bisa gunakan perintah `remove(item)` atau `pop(indeks)` contohnya

```python
#membuat list
siswa = ['ani', 'budi', 'dodi', 'rudy']

#menghapus data ani
siswa.remove('ani')

# menghapus data indeks ke-2
siswa.pop(2)

for i in siswa:
	print ("Nama Siswa ", i)
```

Coba jalankan *nama siswa siapa saja yang masih ada?*

### Latihan

1. Buatlah List dengan elemen-elemen sebagai berikut

```console
data = ['huruf', 500, False, 'A']
```
Tuliskan perintah untuk menampilkan elemen 500

2. Buatlah program untuk mencatat data Task atau Tugas dimana tugas tersebut bisa ditambahkan dan di hapus jika sudah dikerjakan. Berikut adalah contoh tampilannya

```console
To Do Apps

Masukan Tugas _Tugas 3_

Daftar Tugas

Tugas 1
Tugas 2
Tugas 3

Hapus Tugas indeks ke - _2_

Tugas 1
Tugas 2
```

## Mengenal Function

**Function atau Fungsi** adalah sekumpulan intruksi yang dibungkus dalam sebuah blok sehingga code dapat digunakan ulang tanpa harus menulis ulang instruksi di dalamnya.

Tujuan dibuat function adalah
1. Memudahkan dalam mengembangkan program. Program dibagi menjadi beberapa subprogram kecil, sehingga hal ini menjadi kunci dalam pembuatan program terstruktur.
2. Menghemat ukuran program, karena beberapa perintah yang sama dan dijalankan beberapa kali dalam program dapat dijadikan satu kali saja dalam suatu function, kemudian function tersebut dapat dipanggil berulang kali.

Fungsi pada python dibuat dengan kata kunci `def`, lalu diikuti dengan nama fungsinya.

Untuk praktikum buatlah folder kerja **6 Function** didalamnya kita buat file **function1.py**

```python
# Membuat fungsi
def salam():
	print("Hallo Programmer, Salam Kenal")

# Memanggil fungi
salam()
salam()
```

Coba jalankan coding diatas, amatilah hasilnya

Coding diatas menggunakan fungsi tanpa paremeter. Supaya intruksi yang di dalam fungsi lebih dinamis, kita dapat menggunakan parameter untuk memasukkan sebuah nilai ke dalam fungsi. 

**Parameter** adalah variabel yang menampung nilai untuk diproses di dalam fungsi. Nilai tersebut akan diolah di dalam fungsi. 

buatlah file baru dengan nama **function2.py**

```python
# fungsi dengan parameter
def tambah(a,b):
	print("hasil pertambahannya adalah", a+b)

# memanggil fungsi dengan parameter
tambah(2,3)
tambah(4,4)
```

terkadang kita memerlukan fungsi yang mengembalikan suatu nilai untuk diolah pada blok program lain.

coba ubah kode pada file **function2.py** menjadi berikut ini

```python
# fungsi dengan nilai balik
def tambah(a,b):
	return a+b

# memanggil fungsi dengan parameter
hasil=tambah(4,4)

print("Hasil dari fungsi adalah ", hasil)
```

Pengembalian nilai dalam fungsi dapat menggunakan kata kunci `return`.

### Latihan

1. Buatlah program pyhton dengan nama file **latihan-function.py** dimana bisa perhitungan otomatis dengan python untuk mencari (pilih salah satu). 
   - Volume Tabung
   - Volume Balok
   - Luas Kerucut
dimana nilai nilai input berasal dari user, Gunakan function didalamnya

```console
Masukan Panjangnya(cm) = _2_
Masukan Lebarnya(cm) = _3_
Masukan Tingginya(cm) = _1_

Maka Volume balok tersebut adalah 6  
```

2. Dengan menggunakan Fungsi, Buatlah program untuk mencatat data Task atau Tugas dimana tugas tersebut bisa ditambahkan dan di hapus jika sudah dikerjakan. Berikut adalah contoh tampilannya

```console
ToDo Apps

1. Tampilkan Task
2. Tambah Task
3. Hapus Task
4. Keluar

Pilihan Anda [1 s/d 4] = __
```

## Object Oriented Programming

**OOP (Object Oriented Programming)** adalah suatu metode pemrograman yang berorientasi kepada objek. Tujuan dari OOP diciptakan adalah untuk mempermudah pengembangan program dengan cara mengikuti model yang telah ada di kehidupan sehari-hari. Jadi setiap bagian dari suatu permasalahan adalah objek.

Untuk mempermudah penjelasan perhatikan ilustrasi dibawah ini

![Ilustrasi OOP](https://rudyekoprasetya.files.wordpress.com/2020/04/oop1.jpg?w=300&h=150)

Coba jawab satu persatu pertanyaan diatas mengenai gambar tersebut
- **Apakah Nama Object ini ?** katakannya itu adalah Mobil. Mobil adalah sebuah objek. Pesawat itu sendiri terbentuk dari beberapa objek/class yang lebih kecil lagi seperti mesin, roda,  kursi, dll. 
- **Apa Warna Object ini?** Hijau. Itu adalah properties. properties merupakan ciri, atau atrbut yang melekat pada object/class
- **Apa yang harus dilakukan agar bisa jalan?** Mobil bisa berjalan jika diisi bensin, di starter dan diinjak pedal gas. Itulah namanya Event
- **Bagaimana Mobil Tersebut jalan?** Saat di start maka busi akan memantik perapian dan bensin akan turun ke mesin dan terjadilah pembakaran. Pembakaran akan menggerakan piston. Kemudian piston menggerakan komponen lain dan akhirnya mobil bisa jalan. Itu yang disebut sebagai method atau function.

Baik untuk praktikum buatlah folder **7 OOP** didalamnya ada file **Main.py** dengan coding berikut

```python
# Membuat Class
class kendaraan:

	#method utama dalam class
	def __init__(self, jenis, roda, warna):
		#membuat properti class
		self.jenis = jenis
		self.roda = roda
		self.warna = warna

	#method atau fungsi untuk class kendaraan
	def maju(self):
		print('kendaraan jenis', self.jenis , 'Bergerak maju')

	def mundur(self):
		print('kendaraan jenis', self.jenis , 'Bergerak mundur')

	def belok(self, arah):
		print('kendaraan jenis', self.jenis , 'Belok ke arah ',arah)

	def berhenti(self):
		print('kendaraan jenis', self.jenis , 'berhenti')

	def tampil(self):
		print('kendaraan jenis', self.jenis , 'Beroda', self.roda , 'dan memiliki warna', self.warna)
```

sebagai ilustrasi diatas dibuat class kendaraan dimana dia memiliki properti warna, jenis dan jumlah roda. Hal ini bisa dilihat pada coding `def __init__(self, jenis, roda, warna):`. Selain itu kendaraan tersebut bisa melakukan maju, mundur, berbelok, berhenti serta menampilkan informasi.

Kemudian tambahkan coding berikut di baris paling bawah pada file **Main.py** tadi

```python
# membuat instance object
sedan = kendaraan('sedan',4,'hitam')
motor = kendaraan('sepeda motor',2,'putih')

# memanggil fungsi dari instance object
sedan.tampil()
sedan.belok('kiri')
motor.tampil()
motor.maju()
motor.berhenti()
```

Coba jalankan dan amati hasilnya

variable sedan merupakan objek turunan dari class kendaraan secara otomatis dia mewarisi semua properti dan sifat class. Untuk mengakses properti, kita cukup gunakan `nama_objek.properti`. Object tersebut bisa pula memanggil fungsi didalamnya seperti `sedan.belok('kiri')` atau `motor.tampil()`

## Referensi

- [https://docs.python.org/3/](https://docs.python.org/3/)
- [https://www.petanikode.com/python-linux/](https://www.petanikode.com/python-linux/)
- [https://belajarpython.com/tutorial/object-class-python](https://belajarpython.com/tutorial/object-class-python)
- [https://id.wikipedia.org/wiki/Guido_van_Rossum](https://id.wikipedia.org/wiki/Guido_van_Rossum)
-[https://note.nkmk.me/en/python-list-clear-pop-remove-del/](https://note.nkmk.me/en/python-list-clear-pop-remove-del/)
- [https://rudyekoprasetya.wordpress.com/2020/04/20/belajar-javascript/](https://rudyekoprasetya.wordpress.com/2020/04/20/belajar-javascript/)
- [Modul Pemrograman Dasar C++, 2019, Rudy Eko Prasetya](https://drive.google.com/open?id=1vyXPSMO_LFOWQqQ-6EdylB4CKUN4GHhe)

## Tentang

![Profil Rudy](https://rudyekoprasetya.files.wordpress.com/2009/10/mine.jpg?w=138)

Syahdan, Seorang anak laki-laki.. lahir di Tulungagung 02 Desember 1990 tepatnya hari minggu wage, Anak pertama dan terakhir ayah ibu dan ingin sekali belajar sampai ke negara seberang.. (semoga bisa ya…). Kehidupan dimulai saat pendidikan dimulai.. ibu selalu mendidik untuk selalu berbuat baik dan jangan sampai menyakiti hati orang lain, dari TK , SD Ngadirejo 1, dan SMP Negeri 1 di kediri jawa timur, (Bagaimana klo SMA..??) saya ndak pernah SMA, dulu bercita-cita jadi dokter namun saya urungkan, karena kondisi ekonomi orang tua yang tidak mendukung, akhirnya saya banting setir putar haluan ke SMK, Saya Lulusan SMK Negeri 1 Kediri (kediri juga..??) . Namun Tuhan itu adil, impian untuk menjadi dokter akhirnya di wujudkan (Loohhh koq bisa..??) karena saya jadi dokter komputer, saya mengambil jurusan Teknik Komputer Jaringan. dan Alhamdulillah Lulus di Tahun 2009.

Setelah menuntut ilmu, saya mencoba untuk mengamalkannya… lulus dari SMK saya berkeinginnan untuk kuliah, namun tetap berhadapan dengan masalah klasik, yaitu uang, namun klo ada kemauan pasti ada jalan, alhamdulilah saya bekerja disalah satu toko komputer di kediri, dan berkat itu pula saya bisa mendaftar kuliah PTS dikediri, yaitu Universitas Nusantara PGRI. Banyak hal yang bisa dipetik dalam menghadapi kuliah dan kerja ini, khususnya dalam membagi waktu dan perasaan. Sedikit kesulitan pada Tahun Pertama Alhamdulillah bisa diatasi.

Setelah belajar, Mengamalkan, kemudian ada jalan untuk menyampaikan kepada orang lain. Tepatnya September 2010 saya mengajar, meski masih anak bawang dalam dunia pendidikan  namun ndak ada salahnya dicoba, karena belajar yang baik itu adalah belajar untuk menyampaikan ilmu kepada orang lain. Fokus pembelajaran dan riset saya adalah *web development (frontend dan backend), Android Development, Linux SysAdmin, AI (Artificial Intelligent) dan lagi gandrung jua dengan IoT (internet Of Things)*

