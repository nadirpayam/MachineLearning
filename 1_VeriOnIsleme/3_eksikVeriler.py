# -*- coding: utf-8 -*-
"""
Created on Wed Oct  5 20:51:18 2022

@author: NADİR PAYAM
"""
#kütüphaneler
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#eksik verileri düzeltmek

#bazı algoritmalar eksik verilerle çalışmıyor, o verileri düzeltmemiz lazım

veriler = pd.read_csv('eksikveriler.txt') #bazı veriler eksik bu dosyada

#kolonun ortalamasını alıp eksik yerlere yazdıracağız

#sci - kit learn kütüphanesi 
from sklearn.impute import SimpleImputer

imputer = SimpleImputer(missing_values=np.nan,strategy='mean')
#SimpleImputer'da değiştireceğimiz değer nan,yerine gelecek şey kolonun ortalaması
#mean ortalama demek

yas = veriler.iloc[:,1:4].values #yas kolonunu çekebilmek için iloc kullandık 
#bütün satırlar gelsin diye : kullandık sonra
print(yas)
imputer = imputer.fit(yas[:,1:4]) #fit öğrenilecek olan değer, öğretmek için kullanılır kolonların ortalama değerini öğrenir

yas[:,1:4] = imputer.transform(yas[:,1:4]) #fit ile öğrendiği ortalamayı trasnform uyguluyor, nan olanları değiştiriyor
print(yas)


