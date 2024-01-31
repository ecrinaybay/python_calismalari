# def greeting(name):
#     print('Hello', name)

# # print(greeting("Ali"))
# # print(greeting)

# sayHello = greeting  #Data değil datanın adresini atarız.

# # print(sayHello)
# # print(greeting)
# print(greeting('Ali'))
# print(sayHello('Ali'))

# # sayHello'nun adresini değil sayHello'nun tanımlamasını silmiş oluyoruz.
# del sayHello
# print(sayHello) #name ahatası alırız çünkü sayHello tanımlamasını sildik.
# print(greeting)

#********** encapsulation **********

# def outer(num1):
#     print('Outer')
#     def inner_increment(num1):
#         print('Inner')
#         return num1 + 1
#     num2 = inner_increment(num1)
#     print(num1,num2)
    
# outer(10)
# inner_increment(10) #Tanımlayan bir değer olarak hata verir çünkü outer kapsamında çalıştırılır.


def factorial(number):
    if not isinstance(number, int): # Gönderdiğimiz objenin ilgili classa ait olup olmadığını kontrol eder.
        raise TypeError('Number must be an integer')
    if not number >=0:
        raise ValueError('Number must be zero or positive')
        
    def inner_factorial(number):
        if number <= 1:
            return 1
        return number * inner_factorial(number - 1)
    return inner_factorial(number)
try:
    print(factorial("4"))
except Exception as ex:
    print(ex)

