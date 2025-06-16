# pythom -m pip install requests
#python -m pip install beautifulsoup
#=>parse html

#go to git bash
#git config--global user.name"Deepti Subedi"
#git config--global user.email "deeptisubedi7@gmail.com"


import requests 
from bs4 import BeautifulSoup
url="http://books.toscrape.com/"

def scrape_book(url):
    response=requests.get(url)

    #Set encoding explicity to handle special character correctly
    response.encoding=response.apparent_encoding

    if response.status_code!=200:
        return
    
    soup=BeautifulSoup(response.text,"html.parser")
    books=soup.find_all("article",class_="product_pod")
    
    for book in books:
        title=book.h3.a["title"]
        
        price_text=book.find("p",class_="price_color").text

        currency =price_text[0]
        price=float (price_text[1:])
        print(title,currency,price)


scrape_book(url)  

