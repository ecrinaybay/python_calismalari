sayilar = [1,3,5,7,9,12,19,21]

# 1- sayilar listesindeki hangi sayılar 3'ün katıdr?

for sayi in sayilar:
    if(sayi%3 == 0):
        print(sayi)


# 2- sayilar listesinde sayıların toplamı kaçtır?
'''
toplam = 0
for sayi in sayilar:
    toplam = toplam + sayi
print('Toplam: ',toplam)
'''

# 3- sayilar listesindeki tek sayıların karesini alınız.
'''
for sayi in sayilar:
    if(sayi % 2 == 1):
        print(f'Sayı: {sayi} -> Sayınınn karesi: {sayi **2}')

'''
sehirler = ['Kocaeli', 'İstanbul', 'Ankara', 'İzmir', 'Rize']


# 4- Şehirlerden hangileri en fazla 5 karakterlidir?
'''
for sehir in sehirler:
    if(len(sehir) <= 5):
        print(sehir)
'''

urunler = [
    {'name': 'samsung S6', 'price' : '3000'},
    {'name': 'samsung S7', 'price' : '4000'},
    {'name': 'samsung S8', 'price' : '5000'},
    {'name': 'samsung S9', 'price' : '6000'},
    {'name': 'samsung S10', 'price' : '7000'}    
]

# 5- Ürünlerin fiyatları toplamı nedir?
'''toplam = 0
for urun in urunler:
    fiyat = int(urun['price'])
    toplam += fiyat
print('Toplam ürün fiyatı: ', toplam)'''


# 6- Ürünlerden en fazla 5000 olan ürünleri gösteriniz.
'''
for urun in urunler:
    if(int(urun['price']) <= 5000):
        print(urun['name'])
'''

