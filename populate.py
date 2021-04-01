from faker import Faker
from werkzeug.security import generate_password_hash
import random

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
    RecipeID int autoincrement,
    CreationDate date, 
    RecipeName varchar(255),
    PreparationTime int,
    primary key(RecipeID)   
);

CREATE TABLE Meal(
    MealID int autoincrement,
    InputServing int, 
    ImageUpload varchar(255),
    CalorieCount int,
    primary key(MealID)   
);

CREATE TABLE MealPlan(
    MealPlanID int autoincrement,
    primary key(MealPlanID)   
);

CREATE TABLE User(
    UserID int autoincrement,
    fname varchar(50),
    lname varchar(50), 
    password varchar(255),
    primary key(UserID)   
);

CREATE TABLE Ingredient(
    IngredientID int autoincrement,
    IngredientName varchar(255),
    primary key(IngredientID)   
);

CREATE TABLE Measurement(
    MeasurementID int autoincrement,
    quantity int, 
    unit varchar(50),
    primary key(MeasurementID)   
);

CREATE TABLE Instruction(
    RecipeID int,
    StepNumber int autoincrement,
    Direction varchar(255),
    primary key(RecipeID, StepNumber),
    foreign key(RecipeID) references Recipe(RecipeID) on delete cascade
);

CREATE TABLE includes(
    MealPlanID int,
    MealID int ,
    primary key(MealPlanID, MealID),
    foreign key(MealPlanID) references MealPlan(MealPlanID) on delete cascade,
    foreign key(MealID) references Meal(MealID) on delete cascade
);

CREATE TABLE includes(
    MealPlanID int,
    MealID int,
    primary key(MealPlanID, MealID),
    foreign key(MealPlanID) references MealPlan(MealPlanID) on delete cascade,
    foreign key(MealID) references Meal(MealID) on delete cascade
);

CREATE TABLE has(
    MealPlanID int,
    UserID int,
    primary key(MealPlanID, UserID),
    foreign key(MealPlanID) references MealPlan(MealPlanID) on delete cascade,
    foreign key(UserID) references User(UserID) on delete cascade
);

CREATE TABLE kitchen(
    IngredientID int,
    UserID int,
    primary key(IngredientID, UserID),
    foreign key(IngredientID) references Ingredient(IngredientID) on delete cascade,
    foreign key(UserID) references User(UserID) on delete cascade
);

CREATE TABLE uses(
    MeasurementID int,
    IngredientID int,
    primary key(MeasurementID, IngredientID),
    foreign key(MeasurementID) references Measurement(MeasurementID) on delete cascade,
    foreign key(IngredientID) references Ingredient(IngredientID) on delete cascade
);

CREATE TABLE contains(
    RecipeID int,
    IngredientID int
    primary key(RecipeID, IngredientID),
    foreign key(RecipeID) references Recipe(RecipeID) on delete cascade,
    foreign key(IngredientID) references Ingredient(IngredientID) on delete cascade
);

CREATE TABLE creates(
    RecipeID int,
    MealID int
    primary key(RecipeID, MealID),
    foreign key(RecipeID) references Recipe(RecipeID) on delete cascade,
    foreign key(MealID) references Meal(MealID) on delete cascade  
);

CREATE TABLE adds(
    RecipeID int,
    UserID int
    primary key(UserID, RecipeID),
    foreign key(RecipeID) references Recipe(RecipeID) on delete cascade,
    foreign key(UserID) references User(UserID) on delete cascade
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
    result = []
    for i, val in enumerate(ingredients):
        t = val.split()
        n = []
        for j in t:
            n.append(j.capitalize())
        result.append((i+1, ' '.join(n)))
    return result

if __name__ == '__main__':
    measurements = createMeasurementList()
    ingredients = createIngredientsList()
    with open('./planner.sql', 'w+') as r:

        print("Creating planner.sql" + "."*10)
        
        newline = '\r'
        
        print("Inserting Header" + "."*10)
        
        #Insert the inital header into the documents
        r.write("DROP TABLE IF EXISTS planner;\r")
        r.write("CREATE DATABASE planner;\r")
        r.write("USE planner;\r")
        r.write(newline)

        print("Finished Inserting Header" + "."*10)
        
        print("Inserting CREATE Statements" + "."*10)
        
        #insert the create tables statements
        r.write(tables)
        r.write(newline)

        # print("Finished Inserting CREATE Statements" + "."*10)

        # print("Inserting Measurement INSERT Statements" + "."*10)

        # r.write("/*======================================INSERTING Measurements======================================*/\r")
        # r.write(newline)

        # measure_stmt = 'INSERT INTO Measurement(MeasurementID, quantity, unit) VALUES(%d, "%s", "%s");\r'

        # for i in measurements:
        #     r.write(measure_stmt % i)
        # r.write(newline)

        # print("Finished Inserting Measurement INSERT Statements" + "."*10)

        # print("Inserting Ingredient INSERT Statements" + "."*10)

        # r.write("/*======================================INSERTING Ingredients======================================*/\r")
        # r.write(newline)
        # ingredient_stmt = 'INSERT INTO Ingredient(IngredientID, IngredientName) VALUES(%d, "%s");\r'

        # for i in ingredients:
        #     r.write(ingredient_stmt % i)
        # r.write(newline)

        # print("Finished Inserting Ingredient INSERT Statements" + "."*10)
     

        # print("Inserting >200k User INSERT Statements" + "."*10)
        
        # #insert 200,000 users
        # r.write("/*======================================INSERTING 250,000 USERS======================================*/\r")
        # r.write(newline)

        # user_stmt = 'INSERT INTO User(fname,lname,password) VALUES("%s", "%s", "%s");\r'
        fake = Faker()

        # for i in range(1): #Change to 250,000 when it is time to create
        #     r.write(user_stmt % (fake.first_name(), fake.last_name(), generate_password_hash(fake.password(length=10, special_chars=False), method='pbkdf2:sha256')))
        # r.write(newline)

        # print("Finished Inserting >200k User INSERT Statements" + "."*10)

        #insert 600,000
        print("Inserting >600k Recipe INSERT Statements" + "."*10)
        r.write("/*======================================INSERTING 250,000 Database======================================*/\r")
        r.write(newline)

        recipe_stmt = 'INSERT INTO Recipe(RecipeId, CreationDate, RecipeName, PreparationTime) VALUES(%d, "%s", "%s", %d);\r'

        for i in range(6):
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
            for j in range(random.randint(1,5)):
                x = random.choice(ingredients)
                if x not in ingredient_list:
                    ingredient_list.append(x)
            recipes.append((i+1, recipe_name, created_date, preptime, ingredient_list))

            r.write(recipe_stmt % (i+1, recipe_name, created_date, preptime))
        r.write(newline)