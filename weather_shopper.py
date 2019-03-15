"""
Flask app built to teach trainees Selenium
"""

from flask import Flask
from flask import render_template
from flask import request
from flask import redirect, url_for
from flask import _request_ctx_stack
from flask import jsonify
import random 

app = Flask(__name__)

@app.route("/")
def index():
    "Return the home page"
    return render_template('index.html')

@app.route("/moisturizer")
def moisturizer():
    "Return a list of moisturizers"
    all_moisturizers = [{'Wilhelm Aloe Hydration Lotion':365},
    {'Emmanuel Aloe Vera Beauty Gel':299},
    {'Jose Intensive Care Aloe Body Lotion':216},
    {'Alexander Almond & Honey Moisturiser':360},
    {'Max honey and almond moisturiser':195},
    {'Mikhail Natural Almond Moisturizer':220},
    {'Vassily Aloe Attack':199},
    {'Mikhail Almond and Talc':353},
    {'Tigran Aloe Isolani':215},
    {'Boris Almond and Honey':128}]
    moisturizers = random.sample(all_moisturizers,6)

    return render_template('moisturizer.html', moisturizers=moisturizers)

@app.route("/sunscreen")
def sunscreen():
    "Return a list of sunscreens"
    all_sunscreens = [{'Robert Herbals Sunblock SPF-40':350},
    {'Anatoly Ultra Sunblock SPF-50':289},
    {'Gary Bio Sandalwood SPF-50':250},
    {'Vladimir Sun Expert SPF-30':160},
    {'Vishy La Shield Sunscreen spf-30':195},
    {'Magnus Resistant Sunscreen SPF-30':140},
    {'Paul Magnificient SPF-30':121},
    {'Akiba Amazing SPF-50':222},
    {'Vassily Brilliant SPF-30':116}]
    sunscreens = random.sample(all_sunscreens,6)

    return render_template('sunscreen.html', sunscreens=sunscreens)

@app.route("/cart", methods=['GET', 'POST'])
def submit_cart():
    "Go to the cart page"
    cart_items = request.form 
    total_price = 0
    for key,value in cart_items.items():
        total_price += int(value)
        app.logger.info(key)
        app.logger.info(value)
    app.logger.info(cart_items)

    return render_template('cart.html', cart_items=cart_items, total_price=total_price)

@app.route("/confirmation", methods=['POST'])
def confirmation():
    "Confirm the payments"
    result = True if random.uniform(0,1) <0.95 else False
    return render_template('confirmation.html', flag=result)


#----START OF SCRIPT
if __name__=='__main__':
    app.run(host='0.0.0.0',port=6464)