# Import Flask for creating the web application and jsonify for converting Python dictionaries to JSON responses
from flask import Flask, jsonify

# Initialize the Flask application
app = Flask(__name__)

# Define a route for the '/products' endpoint that handles GET requests
@app.route('/products', methods=['GET'])
def get_products():
    # Define a list of sample products with IDs and names
    products = [
        {"id": 1, "name": "Laptop"},
        {"id": 2, "name": "Phone"}
    ]
    
    # Return the product list as a JSON response
    return jsonify(products)

# Run the application on host '0.0.0.0' and port 5000 if this file is executed directly
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
