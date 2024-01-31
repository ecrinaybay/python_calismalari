# #class

# class Person:
#     #class attributes
#     address = 'no information'

#     #constructor(yapıcı metod)
#     def __init__(self, name, year):

#         #object attributes
#         self.name = name
#         self.year = year
        
#     #instance methods
#     def intro(self):
#         print('Hello There. I am  '+ self.name)

#     #instance methods
#     def calculateAge(self):
#         return 2023 - self.year

# #object, instance
# p1 = Person(name ='Ali', year = 1990) #p1 objesi tanımladık.
# p2= Person(name ='Yağmur', year = 1995) #p2 objesi tanımladık.

# p1.intro()
# p2.intro()

# print(f'Adım: {p1.name} Yaşım: {p1.calculateAge()}')
# print(f'Adım: {p2.name} Yaşım: {p2.calculateAge()}')


class Circle:
    #Class object attributes
    pi = 3.14

    def __init__(self,yaricap = 1):
        self.yaricap = yaricap

    #Methods
    def cevre_hesapla(self):
        return 2 * self.pi * self.yaricap
    
    def alan_hesapla(self):
        return self.pi * (self.yaricap ** 2)
    
c1 = Circle() #yaricap = 1
c2 = Circle(5)

print(f'C1 Alan = {c1.alan_hesapla()} Çevre = {c1.cevre_hesapla()}')
print(f'C2 Alan = {c2.alan_hesapla()} Çevre = {c2.cevre_hesapla()}')


