# 1- Girilen 2 sayıdan hangisi büyüktür?
'''a = int(input('a: '))
b = int(input('b: '))

result = (a > b)
print(f'a: {a} b: {b} den büyüktür: {result}')'''

# 2- Kullanıcıdan 2 vize (%60) ve final (%40) notunu alıp ortalma hesaplayınız.
'''vize1 = float(input('1. vize: '))
vize2 = float(input('2. vize: '))
final = float(input('final: '))

ortalama = ((vize1+vize2)/2 * 0.6) + (final * 0.4)

print(f'Not ortalamanız : {ortalama} ve dersten geçme durumunuz :{ortalama >=50}')
'''
# 3- Girilen bir sayının tek mi çift mi olduğunu yazdırın.
''''sayi = int(input('sayi: '))
tekcift = ((sayi%2) == 0)
print(f'Girilen sayının çift olma durumu: {tekcift}')
'''

# 4- Girilen bir sayının negatif pozitif durumunu yazdırın.
'''sayi = int(input('sayi: '))
pozitifmi = (sayi>0)
print(f'Griline sayının pozitif olma durumu: {pozitifmi}')
'''

# 5- Parola ve email bilgiisni isteyip doğruluğunu kontrol ediniz.
#    (email : email@sadikturan.com parola : abc123 )

email = 'email@sadikturan.com'
password = 'abc123'

girilenEmail = input('email: ')
girilenPassword = input('parola: ')

isEmail = (email == girilenEmail.lower().strip())
isPassword = (password == girilenPassword.lower().strip())

print(f'Email bilgisi doğru mu: {isEmail} ve Parola doğru mu {isPassword}')
