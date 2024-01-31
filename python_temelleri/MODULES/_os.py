import os
import datetime

result = dir(os)
result = os.name

# dizin değiştirme
# os.chdir('C:\\')
# os.chdir('../..')

#klasör oluşturma
# os.mkdir("newdirectory")
# os.makedirs("newdirectory/yeniklasör")
# os.rename("newdirectory","yeniklasör")
# os.rmdir("newdirectory")
# os.removedirs("yeniklasör/yeniklasör")

# etkin dizin öğrenme
# result = os.getcwd()

#listeleme
# result = os.listdir()
# result = os.listdir('C:\\')
# for dosya in os.listdir():
#     if dosya.endswith('.py'):
#         print(dosya)

# result = os.stat("date.py")
# result = result.st_size/1024
# result = datetime.datetime.fromtimestamp(result.st_ctime) # Oluşturulma tarihi
# result = datetime.datetime.fromtimestamp(result.st_atime) # Son erişim tarihi
# result = datetime.datetime.fromtimestamp(result.st_mtime)   # Değiştirme tarihi

# os.system("notepad.exe")

#path (Dosya uzantısıyla ilgili işlemler)

result = os.path.abspath("_os.py")  #Dosyanın tam konumunu verir.
result = os.path.dirname("D:/Computer Engineer Department/python_temelleri/_os.py")#Tam konumu verilen dosyanın dizin ismini alıyoruz.
result = os.path.dirname(os.path.abspath("_os.py"))
result = os.path.exists("D:/Computer Engineer Department/python_temelleri/_os.py") #Dizin ya da dosya adı ilgili konumda var mı yok mu onun bilgisini verir.
result = os.path.exists("D:/Computer Engineer Department/python_temelleri") #Klasör de sorgulayabiliriz.
result = os.path.isdir("D:/Computer Engineer Department/python_temelleri") #Klasörse True dosya ise False döndürür.
result = os.path.isfile("D:/Computer Engineer Department/python_temelleri/_os.py")#Dosyaysa True klasörse ise False döndürür.
result = os.path.join("C:\\","deneme","deneme1")
result = os.path.split("C:\\deneme")
result = os.path.splitext("_os.py")
# result= result[0]
result= result[1]

print(result)