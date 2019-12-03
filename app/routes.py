from flask import render_template
from app import app
from request import Item



@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Tony'}
    return render_template('index.html', title='Home', user=user)

@app.route('/price')
def price():
    user = {'username': 'Tony'}
    item1 = Item('https://stockx.com/adidas-yeezy-boost-350-v2-static')
    item2 = Item('https://stockx.com/adidas-yeezy-boost-350-v2-cream-white')
    item3 = Item('https://stockx.com/adidas-yeezy-boost-350-v2-white-core-black-red')
    item4 = Item('https://stockx.com/adidas-yeezy-boost-350-v2-beluga-2-0')
    items = [item1, item2, item3, item4]
    return render_template('price.html', title='Home', user=user, items=items)

@app.route('/test')
def test():
	return "test"
