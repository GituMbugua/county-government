from . import db, login_manager
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from flask import Flask, request, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy
import uuid
import jwt
import datetime
from functools import wraps


class User(db.Model, UserMixin):
    '''
    Define User model
    '''
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(60), index=True, unique=True)
    username = db.Column(db.String(60), index=True, unique=True)
    fullname = db.Column(db.String(256), index=True)
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

    @property
    def password(self):
        '''
        prevent password from being accessed
        '''
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        '''
        Set password to a hashed password
        '''
        self.user_pwd = generate_password_hash(password)

    def verify_password(self, password):
        '''
        check if hashed pwd matches actual pwd
        '''
        return check_password_hash(self.user_pwd, password)

    def save_user(self):
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return '<Reader: {}>'.format(self.username)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))


class County(db.Model):
    __tablename__ = "counties"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256))
    # foreign keys
    user_id = db.Column(db.ForeignKey('users.id'))
    # relationships
    constituencies = db.relationship(
        'Constituency', backref='county', lazy='dynamic')
    governors = db.relationship('Governor', backref='county', lazy='dynamic')
    deputygovernors = db.relationship(
        'DeputyGovernor', backref='dpgovernor', lazy='dynamic')
    senators = db.relationship(
        'Senator', backref='countysenator', lazy='dynamic')
    womenreps = db.relationship(
        'WomanRep', backref='county', lazy='dynamic')
    mcas = db.relationship('MCA', backref='countymcas', lazy='dynamic')


class Constituency(db.Model):
    __tablename__ = 'constituencies'
    id = db.Column(db.Integer, primary_key=True)
    constituency_code = db.Column(db.Integer)
    name = db.Column(db.String(256))
    # foreign keys
    user_id = db.Column(db.ForeignKey('users.id'))
    county_code = db.Column(db.Integer, db.ForeignKey('counties.id'))
    user_id = db.Column(db.ForeignKey('users.id'))
    # relationships
    mca = db.relationship('MCA', backref='constituency', lazy='dynamic')

    @classmethod
    def get_constituencies(cls, id):
        all_constituencies = Constituency.query.filter_by(county_code=id).all()
        return all_constituencies


class Party(db.Model):
    __tablename__ = 'parties'
    id = db.Column(db.Integer, primary_key=True)
    party_code = db.Column(db.String(60))
    name = db.Column(db.String(256))
    abrv = db.Column(db.String(256))
    # foreign keys
    user_id = db.Column(db.ForeignKey('users.id'))
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
    user_id = db.Column(db.ForeignKey('users.id'))
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
    user_id = db.Column(db.ForeignKey('users.id'))
    county_code = db.Column(db.Integer, db.ForeignKey('counties.id'))
    party_code = db.Column(db.Integer, db.ForeignKey('parties.id'))
    governor_id = db.Column(db.Integer, db.ForeignKey('governors.id'))
    user_id = db.Column(db.ForeignKey('users.id'))


class Senator(db.Model):
    __tablename__ = 'senators'
    id = db.Column(db.Integer, primary_key=True)
    surname = db.Column(db.String(256))
    othernames = db.Column(db.String(256))
    # Foreign keys
    user_id = db.Column(db.ForeignKey('users.id'))
    county_code = db.Column(db.Integer, db.ForeignKey('counties.id'))
    party_code = db.Column(db.Integer, db.ForeignKey('parties.id'))


class WomanRep(db.Model):
    __tablename__ = 'womenreps'
    id = db.Column(db.Integer, primary_key=True)
    surname = db.Column(db.String(256))
    othernames = db.Column(db.String(256))
    # Foreign keys
    user_id = db.Column(db.ForeignKey('users.id'))
    county_code = db.Column(db.Integer, db.ForeignKey('counties.id'))
    party_code = db.Column(db.Integer, db.ForeignKey('parties.id'))


class MCA(db.Model):
    __tablename__ = 'mcas'
    id = db.Column(db.Integer, primary_key=True)
    surname = db.Column(db.String(256))
    othernames = db.Column(db.String(256))
    # Foreign keys
    user_id = db.Column(db.ForeignKey('users.id'))
    constituency_code = db.Column(
        db.Integer, db.ForeignKey('constituencies.id'))
    county_code = db.Column(db.Integer, db.ForeignKey('counties.id'))
    party_code = db.Column(db.Integer, db.ForeignKey('parties.id'))

    @classmethod
    def get_mcas(cls, id):
        all_mcas = MCA.query.filter_by(county_code=id).all()
        return all_mcas
