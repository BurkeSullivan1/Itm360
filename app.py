from flask import Flask,request
from flask_login import LoginManager
from routes import blueprint  # Ensure this is the correct import from your routes.py
from models import User  # This imports the User class from models.py

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'your_secret_key_here'  # Consider using a more secure way to set secret keys

    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'  # Redirects unauthenticated users to the login page

    @login_manager.user_loader
    def load_user(user_id):
        # This function reloads the user object from the user ID stored in the session
        return User.get(user_id)

    app.register_blueprint(blueprint)  # Register your routes blueprint

    return app
from werkzeug.security import generate_password_hash, check_password_hash

from werkzeug.security import generate_password_hash, check_password_hash

# Use controlled parameters for scrypt
test_password = '66'
scrypt_hash = generate_password_hash(test_password, method='scrypt', salt_length=8)
print("Generated scrypt Hash:", scrypt_hash)
scrypt_check_result = check_password_hash(scrypt_hash, test_password)
print("scrypt Check Result:", scrypt_check_result)





if __name__ == "__main__":

    app = create_app()
    print(app.url_map)  # This will print the URL map to the console for debugging
    app.run(debug=True)  # Turn on debugger and reloader
