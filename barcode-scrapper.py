import requests
from bs4 import BeautifulSoup as soup

#038000138430 
barcode = input("Enter a 12 digit barcode: ")

if len(barcode) == 12:
	url = "https://www.upcitemdb.com/upc/{}".format(barcode)
	page = requests.get(url)
	soup = soup(page.text, 'html.parser')

	product_list = soup.find("ol", {"class": "num"})
	product_list = product_list.find_all('li')

	FINAL_PRODUCT = product_list[0].text
	print()
	print("The item is", FINAL_PRODUCT)
	print()

	category = input("What food category does the product fall into? (Example: snacks, red meat, dairy, vegetable): ")

	footprint = {
		"chips" : "Production emissions 1.56, Transport emissions 0.09, Waste emissions	0.08",
		"snacks" : "Production emissions 1.56, Transport emissions 0.09, Waste emissions 0.08",
		"crisps" : "Production emissions 1.56, Transport emissions 0.09, Waste emissions 0.08",
		"red meat" : "Production emissions 15.99, Transport emissions 0.19, Waste emissions 0.17",
		"white meat" : "Production emissions 3.39, Transport emissions 0.19, Waste emissions 0.17",
		"fruit" : "Production emissions	0.21, Transport emissions 0.18, Waste emissions 0.17",
		"dairy" : "Production emissions	0.93, Transport emissions 0.18, Waste emissions	0.17",
		"cheese" : "Production emissions 0.93, Transport emissions 0.18, Waste emissions0.17",
		"milk" : "Production emissions	0.93, Transport emissions 0.18, Waste emissions	0.17",
		"cream" : "Production emissions	0.93, Transport emissions 0.18, Waste emissions	0.17",
		"yogurt" : "Production emissions 0.93, Transport emissions 0.18, Waste emissions 0.17",
		"grain" : "Production emissions	0.27, Transport emissions 0.18, Waste emissions	0.17",
		"oil" : "Production emissions 0.83, Transport emissions 0.18, Waste emissions 0.17",
		"vegetable" : "Production emissions	0.23, Transport emissions 0.18, Waste emissions	0.17",
		"crops" : "Production emissions	0.23, Transport emissions 0.18, Waste emissions	0.17",
		"seafood" : "Production emissions 16.72, Transport emissions 0.1, Waste emissions 0.17",
		" " : "No category was selected",
		"" : "No category was selected"

	}

	print(footprint[category])
	print()

	answer = input("Please type 'info' to find more about the emissions. Or 'exit' if you are finished: ")
	if answer == "info":
		info = ["All food carbon emissions are reported above in Kg of CO2e, including major greenhouse gases such as carbon dioxide, methane and nitrous oxide.", "Production emissions are for the production (cradle to farmgate) and any processing of quantity purchased.", " Transport emissions are for the transport of quantity purchased: local transport, any ocean transport, and user-defined long-distance truck transport.", "Waste emissions are for the landfilling of quantity wasted (with typical waste energy recovery).", "Packaging and cooking are not included."]
		for stuff in info:
			print("-", stuff)
			print()
	else:
		pass
else:
	print("*Barcode does not exist or Invalid barcode must be 12 digits*")