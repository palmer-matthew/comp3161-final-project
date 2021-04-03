import random
from dbhelper import *

# - Generate a supermarket list based on the planned meals
# - users should be able to regenerate this meal plan at any time.

def getIngredientsinKitchen(userid):
    conn = connect(database='planner')
    query = 'SELECT DISTINCT ingredientName FROM Ingredient i JOIN kitchen k ON i.ingredientID = k.ingredientID \
             WHERE userID = %d;'
    result = executeRQuery(query % (userid), conn)
    if result == None or result == []:
        close(conn)
        return None
    else:
        close(conn)
        return [i[0].upper() for i in result]

def getShoppingList(planid):
    conn = connect(database='planner')
    query = 'SELECT DISTINCT recipeID FROM MealPlan m JOIN includes i ON m.mealPlanID = i.mealPlanID \
             WHERE m.mealPlanID = %d;'
    result = [i[0] for i in executeRQuery(query % (planid), conn)]
    if result == None or result == []:
        close(conn)
        return None
    else:
        query = f'SELECT ingredientName, quantity, unit FROM Recipe r JOIN contains c JOIN Ingredient i JOIN Measurement m \
             ON r.recipeID = c.recipeID AND c.ingredientID = i.ingredientID AND c.measurementID = m.measurementID  WHERE r.recipeID in {tuple(result)};'
        result = executeRQuery(query, conn)
        print(result, len(result))
        close(conn)
        # return [i[0] for i in result]