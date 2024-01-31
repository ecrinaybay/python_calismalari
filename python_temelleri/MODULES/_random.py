import random

# result = dir(random)
# result = help(random)

result = random.random() # 0.0 - 1.0
result = random.random() * 100
result = int(random.uniform(10,100)) # 10 - 100 arası float sayı üretir sonrasında tam sayı olarak döndürülür
result = random.randint(1,100) # 1 - 100 arası tam sayı üretir

greeting = 'Hello there.'
names = ['Ali','Yağmur','Deniz','Cenk','Ahmet','Efe']

result = names[random.randint(0,len(names)-1)] #names listesinde rastgele bir elemena seçip getirir.
result = random.choice(names) #names listesinde rastgele bir elemena seçip getirir.
result = random.choice(greeting) #greeting string ifadesinden rastgele eleman seçip getirir.

liste = list(range(10))
random.shuffle(liste) # 0'dan 10'a kadar olan karıştırılmış liteyi verir.
result =(liste)

liste = range(100) #0 dahil 100 dahil değil
liste = range(10,100) #10 dahil 100 dahil değil birer birer artım
liste = range(10,100,5) #10 dahil 100 dahil değil beşer beşer artım
for list in liste:
    print(list)
result = random.sample(liste,3) # listenin içinden rastgele 3 eleman çeker
result = random.sample(names,2)

print(result)
