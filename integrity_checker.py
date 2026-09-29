import hashlib
import os

file_path = input("Kontrol edilecek dosyanın yolunu gir: ")

if not os.path.isfile(file_path):
    print("[-] Dosya bulunamadı.")
    exit()

sha256 = hashlib.sha256()

with open(file_path, "rb") as file:
    while chunk := file.read(4096):
        sha256.update(chunk)

print("\n[+] Dosya bulundu.")
print(f"[+] SHA256: {sha256.hexdigest()}")
