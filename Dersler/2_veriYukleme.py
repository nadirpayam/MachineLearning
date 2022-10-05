
#kütüphaneler
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#kodlar
#veri yükleme

veriler = pd.read_csv('veriler.txt') #çift tek tırnak farketmez, bu fonksiyonla verileri okuyabiliyoruz
#parantez içerisinde dosyanın adını yazıyoruz
#csv verilerin arasında virgül olması durumunda kullanıyor, txt dosyamızda veriler arasında virgül şeklinde yazılmıştır

print(veriler)


#veri ön işleme

boy =veriler[['boy']] #boy kolonunu aldık
print(boy)

boykilo=veriler[['boy','kilo']]
print(boykilo)