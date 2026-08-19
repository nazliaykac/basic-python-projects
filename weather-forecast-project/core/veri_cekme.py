

import requests
import os
from dotenv import load_dotenv, find_dotenv #.env dosyasındaki api keyimi import etmek için

load_dotenv()# .env dosyasını okur, içindeki değerleri ortam değişkeni yapar



class havaDurumu:
    def __init__(self):
        self.apiUrl="http://api.weatherapi.com/v1"
        self.apiKey=os.getenv("WEATHER_API_KEY")

    def getHavaDurumu (self,Sehir):
        hedef_url=f"{self.apiUrl}/current.json"

        parametreler={
           "key": self.apiKey,
           "q": Sehir,
            "lang":"tr", 
       }
        try:
            response = requests.get(url=hedef_url, params=parametreler)
        except requests.exceptions.RequestException as e:#requests ile ilgili herhangi bir hata
            print(f"Bağlantı hatası: {e}")
            return None

        if response.status_code == 200:
            data = response.json()  # ham metni 
            
            return data
        else:
            print("Hatalı giden bir şeyler var...")
            print(response.status_code)
            return None
        
    def getGelecekHava(self,sehir,gunSayisi):
        hedef_url=f"{self.apiUrl}/forecast.json"
        parametreler={
            "key":self.apiKey,
            "q":sehir,
            "dt":gunSayisi,
            "lang":"tr",
        }
        try:
            response = requests.get(url=hedef_url, params=parametreler)
        except requests.exceptions.RequestException as e:
            print(f"Bağlantı hatası: {e}")
            return None
        
        if response.status_code == 200:
            data = response.json()  # ham metni 
        
            return data
        else:
            print("Hatalı giden bir şeyler var...")
            print(response.status_code)
            return None









 
    
        

