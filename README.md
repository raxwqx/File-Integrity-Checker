# 🔐 File Integrity Checker

Basit ve hafif bir Python dosya bütünlüğü kontrol aracıdır.

Bu proje, dosyaların SHA256 hash değerlerini hesaplayarak dosya içeriğinin değişip değişmediğini kontrol etmeyi öğrenmek amacıyla geliştirilmiştir.

## ✨ Özellikler

- 🔐 SHA256 hash oluşturur
- 📁 Dosyaları binary modunda okur
- ⚡ Dosyayı küçük parçalar halinde işler
- 🔎 Dosyanın mevcut olup olmadığını kontrol eder
- 🐍 Python `hashlib` ve `os` modüllerini kullanır
- 🧪 Eğitim ve kontrollü lab ortamları için tasarlanmıştır

## 📋 Gereksinimler

- Python 3

Python sürümünü kontrol etmek için:

```bash
python3 --version
```

## 🚀 Kurulum

Projeyi GitHub'dan indirin:

```bash
git clone https://github.com/raxwqx/File-Integrity-Checker.git
```

Proje klasörüne girin:

```bash
cd File-Integrity-Checker
```

## ▶️ Kullanım

Programı çalıştırın:

```bash
python3 integrity_checker.py
```

Program sizden kontrol edilecek dosyanın yolunu ister:

```text
Kontrol edilecek dosyanın yolunu gir: test.txt
```

Dosya mevcutsa SHA256 hash değeri gösterilir:

```text
[+] Dosya bulundu.
[+] SHA256: ...
```

## 🧪 Örnek Test

Örnek bir dosya oluşturmak için:

```bash
echo "Merhaba Styx" > test.txt
```

Ardından programı çalıştırın:

```bash
python3 integrity_checker.py
```

Dosyanın içeriğini değiştirdiğinizde SHA256 hash değeri de değişir.

Örneğin:

```bash
echo "Dosya degisti" > test.txt
```

Programı tekrar çalıştırdığınızda farklı bir hash değeri elde edersiniz.

## 🧠 Nasıl Çalışır?

Program dosyayı binary modunda açar ve içeriğini 4096 byte'lık parçalar halinde okur.

Her parça SHA256 algoritmasına eklenir.

Dosyanın tamamı okunduktan sonra oluşan hash değeri ekrana yazdırılır.

Basit çalışma mantığı:

```text
Dosya
  ↓
Binary olarak oku
  ↓
4096 byte'lık parçalar
  ↓
SHA256 hesapla
  ↓
Hash değerini göster
```

## 📚 Öğrenme Konuları

Bu proje aşağıdaki konuları öğrenmek için hazırlanmıştır:

- SHA256
- Hash fonksiyonları
- Dosya bütünlüğü
- Python `hashlib`
- Python dosya işlemleri
- Binary dosya okuma
- Veri bütünlüğü

## ⚠️ Önemli Not

Bir dosyanın hash değerini daha sonra karşılaştırmak için güvenilir bir **referans hash** değerine ihtiyaç vardır.

Dosyanın hash'i değiştiğinde bu, dosya içeriğinin değişmiş olabileceğini gösterir. Hash tek başına değişikliğin nedenini açıklamaz.

## ⚠️ Yasal Uyarı

Bu proje eğitim, geliştirme ve kontrollü lab ortamlarında kullanılmak üzere hazırlanmıştır.

Yalnızca erişim izniniz bulunan dosyalar ve sistemler üzerinde kullanın.

## 📄 License

MIT License
