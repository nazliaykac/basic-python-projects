from veriTabani import VeriTabani

def veritabani_testi():
    print("--- Veritabanı Testi Başlıyor ---\n")
    
    # Veritabanı nesnesini oluştur
    db = VeriTabani()
    
    print(">> 1. Aşama: Yeni Şehirler Ekleme")
    db.favoriSehirEkle("Ankara")
    db.favoriSehirEkle("İzmir")
    
    print("\n>> 2. Aşama: Çift Kayıt Kontrolü (UNIQUE Testi)")
    db.favoriSehirEkle("Ankara")
    
    print("\n>> 3. Aşama: Veritabanından Şehirleri Okuma")
    kayitli_sehirler = db.favorileriGetir()
    
    if kayitli_sehirler:
        print(f"Veritabanından Gelen Favoriler: {kayitli_sehirler}")
    else:
        print("Uyarı: Favori listeniz boş veya veritabanından okunamadı.")
        
    print("\n--- Test Tamamlandı ---")

if __name__ == "__main__":
    veritabani_testi()