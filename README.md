# solana-base58-to-array
# biasanya kita menjumpai private keys berbasis base58 dalam wallet phantom , backpack atau sejenisnya
skrip ini berguna untuk mengubah private keys "solana" dari base58 menjadi array 
# Konverter Base58 ke Array Solana
Contoh
Berikut adalah contoh output saat Anda menjalankan skrip:

# contoh pk (Base58):
4mWt4K3Dy9vNcMHJ7p2Jz7AfujEn8qPtkTjzMyYsmw5B
# contoh pk (Array):
[123, 67, 89, 101, 234, 45, 203, 156, 255, 78, 0, 124, 210, 183, 43, 94, 91, 73, 146, 200, 211, 99, 54, 240, 179, 203, 178, 65, 33, 84, 92, 234, 101, 134, 97, 43, 176, 240, 90, 12, 130, 209, 56, 192, 145, 210, 76, 124, 179, 203, 45, 189, 76, 90, 212, 201, 78, 104, 170, 33, 98, 211, 210, 56]

Proyek ini mengonversi kunci pribadi Solana dari format Base58 ke format array dan sebaliknya. Proyek ini menggunakan variabel lingkungan untuk menangani data sensitif dengan aman dan diimplementasikan dalam Python

## Fitur
- Mengonversi kunci pribadi Solana dari Base58 ke Array.
- Penanganan data sensitif yang aman menggunakan `.env`.
- Mendukung implementasi dalam Python

## Persyaratan

Pastikan Anda memiliki yang berikut ini terinstal:
- Python 3.12.3 (atau lebih baru) jika menggunakan implementasi Python.
- `git` untuk kontrol versi.
  
Anda juga akan memerlukan pustaka berikut:
- Untuk Python:
  - `python-dotenv`
  - `base58`

## Instalasi

### 1. Kloning Repositori

Klon repositori ini ke mesin lokal Anda menggunakan Git:

```bash
git clone https://github.com/bactiar291/solana-base58-to-array.git
cd solana-base58-to-array
```

### 2. Jangan lupa untuk mengubah nano .env 

 BASE58_ENCODED_KEY=DIISI DENGAN PRIVATE KEYS BASE58 KALIAN

### 3.  Menginstal Dependensi
Untuk Python:
Jika Anda menggunakan implementasi Python, pertama-tama buat lingkungan virtual (opsional tetapi disarankan) dan instal pustaka yang diperlukan:

```bash
python -m venv venv 
source venv/bin/activate  
pip install -r requirements.txt
```


### 4. run atau jalankan 
```bash
python solana-pk.py
```
thank to ANAM BACTIAR 


# Lisensi
Proyek ini dilisensikan di bawah Lisensi MIT. Lihat file LICENSE untuk detail lebih

