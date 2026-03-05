# 🛡️ Implementasi Algoritma RSA (Rivest-Shamir-Adleman) - From Scratch

Proyek ini adalah implementasi mandiri dari algoritma kriptografi asimetris **RSA** menggunakan bahasa pemrograman Python. Proyek ini dibuat untuk memenuhi tugas mata kuliah **Kriptografi**.

## 🧐 Logika & Alur Algoritma
Program ini mensimulasikan seluruh proses kriptografi mulai dari pembuatan kunci hingga pengembalian pesan asli tanpa menggunakan library eksternal.

### 1. Pembangkitan Kunci (Key Generation)
Berdasarkan parameter yang diatur dalam kode:
* **Bilangan Prima**: Dipilih dua bilangan prima $p = 61$ dan $q = 53$.
* **Modulus ($n$)**: Diperoleh dari $p \times q = 3233$. Nilai ini digunakan sebagai dasar untuk kunci publik dan privat.
* **Totient ($\phi$)**: Diperoleh dari $(p-1) \times (q-1) = 3120$.
* **Kunci Publik ($e$)**: Dipilih $e = 17$ (syarat: relatif prima dengan 3120).
* **Kunci Privat ($d$)**: Dihitung menggunakan *Extended Euclidean Algorithm* untuk mencari invers modular dari $e \pmod{\phi}$. Hasilnya adalah $d = 2753$.

### 2. Proses Enkripsi
Pesan asli (Plaintext) diubah menjadi kode rahasia (Ciphertext) menggunakan kunci publik.
* **Rumus**: $C = M^e \pmod{n}$
* **Contoh**: $42^{17} \pmod{3233} = 2557$.

### 3. Proses Dekripsi
Kode rahasia dikembalikan menjadi pesan asli menggunakan kunci privat.
* **Rumus**: $M = C^d \pmod{n}$
* **Contoh**: $2557^{2753} \pmod{3233} = 42$.

## 🛠️ Penjelasan Fungsi Kode
* `is_prime(n)`: Memastikan angka yang digunakan untuk kunci adalah bilangan prima.
* `gcd(a, b)`: Mencari FPB untuk memastikan validitas pemilihan kunci publik.
* `modular_inverse(e, phi)`: Inti dari algoritma yang menghitung kunci privat berdasarkan kunci publik dan nilai totient.
* `pow(base, exp, mod)`: Digunakan untuk menghitung perpangkatan besar dalam modulus secara efisien (Modular Exponentiation).

## 🚀 Cara Menjalankan
1. Pastikan Python 3.x sudah terinstal di komputer Anda.
2. Clone repositori ini atau simpan file sebagai `RSA.py`.
3. Jalankan melalui terminal:
   ```bash
   python RSA.py
