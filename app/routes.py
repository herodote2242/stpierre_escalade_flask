#!/usr/bin/env python3
# -*- coding: Utf-8 -*

from flask import render_template, redirect
from app import app

@app.route('/')
def visit_index():
    return render_template('index.html')

@app.route('/club')
def visit_club():
    return render_template('club.html')

@app.route('/media')
def visit_media():
    return render_template('media.html')

@app.route('/horaires')
def visit_horaires():
    return render_template('horaires.html')

@app.route('/ffme')
def visit_ffme():
    return redirect('https://www.ffme69.fr')

@app.route('/facebook')
def visit_fb():
    return redirect('https://www.facebook.com/SaintPierreEscalade')
