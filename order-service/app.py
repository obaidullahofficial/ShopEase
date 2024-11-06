# Import Flask for creating the web application and jsonify for converting Python dictionaries to JSON responses
from flask import Flask, jsonify

# Import requests to make HTTP requests to other services
import requests

# Initialize the Flask application
app = Flask(__name__)

# Define a route for the '/orders' endpoint that handles GET requests
@app.route('/orders', methods=['GET'])
def create_order():
    # Make a request to the user service to get user data
    users = requests.get('http://user-service:5000/users').json()
    
    # Make a request to the product service to get product data
    products = requests.get('http://product-service:5000/products').json()
    
    # Create an order by selecting the first user and first product from the responses
    order = {
        "user": users[0],  # Just pick the first user
        "product": products[0]  # Pick the first product
    }
    
    # Return the order as a JSON response
    return jsonify(order)

# Run the application on host '0.0.0.0' and port 5000 if this file is executed directly
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
