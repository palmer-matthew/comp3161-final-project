from random import random
import random
from app import app
from flask import render_template, url_for, redirect, flash, request, session
from .forms import addRecipe
from .function import *

@app.route("/")
def home():
    session['log'] = True
    if session.get('log') == None:
        return render_template('home.html', log=False)
    else:
        return render_template('home.html', log=session.get('log'))


@app.route("/addrecipe")
def addrecipe():
    recipeform = addRecipe()
    return render_template('addrecipe.html' , form=recipeform)

@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response

"""Yannik Lyn Fatt"""
@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404
    
def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ), 'danger')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)