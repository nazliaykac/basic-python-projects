import datetime
from os import name



class person:
    def __init__(self, name, surname, hesapNo, girisSifre,bakiye=0,paraYatirma=0,paraCekme=0):
        self.name = name
        self.surname = surname
        self.hesapNo = hesapNo
        self.girisSifre = girisSifre
        self.bakiye = bakiye
        self.paraYatirma = paraYatirma
        self.paraCekme = paraCekme


print("Bankamıza Hoşgeldiniz")

p1=person("Ahmet", "Yılmaz", 123456, 156153, bakiye=1000)
print ("Lütfen Giriş Yapınız")
inputgirisSifre = int(input("Giriş Şifrenizi Giriniz: "))
if inputgirisSifre == p1.girisSifre:
    print("Giriş Başarılı")
    print ("1-Para Yatırma\n2-Para Çekme\n3-Bakiye Sorgulama\n4-Çıkış")
    inputislem = int(input("Yapmak İstediğiniz İşlemi Seçiniz: "))
    if inputislem == 1:
        print("Güncel Bakiye:", p1.bakiye)
        print("Yatırmak İstediğiniz Tutarı Giriniz")
        inputparaYatirma = int(input("Tutar: "))
        p1.bakiye=p1.bakiye+inputparaYatirma
        print("Güncel Bakiye:", p1.bakiye)
    elif inputislem == 2:
        print("Güncel Bakiye:", p1.bakiye)
        print("Çekmek İstediğiniz Tutarı Giriniz")
        inputparaCekme=int(input("Tutar: "))
        p1.bakiye=p1.bakiye-inputparaCekme
        print("Güncel Bakiye:", p1.bakiye)
    elif inputislem == 3:
        print("Güncel Bakiye:",p1.bakiye)
    elif inputislem == 4:
        print("Çıkış Yapılıyor...")
        exit()
    else:
        print("Hatalı İşlem Seçimi")
else:
    print("Hatalı Giriş Şifresi")





