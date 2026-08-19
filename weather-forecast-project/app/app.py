import  tkinter as tk
from core.veri_analiz import veriAnaliz
from core.veri_cekme import havaDurumu 



window=tk.Tk()


metin=tk.Label(text="Hava Durumu Bilgisi",
               foreground="Yellow",
               background="black",
               width=30,
               height=5)
metin.pack()


buton1=tk.Button(
    text="Hava Durumu Sorgula",
    background="Black",
    foreground="Yellow",
    width=30,
    height=5
)
buton1.pack()































window.mainloop()