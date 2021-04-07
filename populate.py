import random, os
from re import T
from faker import Faker
from werkzeug.security import generate_password_hash
from dbhelper import *

#Ingredients, Adjectives, Units, Quantities

ingredients = ['molasses', 'almond', 'pecans', 'plum tomato', 'cashew nut', 'apple', 'legume', 'curry paste', \
     'barbecue sauce', 'chilli flake', 'lemon', 'endive', 'kale', 'torte', 'salt', 'cashew', 'honeydew melon', \
     'rice paper', 'pea', 'saffron', 'berry', 'soy ice cream', 'rice', 'brussels sprout', 'pretzel', 'guava', \
     'pumpernickel', 'flax seed', 'jackfruit', 'chives', 'durian', 'raisin', 'snow pea', 'cornflake', 'bran', \
     'blackberry', 'pear' , 'cucumber', 'cornstarch', 'jalapeno', 'chicken', 'pork']

adjectives = ['baked', 'beated', 'boiled', 'burned', 'carved', 'chopped', 'diced', 'fried', 'grated', 'greased', \
    'grilled', 'herbal', 'mashed', 'curried', 'barbi-fried', 'melted', 'mixed', 'peeled', 'sweet', 'sour', 'grinded', \
    'sweet & Sour', 'jerked', 'roasted', 'sautéed' , 'served', 'spicy', 'sprinkled', 'steamed', 'stirred', 'stir-fried', \
    'whisked', 'blended', 'barbequed', 'smoked', 'juiced', 'broiled', 'acidic', 'crispy', 'buttered', 'candied', 'chunky', 'creamed']

unit = ["tbsp", "tsp", "cups", 'pds', 'oz', 'whole']

quantity =  [ .25, .5, .75, 1, 1.5, 2, 2.25, 4, 6, 8]

dishes = ['cake', 'juice', 'alfredo', 'risotto', 'chips', 'tart', 'pudding', 'casserole', 'soup', 'N/A']

tables = None
measurements = None
recipes = []

names = ['Recipe', 'MealPlan', 'User', 'Ingredient', 'Measurement', 'Instruction', 'includes', 'has', 'kitchen','contains','adds']
lines = [['recipeID int auto_increment', 'creationDate date', 'recipeName varchar(255)', 'preparationTime int', 'inputServing int','imageUpload varchar(255)', 'calorieCount int', 'primary key(recipeID)'], \
         ['mealPlanID int auto_increment', 'planName varchar(150)', 'dateCreated date', 'primary key(mealPlanID)'],\
         ['userID int auto_increment','fname varchar(50)','lname varchar(50)','username varchar(150)','user_password varchar(255)', 'primary key(userID)'],\
         ['ingredientID int auto_increment', 'ingredientName varchar(255)','primary key(ingredientID)'], \
         ['measurementID int auto_increment','quantity decimal(8,2)','unit varchar(50)','primary key(measurementID)'], \
         ['recipeID int', 'stepNumber int', 'direction varchar(255)', 'primary key(recipeID, stepNumber)', 'foreign key(recipeID) references Recipe(recipeID) on delete cascade'], \
         ['mealPlanID int','recipeID int', 'dayNum int', 'mealNum int', 'primary key(mealPlanID, recipeID, dayNum, mealNum)','foreign key(mealPlanID) references MealPlan(mealPlanID) on delete cascade','foreign key(recipeID) references Recipe(recipeID) on delete cascade'], \
         ['mealPlanID int','userID int','primary key(mealPlanID)','foreign key(mealPlanID) references MealPlan(mealPlanID) on delete cascade','foreign key(userID) references User(userID) on delete cascade'], \
         ['ingredientID int','userID int','primary key(ingredientID, userID)','foreign key(ingredientID) references Ingredient(ingredientID) on delete cascade','foreign key(userID) references User(userID) on delete cascade'], \
         ['recipeID int','ingredientID int','measurementID int','primary key(recipeID, ingredientID)','foreign key(recipeID) references Recipe(recipeID) on delete cascade','foreign key(ingredientID) references Ingredient(ingredientID) on delete cascade','foreign key(measurementID) references Measurement(measurementID) on delete cascade'], \
         ['recipeID int','userID int','primary key(userID, recipeID)','foreign key(recipeID) references Recipe(recipeID) on delete cascade','foreign key(userID) references User(userID) on delete cascade']  
        ]

extra = """
/*==========================================CREATION OF STORED PROCEDURES===============================================*/
DELIMITER //       
    CREATE PROCEDURE GetShoppingList(IN planid int)
    BEGIN
        SELECT DISTINCT ingredientName FROM Recipe r JOIN contains c JOIN Ingredient i 
             ON r.recipeID = c.recipeID AND c.ingredientID = i.ingredientID WHERE r.recipeID IN
                (SELECT DISTINCT recipeID FROM MealPlan m JOIN includes i ON m.mealPlanID = i.mealPlanID 
                    WHERE m.mealPlanID = planid);  
    END //
DELIMITER ;
DELIMITER //  
    CREATE PROCEDURE GetKitchen(IN id int)
    BEGIN
        SELECT DISTINCT ingredientName FROM Ingredient i JOIN kitchen k ON i.ingredientID = k.ingredientID WHERE k.userID = id;
    END //
DELIMITER ;
DELIMITER //  
    CREATE PROCEDURE GetIntKitchen(IN id int)
    BEGIN
        SELECT DISTINCT k.ingredientID FROM Ingredient i JOIN kitchen k ON i.ingredientID = k.ingredientID WHERE k.userID = id;
    END //
DELIMITER ;
DELIMITER //  
    CREATE PROCEDURE insertContains(IN rid int, iid int, mid int)
    BEGIN
        INSERT INTO contains(recipeID, ingredientID, measurementID) VALUES(rid, iid, mid);
    END //
DELIMITER ;
DELIMITER //  
    CREATE PROCEDURE insertInstruction(IN rid int, step int, direct varchar(255))
    BEGIN
        INSERT INTO Instruction(recipeID, stepNumber, direction) VALUES(rid, step, direct);
    END //
DELIMITER ;
DELIMITER //
    CREATE PROCEDURE calorieCount(IN calories int, amt int)
    BEGIN
        SELECT recipeID, recipeName, inputServing, calorieCount FROM Recipe WHERE calorieCount <= calories LIMIT amt;
    END //
DELIMITER ;
DELIMITER //
    CREATE PROCEDURE getPlanDay(IN mid int, day int)
    BEGIN
        SELECT mealNum, i.recipeID, recipeName, inputServing, calorieCount FROM includes i JOIN Recipe r ON i.recipeID = r.recipeID WHERE i.mealPlanID = mid AND i.dayNum = day ORDER BY mealNum;
    END //
DELIMITER ;
"""

def createTable():
    result = []
    table_stmt = 'CREATE TABLE %s(%s);\r'
    for i,val in enumerate(names):
        result.append(table_stmt % (val, ','.join(lines[i])))
    return result
        
def createMeasurementList():
    global unit, quantity
    result, count = [], 1
    for i in unit:
        for j in quantity:
            result.append((count, j, i))
            count += 1
    return result

def createIngredientsList():
    result, d = [], {}
    for i, val in enumerate(ingredients):
        t = val.split()
        n = []
        for j in t:
            n.append(j.capitalize())
        y = ' '.join(n)
        result.append((i+1, y))
        d[i+1] = y
    return result, d

if __name__ == '__main__':
    try:
        measurements = createMeasurementList()
        ingredients, dver = createIngredientsList()
        tables = createTable()
        with open('./planner.sql', 'w+') as r:

            print("Creating planner.sql" + "."*10)
            
            newline = '\r'
            
            print("Inserting Header" + "."*10)
            
            #Insert the inital header into the documents
            r.write("DROP DATABASE IF EXISTS planner;\r")
            r.write("CREATE DATABASE planner;\r")
            r.write("USE planner;\r")

            print("Finished Inserting Header" + "."*10)
            
            print("Inserting CREATE Statements" + "."*10)
            
            #insert the create tables statements
            r.write("/*======================================CREATE STATEMENTS======================================*/\r")
            for i in tables: 
                r.write(i)

            print("Finished Inserting CREATE Statements" + "."*10)

            print("Inserting Measurement INSERT Statements" + "."*10)

            r.write("/*======================================INSERTING Measurements======================================*/\r")

            measure_stmt = 'INSERT INTO Measurement(measurementID, quantity, unit) VALUES(%d, %.2f, "%s");\r'

            for i in measurements:
                r.write(measure_stmt % i)

            print("Finished Inserting Measurement INSERT Statements" + "."*10)

            print("Inserting Ingredient INSERT Statements" + "."*10)

            r.write("/*======================================INSERTING Ingredients======================================*/\r")
            ingredient_stmt = 'INSERT INTO Ingredient(ingredientID, ingredientName) VALUES(%d, "%s");\r'

            for i in ingredients:
                r.write(ingredient_stmt % i)

            print("Finished Inserting Ingredient INSERT Statements" + "."*10)
        

            print("Inserting >200k User INSERT Statements" + "."*10)
            
            #insert 200,000 users
            r.write("/*======================================INSERTING 250,000 USERS======================================*/\r")

            user_stmt = 'INSERT INTO User(fname,lname,username, user_password) VALUES("%s", "%s", "%s", "%s");\r'
            fake = Faker()
            nusers = 250000
            fake.unique.clear()
            for i in range(nusers): 
                r.write(user_stmt % (fake.first_name(), fake.last_name(), fake.unique.user_name() ,fake.password(length=10, special_chars=False)))

            print("Finished Inserting >200k User INSERT Statements" + "."*10)

            #insert 600,000
            print("Inserting Recipe INSERT Statements and Connection Statements" + "."*10)
            r.write("/*======================================INSERTING 600,000 Recipes and Connections======================================*/\r")

            num = 650000
            recipe_stmt = 'INSERT INTO Recipe(recipeID, creationDate, recipeName, preparationTime, inputServing, imageUpload, calorieCount) VALUES(%d, "%s", "%s", %d, %d, "%s", %d);\r'
            contains_stmt = 'INSERT INTO contains(recipeID, ingredientID, measurementID) VALUES(%d, %d, %d);\r'
            instruct_stmt =  'INSERT INTO Instruction(recipeID, stepNumber, direction) VALUES(%d, %d, "%s");\r'
            add_stmt =  'INSERT INTO adds(recipeID, userID) VALUES(%d, %d);\r'
            kitchen_stmt = 'INSERT INTO kitchen(ingredientID, userID) VALUES(%d, %d);\r'
            includes_stmt = 'INSERT INTO includes(mealPlanID, recipeID) VALUES(%d, %d);\r'
            has_stmt = 'INSERT INTO has(mealPlanID, userID) VALUES(%d, %d);\r'
            plan_stmt = 'INSERT INTO MealPlan(planName, dateCreated) VALUES("%s", "%s");\r'

            for i in range(num):
                ingredient_list  = []
                main_ingredient = random.choice(ingredients)
                ingredient_list.append(main_ingredient)
                dish  = random.choice(dishes).capitalize()
                adj1 = random.choice(adjectives)
                adj2  = adj1
                while adj2 == adj1:
                    adj2 = random.choice(adjectives)
                if dish == 'N/a':
                    recipe_name = f'{adj1.capitalize()} {adj2.capitalize()} {main_ingredient[1]}'
                else:
                    recipe_name = f'{adj1.capitalize()} {adj2.capitalize()} {main_ingredient[1]} {dish}'
                created_date = fake.past_date().strftime('%Y-%m-%d')
                preptime = random.randint(1, 300)
                for j in range(random.randint(1,3)):
                    x = random.choice(ingredients)
                    if x not in ingredient_list:
                        ingredient_list.append(x)
                serving = random.randint(1,10)
                image_name = fake.image_url()
                calorie = random.randint(200, 1000)
                r.write(recipe_stmt % (i+1, created_date, recipe_name, preptime, serving, image_name, calorie))
                recipes.append((i+1, ingredient_list))

            for i in range(4):                 
                if i == 0:
                    r.write("/*======================================INSERTING Relationship: contains======================================*/\r")
                    for i in recipes:
                        for j in i[1]:
                            measure =  random.choice(measurements)
                            r.write(contains_stmt % (i[0], j[0], measure[0]))
                elif i == 1:
                    r.write("/*======================================INSERTING Instructions======================================*/\r")
                    for i in recipes:
                        for j in range(random.randint(1,3)):
                            direction = fake.paragraph(nb_sentences=2)
                            r.write(instruct_stmt % (i[0], j+1, direction))
                elif i == 2:
                    r.write("/*======================================INSERTING Relationship: adds======================================*/\r")
        
                    for i in recipes:
                        user_id = random.randint(1,nusers)
                        r.write(add_stmt % (i[0], user_id))
                elif i == 3:
                    r.write("/*======================================INSERTING Relationship: kitchen======================================*/\r")
        
                    for i in range(nusers):
                        ingredient_list  = []
                        for j in range(random.randint(1,4)):
                            x = random.choice(ingredients)
                            if x[0] not in ingredient_list:
                                ingredient_list.append(x[0])
                                r.write(kitchen_stmt % (x[0], i+1))
                # elif i == 4:
                #     r.write("/*======================================INSERTING MealPlan======================================*/\r")
                #     number = random.randint(1, 5)
                #     for i in range(number):
                #         name = fake.text(max_nb_chars=15)
                #         created_date = fake.past_date().strftime('%Y-%m-%d')
                #         r.write(plan_stmt % (name, created_date))
                # elif i == 5:
                #     r.write("/*======================================INSERTING Relationship: includes======================================*/\r")
                #     for i in range(number):
                #         unique = []
                #         for j in range(21):
                #             recipe = random.randint(1, num)
                #             if recipe not in unique:
                #                 r.write(includes_stmt % (i+1, recipe))
                #                 unique.append(recipe)
                # elif i == 6:
                #     r.write("/*======================================INSERTING Relationship: has======================================*/\r")
                #     for i in range(number):
                #         user = random.randint(1, nusers)
                #         r.write(has_stmt % (i+1, user))
            print("Finished Inserting Recipe INSERT Statements and Connection Statements" + "."*10)
            print("Inserting Stored Procedure Statements" + "."*10)
            r.write(extra)
            print("Finished Inserting Stored Procedure Statements" + "."*10)
        print('Sucess...... Closing Script, planner.sql created')
        # print('Connecting to SQL Server')
        # connection = connect()
        # if connection == None:
        #     print('Failed to Connect')
        #     exit()
        # else:
        #     print('Connection Established')
        #     print('Excecuting planner.sql')
        #     try:
        #         with open('planner.sql', 'r') as r:
        #             with connection.cursor() as curs:
        #                 for line in r:
        #                     if line == '\r' or line == '':
        #                         continue
        #                     else:
        #                         curs.execute(line)
        #                         connection.commit()
        #         close(connection)
        #         print('Sucess...... Closing Script')
        #     except Exception as e:
        #         print(f'Error Occured while exceuting Script\n{e}')
        #         exit()
    except Exception as e:
        print(e.msg)
        exit()
        
