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


@main.route('/regions/constituencies', methods=['GET', 'POST'])
def find_constituencies():
    # county = County.query.get(id)

    Mombasa = Constituency.get_constituencies(1)
    Kwale = Constituency.get_constituencies(2)
    Kilifi = Constituency.get_constituencies(3)
    TanaRiver = Constituency.get_constituencies(4)
    Lamu = Constituency.get_constituencies(5)
    TaitaTaveta = Constituency.get_constituencies(6)
    Garissa = Constituency.get_constituencies(7)
    Wajir = Constituency.get_constituencies(8)
    Mandera = Constituency.get_constituencies(9)
    Marsabit = Constituency.get_constituencies(10)
    Isiolo = Constituency.get_constituencies(11)
    Meru = Constituency.get_constituencies(12)
    TharakaNithi = Constituency.get_constituencies(13)
    Embu = Constituency.get_constituencies(14)
    Kitui = Constituency.get_constituencies(15)
    Machakos = Constituency.get_constituencies(16)
    Makueni = Constituency.get_constituencies(17)
    Nyandarua = Constituency.get_constituencies(18)
    Nyeri = Constituency.get_constituencies(19)
    Kirinyaga = Constituency.get_constituencies(20)
    Muranga = Constituency.get_constituencies(21)
    Muranga = Constituency.get_constituencies(21)
    Kiambu = Constituency.get_constituencies(22)
    Turkana = Constituency.get_constituencies(23)
    WestPokot = Constituency.get_constituencies(24)
    Samburu = Constituency.get_constituencies(25)
    TransNzoia = Constituency.get_constituencies(26)
    UasinGishu = Constituency.get_constituencies(27)
    ElgeyoMarakwet = Constituency.get_constituencies(28)
    Nandi = Constituency.get_constituencies(29)
    Baringo = Constituency.get_constituencies(30)
    Laikipia = Constituency.get_constituencies(31)
    Nakuru = Constituency.get_constituencies(32)
    Narok = Constituency.get_constituencies(33)
    Kajiado = Constituency.get_constituencies(34)
    Kericho = Constituency.get_constituencies(35)
    Bomet = Constituency.get_constituencies(36)
    Kakamega = Constituency.get_constituencies(37)
    Vihiga = Constituency.get_constituencies(38)
    Bungoma = Constituency.get_constituencies(39)
    Busia = Constituency.get_constituencies(40)
    Siaya = Constituency.get_constituencies(41)
    Kisumu = Constituency.get_constituencies(42)
    HomaBay = Constituency.get_constituencies(43)
    Migori = Constituency.get_constituencies(44)
    Kisii = Constituency.get_constituencies(45)
    Nyamira = Constituency.get_constituencies(46)
    Nairobi = Constituency.get_constituencies(47)

    return render_template('regions/constituencies.html', Mombasa=Mombasa, Kwale=Kwale, Kilifi=Kilifi, TanaRiver=TanaRiver, Lamu=Lamu, TaitaTaveta=TaitaTaveta, Garissa=Garissa, Wajir=Wajir, Mandera=Mandera, Marsabit=Marsabit, Isiolo=Isiolo, Meru=Meru, TharakaNithi=TharakaNithi, Embu=Embu, Kitui=Kitui, Machakos=Machakos, Makueni=Makueni, Nyandarua=Nyandarua, Nyeri=Nyeri, Kirinyaga=Kirinyaga, Muranga=Muranga, Kiambu=Kiambu, Turkana=Turkana, WestPokot=WestPokot, Samburu=Samburu, TransNzoia=TransNzoia, UasinGishu=UasinGishu, ElgeyoMarakwet=ElgeyoMarakwet, Nandi=Nandi, Baringo=Baringo, Laikipia=Laikipia, Nakuru=Nakuru, Narok=Narok, Kajiado=Kajiado, Kericho=Kericho, Bomet=Bomet, Kakamega=Kakamega, Vihiga=Vihiga, Bungoma=Bungoma, Busia=Busia, Siaya=Siaya, Kisumu=Kisumu, HomaBay=HomaBay, Migori=Migori, Kisii=Kisii, Nyamira=Nyamira, Nairobi=Nairobi)


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
