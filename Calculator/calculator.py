import customtkinter as ctk

# 1. TEMA VE PENCERE AYARLARI
ctk.set_appearance_mode("dark")  # Karanlık tema
ctk.set_default_color_theme("blue")  # Buton renk teması

app = ctk.CTk()
app.title("Hesap Makinesi")
app.geometry("320x450")
app.resizable(False, False) # Pencere boyutu sabit kalsın

# 2. EKRAN (Giriş Kutusu)
# justify="right" ile sayıların sağdan yazılmasını sağlıyoruz
ekran = ctk.CTkEntry(app, font=("Helvetica", 36), justify="right", height=60)
ekran.grid(row=0, column=0, columnspan=4, padx=10, pady=20, sticky="ew")

# 3. FONKSİYONLAR (Arka Plan Mantığı)
def buton_tikla(deger):
    mevcut = ekran.get() # Ekrandaki mevcut metni al
    ekran.delete(0, ctk.END) # Ekranı temizle
    ekran.insert(0, str(mevcut) + str(deger)) # Eskinin yanına yeniyi ekle

def temizle():
    ekran.delete(0, ctk.END) # Tüm ekranı sil

def hesapla():
    try:
        # eval() string içindeki matematik işlemini otomatik yapar
        sonuc = eval(ekran.get())
        ekran.delete(0, ctk.END)
        ekran.insert(0, str(sonuc))
    except Exception:
        # Eğer hatalı bir işlem girilirse (örn: 5/0) Hata yazdır
        ekran.delete(0, ctk.END)
        ekran.insert(0, "Hata")

# 4. BUTONLARI YERLEŞTİRME (Grid Sistemi)
# (Buton Metni, Satır, Sütun)
butonlar = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('C', 4, 0), ('0', 4, 1), ('=', 4, 2), ('+', 4, 3)
]

for (text, row, col) in butonlar:
    if text == '=':
        btn = ctk.CTkButton(app, text=text, font=("Helvetica", 24), width=70, height=60, 
                            fg_color="#2FA572", hover_color="#107C41", command=hesapla)
    elif text == 'C':
        btn = ctk.CTkButton(app, text=text, font=("Helvetica", 24), width=70, height=60, 
                            fg_color="#D93025", hover_color="#A50E0E", command=temizle)
    else:
        # lambda kullanımı: Hangi butona basıldığını fonksiyona parametre olarak göndermek için
        btn = ctk.CTkButton(app, text=text, font=("Helvetica", 24), width=70, height=60, 
                            command=lambda t=text: buton_tikla(t))
    
    # Butonu ekrana yerleştir
    btn.grid(row=row, column=col, padx=5, pady=5)

# Uygulamayı başlat (Döngüyü çalıştır)
app.mainloop()