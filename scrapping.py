from bs4 import BeautifulSoup
import requests

url = 'https://www.worldometers.info/coronavirus'

response = requests.get(url)
content = response.content
soup = BeautifulSoup(content, 'html.parser')
print(soup.table.tr.text)

columns = soup.table.tr.text
cells = soup.find_all('tr')
for tr  in cells:
    for td  in tr.find_all('td'):
        print(td.text)

   


