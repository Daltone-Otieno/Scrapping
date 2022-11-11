from bs4 import BeautifulSoup
import requests
from csv import writer

url = "https://www.pararius.com/apartments/armsterdam?ac=1"
page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')
lists = soup.find_all('section', class_='listing-search-items')

with open('Housing.csv', 'w', encoding='utf8', newline='') as f:
    theWriter = writer(f)
    header = ['Title', 'Location', 'Price', 'Area']
    theWriter.writerow(header)
    for list in lists:
        title = list.find(
            'a', class_='listing-search-item_link--tittle').text.replace('\n', '')
        location = list.find(
            'div', class_='listing-search-item_location').text.replace('\n', '')
        price = list.find(
            'span', class_='listing-search-item_price').text.replace('\n', '')
        area = list.find(
            'span', class_='illustrated-features_description').text.replace('\n', '')

        info = [title, location, price, area]
        theWriter.writerow(info)
