"""
VERİ ÖN İŞLEME ŞABLONUMUZ

"""

#1.kütüphaneler
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#2.veri ön işleme

#kodlar
#2.1veri yükleme

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

#eksik veriler
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

#kategorik kolonun sayısala dönüştürüyoruz
#yani kategorik verileri sayısal verilere çevirdik

#encoder kateogoric to numeric
from sklearn import preprocessing
ulke = veriler.iloc[:,0:1].values #ülke kolonunu aldık

le = preprocessing.LabelEncoder() #label encodik sayısal değere döndürecek ülkeler tr,fr diye tanımkanmış ya

ulke[:,0] = le.fit_transform(veriler.iloc[:,0]) #fit öğrenme, trans uygulama verilerdek ilk kolonu aldık bunu transform edicez
print(ulke)

che = preprocessing.OneHotEncoder()
ulke = che.fit_transform(ulke).toarray()
print(ulke)

ulke = veriler.iloc[:,0:1].values



le = preprocessing.LabelEncoder()
ulke[:,0] = le.fit_transform(veriler.iloc[:,0])


ohe = preprocessing.OneHotEncoder()
ulke = ohe.fit_transform(ulke).toarray()

#bu kısımda verileri birleştiriyoruz, üst kodlar eksik verileri düzetlme ve kategorik verileri sayısala çevirme kodları yani birönceki dersler
#numpy dizilerei dataframe'e dönüştürme
print(list(range(22))) #ilk satır 0 totalde 22 
sonuc = pd.DataFrame(data=ulke, index = range(22), columns = ['fr','tr','us'])
print(sonuc) #dizilerde indeks yok, dataframe'lerde indeks kolon başlığı var


sonuc2 = pd.DataFrame(data=yas, index = range(22), columns = ['boy','kilo','yas'])
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

#verilerin eğitim ve test için bölünmesi
from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(s,sonuc3,test_size=0.33, random_state=0)

#verilerin ölçeklenmesi


from sklearn.preprocessing import StandardScaler

sc = StandardScaler()
X_train = sc.fit_transform(x_train) #parametre dönüştürmek istediğimiz sayısal değerler
X_test =sc.fit_transform(x_test)



