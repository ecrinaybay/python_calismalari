# r+ hem okuma hem yazma modunu temsil eder.

# with open("newfile.txt","r+",encoding = 'utf-8') as file: 
#     file.seek(20)
#     file.write("deneme")

# with open("newfile.txt","r+",encoding= 'utf-8') as file: 
#     print(file.read())


# ************** Sayfa sonunda güncelleme ***********

# a modu ile açtığımızda var olan içeriğe dokunmuyoruz cusor(imleç) 
# sayfanın en sonuna gelip bir eklme işlemi yapar.

# with open("newfile.txt","a",encoding = 'utf-8') as file:
#     file.write("\nEmel Turan")


# *********** Sayfa başında güncelleme *********

# with open("newfile.txt","r+",encoding= 'utf-8') as file: 
#     content = file.read()
#     content = "Efe Turan\n" + content 
#     file.seek(0) 
#     file.write(content)
#     print(content)

# with open("newfile.txt","r",encoding= 'utf-8') as file: 
#     print(file.read())

# ********* Sayfa ortasında güncelleme **********

with open("newfile.txt","r+",encoding= 'utf-8') as file: 
    list = file.readlines()
    list.insert(1,"Yılmaz Aygün\n")
    file.seek(0)
    # for i in list:
    #     file.write(i)
    file.writelines(list)
    
with open("newfile.txt","r",encoding= 'utf-8') as file: 
    print(file.read())

