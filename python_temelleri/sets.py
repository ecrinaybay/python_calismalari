fruits = {'orange', 'apple', 'banana'}

#print(fruits[0]) --> indekslenemez

for x in fruits:
    print(x)

fruits.add('cherry')
fruits.update(['mango','grape','apple']) #Aynı eleman eklenmez
fruits.remove('mango')
fruits.discard('apple')#Bu da eleman silmeye yarar.

fruits.pop() #Normalde listelerde son elemanı siler ama burada sıralı bir durum söz konusu olmadığı için hangi elemanı sileceği belli olmaz.

fruits.clear() #Tüm elemanlar silinir.

print(fruits)

#myList = [1, 2, 5, 4, 4, 2, 1]
#print(myList)
#print(set(myList)) #Tekrarlayan elemanlar liste içeirinden çıkarılır.


