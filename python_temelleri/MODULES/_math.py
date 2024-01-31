#YÖNTEM 1

# import math
# import math as islem #math kütüphanesine islem takma adıyla ulaşmamızı sağlar.

#math modülü içerisindeki tüm fonksiyonları bize getirir.
# value = dir(math) 
# print(value)

#math modülündeki fonksiyonlar hakkında bilgi sahip olmak istiyorsak kullanabiliriz.
# value = help(math) 
# print(value)

#Spesifik olarak bilgiye sahip olmak istediğimiz fonksiyon için kullanabiliriz.
# value = help(math.factorial)
# print(value)

# value = math.sqrt(49)
# value = math.factorial(5)
# value = math.floor(5.9)
# value = math.ceil(5.9)

# value = islem.factorial(5)


#YÖNTEM 2

#İlgili modülden hepsini import etmeye yarar. math. diyerek fonksiyonu yazmaya gerek kalmaz.
#from math import *

#Eğer tanımladığımız fonksiyonu alttaki importun altına yazarsak bizim kendi tanımladığımız
#fonksiyon kabul görür.
def sqrt(x): 
    print('x: ' +str(x))

#İlgili modül üzerinden sadece kullacaklarımızı import etmiş oluruz.
from math import factorial,sqrt,ceil

#Bu şekilde yaptığmızda bizim tanımladığımız fonksiyon kabul gördü.
def sqrt(x):
    print('x: ' +str(x))

value = factorial(5)
value = sqrt(9)
#value = ceil(9.8)

print(value)



