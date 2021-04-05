import random
from app import app
from flask import render_template, url_for, redirect, flash, request, session, jsonify
from werkzeug.security import generate_password_hash
from .function import *

#Global Values
userid = 1

@app.route("/")
def home():
    session.pop('log', None) 
    if session.get('log') == None:
        return render_template('home.html', log=False)
    else:
        return render_template('home.html', log=session.get('log'))


@app.route("/login", methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != app.config['ADMIN_USERNAME'] or request.form['password'] != app.config['ADMIN_PASSWORD']:
            error = 'Invalid username or password'
        else:
            session['logged_in'] = True
            
            flash('You were logged in', 'success')
            return redirect(url_for('home')) 
    return render_template('login.html', error=error)


@app.route("/Signup")
def Signup():
    return render_template('Signup.html') #error=error)

@app.route('/Signup', methods=['POST'])
def signup_post():
    username = request.form['uname']
    password = request.form['psw']
    fname = request.form['fname']
    lname = request.form['lname']
    
    if getUser(username): 
        return redirect(url_for('signup'))

    if addUser():
        new_user = username(userN= username, fname= fname, lname=lname, password=generate_password_hash(password, method='sha256'))

    return redirect(url_for('login'))
    
@app.route("/Search")
def Search():
    search = request.form['search']
    if SearchRecipe(search) | SearchMealPlan(search):
        return render_template('search.html')

@app.route("/profile")
def profile():
    session['log'] = True
    if session.get('log') == None:
        return render_template('home.html', log=False)
    else:
        result = getIngredientsinKitchen(userid)
        return render_template('profile.html', log=session.get('log'), kitchen=result)

@app.route("/plan")
def plan():
    session['log'] = True
    if session.get('log') == None:
        return render_template('home.html', log=False)
    else:
        return render_template('generate_plan.html', log=session.get('log'))

@app.route("/planview")
def plan_view():
    session['log'] = True
    if session.get('log') == None:
        return render_template('home.html', log=False)
    else:
        return render_template('plan_view.html', log=session.get('log'))

@app.route("/shopping")
def shopping():
    session['log'] = True
    if session.get('log') == None:
        return render_template('home.html', log=False)
    else:
        return render_template('shopping.html', log=session.get('log'))

@app.route("/recipe")
def recipe():
    session['log'] = True
    if session.get('log') == None:
        return render_template('home.html', log=False)
    else:
        return render_template('recipe.html', log=session.get('log'))


#Server API Endpoints
@app.route("/api/ingredients", methods=['GET'])
def get_ingredients():
    result = getIngredients()
    if result == None:
        return jsonify({ 'data' : 'NOK'})
    else:
        return jsonify({ 'data' : result})

@app.route("/api/inventory", methods=['POST'])
def inventory():
    if request.method == 'POST':
        result = addToInventory(userid, request.form['iID'])
        if result == 'OK':
            return jsonify({'data': 'OK'})
    return jsonify({'data': 'NOK'})

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