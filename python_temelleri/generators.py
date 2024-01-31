# generators bize bellekte yer işgal etmeyen iterators üretir.

# def cube():
#     result = []

#     for i in range(5):
#         result.append(i**3)
#     return result

# print(cube())


# def cube():
   
#     for i in range(5):
#         yield i**3 #burada bir değer üretiliyor ama sonrasında bir yerde saklanmıyor.

# for i in cube(): #Son hali
#     print(i)

# kupler = cube() # Burada cube fonksiyonu çalıştırmış olmuyoruz sadece  bize iterate edilebilen 
# # yani üzerinde dolaşabileceğimiz bir iterable objesi gönderiyor. Bu obje üzerinde dolaşabi-
# # liyoruz next() fonskiyonu ile.

# generator = cube()
# iterator = iter(generator) #Böyle yapmak terine aşğıdaki gibi de yapabiliriz.

# iterator = cube()

# for i in iterator:
#     print(i)


# liste = [i**3 for i in range(5)]
# print(liste)
#Gelen sonucu bir generators şeklinde döndürmek istiyorsak köşeli parantezler yerine normal paranteazler koyarız.
generator = (i**3 for i in range(5))
print(generator)
for i in generator: 
    print(i)
