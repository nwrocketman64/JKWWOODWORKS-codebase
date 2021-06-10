# Import the needed libraries.
from flask import Flask, render_template
from flask_session import Session

# Import the controllers.
from controllers.shop import shop
from controllers.auth import auth

# Create the applications.
app = Flask(__name__)

# Configure the sessions in the web app.
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
app.secret_key = "\xd5$\xa2\xd5\xd8\x06\xab\xa4\xb5\x86\xec\xf1Tn[s"
Session(app)

# Call the shop blueprint.
app.register_blueprint(auth)
app.register_blueprint(shop)

# The 404 handler.
@app.errorhandler(404)
def not_found(e):
    # Gather the need information.
    kmarge = {
        'title': 'Page Not Found',
        'path': '/home'
    }

    # Render the page and return the 404 code.
    return render_template('404.html', **kmarge), 404

# Start the application.
if __name__ == '__main__':
    app.run(debug=True)