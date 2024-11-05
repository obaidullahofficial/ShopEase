# order-service/app.py
from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/orders', methods=['GET'])
def create_order():
    users = requests.get('http://user-service:5000/users').json()
    products = requests.get('http://product-service:5000/products').json()
    order = {
        "user": users[0],  # Just pick the first user
        "product": products[0]  # Pick the first product
    }
    return jsonify(order)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

