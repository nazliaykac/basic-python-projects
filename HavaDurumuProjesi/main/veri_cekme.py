import requests 
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv()

class HavaDurumu:
    def __init__(self):
        self.apiUrl = "http://api.weatherapi.com/v1"
        self.apiKey = os.getenv("WEATHER_API_KEY")
        
    def havaDurumuGetir(self, sehir):
        hedef_url = f"{self.apiUrl}/current.json"
        parametreler = {
            "key": self.apiKey,
            "q": sehir,
            "lang": "tr"
        }
        
        
        ham_veri = self.istekYarat(hedef_url, parametreler)
        
        #Eğer veri geldiyse, ayıklayıcı metoda gönder temiz halini döndürür
        if ham_veri is not None:
            return self.veriAyikla(ham_veri)
        
        return None # Veri gelmediyse (hata varsa) None döndür

    def tahminiHavaDurumu(self, sehir, gun):
        hedef_url = f"{self.apiUrl}/forecast.json" 
        parametreler = {
            "q": sehir,
            "key": self.apiKey,
            "days": gun,
            "lang": "tr"
        }
        
       
        ham_veri = self.istekYarat(hedef_url, parametreler)
        
        
        if ham_veri is not None:
            return self.tahminAyikla(ham_veri)
            
        return None

    def veriAyikla(self, hamVeri):
        temiz_veri = {
            "sehir": hamVeri["location"]["name"],
            "sicaklik": hamVeri["current"]["temp_c"],
            "durum": hamVeri["current"]["condition"]["text"],
            "icon": hamVeri["current"]["condition"]["icon"],
            "ruzgar": hamVeri["current"]["wind_kph"]
        }
        return temiz_veri   
        
    def tahminAyikla(self, hamVeri):
        temiz_tahminler = []
        gunler = hamVeri["forecast"]["forecastday"]
        for gun in gunler:
            gunluk_veri = {
                "tarih": gun["date"],
                "max_sicaklik": gun["day"]["maxtemp_c"],
                "min_sicaklik": gun["day"]["mintemp_c"],
                "durum": gun["day"]["condition"]["text"],
                "icon": gun["day"]["condition"]["icon"]
            }
            temiz_tahminler.append(gunluk_veri)
            
        return temiz_tahminler

    
    def istekYarat(self, url, parametreler):
        try:
            response = requests.get(url=url, params=parametreler)
            
            if response.status_code == 200:
                return response.json() 
                
            elif response.status_code == 400:
                print("Hata: Girdiğiniz şehir bulunamadı. Lütfen yazımı kontrol edip tekrar deneyin.")
                return None
                
            else:
                print(f"Beklenmeyen bir API hatası! Hata Kodu: {response.status_code}")
                return None
                
        except requests.exceptions.RequestException as e:
            print(f" Bağlantı hatası oluştu: {e}")
            return None

        
