from os import getenv
from dotenv import load_dotenv
from mssql_python import connect

load_dotenv()

class VeriTabani:
    def __init__(self):
        
        self.conn_string = getenv("SQL_CONNECTION_STRING")

    def bağlanti_olustur(self):
        
        return connect(self.conn_string)

    def favoriSehirEkle(self, sehir_adi):
        sehir_adi = sehir_adi.title()
        try:
            baglanti = self.bağlanti_olustur()
            imlec = baglanti.cursor()
            
            sorgu = "INSERT INTO FavoriSehirler (SehirAdi) VALUES (?)"
           
            imlec.execute(sorgu, (sehir_adi,))
            baglanti.commit()
            
            print(f" {sehir_adi} başarıyla favorilere eklendi!")
            
        except Exception as e:
            hata_mesaji = str(e)
           
            if "UNIQUE" in hata_mesaji or "Violation" in hata_mesaji:
                print(f"ℹ️ {sehir_adi} zaten favorilerinde bulunuyor.")
            else:
                print(f" Veritabanı hatası oluştu: {e}")
        finally:
            if 'baglanti' in locals():
                baglanti.close()

    def favorileriGetir(self):
        try:
            baglanti = self.bağlanti_olustur()
            imlec = baglanti.cursor()
            
            sorgu = "SELECT SehirAdi FROM FavoriSehirler"
            imlec.execute(sorgu)
            
            satirlar = imlec.fetchall()
            
           
            favoriler = [satir[0] for satir in satirlar]
            return favoriler
            
        except Exception as e:
            print(f" Veri okuma hatası: {e}")
            return []
        finally:
            if 'baglanti' in locals():
                baglanti.close()