from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq

my_url = 'https://www.flipkart.com/search?q=apple&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off'

uClient =uReq(my_url)    #opens the connection, open webpage and tightly loaded
page_html = uClient.read() #dump all the data and store in the variable
uClient.close()
page_soup = soup(page_html , 'html.parser')

#insert the class name of the product
#find all the div tag

containers =page_soup.findAll("div",{"class": "_2kHMtA"})

print(len(containers))   #40 products in one page

#prettify is a function to bring the html in structure or organized manner

print(soup.prettify(containers[0]))

#travesing the elements

container = containers[0]
#print(container.div.img['alt'])

price = container.findAll("div",{"class": "col col-5-12 nlI3QM"})
print(price[0].text)

ratings = container.findAll("div",{"class": "gUuXy-"})
print(ratings[0].text)

filename = "flipkart_Scrap.csv"
f = open(filename,"w")

headers = "Product_name, Pricing, Ratings\n"
f.write(headers)

for container in containers:
  product_name = container.img["alt"]
  
    
  price_container = container.findAll("div",{"class": "col col-5-12 nlI3QM"})
  price = price_container[0].text.strip()    #strip to eliminate all the unnecessary components(remove extra spacing)
    
  rating_container =container.findAll("div",{"class": "gUuXy-"})
  rating = rating_container[0].text
    
    
  #print(product_name)
  #print( price)
  #print( rating)
    
  trim_price = ''.join(price.split(','))
  rm_rupee = trim_price.split("₹")
  add_rs_price = "Rs." + rm_rupee[1]
  split_price =add_rs_price.split(' ')
  final_price = split_price[0]
    
  split_rating = rating.split(" ")
  final_rating = split_rating[0]
    
  print(product_name.replace(",","|") + "," + final_price + "," + final_rating + "\n")
  f.write(product_name.replace(",","|") + "," + final_price + "," + final_rating + "\n")
    
f.close()
