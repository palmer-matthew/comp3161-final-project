import random
from dbhelper import *
from werkzeug.security import generate_password_hash
from json import dumps
from datetime import date

# - users should be able to regenerate this meal plan at any time.

def addToInventory(userid , iID):
    conn = connect(database='planner')
    result = getIngredientsinKitchen(userid, string=False)
    if result == None:
        return result
    elif int(iID) not in result:
        query = 'INSERT INTO kitchen(ingredientID, userID) VALUES(%d, %d);\r'
        result = executeNQuery(query % (int(iID), userid), conn)
        if result == None:
            close(conn)
            return None
        else:
            close(conn)
            return 'OK'
    else:
        return 'NOK'
        

def addNewRecipe(recipeName, preparationTime, inputServing, imageUpload, calorieCount):
    conn = connect(database='planner')
    today = date.today()
    createddate = today.strftime('%Y-%m-%d')
    query = 'INSERT INTO Recipe(creationDate, recipeName, preparationTime, inputServing, imageUpload, calorieCount) VALUES("%s", "%s", %d, %d, "%s", %d);'
    result = executeNQuery(query % (createddate, recipeName, int(preparationTime), int(inputServing), imageUpload , int(calorieCount)), conn)
    if result == None:
        close(conn)
        return None
    else:
        query = 'SELECT recipeID FROM Recipe ORDER BY recipeID DESC LIMIT 1;'
        result = executeRQuery(query, conn)
        if result == None:
            close(conn)
            return None
        else:
            close(conn)
            result = [i[0] for i in result][0]
            return 'OK', result

def addConnections(recipeID, ingredients, instructions, userid):
    conn = connect(database='planner')
    link = ingredients.split(',')
    query = 'call insertContains(%d, %d, %d);'
    for i in link:
        part = list(map(int, i.split('|')))
        result = executeNQuery(query % (int(recipeID), part[1], part[0]), conn)
        if result == None:
            return None
    direct = instructions.split('|')
    query = 'call insertInstruction(%d, %d, "%s");'
    for i, val in enumerate(direct):
        result = executeNQuery(query % (int(recipeID), i+1, val), conn)
        if result == None:
            return None
    query = 'INSERT INTO adds(recipeID, userID) VALUES(%d, %d);'
    result = executeNQuery(query % (int(recipeID), userid), conn)
    if result == None:
        return None
    close(conn)
    return 'OK'

    
def getIngredientsinKitchen(userid, string=True):
    conn = connect(database='planner')
    if string==True:
        query = 'call GetKitchen(%d);'
    else:
        query = 'call GetIntKitchen(%d);'
    result = executeRQuery(query % (userid), conn)
    if result == None:
        close(conn)
        return None
    else:
        close(conn)
        return [i[0] for i in result]

def getIngredients():
    conn = connect(database='planner')
    query = 'SELECT * FROM Ingredient i ORDER BY ingredientName;'
    result = executeRQuery(query, conn)
    if result == None:
        close(conn)
        return None
    else:
        close(conn)
        rslt = []
        for i in result:
            rslt.append({'key': i[0], 'name': i[1]})
        return rslt

def getMeasurements():
    conn = connect(database='planner')
    query = 'SELECT * FROM Measurement i ORDER BY unit;'
    result = executeRQuery(query, conn)
    if result == None:
        close(conn)
        return None
    else:
        close(conn)
        rslt = []
        for i in result:
            rslt.append({'key': i[0], 'qty': float(i[1]), 'unit': i[2]})
        return rslt

"""
GRANT ALL PRIVILEGES ON world.* TO 'lab5_user'@'localhost'
IDENTIFIED BY 'password123';
"""
def getShoppingList(planid):
    conn = connect(database='planner')
    query = 'call GetShoppingList(%d);'
    result = executeRQuery(query % (planid), conn)
    if result == None:
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
    if result == None:
        close(conn)
        return None
    else:
        close(conn)
        return 'OK'

def checkUser(username):
    conn = connect(database= "planner")
    query = 'SELECT DISTINCT userID FROM User WHERE username = "%s";'
    result = executeRQuery(query % (username), conn)
    if result == None:
        close(conn)
        return None
    else:
        close(conn)
        if result == []:
            return None
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


def SearchRecipe(search):
    conn = connect(database= "planner")
    query = 'SELECT DISTINCT * FROM Recipe WHERE recipeName LIKE "%s" LIMIT 500;'
    result = None
    recipes = executeRQuery(query % (search), conn)
    for res in result:
        print(res)
    if result == None or result == []:
        close(conn)
        return None
    else:
        close(conn)
        return None 

def SearchMealPlan(search):
    conn = connect(database= "planner")
    query = 'SELECT DISTINCT * FROM mealPLan WHERE planName LIKE "%s" LIMIT 500;'
    result = None
    recipes = executeRQuery(query % (search), conn)
    for res in result:
        print(res)
    if result == None or result == []:
        close(conn)
        return None
    else:
        close(conn)
        return None



def createMealPlan(calorieCount=None):
    conn = connect(database='planner')
    query = "SELECT COUNT(recipeID) FROM Recipe;"
    result = executeRQuery(query, conn)
    if result == None or result == []:
        close(conn)
        return None
    elif calorieCount == None:
        nrecipe, lst, distinct = [i[0] for i in result][0], [], []
        for i in range(7):
            m1, m2, m3 = random.randint(1, nrecipe), random.randint(1, nrecipe), random.randint(1, nrecipe)
            if m1 not in distinct:
                distinct.append(m1)
            if m2 not in distinct:
                distinct.append(m2)
            if m3 not in distinct:
                distinct.append(m3)
            lst.append((m1,m2,m3))
        query = f"SELECT recipeID, recipeName, inputServing, calorieCount FROM Recipe WHERE recipeID IN {tuple(distinct)}"
        result = executeRQuery(query, conn)
        if result == None or result == []:
            close(conn)
            return None
        else:
            final, total = [], []
            for i in lst:
                tpl = []
                for j in i:
                    for n in result:
                        if n[0] == j:
                            tpl.append(n)
                            total.append(n[-1])
                            break
                final.append(tpl)
            return final, sum(total)
    else:
        pass
        # close(conn)
        # nrecipe, lst, distinct = [i[0] for i in result][0], [], []
        # for i in range(7):
        #     m1, m2, m3 = random.randint(1, nrecipe), random.randint(1, nrecipe), random.randint(1, nrecipe)
        #     if m1 not in distinct:
        #         distinct.append(m1)
        #     if m2 not in distinct:
        #         distinct.append(m2)
        #     if m3 not in distinct:
        #         distinct.append(m3)
        #     lst.append((m1,m2,m3))
        # query = f"SELECT recipeID, recipeName, inputServing, calorieCount FROM Recipe WHERE recipeID IN {tuple(distinct)}"
        # result = executeRQuery(query, conn)
        # if result == None or result == []:
        #     close(conn)
        #     return None
        # else:
        #     final, total = [], []
        #     for i in lst:
        #         tpl = []
        #         for j in i:
        #             for n in result:
        #                 if n[0] == j:
        #                     tpl.append(n)
        #                     total.append(n[-1])
        #                     break
        #         final.append(tpl)
        #     return final, sum(total)
        
        

# def saveMealPlan(mealPlan):
#     query = 'INSERT INTO MealPlan(MealPlanID, planName, dateCreated) VALUES(%d, "%s", "%s") From recipe r JOIN calorieCount c \
#          ON r.recipeID = c. LIMIT 1;'
#     result = [i[0] for i in executeRQuery(query % (calorieCount), conn)]
#     if result == None or result == []:
#         close(conn)
#         return None
#     else:
#         close(conn)
#         return [i[0].upper() for i in result]



# def randomMeal(MealPlanID):
#     conn = connect(database='planner')
#     query= 'SELECT  FROM table  ORDER BY RAND () LIMIT 1' 

# def generateMealPlan(recipeId):
#     conn = connect(database='planner')
#     query = 'SELECT * FROM recipe WHERE recipeName = %s LIMIT 21;'
#     result = [i[0] for i in executeRQuery(query % (recipeId), conn)]
#     if result == None or result == []:
#         close(conn)
#         return None
#     else:
#         close(conn)
#         return [i[0].upper() for i in result]


