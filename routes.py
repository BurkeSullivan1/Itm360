from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user
from models import User, db_connect  # Make sure these are correctly imported
from werkzeug.security import generate_password_hash, check_password_hash

blueprint = Blueprint('auth', __name__, template_folder='templates')

@blueprint.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        mno = request.form['mno']
        password = request.form['password']
        print(f"Received password: {password}")  # This should show the plaintext password
        user = User.authenticate(mno, password)
        if user:
            login_user(user)
            return redirect(url_for('auth.protected'))
        else:
            flash('Invalid member number or password')
            return redirect(url_for('auth.invalid'))
    return render_template('login.html')

@blueprint.route('/invalid')
def invalid():
    return 'Invalid login attempt. Please try again.', 200

@blueprint.route('/protected')
@login_required
def protected():
    conn = db_connect()
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT Bno FROM Issue WHERE Mno = %s", (current_user.get_id(),))
        bnos = cursor.fetchall()
        bnames = []
        for bno in bnos:
            cursor.execute("SELECT Bname FROM Bookrecord WHERE Bno = %s", (bno[0],))
            bname = cursor.fetchone()
            if bname:
                bnames.append(bname[0])
    finally:
        cursor.close()
        conn.close()
    return render_template('protected.html', books=bnames, user=current_user)

@blueprint.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

@blueprint.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        mno = request.form['mno']
        password = request.form['password']
        existing_user = User.get(mno)
        if existing_user is None:  # Check if the user does not already exist
            hashed_password = generate_password_hash(password)
            new_user = User.create(mno, hashed_password)
            if new_user:
                flash('Account created successfully! Please log in.')
                return redirect(url_for('auth.login'))
            else:
                flash('Failed to create an account. Please try again.')
        else:
            flash('Member number already exists. Please use a different member number or log in.')
            return redirect(url_for('auth.signup'))  # Optionally redirect back to signup page

    return render_template('signup.html')
