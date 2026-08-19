import random

pcSkor = 0
oyuncuSkor = 0

while True:
    print("\n--- Yeni Tur ---")
    print("Oyuna Hoşgeldiniz seçim yapınız:")
    secim = ['t', 'k', 'm']
    oyuncuSecim = input("Taş, Kağıt, Makas (t/k/m) - Çıkmak için 'q' tuşlayınız: ")

    
    if oyuncuSecim == 'q' or oyuncuSecim == 'Q': 
        print("Oyundan Çıkılıyor...")
        break

    
    if oyuncuSecim != 't' and oyuncuSecim != 'k' and oyuncuSecim != 'm':
        print("Geçersiz işlem tuşu! Lütfen sadece t, k veya m giriniz.")
        continue 

    
    pcSecim = random.choice(secim)
    print(f"Bilgisayarın seçimi: {pcSecim}")

    if oyuncuSecim == 't' and pcSecim == 'k':
        print("PC oyunu kazandı")
        pcSkor += 1
        print(f"Toplam skor: PC {pcSkor} - Sen {oyuncuSkor}")
        
    elif oyuncuSecim == 'k' and pcSecim == 't':
        print("Oyuncu oyunu kazandı")
        oyuncuSkor += 1
        print(f"Toplam skor: PC {pcSkor} - Sen {oyuncuSkor}")
        
    elif oyuncuSecim == 'm' and pcSecim == 't':
        print("PC Oyunu kazandı")
        pcSkor += 1
        print(f"Toplam skor: PC {pcSkor} - Sen {oyuncuSkor}")
        
    elif oyuncuSecim == 't' and pcSecim == 'm':
        print("Oyuncu oyunu kazandı")
        oyuncuSkor += 1
        print(f"Toplam skor: PC {pcSkor} - Sen {oyuncuSkor}")
        
    elif oyuncuSecim == 'm' and pcSecim == 'k':
        print("Oyuncu oyunu kazandı")
        oyuncuSkor += 1
        print(f"Toplam skor: PC {pcSkor} - Sen {oyuncuSkor}")
        
    elif oyuncuSecim == 'k' and pcSecim == 'm':
        
        print("PC Oyunu kazandı") 
        pcSkor += 1
        print(f"Toplam skor: PC {pcSkor} - Sen {oyuncuSkor}")
        
    elif oyuncuSecim == pcSecim:
        print("Berabere")
        print(f"Toplam skor: PC {pcSkor} - Sen {oyuncuSkor}")