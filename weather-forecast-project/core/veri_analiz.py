
def veriAnalizi(ham_veri):
   anlik_temp = ham_veri["current"]["temp_c"]
   hava_metin= ham_veri["current"]["condition"]["text"]
   sehir= ham_veri["location"]["name"]
   rüzgar = ham_veri["current"]["wind_mph"]
   hava_icon=  ham_veri["current"]["condition"]["icon"]
   max_temp = ham_veri["forecast"]["forecastday"][0]["day"]["maxtemp_c"]
   min_temp = ham_veri["forecast"]["forecastday"][0]["day"]["mintemp_c"] 
   return {
    "sicaklik": anlik_temp,
    "aciklama": hava_metin,
    "sehir": sehir,
    "ruzgar": rüzgar,
    "icon": hava_icon,
    "max_sicaklik": max_temp,
    "min_sicaklik": min_temp,
}




        