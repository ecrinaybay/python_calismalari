import numpy as np

# result = np.array([1,3,5,7,9])
# result = np.arange(1,10) # 1 dahil 10 dahil değil.
# result = np.arange(10,100,3) # 10 ve yüz arasında üçer üçer artan bir dizi.
# result = np.zeros(10)
# result= np.ones(10)
# result = np.linspace(0,100,5)#0 ve 100 arasını 5 eşit parçaya böler.
# result = np.linspace(0,5,5)
# result = np.random.randint(0,10) # 0 dahil 10 dahil değil rastgele  int sayı üretir
# result = np.random.randint(20) # Sadece üst değeri veririz ve sıfırdan başlantmış gibi olur. (0 dahil üst değer dahil değil.)
# result = np.random.randint(1,10,3) # Belitilen aralıkta rastgele 3 sayı üretir.
# result = np.random.rand(5) # 0 ile 1 arasında 5 tane sayı üretir.
# result = np.random.randn(5) # Eksi değerler de üretir.
# result = np.arange(50) # 0'dan 50'ye kadar(50 dahil değil) bir dizi karşımıza gelir.

# np_array = np.arange(50)
# np_multi = np_array.reshape(5,10) #5x10 matris
# print(np_multi.sum(axis = 1)) #satırların toplamı --> [ 45 145 245 345 445]
# print(np_multi.sum(axis = 0)) #Sütunların toplamı --> [100 105 110 115 120 125 130 135 140 145]

rnd_numbers = np.random.randint(1,100,10)
print(rnd_numbers)
result = rnd_numbers.max()
result = rnd_numbers.min()
result = rnd_numbers.mean() # Üretilen sayıların ortalaması
result = rnd_numbers.argmax() # Üretilen maximum sayının index numarasını verir.
result = rnd_numbers.argmin() # Üretilen minimum sayının index numarasını verir.

print(result)

