# with komutu kulandığımız zaman if ve fro döngüsünde olduğu gibi blok komutlarında olduğu gibi
# bir blok oluşturyoruz. Ayrıca bu şekilde yazımda dosyasyı kapatmak için file.close() komutunu
# kullanmamıza gerek yoktur.Blok zaten bittiğinde otomatik çağrılmış oluyor.

with open("newfile.txt","r",encoding="utf-8") as file:
    content = file.read(10) #İlk 10 karakteri(byte) okunur.
    print(content)
    file.seek(0) #seek() fonskiyonu ile Cursor(İmleç)u istediğimiz konuma getiririz.Mesela burada 
# cursor(imleç) 0'a yani en başa geldi.    
    print(file.tell()) #tell() fonksiyonu o anki cursor(imleç) konumu verir.
    content2 = file.read()
    print(content2) #Burada bir içerik gelmez zaten okuma işleminde cursor(imleç) sondaydı.



