#value typelarda verinin kendisiyle reference typelarda listenin adresiyle ilgileniyoruz.

#value types --> string, number
x = 5
y = 25

x = y

y= 10

#print(x,y)

#reference types --> list, class
a = ["apple","banana"]
b = ["apple","banana"]

a = b #Adresler birbirine eşitlenir. İkiside aynı adresi gösterir

b[0] = "grape"

print(a,b)

