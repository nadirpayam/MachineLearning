
#kutuphaneler
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

veriler = pd.read_csv('eksikveriler.txt')
boy = veriler[['boy']]
boykilo = veriler[['boy','kilo']]
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
sonuc = pd.DataFrame(data=ulke, index = range(22), columns = ['fr','tr','us'])
sonuc2 = pd.DataFrame(data=Yas, index = range(22), columns = ['boy','kilo','yas'])
cinsiyet = veriler.iloc[:,-1].values
sonuc3 = pd.DataFrame(data = cinsiyet, index = range(22), columns = ['cinsiyet'])
s=pd.concat([sonuc,sonuc2], axis=1)
s2=pd.concat([s,sonuc3], axis=1)


#veri bölmeye buradan başlıyoruz
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(s,sonuc3,test_size=0.33, random_state=0)


#verileri ölçeklendirmeye buradan başlıyoruz

from sklearn.preprocessing import StandardScaler

sc = StandardScaler()
X_train = sc.fit_transform(x_train) #parametre dönüştürmek istediğimiz sayısal değerler
X_test =sc.fit_transform(x_test)

"""
burda amacımız şu: farklı verileri kullanarak bir tahmin yapıyoruz ya ama mesela veriler birbiriyle uzak olabiliyor
bir kilo ile boy verilerin başlangıç sayıları falan farklı birisi 60 diğeri 180 falan yani sayısal olarak uzaklar
biz bunları ölçeklendirerek birbirine yakın oranlar elde etmeye çalışıyoruz mantık bu

"""