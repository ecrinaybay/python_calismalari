# file = open("newfile.txt") #Mod değeri belirtmediğmizde vasayılan olarak read modunda açar.

# try:
#     file = open("newfile.txt","r")
#     print(file)
# except FileNotFoundError:
#     print("Dosya okuma hatası")
# finally:
#     print("Dosya kapandı")
#     file.close()

file = open("newfile.txt","r",encoding ='utf-8')

#*************** for döngüsü ******************

# for i in file:
#     print(i, end ="") #print ifadesinde yazdırılırken boş bir satır eklenmesini engelliyoruz.
# file.close()

#read() fonskiyonu

# content = file.read()
# print(content)
# file.close()

#************** read() fonskiyonu **************

# content1 = file.read()
# print("İçerik 1")
# print(content1)

# file = open("newfile.txt","r",encoding ='utf-8')
# content2 = file.read()
# print("İçerik 2")
# print(content2)

# content = file.read(5) #(5byte) İçeriğin ilk 5 karakterini alır
# content = file.read(3) # İlk beş karakterden sonraki 3 karakteri alır
# content = file.read(3)
# print(content)
# file.close()

#*************** readline() fonksiyonu **************
#readline() fonksiyonu her seferinde bir satırı okur.

# print(file.readline(),end="")
# print(file.readline(),end="")
# print(file.readline(),end="")
# print(file.readline(),end="")
# print(file.readline())
# print(file.readline())
# print(file.readline())


# ************** readlines() fonksiyonu *************

liste = file.readlines() #Her satırdaki bilgi bir dizi bir liste elemanı olarak ortaya çıkar.

print(liste)

print(liste[0])
print(liste[1])
print(liste[2])

file.close()