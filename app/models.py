from . import db, login_manager
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


class User(db.Model, UserMixin):
    '''
    Define User model
    '''
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(60), index=True, unique=True)
    username = db.Column(db.String(60), index=True, unique=True)
    fullname = db.Column(db.String(60), index=True)
    user_pwd = db.Column(db.String(128))
    is_admin = db.Column(db.Boolean, default=False)
    # relationships
    counties = db.relationship('County', backref='user', lazy='dynamic')
    constituencies = db.relationship(
        'Constituency', backref='user', lazy='dynamic')
    parties = db.relationship('Party', backref='user', lazy='dynamic')
    governors = db.relationship('Governor', backref='user', lazy='dynamic')
    deputygovernors = db.relationship(
        'DeputyGovernor', backref='county', lazy='dynamic')
    senators = db.relationship('Senator', backref='user', lazy='dynamic')
    womenreps = db.relationship('WomanRep', backref='user', lazy='dynamic')
    mcas = db.relationship('MCA', backref='user', lazy='dynamic')

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))


class County(db.Model):
    __tablename__ = "counties"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256))
    # county_code = db.Column(db.String(60))
    # relationships
    constituencies = db.relationship(
        'Constituency', backref='county', lazy='dynamic')
    governors = db.relationship('Governor', backref='county', lazy='dynamic')
    deputygovernors = db.relationship(
        'DeputyGovernor', backref='county', lazy='dynamic')
    senators = db.relationship('Senator', backref='county', lazy='dynamic')
    womenreps = db.relationship('WomanRep', backref='county', lazy='dynamic')
    mcas = db.relationship('MCA', backref='county', lazy='dynamic')


class Constituency(db.Model):
    __tablename__ = 'constituencies'
    id = db.Column(db.Integer, primary_key=True)
    constituency_code = db.Column(db.Integer)
    name = db.Column(db.String(256))
    # foreign keys
    county_code = db.Column(db.Integer, db.ForeignKey('counties.id'))
    # relationships
    mca = db.relationship('MCA', backref='constituency', lazy='dynamic')


class Party(db.Model):
    __tablename__ = 'parties'
    id = db.Column(db.Integer, primary_key=True)
    party_code = db.Column(db.String(60))
    name = db.Column(db.String(256))
    abrv = db.Column(db.String(256))
    # relationships
    governors = db.relationship(
        'Governor', backref='party', lazy='dynamic')
    deputygovernors = db.relationship(
        'DeputyGovernor', backref='party', lazy='dynamic')
    senators = db.relationship('Senator', backref='party', lazy='dynamic')
    womenreps = db.relationship('WomanRep', backref='party', lazy='dynamic')
    mcas = db.relationship('MCA', backref='party', lazy='dynamic')


class Governor(db.Model):
    __tablename__ = 'governors'
    id = db.Column(db.Integer, primary_key=True)

    surname = db.Column(db.String(256))
    othernames = db.Column(db.String(256))
    # Foreign keys
    county_code = db.Column(db.Integer, db.ForeignKey('counties.id'))
    party_code = db.Column(db.Integer, db.ForeignKey('parties.id'))
    # relationships
    deputygovernors = db.relationship(
        'DeputyGovernor', backref='governor', lazy='dynamic')


class DeputyGovernor(db.Model):
    __tablename__ = 'deputygovernors'
    id = db.Column(db.Integer, primary_key=True)

    surname = db.Column(db.String(256))
    othernames = db.Column(db.String(256))
    # Foreign keys
    county_code = db.Column(db.Integer, db.ForeignKey('counties.id'))
    party_code = db.Column(db.Integer, db.ForeignKey('parties.id'))
    governor_id = db.Column(db.Integer, db.ForeignKey('governors.id'))


class Senator(db.Model):
    __tablename__ = 'senators'
    id = db.Column(db.Integer, primary_key=True)
    surname = db.Column(db.String(256))
    othernames = db.Column(db.String(256))
    # Foreign keys
    county_code = db.Column(db.Integer, db.ForeignKey('counties.id'))
    party_code = db.Column(db.Integer, db.ForeignKey('parties.id'))


class WomanRep(db.Model):
    __tablename__ = 'womenreps'
    id = db.Column(db.Integer, primary_key=True)
    surname = db.Column(db.String(256))
    othernames = db.Column(db.String(256))
    # Foreign keys
    county_code = db.Column(db.Integer, db.ForeignKey('counties.id'))
    party_code = db.Column(db.Integer, db.ForeignKey('parties.id'))


class MCA(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    surname = db.Column(db.String(256))
    othernames = db.Column(db.String(256))
    # Foreign keys
    constituency_code = db.Column(
        db.Integer, db.ForeignKey('constituencies.id'))
    county_code = db.Column(db.Integer, db.ForeignKey('counties.id'))
    party_code = db.Column(db.Integer, db.ForeignKey('parties.id'))
