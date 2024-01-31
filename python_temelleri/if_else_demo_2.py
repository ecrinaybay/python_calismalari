'''
1- Girilen bir sayının 0 - 100 arasında olup olmadığını kontrol ediniz.

sayi = float(input('sayı: '))

if (sayi > 0) and (sayi <= 100):
    print (f'Sayı 0 - 100 arasında.')
else:
    print('Sayı 0 - 100 arasında değildir.')

'''

'''
2- Girilen bir sayının pozitif çift sayı olup olmadığını kontrol ediniz.

sayi = int(input('sayı: '))
if (sayi>0):
    if((sayi % 2) == 0):
        print('Girilen sayı pozitif çift sayıdır')
    else:
        print('Girilen sayı pozitif sayıdır ancak tek bir sayıdır')
elif (sayi == 0):
    print('Girdiğiniz sayı çift sayıdır ama pozitif ya da negatif bir sayı değildir.')
else:
    print('Girilen sayı negatif bir sayıdır.')

'''

'''
# 3- Email ve parola bilgilerini ile giriş kontrolü yapınız.

email = 'ecrin@gmail.com'
parola = 'abc123'

girilen_mail = input('Email: ')
girilen_parola = input('Parola: ')

if(email == girilen_mail):
    if (parola == girilen_parola):
        print('Uygulamaya giriş başarılı')
    else:
        print('Parola yanlış uygulamaya giriş başarısız')
else: 
    print('E-mail adresiniz yanlış uygulamaya girşi başarısız.')

'''


'''
# 4- Girilen 3 sayıyı büyüklük olarak karşılaştırınız.

a = int(input('a: '))
b = int(input('b: '))
c = int(input('c: '))

if((a > b) and (a > c)):
    print('a en büyük sayıdır')

elif((b > a) and (b > c)):
    print(f'b en büyük sayıdır.')

elif((c > a) and (c > b)):
    print('c en büyük sayıdır.')

'''

'''# 5- Kullanıcıdan 2 vize(%60) ve final (%40) notunu alıp ortalma hesaplayınız.
#   Eğer ortalama 50 ve üstündeyse geçti değilse kaldı yazdırın
#   a) Ortalama 50 olsa bile final notu en az 50 olmalıdır.
#   b) Finalden 70 alındığında ortalamanın önemi olmasın.

vize1 = float(input('1. Vize: '))
vize2 = float(input('2. Vize: '))
final = float(input('Final: '))

ortalama = (((vize1 + vize2) / 2) * 0.6) + final * 0.4
if(ortalama >= 50):
    if(final >= 50):
        print(f'Öğrencinin ortalaması: {ortalama} ve başarılı')
    else:
        print(f'Öğrencinin ortalaması: {ortalama} ve başarsız finalden en az 50 almanız gerekiyor.')
elif(final >= 70):
    print(f'Öğrencinin ortalaması: {ortalama} ve başarılı çünkü final notu en az 70.')
else:
    print(f'Öğrencinin ortalaması: {ortalama} ve başarısız')

'''


'''
# 6- Kişinin ad, kilo, ve boy bilgilerini alıp kilo indekslerini hesaplayınız.
#   Formül: (Kilo / boy uzunluğunun karesi)
#   Aşağıdaki taplaya göre kişi hangi gruba girmektedir.
#   00.0 - 18.4   => Zayıf
#   18.5 - 24.9   => Normal
#   25.0 - 29.9   => Fazla kilolu
#   30.0 - 34.9   => Şişman(Obez)

name = input('İsim: ')
kg = float(input('Kilonuz: '))
hg = float(input('Boyunuz: '))

index = kg / (hg**2)

if((index > 00.0) and (index <= 18.4)):
    print(f'{name} indeksi: {index} ve zayıf.')
elif((index >= 18.5) and (index <= 24.9)):
    print(f'{name} indeksi: {index} ve normal.')
elif((index >= 25.0) and (index <= 29.9)):
    print(f'{name} indeksi: {index} ve fazla kilolu.')
elif((index >= 30.0) and (index <= 49.9)):
    print(f'{name} indeksi: {index} ve obez.')
else:
    print('Bilgileriniz yanlış')
    
'''



