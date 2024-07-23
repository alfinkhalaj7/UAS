def divide_numbers(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Error: Pembagian oleh nol tidak diizinkan!")
    else:
        print(f"Hasil pembagian {a} oleh {b} adalah {result}")
    finally:
        print("Eksekusi blok finally selesai.")

# Contoh pemanggilan fungsi dengan penanganan exception
divide_numbers(10, 2)  # Output: Hasil pembagian 10 oleh 2 adalah 5.0 Eksekusi blok finally selesai.
divide_numbers(10, 0)  # Output: Error: Pembagian oleh nol tidak diizinkan! Eksekusi blok finally selesai.
