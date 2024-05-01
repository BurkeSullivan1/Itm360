from flask import Flask, request, jsonify
from flask_cors import CORS  # Import CORS
import flask_login
from FinalDb import check_user, create_user, get_user_details, update_user_plan
import logging

app = Flask(__name__)
app.secret_key = 'your_secret_key'
logging.basicConfig(level=logging.DEBUG)

# Setup CORS with support for credentials
CORS(app, supports_credentials=True)


login_manager = flask_login.LoginManager()
login_manager.init_app(app)

# user class for flask login
class User(flask_login.UserMixin):
    def __init__(self, id, username, age):
        self.id = id
        self.username = username
        self.age = age
##load user manager
@login_manager.user_loader
def load_user(user_id):
    # Assuming get_user_details fetches user details correctly
    user_info = get_user_details(user_id)
    if user_info:
        return User(user_info['id'], user_info['username'], user_info['age'])
    return None
# login
@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    user_info = check_user(username, password)
    if user_info:
        user_obj = User(user_info['id'], username, user_info['age'])
        flask_login.login_user(user_obj, remember=True)  # Ensure the session is set to remember if necessary
        app.logger.info(f"User {user_obj.username} logged in successfully.")
        return jsonify(success=True, id=user_obj.id, username=user_obj.username, age=user_obj.age, insurance_type=user_info['insurance_type'], message="Logged in successfully.")
    return jsonify(success=False, message="Invalid credentials.")

@app.route('/update_plan', methods=['POST'])
@flask_login.login_required
def update_plan():
    user_id = flask_login.current_user.id
    new_plan = request.form.get('new_plan')
    logging.debug(f"Received plan update request from user {user_id} to change plan to {new_plan}")
    if not new_plan:
        logging.error("No new plan provided")
        return jsonify(success=False, message="No new plan provided."), 400
    try:
        update_user_plan(user_id, new_plan)
        logging.info(f"Plan updated to {new_plan} for user {user_id}")
        return jsonify(success=True, message="Insurance plan updated successfully.")
    except Exception as e:
        logging.error(f"Error updating plan for user {user_id}: {e}")
        return jsonify(success=False, message=str(e)), 500
# route to register user
@app.route('/register', methods=['POST'])
def register():
    username = request.form['username']
    password = request.form['password']
    insurance_type = request.form['insurance_type']
    age = request.form['age']  # Retrieve age from form data
    create_user(username, password, insurance_type, age)  # Pass age to the create_user function
    return jsonify(success=True, message="User registered successfully.")


@app.route('/protected')
@flask_login.login_required
def protected():
    app.logger.info(f"Accessing protected route by user {flask_login.current_user.username}")
    return jsonify(data=f"Secret data for {flask_login.current_user.username}")

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)