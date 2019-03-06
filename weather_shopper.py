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
    return render_template('moisturizer.html')

@app.route("/sunscreen")
def sunscreen():
    "Return a list of sunscreens"
    return render_template('sunscreen.html')

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