from flask import render_template, redirect, url_for
from app import app

@app.route('/')
@app.route('/index')

def index():
    return render_template('index.html')

def club():
    return render_template('club.html')

def media():
    return render_template('media.html')

def horaires():
    return render_template('horaires.html')

def ffme():
    return redirect('https://www.ffme69.fr')
