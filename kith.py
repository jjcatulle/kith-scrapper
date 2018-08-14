from bs4 import BeautifulSoup
#import BeautifulSoup4
import requests

page_link ='https://kith.com/collections/footwear/sneaker'
# fetch the content from url
page_response = requests.get(page_link, timeout=5)


# parse html
page_content = BeautifulSoup(page_response.content, "html.parser")
for html in page_content.find_all(class_="product-card-info"):
    name=html.p.text
    price=html.find('p',class_='product-card-meta product-card-price').text
    #link=page_content.find('a',class_="product-card-info")['href']
    size=html.find(class_="product-card-info-variants").text



    print(name)
    print(price)
    #print(link)
    print(size)
   


#for items in page_content.find_all(class_="product-card-
#f=open('items.csv','a')
  
#f.write(match.text.encode('utf-8'))
