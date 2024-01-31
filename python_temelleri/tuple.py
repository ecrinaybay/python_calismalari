""" Tuple lar listeler gibidir ama herhangi bir eleman üzerinde güncelleme yapılamaz
silme işlemi ya da bir eleman eklme işlemini yapamıyoruz."""

list = [1, 2, 3]

tuple = (1, 'iki', 3)

print(type(list))
print(type(tuple))

print(list[2])
print(tuple[2])

print(len(list))
print(len(tuple))

list = ['Ali', 'Veli']
tuple = ('Ayşe','Ayşe', 'Fatma')
names = ('Demet','Emel', 'Ayşe') +tuple

print(names)

list[0] = 'Ahmet'
#tuple[0] = 'Deniz' # Tupleda böyle atama yapamayız.


print(tuple.count('Ayşe'))
print(tuple.index('Ayşe'))