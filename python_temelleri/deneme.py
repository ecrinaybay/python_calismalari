# sayi = int(input('Bir sayı girin: '))
# for i in range(2,sayi):
#     asal = True
#     for k in range (2,i):
#         if i % k ==0:
#             asal = False
#             break
#     if asal:
#         print(i)

# for i in range(1,5):
#     print(i)
# def cift(x):
#     return x%2 == 0
# print(list(map(cift, range(20)))) # True ve False'lardan oluşan liste
# print(list(filter(cift, range(20)))) # 20'den küçük çift sayı listesi

# liste = ['Ali', 'Ahmet', 'Mehmet']
# print(liste)
# liste.insert(0, 'Hasan')
# print(liste)
# liste.insert(1, 'Ayşe')
# print(liste)

# sozluk ={'a': 'alpha', 'o':'omega', 'g':'gamma'}
# print(sozluk) # {'a': 'alpha', 'o': 'omega', 'g': 'gamma'}
# sozluk=dict()
# sozluk[1]='alpha'
# sozluk['o']='omega'
# 4
# sozluk['g']='gamma'
# print(sozluk[1]) # {'a': 'alpha', 'o': 'omega', 'g': 'gamma'}
# for döngüsü varsayılan olarak anahtarlarda dolaşır
# for anahtar in sozluk:
#     print(anahtar + ':' + sozluk[anahtar])
#     # Aşağıdakiler listeye dönüştürülebilir.
# print(sozluk.keys()) # dict_keys(['a', 'o', 'g'])
# print(sozluk.values()) # dict_values(['alpha', 'omega', 'gamma'])
#     # # anahtar değer çiftleri üzerinde dolaşma

# for anahtar, deger in sozluk.items():
#     print(anahtar,deger)
# del sozluk['a'] # silmek için kullanılır
# print(sozluk.keys()) # dict_keys(['a', 'o', 'g'])
# print(sozluk.values()) # dict_values(['alpha', 'omega', 'gamma'])

# print([(x, "2'nin katı" if x%2==0 else "2'nin katı değil") for x in range(20)])

# def fonksiyon(sayi): # tanım
#     if sayi<1000:
#         return True, 'Sayı 1000\'den küçük'
#     else:
#         return False, 'Sayı 1000\'den büyük'
# sonuc, metin = fonksiyon(150) # fonksiyon çağrısı
# print(sonuc, metin)

def cift(x):
    return x%2 == 0

print(map(cift, range(20))) #<map object at 0x0000021D7C9695A0>
print(list(map(cift, range(20)))) # True ve False'lardan oluşan liste
print(list(filter(cift, range(20)))) # 20'den küçük çift sayı listesi



