# 1- "Bmw,Mercedes,Opel,Mazda" elemanlarına sahip bir liste oluşturunuz.
arabalar = ['Bmw',"Mercedes",'Opel','Mazda']
print(arabalar)

# 2- Liste kaç elemanlıdır?
result = len(arabalar)
print(result)

# 3- Listenin ilk ve son elemanı nedir?
result = arabalar[0]
print(result)
result = arabalar[len(arabalar)-1]
#ya da result[-1] 'de olur sondan sayarsak başına - ekleyerek yapabiliriz.
print(result)

# 4- Mazda değerimi Toyota ile değiştirin.
arabalar[-1]='Toyota'
result=arabalar
print(result)

# 5- Mercedes listenin bir elemanı mıdır?
result = 'Mercedes' in arabalar
print(result)

# 6- Listenin -2 indeksindeki değer nedir?
result = arabalar[-2]
print(result)

# 7- Listenin ilk üç elemanını alın.
result = arabalar[0:3]
result= arabalar[0:3]
result = arabalar[-2:]
print(result)

# 8- Listenin son iki elemanı yerine "Toyota" ve "Renault" değerlerini ekleyin.
arabalar[-2:] =["Toyata","Renault"]
result = arabalar
print(arabalar)

# 9- Listenin üzerine "Audi" ve "Nissan" değerlerini ekleyin.
result= arabalar + ['Audi', 'Nissan'] 
#Arabalar hâlâ 4 elemanlı biz burada result  isimli yeni bir listenin üzerine ekleme yapmış olduk arabalar listesini değişitirmek için özel farklı metotlar varmış.
print(result)

# 10- Listenin son elemanını silin.
del arabalar[-1]
result=arabalar
print(result)

# 11- Liste elemanlarını tersten yazdırınız.
result= arabalar[::-1]
print(result)

# 12- Aşağıdaki verileri bir liste içinde saklayınız.

        # studentA: Yiğit Bilgi 2010,(70,60,70)
        # studentB: Sena Turan 1999,(80,80,70)
        #studentC: Ahmet Turan 1998(80,70,90)

studentA = ['Yiğit','Bilgi',2010,[70,60,70]]
studentB = ['Sena', 'Turan', 1999,[80,80,70]]
studentC = ['Ahmet','Turan',1998,[80,70,90]]

result = studentA[0]
result = studentB[1]
result = studentC[3][1]

result = f"{studentA[0]} {studentA[1]} {2019-studentA[2]} yaşında ve not ortalaması {(studentA[3][0] + studentA[3][1] + studentA[3][2])/3}"

print(result)


# 13- Liste elemanlarını ekrana yazdırınız.