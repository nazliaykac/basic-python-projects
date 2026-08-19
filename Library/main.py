from Kütüphane_class import Kitap, Kullanici, Kutuphane
kitap1 = Kitap("Dune", "Frank Herbert", "1965", "101")
kitap2 = Kitap("1984", "George Orwell", "1949", "102")
kitap3 = Kitap("Yüzüklerin Efendisi", "J.R.R. Tolkien", "1954", "103")
kitap4 = Kitap("Simyacı", "Paulo Coelho", "1988", "104")
kitap5 = Kitap("Suç ve Ceza", "Dostoyevski", "1866", "105")

# 2. Bu ürettiğimiz kitapları bir listenin (array) içine topluyoruz
hazir_kitaplar = [kitap1, kitap2, kitap3, kitap4, kitap5]

# 3. Kütüphaneyi kurarken bu listeyi içeri (TümKitaplar parametresine) gönderiyoruz
Kutup1 = Kutuphane(hazir_kitaplar)


aktifKullanici=None

print("--- Kütüphaneye Hoşgeldiniz ---")


giris = input("Lütfen giriş yapınız veya kaydolunuz (1- Giriş, 2- Kaydol): ")

if giris == "2":
    print("\nBilgilerinizi Giriniz:")
    KullaniciAd = input("Adınız: ")
    KullaniciSoyad = input("Soyadınız: ")
    KullaniciNo = input("Kullanıcı Numaranız: ")

    yeniOlanKullanici = Kullanici(KullaniciAd, KullaniciSoyad, KullaniciNo)
    Kutup1.TümÜyeler.append(yeniOlanKullanici)
    print("Kayıt Başarılı!")
    aktifKullanici=yeniOlanKullanici

elif giris == "1":
    print("\nGiriş Kullanıcı numaranızı giriniz.")
    ArananNo = input("Kullanıcı Numarası: ") 
    
    giris_basarili_mi = False
    
    for uye in Kutup1.TümÜyeler:
        
        if uye.KullaniciNo == ArananNo:
           print(f"Sisteme Hoşgeldiniz, {uye.KullaniciAd} {uye.KullaniciSoyad}!")
           giris_basarili_mi = True
           aktifKullanici=uye
           break
           
    
    if giris_basarili_mi == False:
         print("Hata: Bu numaraya ait bir kayıt bulunamadı!")

else:
    print("Hatalı tuşlama yaptınız!")


if aktifKullanici != None:
    while True:
        print("\n--- İŞLEMLER MENÜSÜ ---")
        print("1- Kitap Ekle")
        print("2- Kitap Sil")
        print("3- Tüm Kitapları Listele")
        print("4- Çıkış Yap")
        
        secim = input("Ne yapmak istersiniz? : ")
        if secim=="1":
           Kutup1.KitapEkle()
        elif secim=="2":
            Kutuphane.KitapSil()
        elif secim=="3":
            hazir_kitaplar()


  