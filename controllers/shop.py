# Import the needed libraries.
from flask import Blueprint, render_template
from bson.objectid import ObjectId

# Create the shop blueprint.
shop = Blueprint('shop', __name__, template_folder='templates')

# Import the database.
from app import products_db

# GET / aka the homepage.
@shop.route('/')
def index():
    # Gather the needed information.
    kmarge = {
        'title': 'Home',
        'path': '/home'
    }

    # Render the page.
    return render_template('index.html', **kmarge)

# GET /products
# The routes gives the list of products.
@shop.route('/products')
def products():
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
        'title': 'Products',
        'path': '/products',
        'items': products
    }

    # Render the page.
    return render_template('products.html', **kmarge)


@shop.route("/product-view/<id>")
def product_view(id):
    # Connect to the database and get the product with the right id.
    products = []
    data = products_db.find({'_id': ObjectId(id)})
    for product in data:
        output = {
            'id': str(product['_id']),
            'title': product['title'],
            'imageUrl': product['imageUrl'],
            'description': product['description'],
            'price': product['price']
        }
        products = output

    # Gather the needed information.
    kmarge = {
        'title': 'Products',
        'path': '/products',
        'item': products
    }

    # Render the page.
    return render_template('product-view.html', **kmarge)


# GET /order
# The routes gives the order form.
@shop.route('/order')
def order():
    # Gather the needed information.
    kmarge = {
        'title': 'Order',
        'path': '/order'
    }

    # Render the page.
    return render_template('order.html', **kmarge)

# GET /contact
# The route gives the contact form.
@shop.route('/contact')
def contact_us():
    # Gather the needed information.
    kmarge = {
        'title': 'Contact Us',
        'path': '/contact'
    }

    # Render the page.
    return render_template('contact.html', **kmarge)

# GET /about
# The route give the about information.
@shop.route('/about')
def about_us():
    # Gather the needed information.
    kmarge = {
        'title': 'About Us',
        'path': '/about'
    }

    # Render the page.
    return render_template('about.html', **kmarge)