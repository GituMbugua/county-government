from flask import render_template, request, redirect, url_for, abort
from . import main

@main.route('/')
def index():
    '''
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