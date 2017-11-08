from flask import flash, redirect, render_template, url_for, request
from flask_login import login_required, login_user, logout_user

from . import auth
from . forms import RegistrationForm, LoginForm
from .. import db
from app.models import User


@auth.route('/register', methods=['GET', 'POST'])
def register():
    '''
    handles requests to the /register route
    adds a user to the db
    '''
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(email=form.email.data,
                    username=form.username.data,
                    fullname=form.fullname.data,
                    password=form.password.data)

        # save user in database
        user.save_user()
        flash('You have successfully registered!')

        # redirect to login page
        return redirect(url_for('auth.login'))
    # load Registration Form - registration template
    title = "Create New Account"
    return render_template('auth/register.html', form=form, title=title)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    '''
    handles requests to the login route
    logs on / signs in through the login form
    '''
    # craete an instnace pf the LoginForm
    login_form = LoginForm()

    if login_form.validate_on_submit():
        '''
        check whether user exists in DB through email and
        whether the pwd entered matches the pwd in DB
        '''
        user = User.query.filter_by(email=login_form.email.data).first()
        if user is not None and user.verify_password(login_form.password.data):
            # sign in
            login_user(user)

            # redirect user to the appropriate dashboard page
            if user.is_admin:
                return redirect(url_for('main.admin_dashboard'))
            else:
                return redirect(url_for('main.dashboard'))
        else:
            flash("Inavlid email or password")
    title = "Ugatuzi Sign In"
    return render_template('auth/login.html', login_form=login_form, title=title)


@auth.route('/logout')
@login_required
def logout():
    """
    Handle requests to the /logout route
    Log user out through the logout link
    """
    logout_user()
    flash('You have successfully been logged out.')

    # redirect to the login page
    return redirect(url_for('auth.login'))
