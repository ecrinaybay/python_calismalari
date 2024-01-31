 # Fonksiyon oluştururken kullandığımız anahtar kelime "def"

def sayHello(name = 'user'):
    return 'Hello ' + name

msg = sayHello('Ecrin')
msg = sayHello('Nazar')
print(msg)


def total(num1, num2):
    return num1+num2
result = total(10,20)
result = total(15,20)
print(result)

def yasHesapla(dogumYili):
    return 2023 - dogumYili

ageEcrin = yasHesapla(2003)
print(ageEcrin)

def EmekliligeKacYilKaldi(dogumYili,isim):
    '''
    DOCSTRING: Doğum yılınıza göre emekliliğinize kaç yıl kaldı.
    INPUT: Doğum yılı
    OUTPUT: Hesaplanan yıl bilgisi
    '''
    yas = yasHesapla(dogumYili)
    emeklilik = 65 - yas

    if emeklilik > 0:
        print(f'Emekliliğinize {emeklilik} yıl kaldı.')
    else:
        print('Zaten emekli oldunuz.')

EmekliligeKacYilKaldi(2003,'Ecrin')

print(help(EmekliligeKacYilKaldi))


list = [1,2,3]
print(help(list.append))
