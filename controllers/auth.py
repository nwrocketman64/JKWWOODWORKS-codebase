# Import the needed libraries.
from flask import Blueprint, render_template

# Create the authentication blueprint.
auth = Blueprint('auth', __name__, template_folder='templates')

@auth.route('/login')
def login():
    # Gather the needed information.
    kmarge = {
        'title': 'login',
        'path': '/home'
    }

    # Render the page.
    return render_template('login.html', **kmarge)