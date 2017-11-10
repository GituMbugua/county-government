from flask import flash, render_template, abort
from flask_login import login_required, current_user
from . import main
from .. import db
from app.models import County, Constituency, Governor, DeputyGovernor, Senator, WomanRep, MCA


@main.route('/')
def index():
    '''
    render homepage template on the /route
    '''
    return render_template('index.html', title='Welcome to Gypsy Blogs')


@main.route('/dashboard')
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


@main.route('/regions', methods=['GET', 'POST'])
def find_regions():
    counties = County.query.all()
    print(counties)
    return render_template('regions/regions.html', counties=counties)


@main.route('/constituencies', methods=['GET', 'POST'])
def find_constituencies():
    counties = County.query.all()
    print(counties)
    return render_template('regions/regions.html', counties=counties)


@main.route('/executives/governors', methods=['GET', 'POST'])
def find_governors():
    deputygovernors = DeputyGovernor.query.all()
    print(deputygovernors)
    return render_template('executives/governors.html', deputygovernors=deputygovernors)


@main.route('/executives/senators', methods=['GET', 'POST'])
def find_senators():
    senators = Senator.query.all()
    print(senators)
    return render_template('executives/senators.html', senators=senators)


@main.route('/executives/womenreps', methods=['GET', 'POST'])
def find_womenreps():
    womenreps = WomanRep.query.all()
    print(womenreps)
    return render_template('executives/womenreps.html', womenreps=womenreps)
