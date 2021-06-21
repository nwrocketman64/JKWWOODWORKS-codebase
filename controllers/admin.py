# Import the needed libraries.
from flask import Blueprint, render_template

# Create the shop blueprint.
admin = Blueprint('admin', __name__, template_folder='templates')

# Import the database.
from app import products_db

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