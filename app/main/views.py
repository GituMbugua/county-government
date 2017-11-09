<<<<<<< HEAD
from flask import render_template, request, redirect, url_for, abort
from . import main
=======
from flask import flash, render_template, abort
from flask_login import login_required, current_user
from . import main
from .. import db

>>>>>>> 7319c7d6518d1a577598c2ecab03500078cba31e

@main.route('/')
def index():
    '''
<<<<<<< HEAD
    view route page that returns index page
    '''
    title = 'Home'
    return render_template('index.html', title = title)

@main.route('/counties')
def counties():
    '''
    display the counties in this route
    '''
    title = 'Counties'
    return render_template('counties.html')
=======
    render homepage template on the /route
    '''
    return render_template('index.html', title='Welcome to Gypsy Blogs')


@main.route('/dashboard')
@login_required
def dashboard():
    return render_template('main/dashboard.html', title='Dashboard')

# admin dashboard view


@main.route('/admin/dashboard')
@login_required
def admin_dashboard():
    # prevent non-admins from accessing the admin dashboard
    if not current_user.is_admin:
        abort(403)
    title = "Ugatuzi Admin"
    return render_template('admin/admin_dashboard.html', title=title)
>>>>>>> 7319c7d6518d1a577598c2ecab03500078cba31e
