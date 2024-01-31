#error handling => Hata yönetimi

#Hata gelebilecek olan kod bloklarını try içine alıyoruz.

# try:
#     x = int(input('x: '))
#     y = int(input('y: '))
#     print(x/y)
# except ZeroDivisionError:
#     print('y için 0 girilemez.')
# except ValueError:
#     print('x ve y için sayısal değer girilmelidir.')

# try:
#     x = int(input('x: '))
#     y = int(input('y: '))
#     print(x/y)
# except (ZeroDivisionError, ValueError):
#     print('Yanlış bilgi girdiniz.')

# try:
#     x = int(input('x: '))
#     y = int(input('y: '))
#     print(x/y)
# except (ZeroDivisionError, ValueError) as e: #Hatayı isimlendirerek obje şeklinde alıyoruz.
#     print('Yanlış bilgi girdiniz.')
#     print(e)

# try:
#     x = int(input('x: '))
#     y = int(input('y: '))
#     print(x/y)
# except : 
#     print('Yanlış bilgi girdiniz.')

# try:
#     x = int(input('x: '))
#     y = int(input('y: '))
#     print(x/y)
# except : 
#     print('Yanlış bilgi girdiniz.')
# else: #exceptin else'i olarak düşünmeliyiz
#     print('Her şey yolunda.')

# while True:
#     try:
#         x = int(input('x: '))
#         y = int(input('y: '))
#         print(x/y)
#     except : 
#         print('Yanlış bilgi girdiniz.')
#     else:
#         break #Her şey yolundaysa while bloğundan çıkmak için break ifadesi kullanıyoruz.   
#Ayrıca bu kısım ile kullanıcıdan tekrar yeni bilgi girilmesini isteriz.
#Doğru bir bilgi girene kadar bizden bilgi girilmesini ister.

# while True:
#     try:
#         x = int(input('x: '))
#         y = int(input('y: '))
#         print(x/y)
#     except Exception as ex: #Hatayı isimlendirerek obje şeklinde alıyoruz.
#         print('Yanlış bilgi girdiniz. ',ex)
#     else:
#         break

while True:
    try:
        x = int(input('x: '))
        y = int(input('y: '))
        print(x/y)
    except Exception as ex: #Hatayı isimlendirerek obje şeklinde alıyoruz.
        print('Yanlış bilgi girdiniz. ',ex)
    else:
        break
    finally: # Kaynakların kapatılması aşamasında kullanırız. Mesela dosya açtık sonrasında kapatmak için kullanırız.
        print('Try except sonlandı.')


