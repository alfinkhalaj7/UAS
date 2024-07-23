print(f"Function (Fungsi)")
def greet(name):
    # Fungsi ini menyapa pengguna berdasarkan nama yang diberikan
    print(f"Hello, {name}!")

greet("Alfin")
greet("Bob")

print(f"                   ")
print(f"Recursive (Rekursi)")
def factorial(n):
    # Fungsi rekursif untuk menghitung faktorial dari n
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

result = factorial(5)
print("Factorial of 5 is:", result)
