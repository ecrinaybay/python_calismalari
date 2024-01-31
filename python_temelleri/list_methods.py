numbers = [1, 10, 5, 16, 4, 9, 10]
letters = ['a', 'g', 's', 'b', 'y', 'a','s']

val = min(numbers)
val = max(numbers)
val = max(letters)
val = min(letters)

val = numbers[3:6]
val = numbers[:3]
val = numbers[4:]

numbers[4] = 40

numbers.append(49) #Listenin sonuna eleman eklemek için kullanılır.
numbers.append(59)
numbers.insert(3,78) # 3. indexten önce eleman eklemiş oluruz liste kayar eski 3. indexteki sayı 4. indekse geçer ekldiğimiz sayı ise 3. indexte olur.
numbers.insert(-1,52)

print(numbers)
numbers.pop() # Listeden elemen sileriz
numbers.pop(2) # 2. indexteki eleman silinir.

numbers.remove(49) #Silmek istediğimiz karakteri veririz.

numbers.sort() #liste sıralanır.
print(numbers)
letters.sort()
print(letters)

numbers.reverse() #listeyi tersine çevirir.
print(numbers)
letters.reverse()
print(letters)

print(len(numbers)) #Eleman sayısını verir
print(len(letters))

print(numbers.count(10)) #istediğimiz elemanın kaç tane olduğunu verir.
print(letters.count('a'))

numbers.clear() #Elemanları temizlemiş olduk.
print(numbers)

