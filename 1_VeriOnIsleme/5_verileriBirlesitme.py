# -*- coding: utf-8 -*-
"""
Created on Thu Oct  6 13:00:35 2022

@author: NADİR PAYAM
"""

#kutuphaneler
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#kodlar
#veri yukleme

veriler = pd.read_csv('eksikveriler.txt')
#pd.read_csv("veriler.csv")


#veri on isleme
boy = veriler[['boy']]
boykilo = veriler[['boy','kilo']]
#eksik veriler
#sci - kit learn

from sklearn.impute import SimpleImputer

imputer = SimpleImputer(missing_values=np.nan, strategy='mean')

Yas = veriler.iloc[:,1:4].values

imputer = imputer.fit(Yas[:,1:4])
Yas[:,1:4] = imputer.transform(Yas[:,1:4])


ulke = veriler.iloc[:,0:1].values


from sklearn import preprocessing

le = preprocessing.LabelEncoder()
ulke[:,0] = le.fit_transform(veriler.iloc[:,0])


ohe = preprocessing.OneHotEncoder()
ulke = ohe.fit_transform(ulke).toarray()

#bu kısımda verileri birleştiriyoruz, üst kodlar eksik verileri düzetlme ve kategorik verileri sayısala çevirme kodları yani birönceki dersler

print(list(range(22))) #ilk satır 0 totalde 22 
sonuc = pd.DataFrame(data=ulke, index = range(22), columns = ['fr','tr','us'])
print(sonuc) #dizilerde indeks yok, dataframe'lerde indeks kolon başlığı var


sonuc2 = pd.DataFrame(data=Yas, index = range(22), columns = ['boy','kilo','yas'])
print(sonuc2)

cinsiyet = veriler.iloc[:,-1].values
print(cinsiyet)

sonuc3 = pd.DataFrame(data = cinsiyet, index = range(22), columns = ['cinsiyet'])
print(sonuc3)

s=pd.concat([sonuc,sonuc2], axis=1) #dataframe'leri concat ile birleştirdik
print(s)
#concat dikey boyutta yapılıyor 0-22 0-22 diye gidiyor
#biz yönün yan yana ekleme olmasını istedik bunun için axis=1, axis=0 olursa alt alta ekliyor 
#axis birbirine tutuşan yerleri eşliyor
s2=pd.concat([s,sonuc3], axis=1)
print(s2)
