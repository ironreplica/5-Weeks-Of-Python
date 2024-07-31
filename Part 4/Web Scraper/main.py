# LEGAL Web scraper
# Trevor Childs, 7/29/2024
import requests
from bs4 import BeautifulSoup

req = requests.get('https://quotes.toscrape.com/')

soup = BeautifulSoup(req.content, 'html.parser')
quotes_raw = soup.find_all('span', class_='text')
authors_raw = soup.find_all('small', itemprop='author')

# Split the html data into readable text.
# Starts as <span class="text" itemprop="text">“It is our choices, Harry, that show what we truly are, far more than our abilities.”</span>
# Remove the characters before the >, and remove the characters after the <
authors = [str(author).split('>',1)[1].split('<',1)[0] for author in authors_raw]
quotes = [str(quote).split('>',1)[1].split('<',1)[0] for quote in quotes_raw]

auth_quote_dict = { k:v for (k,v) in zip(authors, quotes)}

print(auth_quote_dict)