import requests
from bs4 import BeautifulSoup

class Item:
    def __init__(self, link):
        self.soup = BeautifulSoup(requests.get(link).text,
                                  features="html.parser")
        self.name = self.soup.find('h1', {'class' : 'name'}).text
        self.sale = self.soup.find('div',{'class' : 'sale-value'}).text
        self.sale_size = self.soup.find('div', {'class' : 'last-sale-block'}
                                       ).find('div',
                                              {'class' : 'size-container'}).text
        self.sale_full = self.soup.find('div',{'class' : 'last-sale'}).text
        self.low = self.soup.find('div', {'class' : 'bid bid-button-b'}).find(
            'div', {'class' : 'stat-value stat-small'}).text
        self.low_size = self.soup.find('div', {'class' : 'bid bid-button-b'}
                                       ).find('div',
                                              {'class' : 'size-container'}).text
        self.high = self.soup.find('div', {'class' : 'ask ask-button-b'}).find(
            'div', {'class' : 'stat-value stat-small'}).text
        self.high_size = self.soup.find('div', {'class' : 'ask ask-button-b'}
                                       ).find('div',
                                              {'class' : 'size-container'}).text



if __name__ == '__main__':
	item1 = Item('https://stockx.com/adidas-yeezy-boost-350-v2-static')
	item2 = Item('https://stockx.com/adidas-yeezy-boost-350-v2-cream-white')
	item3 = Item('https://stockx.com/adidas-yeezy-boost-350-v2-white-core-black-red')
	item4 = Item('https://stockx.com/adidas-yeezy-boost-350-v2-beluga-2-0')
	items = [item1, item2, item3, item4]

	for x in items:
	    print(x.name)
	    print("Last Sale: " + x.sale + ", for a " + x.sale_size)
	    #print(item1.sale_full)
	    print("Lowest Ask: " + x.low + ", for a " + x.low_size)
	    print("Highest Bid: " + x.high + ", for a " + x.high_size + "\n")





