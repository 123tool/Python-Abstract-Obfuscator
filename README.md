# 🛡️ Python Abstract Obfuscator

**Alat enkripsi kode Python tingkat lanjut yang dirancang untuk melindungi kekayaan intelektual (Source Code) dari pencurian, plagiarisme, dan reverse engineering.**

## 💎 Fitur Unggulan
- **Marshal Bytecode Serialization**: Mengubah kode Python menjadi instruksi biner tingkat rendah.
- **XOR & Bit-Shift Encryption**: Mengenkripsi data biner sehingga tidak bisa di-decode dengan base64 biasa.
- **Triple-Layer Encoding**: Menggunakan algoritma Base16, Base32, dan Base64 secara berurutan.
- **Payload Reversal**: Membalikkan urutan string payload untuk mengecoh deteksi otomatis.
- **Dynamic Variable Injection**: Setiap hasil enkripsi menghasilkan nama variabel acak yang unik.
- **Memory Execution**: Kode dijalankan langsung di RAM tanpa membuat file temporary.

## 📥 Instalasi

### Windows / Linux / MacOS
Pastikan Python 3.x sudah terinstal.
```bash
# Clone repository
git clone [https://github.com/123tool/Python-Abstract-Obfuscator.git](https://github.com/123tool/Python-Abstract-Obfuscator.git)

# Masuk ke direktori
cd Python-Abstract-Obfuscator

# Jalankan alat
python abstract_obfuscator.py

