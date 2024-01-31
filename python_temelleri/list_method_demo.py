names = ['Ali', 'Yağmur', 'Hakan','Deniz']
years = [1998, 2000, 1998, 1987]

# 1- "Cenk" ismini listenin sonuna ekleyiniz.
names.append('Cenk')
print(names)

# 2- "Sena" değerini listenin başına ekleyiniz.
names.insert(0,'Sena') # 0. indexten önce eklemiş olduk.
print(names)

# 3- "Deniz" ismini listeden siliniz.
names.remove('Deniz')
# names.pop(1) # 1. indexteki elemanı siler
print(names)

# 4- "Sena" isminin indexi nedir?
index = names.index('Sena')
print(index)

# 5- "Ali" listenin bir elemanı mıdır?
result = 'Ali' in names
print(result)

# 6- Liste elemanlarını ters çevirin.
names.reverse()
print(names)

# 7- Liste elemanlarını alfabetik olarak sıralayınız.
names.sort()
print(names)

# 8- years listesini rakamsal büyüklüğe göre sıralayınız.
years.sort()
print(years)

# 9- str = "Checrolet, Dacia" karakter dizisini listeye çevriniz.
str = "Checrolet, Dacia"
result = str.split(',')
print(result)

# 10- years dizinin en büyük ve ne küçük elemanı nedir?
min = min(years)
max = max(years)
print(min,max)

# 11- years dizisinde kaç tane 1998 değeri vardır?
result = years.count(1998)
print(result)

# 12- years dizisinin tüm elemanlarını siliniz.
years.clear()
print(years)

# 13- Kullanıcıdan alacağınız 3 tane marka bilgisini bir listede saklaynız.

markalar = []

marka= input("marka: ")
markalar.append(marka)
marka= input("marka: ")
markalar.append(marka)
marka= input("marka: ")
markalar.append(marka)

print(markalar)