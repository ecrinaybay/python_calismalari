#x = 5
#y = 10
#z = 20

#x,y,z = 5,16,20

#x,y= y,x

'''x+=5 #x=x+5
x-=5 #x=x-5
x*=5 #x=x*5
x/=5 #x=x/5
x%=5 #x=x%5
y//=5 #Tam bölme yapılır tam kısmıyla ilgilenir
y**=5 #y^5'''

values = 1,2,3,4,5 
'''x,y,z gibi üç değişkene atama yapacaksak tupledaki eleman sayısı üçten fazla ya da eksik olmamalıdır.
ancak z'nin başına * koyarak durumu farklılaştırabiliriz. Bu sayede geriye kalan elemanlar dizi şekilde 
z'ye gider. z için bir liste oluşturmuş oluruz.
'''
print(type(values))

x,y,*z = values

print(x,y,z)
print(x,y,z[1])

