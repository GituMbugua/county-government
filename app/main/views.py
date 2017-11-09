from flask import flash, render_template, abort
from flask_login import login_required, current_user
from . import main
from .. import db


@main.route('/')
def index():
    '''
    render homepage template on the /route
    '''
    return render_template('index.html', title='Welcome to Gypsy Blogs')

@main.route('/counties')
def counties():

    return render_template('counties.html')


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

@main.route('/search/<county_name>')
def search_county(county_name):
    county_name_list = county_name.split(" ")
    county_name_format = "+".join(county_name_list)
    searched_counties = search_county(county_name_format)
    title = f"Search results for {county_name}"

    return render_template("search.html", counties = searched_counties)
