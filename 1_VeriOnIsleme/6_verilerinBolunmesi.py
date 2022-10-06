
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

#verimizi 4 parçaya böleceğiz, x bağımsız, y bağımlı değişken
# train ve test bölümü verinin satır bazlı bölümünü belli bir satır train sonraıs test
# x ve y ise verinin bağımsız ve bağımlı şekilde bölünmesidir
# fr,tr,us,boy,kilo,yas x'imizi veriyor, y ise cinsiyet
# test_size 0.33 demek %67 train, ^%33^ü test için bölünecek verilerin demek
#random rastsal bölünmeyi sağlıyor


#tablo 4'e bölündü x_train,x_test= bağımsız kolonlardan bölündğ
# y_train,y_test ise bağımlı kolundan bölündü




"""
burdaki mantık şudur eğitim kolonları verilerin olduğu kolondur bu verilerle algoritmayı eğitirsin mesela şu kadar şey şu kadarmış
sonra ise test kolonları vardır bu kolonlar ise tahmin edilmesi istenen şeylerin olduğu kısımdır yani şunlar şu kadarmış peki şu ne kadardır? mantığı
eğitirsin ve test ettirirsin mantık budur.

"""