import requests
from bs4 import BeautifulSoup
import csv

website = "http://www.yubarajshrestha.com.np"
url = website + "/my-portfolio"
source_code = requests.get(url) # html dom element as a response
plain_text = source_code.text # getting element as a plain text
soup = BeautifulSoup(plain_text, "html.parser")

portfolios = []

for item in soup.find('section', {'id': 'portfolio'}).findAll('div', {'class': 'grid-item'}):
	image = website + item.find('div', {'class': 'card-img'}).find('img').get('src')
	title = item.find('div', {'class': 'card-block'}).find('h4').text
	published = item.find('div', {'class': 'card-block'}).find('div', {'class': 'info_date'}).find('span', {'class': 'date'}).text
	portfolio = {'title': title, 'published_date': published, 'image': image}
	portfolios.append(portfolio)

keys = portfolios[0].keys()
with open('portfolios.csv', 'w') as output_file:
	dict_writer = csv.DictWriter(output_file, keys)
	dict_writer.writeheader()
	dict_writer.writerows(portfolios)