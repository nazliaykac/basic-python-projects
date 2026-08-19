class Kitap:
    def __init__(self, kitapİsim, KitapYazar, BasimYili, KitapNo):
        self.kitapİsim = kitapİsim
        self.KitapYazar = KitapYazar
        self.BasimYili = BasimYili
        self.KitapNo = KitapNo
        self.Durum = "Rafta"

class Kullanici:
    def __init__(self, KullaniciAd, KullaniciSoyad, KullaniciNo):
        self.KullaniciAd = KullaniciAd
        self.KullaniciSoyad = KullaniciSoyad
        self.KullaniciNo = KullaniciNo
        self.OduncKitap = []

class Kutuphane:
    def __init__(self, TümKitaplar):
        self.TümKitaplar = TümKitaplar
        self.TümÜyeler = []
        
    
    def KitapEkle(self, KitapAd, KitapYazar, BasimYil, KitapNo):
        
        yeni_Kitap = Kitap(KitapAd, KitapYazar, BasimYil, KitapNo)
        
        
        self.TümKitaplar.append(yeni_Kitap)
        print(f"{KitapAd} kütüphaneye başarıyla eklendi...")

    def KitapSil(self, KitapAdi):
        kitap_bulundu_mu = False
        
        
        for kitap in self.TümKitaplar:
            if kitap.kitapİsim == KitapAdi:
                self.TümKitaplar.remove(kitap) 
                print(f"{KitapAdi} adlı kitap kütüphaneden silindi.")
                kitap_bulundu_mu = True
                break
                
        if kitap_bulundu_mu == False:
            print("Hata: Silmek istediğiniz kitap kütüphanede bulunamadı!")