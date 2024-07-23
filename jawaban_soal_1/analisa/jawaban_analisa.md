## Fungsi (Function) :
Fungsi dalam Python adalah blok kode yang dapat dipanggil untuk menyelesaikan tugas tertentu. Fungsi membantu dalam mengorganisir kode, mengurangi duplikasi, dan membuat kode lebih mudah dipahami dan diatur. Berikut adalah beberapa poin penting tentang fungsi di Python:

#### 1. Deklarasi Fungsi:
Fungsi dideklarasikan menggunakan kata kunci def, diikuti dengan nama fungsi dan parameter (jika ada), dan diakhiri dengan blok kode yang diberi indentasi.

#### 2. Pemanggilan Fungsi:
Fungsi dipanggil dengan menuliskan nama fungsi diikuti dengan tanda kurung dan argumen yang sesuai (jika ada).


## Rekursi (Recursion) di Python:
Rekursi adalah teknik di mana fungsi memanggil dirinya sendiri untuk menyelesaikan tugas. Dalam Python, rekursi sering digunakan untuk menyelesaikan masalah yang dapat dipisahkan menjadi kasus yang lebih kecil, yang sering kali memiliki struktur yang mirip.

#### 1. Struktur Rekursif:
Rekursi biasanya terdiri dari dua bagian: kasus dasar (base case) dan kasus rekursif.

    Base Case: Kasus yang tidak memerlukan rekursi dan menghentikan pemanggilan berulang.

    Kasus Rekursif: Bagian dari fungsi yang memanggil dirinya sendiri dengan argumen yang berbeda untuk mendekati base case.

#### 2. Keuntungan dan Keterbatasan Rekursi:

Keuntungan: Memecahkan masalah secara elegan ketika strukturnya cocok dengan rekursi.
Keterbatasan: Memiliki overhead tambahan untuk memanggil fungsi dan dapat mengakibatkan runtime error (recursion depth exceeded) jika tidak diimplementasikan dengan hati-hati.
