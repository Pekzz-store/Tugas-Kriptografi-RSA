import random

# 1. Fungsi untuk mengecek bilangan prima
def is_prime(n):
    if n < 2: return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0: return False
    return True

# 2. Algoritma Euclidean untuk mencari FPB (GCD)
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# 3. Extended Euclidean Algorithm untuk mencari Modular Inversed
def modular_inverse(e, phi):
    d_old, d_new = 0, 1
    r_old, r_new = phi, e
    while r_new != 0:
        quotient = r_old // r_new
        d_old, d_new = d_new, d_old - quotient * d_new
        r_old, r_new = r_new, r_old - quotient * r_new
    return d_old % phi

# --- PROSES UTAMA ---

# Pilih dua bilangan prima (kecil saja untuk demonstrasi)
p = 61
q = 53
n = p * q
phi = (p-1) * (q-1)

# Pilih e yang relatif prima dengan phi
e = 17 
d = modular_inverse(e, phi)

print(f"Kunci Publik: (e={e}, n={n})")
print(f"Kunci Privat: (d={d}, n={n})")

# Pesan (Plaintext)
message = 42
print(f"\nPlaintext: {message}")

# Enkripsi: C = (M^e) % n
ciphertext = pow(message, e, n)
print(f"Ciphertext (setelah enkripsi): {ciphertext}")

# Dekripsi: M = (C^d) % n
decrypted_msg = pow(ciphertext, d, n)
print(f"Plaintext (setelah dekripsi): {decrypted_msg}")