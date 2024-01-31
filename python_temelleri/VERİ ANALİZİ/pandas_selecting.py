import pandas as pd
from numpy.random import randn

df = pd.DataFrame(randn(3,3), index = ["A", "B", "C"], columns = ["Column1", "Column2", "Column3"] )

result = df
result = df["Column1"]
result = type(df["Column1"])
result = df[["Column1","Column2"]]

# loc["row","column"] => loc["row"] => loc[:,"column"]

result = df.loc["A"] #loc -->location
result = type(df.loc["A"])
result = df.iloc[2] # C satırı bize getirir
result = df.loc[:,"Column1"]
result = df.loc[:,["Column1","Column2"]]
result = df.loc[:,"Column1":"Column3"] # İstediğimiz sütunlar arasındaki bilgiyi alır. Bşlangıç ve bitiş dahil.
result = df.loc[:,:"Column2"] #Başlangıç sütununu belirmeden de bşatan istediğimiz sütuna kadar seçebiliriz.
result = df.loc["A":"C",:"Column2"] # A ve  C arası tüm satırlar ve Column1 ve Colmun2 getiririlir.
result = df.loc[:"B",:"Column2"] #Baştan B'ye kdar olanları getirir
result = df.loc["A","Column1"] #A satırı ve Column1'in birleşim noktasını verir.
result = df.loc["C","Column1"]
result = df.loc[["A","B"],["Column1","Column2"]]

df["Column4"] = pd.Series(randn(3), ["A", "B", "C"])  #4. sütunu oluşturuyoruz.
df["Column5"] = df["Column1"] + df["Column3"] #İki seriyi toplayıp 5. sütunu oluşturduk. Orijinal dataFrame içinde değişiklik yapılmadı.

# print(df.drop("Column5", axis = 1))  #Silmek istedğimiz sütunu yazarız.

result = df.drop("Column5", axis = 1, inplace = True)  #Orijinal Data Frame üzerinde de değşiklik yapılıyor. False olsaydı orijinal halinde değişiklik olmazdı


print(df)


