#key - value

#41=>Kocaeli 34 =>İstanbul

#Liste ile
#sehirler = ['Kocaeli', 'İstanbul']
#plaklar = [41,34]
#print(plaklar[sehirler.index('Kocaeli')])

#Dictionary

#print(plakalar['Kocaeli']) yazarsak burada 41'e götürmesini bekliyoruz.

#plaklar = {'key' : 'value'}

#plaklar = {'Kocaeli' : 41, 'İstanbul': 34}

#print(plaklar['Kocaeli'])
#print(plaklar['İstanbul'])

#plaklar['Ankara'] = 6
#plaklar['Kocaeli']= 'new value'

#print(plaklar)

users = {
    'sadikturan' : {
        'age' : 36,
        'roles' : ['users'],
        'email' : 'sadikturan@gmail.com',
        'adress' : 'Kocaeli',
        'phone' : '1231231'

    },
    'cinarturan': {
        'age' : 2,
        'roles' : ['admin','users'],
        'email' : 'cinarturan@gmail.com',
        'adress' : 'Kocaeli',
        'phone' : '1231231'
    }
}
print(users['cinarturan']['roles'][0])




