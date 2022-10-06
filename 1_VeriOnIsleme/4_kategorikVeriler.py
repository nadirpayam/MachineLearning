# -*- coding: utf-8 -*-
"""
Created on Thu Oct  6 11:55:09 2022

@author: NADİR PAYAM
"""

#kategorik veriler kategorilenme amacıyla oluşturulmuş birbirşyle arasında 4 işlem, küçüktür büyüktür gibi karşılaştırmaların
#olmadığı verilerdir örneğin plakalar bu plakar şehirler arasında büyüklük küçüklük belirtmiyor, amaç sadece kategorize etmek

#kütüphaneler
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

veriler = pd.read_csv('eksikveriler.txt') 

ulke = veriler.iloc[:,0:1].values #ülke kolonunu aldık
print(ulke)

#kategorik kolonun sayısala dönüştürüyoruz
#yani kategorik verileri sayısal verilere çevirdik

from sklearn import preprocessing

le = preprocessing.LabelEncoder() #label encodik sayısal değere döndürecek ülkeler tr,fr diye tanımkanmış ya

ulke[:,0] = le.fit_transform(veriler.iloc[:,0]) #fit öğrenme, trans uygulama verilerdek ilk kolonu aldık bunu transform edicez
print(ulke)

che = preprocessing.OneHotEncoder()
ulke = che.fit_transform(ulke).toarray()
print(ulke)


"""
şöyle yaptık şimdi bizim ülkelerimiziz kodları var tr,fr,us gibi verilerde herhangi bir kişinin o ülkeden olup olmadığını anlamak istiyoruz
bunun için de  1,0 kullanmak istedik oralıysa 1, değilse 0 anlamında. 
adımlar
-ilk önce ülkelere numerik olarak sayısal değer verdik tr=1 fr=2 us=0 oldu bunu kod kendisi otomatik yapıyor
sonra da dizi oluşturduk üst kısma tr,fr,us gibi düşün eğer veri tr'ye aitse altında bir diğerlerinde 0 görünecek
bu tüm ülkeler için geçerli, yani ülkeleri sayısal olarak sıraladık sonra o ülkeden mi değil mi diye 1,0 mekanizması kurduk true false baabında

"""

