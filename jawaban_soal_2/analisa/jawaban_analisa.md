## Exception Handling (Penanganan Pengecualian):

Exception Handling adalah teknik dalam pemrograman untuk menangani situasi atau kondisi yang tidak terduga atau diluar kendali (exceptions) yang dapat terjadi selama eksekusi program. Tujuan utama dari exception handling adalah untuk mencegah program mengalami kegagalan atau crash ketika terjadi kesalahan atau kondisi yang tidak diharapkan, serta memberikan cara untuk mengelola dan merespons kejadian-kejadian tersebut dengan baik.

### Komponen-Komponen Exception Handling dalam Python:

#### Try Block:

Blok kode yang berpotensi menimbulkan pengecualian ditempatkan di dalam blok try.
Python akan mengeksekusi blok try secara normal. Jika tidak terjadi pengecualian, maka blok except akan dilewati.

#### Except Block:

Blok except digunakan untuk menangkap dan menangani pengecualian yang terjadi di dalam blok try.
Anda dapat menentukan jenis pengecualian tertentu yang ingin ditangkap, atau menggunakan except Exception untuk menangkap semua jenis pengecualian.

#### Finally Block:

    Opsional, blok finally dapat digunakan untuk menentukan kode yang akan dijalankan selalu, baik pengecualian terjadi atau tidak.

    Digunakan untuk membersihkan sumber daya atau menyelesaikan tindakan tertentu, misalnya menutup file atau koneksi database.

#### Keuntungan Penggunaan Exception Handling:

    Mencegah Program Crash: Exception handling memungkinkan program untuk tetap berjalan meskipun terjadi kesalahan atau kondisi tidak terduga.

    Keselamatan Data: Memastikan data terlindungi dan aplikasi dapat beroperasi dengan aman bahkan dalam kondisi tidak ideal.