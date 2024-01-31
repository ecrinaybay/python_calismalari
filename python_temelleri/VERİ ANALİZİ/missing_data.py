import pandas as pd
import numpy as np

data = np.random.randint(10,100,15).reshape(5,3)

df = pd.DataFrame(data, index = ['a', 'c', 'e', 'f', 'h'], columns = ['column1', 'column2', 'column3'])

df = df.reindex(['a','b','c','d','e','f','g','h'])

newColumn = [np.nan,30,np.nan,51,np.nan,30,np.nan,10]
df["column4"] = newColumn

result = df
print(result)
result = df.drop("column1", axis = 1) #column1'i sileriz
result = df.drop(["column1","column2"], axis = 1)
result = df.drop('a', axis = 0) #axis = 0 satır, axis = 1 sütun
result = df.drop(['a','b','h'], axis = 0)

result = df.isnull() #NaN olanlar True olmayanlar False
result = df.notnull() #NaN olanlar False olmayanlar True
result = df.isnull().sum() #Null değrleri saymış oluruz.
result = df["column1"].isnull()
result = df["column1"].isnull().sum()
result = df[df["column1"].isnull()][["column1"]] #Column1 NaN değerler gelir 
result = df[df["column1"].notnull()][["column1"]] #column1 NaN olmayan değerleri getir.

result = df.dropna()  #Varsayılan axis = 0
result = df.dropna(axis = 1)
result = df.dropna(how = "any") #Herhangi bir NaN varsa siler.
result = df.dropna(how = "all") # Tüm satır NaN ise karşımıza gelmez.
result = df.dropna(subset = ["column1","column2"],how ="all")
result = df.dropna(subset = ["column1","column2"],how ="any")
result = df.dropna(thresh = 2) # İki tane normal veri varsa bu durumda istedğimizi karşılar ve kayıtları silmez
result = df.dropna(thresh = 3) #En az sayıda normal veri

result = df.fillna(value = 'no input') #NaN yerine no input yazılır
result = df.fillna(value = 1) #NaN yerine 1 yazılır

result = df.sum() #Sütunları ayrı ayrı toplar
result = df.sum().sum() #Tüm toplamı verir
result = df.size
result = df.isnull().sum() #Sütunlardaki NaN sayısını verir.
result = df.isnull().sum().sum() #Toplam NaN sayısını verir.


def ortalama(df):
    toplam = df.sum().sum()
    adet = df.size - df.isnull().sum().sum() 
    return toplam/adet

result = df.fillna(value = ortalama(df)) #NaN olan yerlere ortlama değerini yazdırır.

print(result)



