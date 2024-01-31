'''
    1-100 arsaında rastgele üretilecek bir sayıyı aşağı yukarı ifadeleri ile
    buldurmaya çalışın.(hak=5)
    ** "random modülü " için "python random" şeklinde arama yapın.
    ** 100 üzerinden puanlama yapın. Her soru 20 puan.
    ** Hak nbilgiisni kullanıcıdan alın ve her soru belirtilen can sayısı
       üzerinden hesaplansın. 
'''

import random

sayi = random.randint(1,10)
can = int(input('Kaç hak kullnmak istersiniz: '))
hak = can
sayac = 0

while hak > 0:
    hak-=1
    sayac += 1
    tahmin = int(input('Tahmin:'))

    if sayi == tahmin:
        print(f'Tebrikler {sayac}. defada bildiniz.Toplam puanınız: {100 -(100/can)*(sayac-1)}')
        break
    elif sayi > tahmin:
        print('Yukarı')
    else:
        print('Aşağı')
    
    if hak == 0:
        print(f'Hakkınız bitti. Tuttulan sayı: {sayi}')





