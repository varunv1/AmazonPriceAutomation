import csv
import requests
from bs4 import BeautifulSoup
from write_to_csv import write_to_csv

def fetch_data_from_az(sku_id):
    base_url = f'https://www.amazon.in/dp/{sku_id}'
    # headers are needed to include user agent to get amazon website
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:80.0) Gecko/20100101 Firefox/80.0'}
    # make the request to amazon
    page = requests.get(base_url, headers=headers)
    soup = BeautifulSoup(page.content, "html.parser")
    
    # search for elements
    availability = soup.find(id='availability')
    availability = availability.find('span')
    price = soup.find('span', class_ = 'a-price-whole')

    if(len(price.contents) and len(availability.contents)):
        # return data 
        return price.contents[0].strip(), availability.contents[0].strip()
    return '', ''

if __name__ == '__main__':
    filename = 'products.csv'
    final_data =[]
    # csv file headers
    csvFieldNames = ['sku', 'price', 'availability']
    # read the csv file
    with open(filename, newline='') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            price, availability = fetch_data_from_az(row['sku'])
            final_data.append({
                'sku': row['sku'],
                'price': price,
                'availability': availability
            })
    write_to_csv(filename, csvFieldNames, final_data)
