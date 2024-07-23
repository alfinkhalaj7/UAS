import tkinter as tk
from tkinter import messagebox

# Fungsi untuk menampilkan pesan saat tombol ditekan
def show_message():
    messagebox.showinfo("Info", "Halo! Ini adalah pesan dari tombol.")

# Membuat jendela utama
root = tk.Tk()
root.title("Contoh GUI dengan Tkinter")

# Membuat tombol di dalam jendela
button = tk.Button(root, text="Klik Saya", command=show_message)
button.pack(pady=20)

# Menjalankan event loop untuk menjaga jendela tetap terbuka
root.mainloop()
