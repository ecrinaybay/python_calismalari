import pandas as pd
import numpy as np

data = np.random.randint(10,100,75).reshape(15,5)
df = pd.DataFrame(data, columns = ["Column1","Column2","Column3","Column4","Column5",])

result = df
result = df.columns
result =df.head() #İlk 5 satırdaki kayıtlar geldi
result = df.head(10) #İlk 10 satırdaki kayıtlar geldi.
result = df.tail() #Son 5 satırdaki kayıtlar geldi.
result = df.tail(10) #Son 10 satırdaki kayıtlar geldi.
result = df["Column1"].head() # 1. sütundaki il 5 kayıt geldi
result = df.Column1.head() # 1. sütundaki ilk 5 kayıt geldi
result = df[["Column1","Column2","Column3"]] #Birden fazla sütun almak istediğimizde liste halinde sütunların ismini girmeliyiz
result = df[["Column1","Column2"]].head()
result = df[["Column1","Column2","Column3"]].tail()

result = df[5:15] # 6 ve 15 dahil olmak üzere aradaki satırlardaki kayıtları getirir.
result = df[5:15][["Column1","Column2","Column3"]].head() # 6 ve 10. satırın 1,2 ve 3. sütunundaki bilgileri getirdi

result = df >50 #50'den büyük kayıtlar için True olmayan için False getirir.
result = df[df>50] #50^den büyük kayıtları verir olmayanlra NaN yazar
result = df[df % 2 == 0]
result = df["Column1"] >50 
result = df[df["Column1"] >50]
result = df[df["Column1"] >50][["Column1","Column2"]]
result = df[(df["Column2"] > 50) & (df["Column1"] <= 70)]
result = df[(df["Column1"] > 50) & (df["Column1"] <= 70)] # Aynı sütuna filtrmeleme yaptık.
result = df[(df["Column1"] > 50) | (df["Column2"] > 50)]
result = df[(df["Column1"] > 50) | (df["Column2"] > 50)][["Column1","Column2"]]
result = df.query("Column1 >= 50 & Column1 % 2 == 0")
result = df.query("Column1 >= 50 & Column1 % 2 == 0")[["Column1","Column2"]]
result = df.query("Column1 >= 50 | Column1 % 2 == 0")[["Column1","Column2"]]
print(result)


