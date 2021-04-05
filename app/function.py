import random
from dbhelper import *
from werkzeug.security import generate_password_hash

# - users should be able to regenerate this meal plan at any time.

def addToInventory(userid , iID):
    conn = connect(database='planner')
    result = getIngredientsinKitchen(userid, string=False)
    if result == None:
        return result
    elif int(iID) not in result:
        query = 'INSERT INTO kitchen(ingredientID, userID) VALUES(%d, %d);\r'
        result = executeNQuery(query % (int(iID), userid), conn)
        if result == None or result == []:
            close(conn)
            return None
        else:
            close(conn)
            return 'OK'
    else:
        return 'NOK'
        

def addNewRecipe(recipeName, preparationTime, inputServing, imageUpload, calorieCount):
    conn = connect(database='planner')
    query = 'INSERT INTO Recipe(recipeName, preparationTime, inputServing, imageUpload, calorieCount) VALUES("%s", %d, %d ,"%s", %d)'

    executeNQuery(query % (recipeName, preparationTime, inputServing , imageUpload , calorieCount), conn)
    close(conn)

    
def getIngredientsinKitchen(userid, string=True):
    conn = connect(database='planner')
    if string==True:
        query = 'call GetKitchen(%d);'
    else:
        query = 'call GetIntKitchen(%d);'
    result = executeRQuery(query % (userid), conn)
    if result == None or result == []:
        close(conn)
        return None
    else:
        close(conn)
        return [i[0] for i in result]

def getIngredients():
    conn = connect(database='planner')
    query = 'SELECT * FROM Ingredient i ORDER BY ingredientName;'
    result = executeRQuery(query, conn)
    if result == None or result == []:
        close(conn)
        return None
    else:
        close(conn)
        rslt = []
        for i in result:
            rslt.append({'key': i[0], 'name': i[1]})
        return rslt

"""
GRANT ALL PRIVILEGES ON world.* TO 'lab5_user'@'localhost'
IDENTIFIED BY 'password123';
"""
def getShoppingList1(planid):
    conn = connect(database='planner')
    query = 'call GetShoppingList(%d);'
    result = executeRQuery(query % (planid), conn)
    if result == None or result == []:
        close(conn)
        return None
    else:
        close(conn)
        return [i[0] for i in result]

def addUser(username, password, fname, lname):
    conn = connect(database= 'planner')
    query = 'INSERT INTO User(fname,lname,username, user_password) VALUES("%s", "%s", "%s", "%s");\r'
    hash = generate_password_hash(password, method='pbkdf2:sha256')
    result = executeNQuery(query % (fname,lname, username, hash), conn)
    if result == None or result == [] :
        close(conn)
        return None
    else:
        close(conn)
        return 'OK'

def checkUser(username):
    conn = connect(database= "planner")
    query = 'SELECT DISTINCT userID FROM User WHERE username = "%s";'
    result = executeRQuery(query % (username), conn)
    if result == None or result == []:
        close(conn)
        return None
    else:
        close(conn)
        result = [i[0] for i in result]
        return result 

def getUser(username):
    conn = connect(database= "planner")
    query = 'SELECT DISTINCT * FROM User WHERE username = "%s";'
    result = executeRQuery(query % (username), conn)
    if result == None or result == []:
        close(conn)
        return None
    else:
        close(conn)
        result = result[0]
        return result 

def SearchRecipe(recipeName):
    conn = connect(database= "planner")
    query = 'SELECT * FROM Recipe WHERE recipeID = search;'
    result = None
    recipes = query.fetchall()
    if result == None or result == []:
        close(conn)
        return None
    else:
        close(conn)
        return None 

def SearchMealPlan(planName):
    conn = connect(database= "planner")
    query = 'SELECT * FROM mealPLan WHERE mealPlanID = search;'
    result = None
    recipes = query.fetchall()
    if result == None or result == []:
        close(conn)
        return None
    else:
        close(conn)
        return None
