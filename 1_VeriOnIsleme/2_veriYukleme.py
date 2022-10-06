
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

#kısaca oop'ye değinelim

class insan:
    boy = 180
    def kosmak(self,b): #paramatreyi ilave olarak alıyor self ile
        return b + 10
    
ali = insan()
print(ali.boy)    
print(ali.kosmak(90))

l = [1,2,3] #liste

