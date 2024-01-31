# 1- Girilen bir sayının 0-100 arasında olup olmadığını kontrol ediniz.
''''sayi = float(input('sayı: '))
result = ((sayi > 0) and (sayi <= 100))
print(f'Sasyı 0-100 arasında mı: {result}')'''

# 2- Girilen bir sayının pozitif çift sayı olup olmadığını kontrol ediniz.
'''sayi = int(input('sayı: '))
result = ((sayi>0) and ((sayi % 2) == 0))
print(f'Girilen sayı poztif çift sayı mı: {result}')'''

# 3- Email ve parola bilgilerini ile giriş kontrolü yapınız.
'''email = 'ecrin@gmail.com'
parola = 'abc123'

girillen_mail = input('Email: ')
girilen_parola = input('Parola: ')

result = (email == girillen_mail.split()) and (parola == girilen_parola.split())

print(f'Uygulamaya giriş başarılı mı: {result}')'''

# 4- Girilen 3 sayıyı büyüklük olarak karşılaştırınız.
'''a = int(input('a: '))
b = int(input('b: '))
c = int(input('c: '))

result = (a > b) and (a > c)
print(f'a en büyük sayıdır: {result}')

result = (b > a) and (b > c)
print(f'b en büyük sayıdır: {result}')

result = (c > a) and (c > b)
print(f'c en büyük sayıdır: {result}')
'''

# 5- Kullanıcıdan 2 vize(%60) ve final (%40) notunu alıp ortalma hesaplayınız.
#   Eğer ortalama 50 ve üstündeyse geçti değilse kaldı yazdırın
#   a) Ortalama 50 olsa bile final notu en az 50 olmalıdır.
#   b) Finalden 70 alındığında ortalamanın önemi olmasın.

'''vize1 = float(input('1. Vize: '))
vize2 = float(input('2. Vize: '))
final = float(input('Final: '))

ortalama = (((vize1 + vize2) / 2) * 0.6) + final * 0.4

result = ((final>=50) and (ortalama >= 50)) or (final>=70)

print(f'Öğrencinin ortalaması: {ortalama} ve geçme durumu: {result}')
'''

# 6- Kişinin ad, kilo, ve boy bilgilerini alıp kilo indekslerini hesaplayınız.
#   Formül: (Kilo / boy uzunluğunun karesi)
#   Aşağıdaki taplaya göre kişi hangi gruba girmektedir.
#   00.0 - 18.4   => Zayıf
#   18.5 - 24.9   => Normal
#   25.0 - 29.9   => Fazla kilolu
#   30.0 - 34.9   => Şişman(Obez)

'''name = input('İsim: ')
kg = float(input('Kilonu: '))
hg = float(input('Boyunuz: '))

index = kg / (hg**2)

zayıf = ((index > 00.0) and (index <= 18.4))
normal = ((index >= 18.5) and (index <= 24.9))
fazla_kilolu = ((index >= 25.0) and (index <= 29.9))
obez = ((index >= 30.0) and (index <= 34.9))

print(f'{name} kilo indeksiniz: {index} Kilo değerlendrimen zayıf: {zayıf}')
print(f'{name} kilo indeksiniz: {index} Kilo değerlendrimen normal: {normal}')
print(f'{name} kilo indeksiniz: {index} Kilo değerlendrimen kilolu: {fazla_kilolu}')
print(f'{name} kilo indeksiniz: {index} Kilo değerlendrimen obez: {obez}')
'''

