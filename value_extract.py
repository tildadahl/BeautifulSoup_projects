import requests
from bs4 import BeautifulSoup
url = 'https://www.oljepris.nu'
res = requests.get(url)
html_page = res.content
soup = BeautifulSoup(html_page, 'html.parser')

# varje dygn

text = soup.find(id = 'inputPriceSEK')
value = (text.get('value'))
print (value)



