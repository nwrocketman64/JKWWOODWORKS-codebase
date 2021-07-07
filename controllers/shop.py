# Import the needed libraries.
from flask import Blueprint, render_template, session

# Create the shop blueprint.
shop = Blueprint('shop', __name__, template_folder='templates')

# Import the database.
from app import Products

# GET / aka the homepage.
@shop.route('/')
def index():
    # Connect to the database and get the product with the right id.
    products = Products.get_products()

    # Gather the needed information.
    kmarge = {
        'title': 'Home',
        'path': '/home',
        'product': products[len(products) - 1]
    }

    # Render the page.
    return render_template('index.html', **kmarge)

# GET /products
# The routes gives the list of products.
@shop.route('/products')
def products():
    # Connect to the database and get all the products.
    products = Products.get_products()

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
    product = Products.get_product(id)

    # Gather the needed information.
    kmarge = {
        'title': product['title'],
        'path': '/products',
        'item': product
    }

    # Render the page.
    return render_template('product-view.html', **kmarge)

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