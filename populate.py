import random, os
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

quantity =  ['1/4', '1/2', '3/4', '1', '1 1/2', '2', '2 1/4', '4', '6', '10']

dishes = ['cake', 'juice', 'alfredo', 'risotto', 'chips', 'tart', 'pudding', 'casserole', 'soup', 'N/A']

measurements = None
recipes = []

#Tables Info

tables = """
CREATE TABLE Recipe(
    recipeID int auto_increment,
    creationDate date default CURRENT_DATE, 
    recipeName varchar(255),
    preparationTime int,
    primary key(recipeID)   
);

CREATE TABLE Meal(
    mealID int auto_increment,
    inputServing int, 
    imageUpload varchar(255),
    calorieCount int,
    primary key(mealID)   
);

CREATE TABLE MealPlan(
    mealPlanID int auto_increment,
    primary key(mealPlanID)   
);

CREATE TABLE User(
    userID int auto_increment,
    fname varchar(50),
    lname varchar(50), 
    password varchar(255),
    primary key(userID)   
);

CREATE TABLE Ingredient(
    ingredientID int auto_increment,
    ingredientName varchar(255),
    primary key(ingredientID)   
);

CREATE TABLE Measurement(
    measurementID int auto_increment,
    quantity varchar(10), 
    unit varchar(50),
    primary key(measurementID)   
);

CREATE TABLE Instruction(
    recipeID int,
    stepNumber int,
    direction varchar(255),
    primary key(recipeID, stepNumber),
    foreign key(recipeID) references Recipe(recipeID) on delete cascade
);

CREATE TABLE includes(
    mealPlanID int,
    mealID int ,
    primary key(mealPlanID, mealID),
    foreign key(mealPlanID) references MealPlan(mealPlanID) on delete cascade,
    foreign key(mealID) references Meal(mealID) on delete cascade
);

CREATE TABLE has(
    mealPlanID int,
    userID int,
    primary key(mealPlanID, userID),
    foreign key(mealPlanID) references MealPlan(mealPlanID) on delete cascade,
    foreign key(userID) references User(userID) on delete cascade
);

CREATE TABLE kitchen(
    ingredientID int,
    userID int,
    primary key(ingredientID, userID),
    foreign key(ingredientID) references Ingredient(ingredientID) on delete cascade,
    foreign key(userID) references User(userID) on delete cascade
);

CREATE TABLE uses(
    measurementID int,
    ingredientID int,
    primary key(measurementID, ingredientID),
    foreign key(measurementID) references Measurement(measurementID) on delete cascade,
    foreign key(ingredientID) references Ingredient(ingredientID) on delete cascade
);

CREATE TABLE contains(
    recipeID int,
    ingredientID int,
    primary key(recipeID, ingredientID),
    foreign key(recipeID) references Recipe(recipeID) on delete cascade,
    foreign key(ingredientID) references Ingredient(ingredientID) on delete cascade
);

CREATE TABLE creates(
    recipeID int,
    mealID int,
    primary key(recipeID, mealID),
    foreign key(recipeID) references Recipe(recipeID) on delete cascade,
    foreign key(mealID) references Meal(mealID) on delete cascade  
);

CREATE TABLE adds(
    recipeID int,
    userID int,
    primary key(userID, recipeID),
    foreign key(recipeID) references Recipe(recipeID) on delete cascade,
    foreign key(userID) references User(userID) on delete cascade
);
"""
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
    measurements = createMeasurementList()
    ingredients, dver = createIngredientsList()
    with open('./planner.sql', 'w+') as r:

        print("Creating planner.sql" + "."*10)
        
        newline = '\r'
        
        print("Inserting Header" + "."*10)
        
        #Insert the inital header into the documents
        # r.write("DROP DATABASE IF EXISTS planner;\r")
        # r.write("CREATE DATABASE planner;\r")
        r.write("USE planner;\r")
        r.write(newline)

        print("Finished Inserting Header" + "."*10)
        
        print("Inserting CREATE Statements" + "."*10)
        
        #insert the create tables statements
        r.write(tables)
        r.write(newline)

        print("Finished Inserting CREATE Statements" + "."*10)

        print("Inserting Measurement INSERT Statements" + "."*10)

        r.write("/*======================================INSERTING Measurements======================================*/\r")
        r.write(newline)

        measure_stmt = 'INSERT INTO Measurement(measurementID, quantity, unit) VALUES(%d, "%s", "%s");\r'

        for i in measurements:
            r.write(measure_stmt % i)
        r.write(newline)

        print("Finished Inserting Measurement INSERT Statements" + "."*10)

        print("Inserting Ingredient INSERT Statements" + "."*10)

        r.write("/*======================================INSERTING Ingredients======================================*/\r")
        r.write(newline)
        ingredient_stmt = 'INSERT INTO Ingredient(ingredientID, ingredientName) VALUES(%d, "%s");\r'

        for i in ingredients:
            r.write(ingredient_stmt % i)
        r.write(newline)

        print("Finished Inserting Ingredient INSERT Statements" + "."*10)
     

        print("Inserting >200k User INSERT Statements" + "."*10)
        
        #insert 200,000 users
        r.write("/*======================================INSERTING 250,000 USERS======================================*/\r")
        r.write(newline)

        user_stmt = 'INSERT INTO User(fname,lname,password) VALUES("%s", "%s", "%s");\r'
        fake = Faker()
        nusers = 5 #Change to 250,000 when it is time to create

        for i in range(nusers): 
            r.write(user_stmt % (fake.first_name(), fake.last_name(), generate_password_hash(fake.password(length=10, special_chars=False), method='pbkdf2:sha256')))
        r.write(newline)

        print("Finished Inserting >200k User INSERT Statements" + "."*10)

        #insert 600,000
        print("Inserting Recipe INSERT Statements and Connection Statements" + "."*10)
        r.write("/*======================================INSERTING 600,000 Recipes and Connections======================================*/\r")
        r.write(newline)

        num = 5
        recipe_stmt = 'INSERT INTO Recipe(recipeID, creationDate, recipeName, preparationTime) VALUES(%d, "%s", "%s", %d);\r'
        meal_stmt = 'INSERT INTO Meal(mealID, inputServing, imageUpload, calorieCount) VALUES(%d, %d, "%s", %d);\r'
        creates_stmt = 'INSERT INTO creates(recipeID, mealID) VALUES(%d, %d);\r'
        contains_stmt = 'INSERT INTO contains(recipeID, ingredientID) VALUES(%d, %d);\r'
        instruct_stmt =  'INSERT INTO Instruction(recipeID, stepNumber, direction) VALUES(%d, %d, "%s");\r'

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
            recipes.append((i+1, created_date, recipe_name, preptime, ingredient_list))

            r.write(recipe_stmt % (i+1, created_date, recipe_name, preptime))
        r.write(newline)

        for i in range(4):
            if i == 0:
                r.write("/*======================================INSERTING Meals======================================*/\r")
                r.write(newline)

                for i in recipes:
                    serving = random.randint(1,10)
                    image_name = fake.image_url()
                    calorie = random.randint(1, 7000)
                    r.write(meal_stmt % (i[0], serving, image_name, calorie))
                r.write(newline)
            elif i == 1:
                r.write("/*======================================INSERTING Relationship: creates======================================*/\r")
                r.write(newline)

                for i in recipes:
                    r.write(creates_stmt % (i[0], i[0]))
                r.write(newline)
            elif i == 2:
                r.write("/*======================================INSERTING Relationship: contains======================================*/\r")
                r.write(newline)

                for i in recipes:
                    for j in i[4]:
                        r.write(contains_stmt % (i[0], j[0]))
                r.write(newline)
            elif i == 3:
                r.write("/*======================================INSERTING Instructions======================================*/\r")
                r.write(newline)

                for i in recipes:
                    for j in range(random.randint(1,3)):
                        direction = fake.paragraph()
                        r.write(instruct_stmt % (i[0], j+1, direction))
                r.write(newline)
        print("Finished Inserting Recipe INSERT Statements and Connection Statements" + "."*10)
    
    # #Execute the File to Populate the Table
    # root_dir = os.getcwd()
    # path_to_file = os.path.join(root_dir,'planner.sql')
    # query = f"\. {path_to_file}"
    # connection = connect()
    # if connection == None:
    #     print('Failed to Connect to Database')
    #     exit()
    # else:
    #     print('Excecuting File')
    #     result = executeQuery(query, connection)
    #     if result == None:
    #         print('Failed to execute Query')
    #         close(connection)
    #         exit()
    #     else:
    #         print('Sucess...... Closing Script')
