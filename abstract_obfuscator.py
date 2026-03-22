import base64
import zlib
import marshal
import random
import string
import os
import sys
import time

class PythonAbstractPro:
    def __init__(self):
        self.version = "2.5.0-GOLD"
        self.author = "Byexe"
        self.header = f"# Obfuscated by Python Abstract Obfuscator {self.version}\n# Author: {self.author}\n# Time: {time.ctime()}\n"

    def _generate_junk_name(self, length=25):
        """Menghasilkan nama variabel/kelas acak yang sangat panjang."""
        chars = string.ascii_lowercase
        return "".join(random.choice(chars) for _ in range(length)) + "__"

    def _transform_bytes(self, data, key):
        """Manipulasi byte tingkat rendah menggunakan XOR dan bit-shifting."""
        return bytes([(b ^ key | (b << 2 & 0xFF)) & 0xFF for b in data])

    def build(self, source_code):
        # Tahap 1: Kompilasi ke Bytecode (Marshal)
        # Ini mengubah teks kode menjadi instruksi mesin Python (bukan teks lagi)
        try:
            compiled = compile(source_code, '<string>', 'exec')
            marshalled = marshal.dumps(compiled)
        except Exception as e:
            return f"Error Kompilasi: {e}"

        # Tahap 2: Enkripsi & Transformasi Biner
        key = random.randint(50, 200)
        encrypted_bytes = self._transform_bytes(marshalled, key)

        # Tahap 3: Kompresi Berlapis
        compressed = zlib.compress(encrypted_bytes, level=9)

        # Tahap 4: Encoding Multi-Level (Base16 -> Base32 -> Base64 -> Reverse)
        b16 = base64.b16encode(compressed)
        b32 = base64.b32encode(b16)
        b64 = base64.b64encode(b32).decode()
        
        # Reverse String (Membalikkan urutan karakter)
        final_payload = b64[::-1]

        # Tahap 5: Pembuatan Loader (Dekriptor Otomatis)
        v_class = self._generate_junk_name(20) + "protector"
        v_data = self._generate_junk_name(15)
        v_key = self._generate_junk_name(10)
        v_output = self._generate_junk_name(12)

        # Template loader yang akan menjalankan kode di memori
        template = f"""{self.header}
class {v_class}:
    def __init__(self, data, key):
        self.d = data
        self.k = key
    def _execute(self):
        import base64, zlib, marshal
        try:
            # Reversing layers
            p = self.d[::-1].encode()
            p = base64.b64decode(p)
            p = base64.b32decode(p)
            p = base64.b16decode(p)
            p = zlib.decompress(p)
            # Reversing bit-shift logic
            p = bytes([(b ^ self.k) & 0xFF for b in p])
            exec(marshal.loads(p), globals())
        except Exception as e:
            print("Integrity Check Failed: " + str(e))

{v_data} = "{final_payload}"
{v_key} = {key}
{v_class}({v_data}, {v_key})._execute()
"""
        return template

def main():
    obfus = PythonAbstractPro()
    print(f"--- Python Abstract Obfuscator {obfus.version} ---")
    file_path = input("[?] Masukkan nama file (contoh: script.py): ")

    if not os.path.exists(file_path):
        print("[!] File tidak ditemukan!")
        return

    with open(file_path, 'r', encoding='utf-8') as f:
        code = f.read()

    print("[*] Sedang memproses enkripsi abstrak...")
    result = obfus.build(code)

    output_file = "dist_" + os.path.basename(file_path)
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(result)

    print(f"[+] Selesai! File disimpan di: {output_file}")

if __name__ == "__main__":
    main()
