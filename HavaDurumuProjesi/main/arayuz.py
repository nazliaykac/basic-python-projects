import tkinter as tk
from tkinter import ttk, messagebox
import urllib.request
 
from veri_cekme import HavaDurumu
from veriTabani import VeriTabani
 
 
class HavaDurumuUygulamasi:
    """Ana pencereyi ve tüm widget'ları yöneten sınıf."""
 
    def __init__(self, pencere):
        self.pencere = pencere
        self.pencere.title("Hava Durumu Uygulaması")
        self.pencere.geometry("520x680")
        self.pencere.configure(bg="#eef2f7")
        self.pencere.resizable(False, False)
 
        
        self.hava_servisi = HavaDurumu()
        self.db = VeriTabani()
 
        
        self._resimler = {}
 
        self._stil_ayarla()
        self._arama_bolumu_olustur()
        self._sonuc_karti_olustur()
        self._tahmin_bolumu_olustur()
        self._favori_bolumu_olustur()
 
        self._favorileri_yenile()
 
   
    def _stil_ayarla(self):
        stil = ttk.Style()
        stil.theme_use("clam")
        stil.configure("TButton", font=("Segoe UI", 10), padding=6)
        stil.configure("Baslik.TLabel", font=("Segoe UI", 20, "bold"), background="#eef2f7")
        stil.configure("Alt.TLabel", font=("Segoe UI", 11), background="#eef2f7")
 
    
 
    def _arama_bolumu_olustur(self):
        cerceve = tk.Frame(self.pencere, bg="#eef2f7")
        cerceve.pack(pady=(20, 10), padx=20, fill="x")
 
        baslik = ttk.Label(cerceve, text="Hava Durumu", style="Baslik.TLabel")
        baslik.pack(anchor="w")
 
        arama_cercevesi = tk.Frame(cerceve, bg="#eef2f7")
        arama_cercevesi.pack(fill="x", pady=(15, 0))
 
        self.sehir_giris = ttk.Entry(arama_cercevesi, font=("Segoe UI", 12))
        self.sehir_giris.pack(side="left", fill="x", expand=True, ipady=5)
        self.sehir_giris.insert(0, "Şehir adı girin (örn. İstanbul)")
        self.sehir_giris.bind("<FocusIn>", self._placeholder_temizle)
        self.sehir_giris.bind("<Return>", lambda e: self._hava_durumu_sorgula())
 
        ara_buton = ttk.Button(arama_cercevesi, text="Ara", command=self._hava_durumu_sorgula)
        ara_buton.pack(side="left", padx=(8, 0))
 
    def _placeholder_temizle(self, event):
        if self.sehir_giris.get().startswith("Şehir adı"):
            self.sehir_giris.delete(0, "end")
 
  
    def _sonuc_karti_olustur(self):
        self.kart = tk.Frame(self.pencere, bg="#ffffff")
        self.kart.pack(padx=20, pady=10, fill="x")
 
        ust_satir = tk.Frame(self.kart, bg="#ffffff")
        ust_satir.pack(fill="x", padx=20, pady=(15, 0))
 
       
        yazi_alani = tk.Frame(ust_satir, bg="#ffffff")
        yazi_alani.pack(side="left", fill="both", expand=True)
 
        self.sehir_etiket = ttk.Label(yazi_alani, text="—", font=("Segoe UI", 16, "bold"), background="#ffffff")
        self.sehir_etiket.pack(anchor="w")
 
        self.sicaklik_etiket = ttk.Label(yazi_alani, text="", font=("Segoe UI", 32, "bold"), background="#ffffff")
        self.sicaklik_etiket.pack(anchor="w")
 
        self.durum_etiket = ttk.Label(yazi_alani, text="", font=("Segoe UI", 12), background="#ffffff")
        self.durum_etiket.pack(anchor="w")
 
       
        self.ikon_etiket = ttk.Label(ust_satir, background="#ffffff")
        self.ikon_etiket.pack(side="right", padx=(10, 0))
 
        self.ruzgar_etiket = ttk.Label(self.kart, text="Rüzgar: —", background="#ffffff")
        self.ruzgar_etiket.pack(anchor="w", padx=20, pady=(5, 0))
 
        self.favori_ekle_buton = ttk.Button(
            self.kart, text="★ Favorilere Ekle", command=self._favorilere_ekle, state="disabled"
        )
        self.favori_ekle_buton.pack(padx=20, pady=15, anchor="w")
 
    def _tahmin_bolumu_olustur(self):
        cerceve = tk.Frame(self.pencere, bg="#eef2f7")
        cerceve.pack(padx=22, pady=(0, 12), fill="x")
 
        ttk.Label(cerceve, text="3 Günlük Tahmin", style="Alt.TLabel").pack(anchor="w")
 
        self.tahmin_cercevesi = tk.Frame(cerceve, bg="#eef2f7")
        self.tahmin_cercevesi.pack(fill="x", pady=(10, 0))
 
       
        self.tahmin_kartlari = []
        for i in range(3):
            mini_kart = tk.Frame(self.tahmin_cercevesi, bg="#ffffff", width=150, height=110)
            mini_kart.pack(side="left", padx=(0, 10) if i < 2 else 0, fill="both", expand=True)
            mini_kart.pack_propagate(False)
 
            tarih_lbl = ttk.Label(mini_kart, text="—", background="#ffffff", font=("Segoe UI", 9, "bold"))
            tarih_lbl.pack(pady=(8, 0))
 
            ikon_lbl = ttk.Label(mini_kart, background="#ffffff")
            ikon_lbl.pack()
 
            sicaklik_lbl = ttk.Label(mini_kart, text="—", background="#ffffff", font=("Segoe UI", 10))
            sicaklik_lbl.pack()
 
            durum_lbl = ttk.Label(mini_kart, text="", background="#ffffff", font=("Segoe UI", 8))
            durum_lbl.pack()
 
            self.tahmin_kartlari.append({
                "tarih": tarih_lbl, "ikon": ikon_lbl, "sicaklik": sicaklik_lbl, "durum": durum_lbl
            })
 
   
    def _favori_bolumu_olustur(self):
        cerceve = tk.Frame(self.pencere, bg="#eef2f7")
        cerceve.pack(padx=20, pady=(10, 20), fill="both", expand=True)
 
        ttk.Label(cerceve, text="Favori Şehirler", style="Alt.TLabel").pack(anchor="w")
 
        liste_cercevesi = tk.Frame(cerceve, bg="#eef2f7")
        liste_cercevesi.pack(fill="both", expand=True, pady=(8, 0))
 
        self.favori_listesi = tk.Listbox(
            liste_cercevesi, font=("Segoe UI", 11), height=6,
            bg="#ffffff", bd=0, highlightthickness=1, highlightbackground="#d0d7de"
        )
        self.favori_listesi.pack(side="left", fill="both", expand=True)
        self.favori_listesi.bind("<Double-Button-1>", self._favoriden_sorgula)
 
        kaydirma_cubugu = ttk.Scrollbar(liste_cercevesi, orient="vertical", command=self.favori_listesi.yview)
        kaydirma_cubugu.pack(side="right", fill="y")
        self.favori_listesi.configure(yscrollcommand=kaydirma_cubugu.set)
 
    
    def _ikon_indir(self, icon_url, anahtar):
        """
        weatherapi.com ikon URL'leri '//cdn.weatherapi.com/...png' şeklinde,
        başında 'https:' yok. Onu ekleyip görseli indiriyoruz.
        anahtar: aynı ikonu tekrar indirmemek / referansını saklamak için.
        """
        if not icon_url:
            return None
        try:
            tam_url = icon_url if icon_url.startswith("http") else f"https:{icon_url}"
            with urllib.request.urlopen(tam_url, timeout=5) as yanit:
                veri = yanit.read()
            resim = tk.PhotoImage(data=veri)
            self._resimler[anahtar] = resim 
            return resim
        except Exception:
            
            return None
 
   
    def _hava_durumu_sorgula(self):
        sehir = self.sehir_giris.get().strip()
 
        if not sehir or sehir.startswith("Şehir adı"):
            messagebox.showwarning("Uyarı", "Lütfen bir şehir adı girin.")
            return
 
        veri = self.hava_servisi.havaDurumuGetir(sehir)
 
        if veri is None:
            
            messagebox.showinfo("Sonuç Yok", f"'{sehir}' için veri bulunamadı.")
            return
 
        
        self.sehir_etiket.config(text=veri["sehir"])
        self.sicaklik_etiket.config(text=f"{veri['sicaklik']}°C")
        self.durum_etiket.config(text=veri["durum"])
        self.ruzgar_etiket.config(text=f"Rüzgar: {veri['ruzgar']} km/s")
 
        resim = self._ikon_indir(veri.get("icon"), "anlik_ikon")
        self.ikon_etiket.config(image=resim if resim else "")
 
        self.favori_ekle_buton.config(state="normal")
        self._son_sorgulanan_sehir = sehir
 
        
        self._tahmini_guncelle(sehir)
 
    def _tahmini_guncelle(self, sehir):
        tahminler = self.hava_servisi.tahminiHavaDurumu(sehir, 3)
 
        if not tahminler:
            for kart in self.tahmin_kartlari:
                kart["tarih"].config(text="—")
                kart["sicaklik"].config(text="—")
                kart["durum"].config(text="")
                kart["ikon"].config(image="")
            return
 
        for i, gunluk in enumerate(tahminler[:3]):
            kart = self.tahmin_kartlari[i]
            kart["tarih"].config(text=gunluk["tarih"])
            kart["sicaklik"].config(text=f"{gunluk['min_sicaklik']}° / {gunluk['max_sicaklik']}°")
            kart["durum"].config(text=gunluk["durum"])
 
            resim = self._ikon_indir(gunluk.get("icon"), f"tahmin_ikon_{i}")
            kart["ikon"].config(image=resim if resim else "")
 
    def _favorilere_ekle(self):
        sehir = getattr(self, "_son_sorgulanan_sehir", None)
        if not sehir:
            return
 
        
        self.db.favoriSehirEkle(sehir)
        self._favorileri_yenile()
 
    def _favorileri_yenile(self):
        self.favori_listesi.delete(0, "end")
 
        sehirler = self.db.favorileriGetir()
 
        if not sehirler:
            self.favori_listesi.insert("end", "Henüz favori şehir yok.")
            return
 
        for sehir in sehirler:
            self.favori_listesi.insert("end", sehir)
 
    def _favoriden_sorgula(self, event):
        secim = self.favori_listesi.curselection()
        if not secim:
            return
        sehir = self.favori_listesi.get(secim[0])
        if sehir == "Henüz favori şehir yok.":
            return
        self.sehir_giris.delete(0, "end")
        self.sehir_giris.insert(0, sehir)
        self._hava_durumu_sorgula()
 
 
if __name__ == "__main__":
    pencere = tk.Tk()
    uygulama = HavaDurumuUygulamasi(pencere)
    pencere.mainloop()