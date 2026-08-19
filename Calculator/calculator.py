import customtkinter as ctk


ctk.set_appearance_mode("dark")  
ctk.set_default_color_theme("blue")  
app = ctk.CTk()
app.title("Hesap Makinesi")
app.geometry("320x450")
app.resizable(False, False) 


ekran = ctk.CTkEntry(app, font=("Helvetica", 36), justify="right", height=60)
ekran.grid(row=0, column=0, columnspan=4, padx=10, pady=20, sticky="ew")


def buton_tikla(deger):
    mevcut = ekran.get() 
    ekran.delete(0, ctk.END) 
    ekran.insert(0, str(mevcut) + str(deger)) 

def temizle():
    ekran.delete(0, ctk.END) 

def hesapla():
    try:
       
        sonuc = eval(ekran.get())
        ekran.delete(0, ctk.END)
        ekran.insert(0, str(sonuc))
    except Exception:
       
        ekran.delete(0, ctk.END)
        ekran.insert(0, "Hata")


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
       
        btn = ctk.CTkButton(app, text=text, font=("Helvetica", 24), width=70, height=60, 
                            command=lambda t=text: buton_tikla(t))
    

    btn.grid(row=row, column=col, padx=5, pady=5)

)
app.mainloop()
