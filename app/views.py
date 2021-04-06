import random
from app import app
from flask import render_template, url_for, redirect, flash, request, session, jsonify
from werkzeug.security import check_password_hash
from werkzeug.utils import secure_filename
from .function import *
from .forms import LoginForm, SignUpForm, addRecipe, SearchForm
from .globals import *

@app.route("/")
def home():
    return render_template('home.html', log=session.get('log'))

@app.route("/login", methods=['POST', 'GET'])
def login():
    iform = LoginForm()
    if request.method == 'POST':
        if iform.validate_on_submit():
            username = request.form['username']
            password = request.form['password']
            result = getUser(username)
            if result == None:
                flash('Sorry Data Could not be Found on', 'danger')
                return redirect('login')
            elif check_password_hash(result[4], password) == True:
                session['logged_in'] = True
                global userid
                session['userId'], userid =  result[0], result[0]
                session['username'] = result[3]
                session['name'] = result[1], result[2]
                flash('You were logged in', 'success')
                return redirect(url_for('profile'))
        flash_errors(iform)
    return render_template('login.html', form=iform)


@app.route("/signup", methods=['POST', 'GET'])
def signup():
    sform = SignUpForm()
    if request.method == 'POST':
        if sform.validate_on_submit():
            username = request.form['username']
            password = request.form['password']
            fname = request.form['fname']
            lname = request.form['lname']
            
            result = checkUser(username) 
            if result == None:
                result = addUser(username, password, fname, lname)
                if result == 'OK':
                    flash('Successfully Created Account', 'success')
                    return redirect(url_for('login'))
        flash_errors(sform) 
    return render_template('signup.html', form=sform) 

@app.route('/logout')
def logout():
    session.pop('name', None)
    session.pop('username', None)
    session.pop('logged_in', None)
    return redirect(url_for('home'))

@app.route("/addrecipe", methods=['POST', 'GET'])
def addrecipe():
    if session.get('logged_in') == None:
        return redirect(url_for('home'))
    recipeform = addRecipe()
    if request.method == 'POST':
        if recipeform.validate_on_submit():
            recipeName = request.form['recipe_name']
            calorieCount = request.form['calorie_count']
            inputServing = request.form['serving']
            preparationTime = request.form['prep_time']
            ingredients = request.form.get('ingredients')
            instructions = request.form.get('instruct')

            imageUpload = request.files['image']
            filename = secure_filename(imageUpload.filename)
            imageUpload.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

            result = addNewRecipe(recipeName, preparationTime, inputServing, filename, calorieCount)
            if result[0] == 'OK':
                print(result[1])
                result = addConnections(result[1], ingredients, instructions, int(userid))
                if result == 'OK':
                    flash('Recipe Successful Uploaded', 'success')
                    return redirect(url_for('profile'))
                else:
                    # removeRecipe(result[1])
                    flash('Failed to Add Recipe', 'danger')
                    return redirect(url_for('profile'))
            else:
                flash('Recipe Addition was Unsuccessful', 'danger')
                return redirect(url_for('profile'))
        flash_errors(recipeform)
    return render_template('addrecipe.html' ,log=session.get('logged_in'), form=recipeform)


@app.route("/search", methods=['GET', 'POST'])
def search():
    if session.get('logged_in') == None:
        return redirect(url_for('home'))
    searchF = SearchForm()
    if searchF.validate_on_submit() and request.form['matchRecipe']:
        searched = request.form['search']
        result = SearchRecipe(searched)
        if result == None:
            flash('Search not found')
            if result == 'OK':
                return redirect(url_for('recipe'))
        flash_errors(searchF)
    else:
        if searchF.validate_on_submit() and request.form['matchMealPLan']:
            searches = request.form['search']
            result = SearchRecipe(searches)
            if result == None:
                flash('Search not found')
                if result == 'OK':
                    return redirect(url_for('plan-view'))
            flash_errors(searchF)
    return render_template('search.html', form=searchF)

@app.route("/profile")
def profile():
    if session.get('logged_in') == None:
        return redirect(url_for('home'))
    global userid
    result = getIngredientsinKitchen(userid)
    return render_template('profile.html', log=session.get('logged_in'), name=session.get('name'), uname=session.get('username'), kitchen=result)

@app.route("/plan")
def plan():
    if session.get('logged_in') == None:
        return redirect(url_for('home'))
    return render_template('generate_plan.html', log=session.get('logged_in'))

@app.route("/planview")
def plan_view():
    if session.get('logged_in') == None:
        return redirect(url_for('home'))
    return render_template('plan_view.html', log=session.get('logged_in'))

@app.route("/shopping")
def shopping():
    if session.get('logged_in') == None:
        return redirect(url_for('home'))
    return render_template('shopping.html', log=session.get('logged_in'))

@app.route("/recipe")
def recipe():
    if session.get('logged_in') == None:
        return redirect(url_for('home'))
    return render_template('recipe.html', log=session.get('logged_in'))


#Server API Endpoints
@app.route("/api/ingredients", methods=['GET'])
def get_ingredients():
    if session.get('logged_in') == None:
        return jsonify({'data': 'NOK'})
    result = getIngredients()
    if result == None:
        return jsonify({ 'data' : 'NOK'})
    else:
        return jsonify({ 'data' : result})

@app.route("/api/measurements", methods=['GET'])
def get_measurement():
    if session.get('logged_in') == None:
        return jsonify({'data': 'NOK'})
    result = getMeasurements()
    if result == None:
        return jsonify({ 'data' : 'NOK'})
    else:
        return jsonify({ 'data' : result})

@app.route("/api/inventory", methods=['POST'])
def inventory():
    if session.get('logged_in') == None:
        return jsonify({'data': 'NOK'})
    if request.method == 'POST':
        result = addToInventory(userid, request.form['iID'])
        if result == 'OK':
            return jsonify({'data': 'OK'})
    return jsonify({'data': 'NOK'})

@app.route("/api/plan", methods=['POST'])
def create_plan():
    if session.get('logged_in') == None:
        return jsonify({'data': 'NOK'})
    if request.method == 'POST':
        if request.form.get('calorie') == 'NONE':
            result = createMealPlan()
        else:
            result = createMealPlan(request.form.get('calorie'))
        if result == None:
            return jsonify({'data': 'NOK'})
        else:
            global current_meal_plan, current_total
            current_meal_plan, current_total = result[0], result[1]
            return jsonify({ 'data': result[0], 'total': result[1]})
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