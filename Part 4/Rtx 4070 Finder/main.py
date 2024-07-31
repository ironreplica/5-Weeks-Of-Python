# Web scraping NewEgg for RTX 4070 Cards, cheapest to highest
# Trevor Childs, 7/30/2024
import requests
from bs4 import BeautifulSoup

req = requests.get('https://www.newegg.com/p/pl?d=rtx+4070')

soup = BeautifulSoup(req.content, 'html.parser')
links = [str(link).split('href=\"',1)[1].split('\"',1)[0] for link in soup.find_all("a", class_='item-title')]
prices = [int(str(price).split('<strong>', 1)[1].split('</strong>', 1)[0].replace(',','')) for price in soup.find_all('li', class_='price-current')]

product_dict = sorted({ k:v for (k,v) in zip(prices, links)}.items(), key=lambda x: x[0])
queries = int(input('Sorted from lowest to highest, how many options do you want? (int number):\n'))
for i in range(queries):
    print(f'Option {i + 1}:\n{product_dict[i]}')