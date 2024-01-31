'''
ogrenciler = {
    '120' : {
        'ad' : 'Ali',
        'soyad' : 'Yılmaz',
        'telefon' : '532 000 00 01'
    },
    '125' : {        
        'ad' : 'Can',
        'soyad' : 'Korkmaz',
        'telefon' : '532 000 00 02'

    },
    '128' : {
        'ad' : 'Volkan',
        'soyad' : 'Yükselen',
        'telefon' : '532 000 00 03'
    },
}

    1- Bilgileri verilen öğrencileri kullanıcıdan aldığınız bilgilerle dictionary içinde saklayınız.
   
    2- Öğrenci numarasını kullanıcıdan alıp ilgili öğrenci bilgisini gösterin.
'''

ogrenciler = {

}

number = input("Öğrenci no: ")
name = input("Öğrenci adı: ")
surname = input("Öğrenci soyad: ")
phone = input("Öğrenci telefon: ")

'''ogrenciler[number] = {
    'ad' : name,
    'soyad' : surname,
    'telefon' : phone
}'''

#Yukarıda yaptığımız işlemin aynısını update metotu ile de yapabiliriz.
#Update kullanığımızda birden fazla veriyi ekleyebiliyoruz.

ogrenciler.update({
        number: {
            'ad': name,
            'soyad' : surname,
            'telefon' : phone
        },
    })

number = input("Öğrenci no: ")
name = input("Öğrenci adı: ")
surname = input("Öğrenci soyad: ")
phone = input("Öğrenci telefon: ")

ogrenciler.update({
        number: {
            'ad': name,
            'soyad' : surname,
            'telefon' : phone
        },
    })

number = input("Öğrenci no: ")
name = input("Öğrenci adı: ")
surname = input("Öğrenci soyad: ")
phone = input("Öğrenci telefon: ")

ogrenciler.update({
        number: {
            'ad': name,
            'soyad' : surname,
            'telefon' : phone
        },
    })

print('*'*50)

ogrNo = input('Öğrenci no: ')
ogrenci = ogrenciler[ogrNo]

print(f"Aradığınız {ogrNo} nolu öğrencinin adı: {ogrenci['ad']} soyadı: {ogrenci['soyad']} ve telefonu ise {ogrenci['telefon']} ")




