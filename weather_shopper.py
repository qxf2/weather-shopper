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
    all_moisturizers = [{'Wilhelm Aloe Hydration Lotion':{'price':365,'img':'moisturizer_wilhelm.png'}},
    {'Emmanuel Aloe Vera Beauty Gel':{'price':299,'img':'moisturizer_emmanuel.png'}},
    {'Jose Intensive Care Aloe Body Lotion':{'price':216,'img':'moisturizer_jose.png'}},
    {'Alexander Almond & Honey Moisturiser':{'price':360,'img':'moisturizer_alexander.png'}},
    {'Max honey and almond moisturiser':{'price':195,'img':'moisturizer_max.png'}},
    {'Mikhail Natural Almond Moisturizer':{'price':220,'img':'moisturizer_mikhail.png'}},
    {'Vassily Aloe Attack':{'price':199,'img':'moisturizer_vassily.png'}},
    {'Mikhail Almond and Talc':{'price':353,'img':'moisturizer_tal.png'}},
    {'Tigran Aloe Isolani':{'price':215,'img':'moisturizer_tigran.png'}},
    {'Boris Almond and Honey':{'price':128,'img':'moisturizer_boris.png'}}]
    moisturizers = random.sample(all_moisturizers,6)

    return render_template('moisturizer.html', moisturizers=moisturizers)

@app.route("/sunscreen")
def sunscreen():
    "Return a list of sunscreens"
    all_sunscreens = [{'Robert Herbals Sunblock SPF-40':{'price':350,'img':'sunscreen_robert.png'}},
    {'Anatoly Ultra Sunblock SPF-50':{'price':289,'img':'sunscreen_anatoly.png'}},
    {'Gary Bio Sandalwood SPF-50':{'price':250,'img':'sunscreen_gary.png'}},
    {'Vladimir Sun Expert SPF-30':{'price':160,'img':'sunscreen_vladimir.png'}},
    {'Vishy La Shield Sunscreen spf-30':{'price':195,'img':'sunscreen_vishy.png'}},
    {'Magnus Resistant Sunscreen SPF-30':{'price':140,'img':'sunscreen_magnus.png'}},
    {'Paul Magnificient SPF-30':{'price':121,'img':'sunscreen_paul.png'}},
    {'Akiba Amazing SPF-50':{'price':222,'img':'sunscreen_akiba.png'}},
    {'Vassily Brilliant SPF-30':{'price':116,'img':'sunscreen_vassily.png'}}]
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