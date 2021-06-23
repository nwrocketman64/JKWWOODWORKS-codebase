# Import the needed libraries.
from flask import Blueprint, render_template, request, redirect
from webargs import flaskparser, fields

# Create the shop blueprint.
admin = Blueprint('admin', __name__, template_folder='templates')

# Import the database.
from app import products_db

# GET and POST /admin/add-products
@admin.route('/admin/add-products', methods = ['POST', 'GET'])
def add_products():
    if request.method == 'POST':
        # Get the information from the request.
        name = request.form['name']
        price = request.form['price']
        options = request.form['options']
        description = request.form['description']
        imageUrl = request.form['imageUrl']

        # Validate the form input.
        if (bool(name) and bool(price) and bool(options) and bool(description) and bool(imageUrl)):
            # Prepare the information to be inserted in the database.
            product = {
                'title': name,
                'price': price,
                'options': options,
                'description': description,
                'imageUrl': imageUrl
            }

            # Insert the product into the database.
            result = products_db.insert_one(product)

            # Print the results.
            print('Result:', result)

            # Direct the user back the admin page.
            return redirect('/admin')
        
        # If failed, rerender the add-product page.
        else:
            # Gather the needed information.
            kmarge = {
                'title': 'Add Product',
                'path': '/home',
                'productTitle': name,
                'price': price,
                'options': options,
                'description': description,
                'imageUrl': imageUrl
            }

            # Render the page.
            return render_template('add-product.html', **kmarge)

    else:
        # Gather the needed information.
        kmarge = {
            'title': 'Add Product',
            'path': '/home'
        }

        # Render the page.
        return render_template('add-product.html', **kmarge)

# GET /admin
@admin.route('/admin')
def admin_page():
    # Connect to the database and get all the products.
    products = []
    data = products_db.find()
    for product in data:
        output = {
            'id': str(product['_id']),
            'title': product['title'],
            'imageUrl': product['imageUrl'],
            'description': product['description'],
            'price': product['price']
        }
        products.append(output)
    
    # Gather the needed information.
    kmarge = {
        'title': 'Admin',
        'path': '/home',
        'products': products
    }

    # Render the page.
    return render_template('admin.html', **kmarge)