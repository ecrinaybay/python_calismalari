import numpy as np

# numbers = np.array([0,5,10,15,20,25,50,75])

# result = numbers[5]
# result = numbers[-1] # En sağdaki elemanı verir.
# result = numbers[0:3] # 0,1 ve 2. indeksteski değerleri alır.
# result = numbers[:3] # 0,1 ve 2. indeksteski değerleri alır.
# result = numbers[3:] #Üçüncü indeksten(4.eleman) başlayarak sona kadar gitmiş olur.
# result = numbers[::] #Tüm listeyi verir.
# result = numbers [::-1] # Listeyi ters çevir. Buradaki 3. parametre olan -1 ise adım sayısını belirtir.
# result = numbers [::-2] #Sağdan sola doğru ikişer ikişer geriye gider.

# numbers2 = np.array([[0,5,10],[15,20,25],[50,75,85]])
# print(numbers2)

# result = numbers2[0] # --> [ 0  5 10]
# result = numbers2[2] # --> [50 75 85]
# result = numbers2[0,2] # --> 1. satırın 2. indeksini verir. 10
# result = numbers2[2,1] # --> 3. satırın 1. indeksini verir. 85
# result = numbers2[:] #Tüm satırları seçmiş olduk.
# result = numbers2[:,2] #Tüm satırların 3.kolonlarını getirir. --> [10 25 85]
# result = numbers2[:,0]
# result = numbers2[:,0:2] #Tüm satırları ve 0 ve 2. index arasındaki sütunları alırız. 2 indeksine sahip olan elemanlar dahil değil yani 3. sütün dahil değildir.
# result = numbers2[-1,:] #Son satırı verir. --> [50 75 85]
# result = numbers2[:3,:3]
# result = numbers2[:2,:2]

# print(result)

#-------------*---------------
# arr1 = np.arange(0,10)
# arr2 = arr1 #referans kopyalama
# arr2[0] = 20 #Hem arr1 hem de arr2 de değişiklik olur. 

# print(arr1)
# print(arr2)
#-------------*---------------

arr1 = np.arange(0,10)
arr2 = arr1.copy() #arr1 ve arr2 ayrı adreslerde tutulurlar

arr2[0] = 20 #Sadece arr2'de değişiklik olur.

print(arr1)
print(arr2)


