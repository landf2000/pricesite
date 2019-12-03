import requests
from bs4 import BeautifulSoup

item1 = BeautifulSoup(requests.get('https://cuddlypanda5.github.io/index.html').text,
                      features="html.parser")
print(item1.find('div',
                 {'class' :
                  "col-12 col-sm-4 col-lg-2 text-center vertical-align"}).text)
