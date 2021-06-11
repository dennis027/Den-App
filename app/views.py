from flask import render_template
from app import app

#Views
@app.route('/')
def index():
    '''
    view root page function that returns index page and its data
    '''
    title = 'Home -Welcome to Deman App where you will get the best User Experience'
    return render_template('index.html')
