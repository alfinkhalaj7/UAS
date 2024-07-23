import sqlite3

# Membuat koneksi ke database
conn = sqlite3.connect('example.db')

# Membuat cursor untuk mengeksekusi perintah SQL
cursor = conn.cursor()

# Membuat tabel 'user' jika belum ada
cursor.execute('''CREATE TABLE IF NOT EXISTS user
                (Id INTEGER PRIMARY KEY, name TEXT NOT NULL, age INTEGER)''')

# Memasukkan data ke dalam tabel
cursor.execute("INSERT INTO user (name, age) VALUES (?, ?)", ('Alfin', 19))
cursor.execute("INSERT INTO user (name, age) VALUES (?, ?)", ('Bob', 20))

# Commit perubahan ke database
conn.commit()

# Membaca data dari tabel
cursor.execute('SELECT * FROM user')
rows = cursor.fetchall()

# Menampilkan data hasil query
for row in rows:
    print(row)

# Menutup koneksi dan cursor
cursor.close()
conn.close()
