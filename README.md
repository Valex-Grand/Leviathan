# 🌊 Leviathan: İleri Seviye Dosya Parçalama ve Şifreleme Sistemi

<p align="center">
  <img src="https://raw.githubusercontent.com/abhisheknaiidu/awesome-github-profile-readme/master/assets/cyberpunk.gif" width="700">
</p>

**Leviathan**, verileri sadece şifrelemekle kalmayan, aynı zamanda onları atomik parçalara ayırarak güvenliği fiziksel ve mantıksal bir boyuta taşıyan **Rust** tabanlı bir güvenlik motorudur.

---

### 🛠️ Çalışma Mantığı (Mimarisi)

Leviathan, klasik şifreleme yöntemlerinden farklı olarak **"Parçalı Depolama"** mantığını kullanır:

1.  **Parçalama (Fragmentation):** Dosya, belirlenen algoritmaya göre 100 veya daha fazla parçaya bölünür.
2.  **Şifreleme (Encryption):** Her bir parça, birbirinden bağımsız kriptografik anahtarlarla şifrelenir.
3.  **Dağıtım (Distribution):** Parçalar sistem içinde farklı dizinlere veya katmanlara dağıtılır.
4.  **Bütünlük (Integrity Check):** Parçaların tamamı ve doğru anahtar olmadan dosya asla birleştirilemez.

---

### 🚀 Öne Çıkan Özellikler

*   **🦀 Rust Gücü:** Bellek güvenliği (memory safety) ve yüksek performans.
*   **🛡️ Katmanlı Güvenlik:** Tek bir anahtarın ele geçirilmesi, dosyanın tamamına erişim sağlamaz.
*   **⚡ Düşük Kaynak Tüketimi:** Minimum RAM ve CPU kullanımı ile büyük dosyaları işleme kapasitesi.
*   **⏱️ Hız:** Zero-cost abstraction sayesinde milisaniyeler içinde parçalama.

---

### 📦 Kurulum ve Kullanım
```bash
# Depoyu klonlayın
git clone [https://github.com/Valex-Grand/Leviathan.git](https://github.com/Valex-Grand/Leviathan.git)

# Proje dizinine gidin
cd Leviathan

# Gerekli kütüphaneleri kurun
pip install -r requirements.txt

# Çalıştırın
python3 leviathan.py
