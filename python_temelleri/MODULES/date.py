#import datetime #Modül içindeki tüm şeyleri import eder.

from datetime import datetime
from datetime import timedelta
# from datetime import date
# from datetime import time

result = datetime.now() #Şu anki zaman

simdi = datetime.now()
simdi = datetime.today()

result =  simdi.year
result = simdi.month
result = simdi.day
result = simdi.hour
result = simdi.minute
result = simdi.second

result = datetime.ctime(simdi)
result = datetime.strftime(simdi,'%Y') #Sadece yıl
result = datetime.strftime(simdi,'%X') #Sadece saat bilgisi(saat, dakika, saniye)
result = datetime.strftime(simdi,'%d') #Sadece gün
result = datetime.strftime(simdi,'%A') #Gün bilgisini string olarak verir.
result = datetime.strftime(simdi,'%B') #Ay bilgisni string şekilde verir.
result = datetime.strftime(simdi,'%Y %B %A')

# t= '10 Şubat 2023'
# gun, ay, yil = t.split()
# print(gun)
# print(ay)
# print(yil)

t = '10 February 2023 hour 22:26:05'
result = datetime.strptime(t, '%d %B %Y hour %H:%M:%S')
result = result.year
print(result)

birthday = datetime(2023,2,10,23,35,1) #Yıl, ay, gün, saat, dakika, saniye
print(birthday)
result = datetime.timestamp(birthday) #İlgili verilen tarih saniye cinsinden getiririlir 1970 tarihine göre yapılıyor.
result = datetime.fromtimestamp(result) #saniyeyi tarihe çevirir.
result = datetime.fromtimestamp(0) #1970-01-01 03:00:00
result = simdi - birthday #timedelta

# result = result.days
# result = result.seconds
# result = result.microseconds

print(simdi)
result = simdi + timedelta(days=10) #Şimdinin üstüne 10 gün ekledik.
result = simdi + timedelta(days=730, minutes=10)
result = simdi - timedelta(days = 10) #Şimdiden 10 gün geriye gittik

print(result)





