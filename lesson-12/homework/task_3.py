import requests
from bs4 import BeautifulSoup
import json


base_url = 'https://www.demoblaze.com'
laptops_url = f'{base_url}/index.html#'
response = requests.get(laptops_url)
soup = BeautifulSoup(response.content, 'html.parser')


def get_laptops_from_page(soup):
    laptops = []
    items = soup.find_all('div', class_='col-lg-4 col-md-6 mb-4')
    for item in items:
        name = item.find('h4', class_='card-title').text.strip()
        price = item.find('h5').text.strip()
        description = item.find('p', class_='card-text').text.strip()
        laptops.append({
            'name': name,
            'price': price,
            'description': description
        })
    return laptops


all_laptops = []
while True:
    all_laptops.extend(get_laptops_from_page(soup))
    next_button = soup.find('button', id='next2')
    if next_button and 'onclick' in next_button.attrs and 'disabled' not in next_button.attrs:
        next_page_url = f'{base_url}/{next_button["onclick"].split("location.href=\'")[1].split("\'")[0]}'
        response = requests.get(next_page_url)
        soup = BeautifulSoup(response.content, 'html.parser')
    else:
        break


with open('laptops.json', 'w') as json_file:
    json.dump(all_laptops, json_file, indent=4)