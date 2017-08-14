import requests
from bs4 import BeautifulSoup
import csv
import random
import urllib.request

url = "http://www.pluspiecesauto.com/equipementiers-auto/nps-10773/pieces/filtre-a-air-8.html"
source_code = requests.get(url) # html dom element as a response
plain_text = source_code.text # getting element as a plain text
soup = BeautifulSoup(plain_text, "html.parser")

items = []
count = 0

def download_image(url):
	name = 'images/' + str(count) + '.jpg'
	urllib.request.urlretrieve(url, name)


for item in soup.find('div', {'class': 'LISTE-ART-CONTAINER'}).findAll('div', {'class': 'LISTE-ART-CONTAINER-ONE-ITEM-CONTAINER'}):
	count = count + 1
	t_holder = item.find('div', {'class': 'LACOIC-TITLE'}).find('span', {'class': 'LACOIC-ART-FRS-REF'})
	c_holder = item.find('div', {'class': 'LACOIC-TITLE'}).find('span', {'class': 'LACOIC-ART-CAR'})

	title = t_holder.text
	model = c_holder.text
	image = item.find('div', {'class': 'LACOIC-IMAGE'}).find('img').get('src')
	download_image(image)

	collection = {'title': title, 'model': model, 'image': image}
	items.append(collection)

keys = items[0].keys()
with open('data.csv', 'w') as output_file:
	dict_writer = csv.DictWriter(output_file, keys)
	dict_writer.writeheader()
	dict_writer.writerows(items)
