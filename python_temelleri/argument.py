'''
def changeName(n):
    n = 'Ada'

name = 'Yiğit'

changeName(name)
print(name)
'''

'''
def change(n):
    n[0] = 'İstanbul'

sehirler = ['Ankara', 'İzmir']
n = sehirler[:] # slicing

n[0] = 'İstanbul'
print(sehirler)
print(n)
'''
'''
def change(n):
    n[0] = 'İstanbul'

sehirler = ['Ankara', 'İzmir']

change(sehirler[:])

print(sehirler)
'''

'''
def add(a, b, c = 0,d = 0, e = 0):
    return sum((a,b,c))
print(add(10,20))
print(add(10,20,30))
'''

'''
def add(*params):
    print(params)
    print(params[3])
    print(params[0])
    return sum((params))
print(add(10,20,30,50,60,10))
'''
'''
def add(*params):
    print(type(args))
    sum = 0

    for n in params:
        sum = sum + n
    return sum

print(add(10,20))
print(add(10,20,30))
print(add(10,20,30,50,60,10,20))
'''  
def displayUser(**args): # dictionary geldiğini bildrimek için ** koyuyoruz.
    print(type(args))
    for key, value in args.items():
        print('{} is {}'.format(key,value))

displayUser(name = 'Çınar', age = 2, city = 'İstanbul')
displayUser(name = 'Ada', age = 12, city = 'Kocaeli',phone ='123123')
displayUser(name = 'Yiğit', age = 14, city = 'Ankara',phone ='123123',email = 'yigit@gmail.com')


def myFunc(a,b,c,*args,**kwargs):
    print(a)
    print(b)
    print(c)
    print(args)
    print(kwargs)

myFunc(10,20,30,40,50,60,70,key1='value1',key2='value2')

