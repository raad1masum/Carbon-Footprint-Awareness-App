import requests
from bs4 import BeautifulSoup as soup

#retrieved from flask server
barcode = "038000138430"

if len(barcode) == 12:
	url = "https://www.upcitemdb.com/upc/{}".format(barcode)
	page = requests.get(url)
	soup = soup(page.text, 'html.parser')

	product_list = soup.find("ol", {"class": "num"})
	product_list = product_list.find_all('li')

	FINAL_PRODUCT = product_list[0].text
	print(FINAL_PRODUCT)
else:
	print("*Invalid barcode must be 12 digits*")
