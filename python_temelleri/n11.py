import requests
from bs4 import BeautifulSoup

url = "https://www.n11.com/bilgisayar/dizustu-bilgisayar"

html = requests.get(url).content
soup = BeautifulSoup(html,"html.parser")
#BeautifulSoup objemiz var. İkinci parametrede ise parse etmek istediğimiz içeriğin html.parser olduğunu söylüyoruz. 

# print(html) #Almış olduğumuz html'yi pars etmeden direkt kaynak kodlarını yazdırdık.Kaynağı görüntüle dediğimizde 
# karşımıza gelen içerik konsolda yazdırılır.

list = soup.find_all("li",{"class":"column"},limit=1)

for li in list:
    name = li.div.a.h3.text.strip()
    link = li.div.a.get("href")
    oldprice = li.find("div",{"class":"proDetail"}).find_all("a")[0].text.strip().strip('TL') 
    newprice = li.find("div",{"class":"proDetail"}).find_all("a")[1].text.strip().strip('TL')
# a'lar liste halinde geleceği için 0. indekste yazan kayanağa göre eski fiyat 1. indekteki ise yeni fiyat.

print(f"name: {name} link: {link} old price: {oldprice} new price: {newprice}")
