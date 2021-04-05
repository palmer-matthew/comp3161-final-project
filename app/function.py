import random
from dbhelper import *

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