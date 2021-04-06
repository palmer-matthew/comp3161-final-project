DROP DATABASE IF EXISTS planner;CREATE DATABASE planner;USE planner;/*======================================CREATE STATEMENTS======================================*/CREATE TABLE Recipe(recipeID int auto_increment,creationDate date,recipeName varchar(255),preparationTime int,inputServing int,imageUpload varchar(255),calorieCount int,primary key(recipeID));CREATE TABLE MealPlan(mealPlanID int auto_increment,planName varchar(150),dateCreated date,primary key(mealPlanID));CREATE TABLE User(userID int auto_increment,fname varchar(50),lname varchar(50),username varchar(150),user_password varchar(255),primary key(userID));CREATE TABLE Ingredient(ingredientID int auto_increment,ingredientName varchar(255),primary key(ingredientID));CREATE TABLE Measurement(measurementID int auto_increment,quantity decimal(8,2),unit varchar(50),primary key(measurementID));CREATE TABLE Instruction(recipeID int,stepNumber int,direction varchar(255),primary key(recipeID, stepNumber),foreign key(recipeID) references Recipe(recipeID) on delete cascade);CREATE TABLE includes(mealPlanID int,recipeID int,dayNum int,mealNum int,primary key(mealPlanID, recipeID, dayNum, mealNum),foreign key(mealPlanID) references MealPlan(mealPlanID) on delete cascade,foreign key(recipeID) references Recipe(recipeID) on delete cascade);CREATE TABLE has(mealPlanID int,userID int,primary key(mealPlanID),foreign key(mealPlanID) references MealPlan(mealPlanID) on delete cascade,foreign key(userID) references User(userID) on delete cascade);CREATE TABLE kitchen(ingredientID int,userID int,primary key(ingredientID, userID),foreign key(ingredientID) references Ingredient(ingredientID) on delete cascade,foreign key(userID) references User(userID) on delete cascade);CREATE TABLE contains(recipeID int,ingredientID int,measurementID int,primary key(recipeID, ingredientID),foreign key(recipeID) references Recipe(recipeID) on delete cascade,foreign key(ingredientID) references Ingredient(ingredientID) on delete cascade,foreign key(measurementID) references Measurement(measurementID) on delete cascade);CREATE TABLE adds(recipeID int,userID int,primary key(userID, recipeID),foreign key(recipeID) references Recipe(recipeID) on delete cascade,foreign key(userID) references User(userID) on delete cascade);/*======================================INSERTING Measurements======================================*/INSERT INTO Measurement(measurementID, quantity, unit) VALUES(1, 0.25, "tbsp");INSERT INTO Measurement(measurementID, quantity, unit) VALUES(2, 0.50, "tbsp");INSERT INTO Measurement(measurementID, quantity, unit) VALUES(3, 0.75, "tbsp");INSERT INTO Measurement(measurementID, quantity, unit) VALUES(4, 1.00, "tbsp");INSERT INTO Measurement(measurementID, quantity, unit) VALUES(5, 1.50, "tbsp");INSERT INTO Measurement(measurementID, quantity, unit) VALUES(6, 2.00, "tbsp");INSERT INTO Measurement(measurementID, quantity, unit) VALUES(7, 2.25, "tbsp");INSERT INTO Measurement(measurementID, quantity, unit) VALUES(8, 4.00, "tbsp");INSERT INTO Measurement(measurementID, quantity, unit) VALUES(9, 6.00, "tbsp");INSERT INTO Measurement(measurementID, quantity, unit) VALUES(10, 8.00, "tbsp");INSERT INTO Measurement(measurementID, quantity, unit) VALUES(11, 0.25, "tsp");INSERT INTO Measurement(measurementID, quantity, unit) VALUES(12, 0.50, "tsp");INSERT INTO Measurement(measurementID, quantity, unit) VALUES(13, 0.75, "tsp");INSERT INTO Measurement(measurementID, quantity, unit) VALUES(14, 1.00, "tsp");INSERT INTO Measurement(measurementID, quantity, unit) VALUES(15, 1.50, "tsp");INSERT INTO Measurement(measurementID, quantity, unit) VALUES(16, 2.00, "tsp");INSERT INTO Measurement(measurementID, quantity, unit) VALUES(17, 2.25, "tsp");INSERT INTO Measurement(measurementID, quantity, unit) VALUES(18, 4.00, "tsp");INSERT INTO Measurement(measurementID, quantity, unit) VALUES(19, 6.00, "tsp");INSERT INTO Measurement(measurementID, quantity, unit) VALUES(20, 8.00, "tsp");INSERT INTO Measurement(measurementID, quantity, unit) VALUES(21, 0.25, "cups");INSERT INTO Measurement(measurementID, quantity, unit) VALUES(22, 0.50, "cups");INSERT INTO Measurement(measurementID, quantity, unit) VALUES(23, 0.75, "cups");INSERT INTO Measurement(measurementID, quantity, unit) VALUES(24, 1.00, "cups");INSERT INTO Measurement(measurementID, quantity, unit) VALUES(25, 1.50, "cups");INSERT INTO Measurement(measurementID, quantity, unit) VALUES(26, 2.00, "cups");INSERT INTO Measurement(measurementID, quantity, unit) VALUES(27, 2.25, "cups");INSERT INTO Measurement(measurementID, quantity, unit) VALUES(28, 4.00, "cups");INSERT INTO Measurement(measurementID, quantity, unit) VALUES(29, 6.00, "cups");INSERT INTO Measurement(measurementID, quantity, unit) VALUES(30, 8.00, "cups");INSERT INTO Measurement(measurementID, quantity, unit) VALUES(31, 0.25, "pds");INSERT INTO Measurement(measurementID, quantity, unit) VALUES(32, 0.50, "pds");INSERT INTO Measurement(measurementID, quantity, unit) VALUES(33, 0.75, "pds");INSERT INTO Measurement(measurementID, quantity, unit) VALUES(34, 1.00, "pds");INSERT INTO Measurement(measurementID, quantity, unit) VALUES(35, 1.50, "pds");INSERT INTO Measurement(measurementID, quantity, unit) VALUES(36, 2.00, "pds");INSERT INTO Measurement(measurementID, quantity, unit) VALUES(37, 2.25, "pds");INSERT INTO Measurement(measurementID, quantity, unit) VALUES(38, 4.00, "pds");INSERT INTO Measurement(measurementID, quantity, unit) VALUES(39, 6.00, "pds");INSERT INTO Measurement(measurementID, quantity, unit) VALUES(40, 8.00, "pds");INSERT INTO Measurement(measurementID, quantity, unit) VALUES(41, 0.25, "oz");INSERT INTO Measurement(measurementID, quantity, unit) VALUES(42, 0.50, "oz");INSERT INTO Measurement(measurementID, quantity, unit) VALUES(43, 0.75, "oz");INSERT INTO Measurement(measurementID, quantity, unit) VALUES(44, 1.00, "oz");INSERT INTO Measurement(measurementID, quantity, unit) VALUES(45, 1.50, "oz");INSERT INTO Measurement(measurementID, quantity, unit) VALUES(46, 2.00, "oz");INSERT INTO Measurement(measurementID, quantity, unit) VALUES(47, 2.25, "oz");INSERT INTO Measurement(measurementID, quantity, unit) VALUES(48, 4.00, "oz");INSERT INTO Measurement(measurementID, quantity, unit) VALUES(49, 6.00, "oz");INSERT INTO Measurement(measurementID, quantity, unit) VALUES(50, 8.00, "oz");INSERT INTO Measurement(measurementID, quantity, unit) VALUES(51, 0.25, "whole");INSERT INTO Measurement(measurementID, quantity, unit) VALUES(52, 0.50, "whole");INSERT INTO Measurement(measurementID, quantity, unit) VALUES(53, 0.75, "whole");INSERT INTO Measurement(measurementID, quantity, unit) VALUES(54, 1.00, "whole");INSERT INTO Measurement(measurementID, quantity, unit) VALUES(55, 1.50, "whole");INSERT INTO Measurement(measurementID, quantity, unit) VALUES(56, 2.00, "whole");INSERT INTO Measurement(measurementID, quantity, unit) VALUES(57, 2.25, "whole");INSERT INTO Measurement(measurementID, quantity, unit) VALUES(58, 4.00, "whole");INSERT INTO Measurement(measurementID, quantity, unit) VALUES(59, 6.00, "whole");INSERT INTO Measurement(measurementID, quantity, unit) VALUES(60, 8.00, "whole");/*======================================INSERTING Ingredients======================================*/INSERT INTO Ingredient(ingredientID, ingredientName) VALUES(1, "Molasses");INSERT INTO Ingredient(ingredientID, ingredientName) VALUES(2, "Almond");INSERT INTO Ingredient(ingredientID, ingredientName) VALUES(3, "Pecans");INSERT INTO Ingredient(ingredientID, ingredientName) VALUES(4, "Plum Tomato");INSERT INTO Ingredient(ingredientID, ingredientName) VALUES(5, "Cashew Nut");INSERT INTO Ingredient(ingredientID, ingredientName) VALUES(6, "Apple");INSERT INTO Ingredient(ingredientID, ingredientName) VALUES(7, "Legume");INSERT INTO Ingredient(ingredientID, ingredientName) VALUES(8, "Curry Paste");INSERT INTO Ingredient(ingredientID, ingredientName) VALUES(9, "Barbecue Sauce");INSERT INTO Ingredient(ingredientID, ingredientName) VALUES(10, "Chilli Flake");INSERT INTO Ingredient(ingredientID, ingredientName) VALUES(11, "Lemon");INSERT INTO Ingredient(ingredientID, ingredientName) VALUES(12, "Endive");INSERT INTO Ingredient(ingredientID, ingredientName) VALUES(13, "Kale");INSERT INTO Ingredient(ingredientID, ingredientName) VALUES(14, "Torte");INSERT INTO Ingredient(ingredientID, ingredientName) VALUES(15, "Salt");INSERT INTO Ingredient(ingredientID, ingredientName) VALUES(16, "Cashew");INSERT INTO Ingredient(ingredientID, ingredientName) VALUES(17, "Honeydew Melon");INSERT INTO Ingredient(ingredientID, ingredientName) VALUES(18, "Rice Paper");INSERT INTO Ingredient(ingredientID, ingredientName) VALUES(19, "Pea");INSERT INTO Ingredient(ingredientID, ingredientName) VALUES(20, "Saffron");INSERT INTO Ingredient(ingredientID, ingredientName) VALUES(21, "Berry");INSERT INTO Ingredient(ingredientID, ingredientName) VALUES(22, "Soy Ice Cream");INSERT INTO Ingredient(ingredientID, ingredientName) VALUES(23, "Rice");INSERT INTO Ingredient(ingredientID, ingredientName) VALUES(24, "Brussels Sprout");INSERT INTO Ingredient(ingredientID, ingredientName) VALUES(25, "Pretzel");INSERT INTO Ingredient(ingredientID, ingredientName) VALUES(26, "Guava");INSERT INTO Ingredient(ingredientID, ingredientName) VALUES(27, "Pumpernickel");INSERT INTO Ingredient(ingredientID, ingredientName) VALUES(28, "Flax Seed");INSERT INTO Ingredient(ingredientID, ingredientName) VALUES(29, "Jackfruit");INSERT INTO Ingredient(ingredientID, ingredientName) VALUES(30, "Chives");INSERT INTO Ingredient(ingredientID, ingredientName) VALUES(31, "Durian");INSERT INTO Ingredient(ingredientID, ingredientName) VALUES(32, "Raisin");INSERT INTO Ingredient(ingredientID, ingredientName) VALUES(33, "Snow Pea");INSERT INTO Ingredient(ingredientID, ingredientName) VALUES(34, "Cornflake");INSERT INTO Ingredient(ingredientID, ingredientName) VALUES(35, "Bran");INSERT INTO Ingredient(ingredientID, ingredientName) VALUES(36, "Blackberry");INSERT INTO Ingredient(ingredientID, ingredientName) VALUES(37, "Pear");INSERT INTO Ingredient(ingredientID, ingredientName) VALUES(38, "Cucumber");INSERT INTO Ingredient(ingredientID, ingredientName) VALUES(39, "Cornstarch");INSERT INTO Ingredient(ingredientID, ingredientName) VALUES(40, "Jalapeno");INSERT INTO Ingredient(ingredientID, ingredientName) VALUES(41, "Chicken");INSERT INTO Ingredient(ingredientID, ingredientName) VALUES(42, "Pork");/*======================================INSERTING 250,000 USERS======================================*/INSERT INTO User(fname,lname,username, user_password) VALUES("David", "Mcconnell", "zwiley", "P76NUyT1OH");INSERT INTO User(fname,lname,username, user_password) VALUES("Erika", "Rodriguez", "stephensfred", "W0HgracDZz");INSERT INTO User(fname,lname,username, user_password) VALUES("Clinton", "Obrien", "ethomas", "fG6XKoXS51");INSERT INTO User(fname,lname,username, user_password) VALUES("Travis", "Underwood", "diana48", "1ZRHBlkQLZ");INSERT INTO User(fname,lname,username, user_password) VALUES("Arthur", "Massey", "freemanjames", "1ODWNdvc4B");INSERT INTO User(fname,lname,username, user_password) VALUES("Eric", "Miller", "sanchezmichele", "TOkxH5Pp0z");INSERT INTO User(fname,lname,username, user_password) VALUES("Jonathan", "Nelson", "colemichelle", "6Q2pKTWeVn");INSERT INTO User(fname,lname,username, user_password) VALUES("Michael", "Cruz", "robinmendez", "W8SXi8lwgz");INSERT INTO User(fname,lname,username, user_password) VALUES("Kellie", "Cooper", "jacquelineorr", "9iJW9PxgT4");INSERT INTO User(fname,lname,username, user_password) VALUES("Kimberly", "Barrett", "cooperrobert", "2zT8AzUd0s");INSERT INTO User(fname,lname,username, user_password) VALUES("William", "Flowers", "wongjames", "5Or1HwRiXK");INSERT INTO User(fname,lname,username, user_password) VALUES("James", "Greene", "jefferyowens", "7PvlLrqKTl");INSERT INTO User(fname,lname,username, user_password) VALUES("Tom", "Williams", "scott63", "DB4CLWEj6p");INSERT INTO User(fname,lname,username, user_password) VALUES("Geoffrey", "Campbell", "bonnieowen", "wmBe33Eq33");INSERT INTO User(fname,lname,username, user_password) VALUES("Jared", "Martinez", "ortegakaren", "ezJv2SoUix");INSERT INTO User(fname,lname,username, user_password) VALUES("Patricia", "Smith", "svalencia", "321ScQksrB");INSERT INTO User(fname,lname,username, user_password) VALUES("Christopher", "Williams", "michaelnelson", "hRw6eSVkMe");INSERT INTO User(fname,lname,username, user_password) VALUES("Rhonda", "Myers", "mayerjoshua", "nslfqHeb8E");INSERT INTO User(fname,lname,username, user_password) VALUES("Desiree", "Davis", "davissarah", "hR5EmlEsmn");INSERT INTO User(fname,lname,username, user_password) VALUES("Ashley", "Stanley", "cwells", "YW8QS8tvq5");/*======================================INSERTING 600,000 Recipes and Connections======================================*/INSERT INTO Recipe(recipeID, creationDate, recipeName, preparationTime, inputServing, imageUpload, calorieCount) VALUES(1, "2021-03-07", "Baked Grated Pear Tart", 134, 5, "https://placekitten.com/349/530", 375);INSERT INTO Recipe(recipeID, creationDate, recipeName, preparationTime, inputServing, imageUpload, calorieCount) VALUES(2, "2021-03-22", "Sour Chunky Legume Pudding", 11, 9, "https://placeimg.com/959/342/any", 817);INSERT INTO Recipe(recipeID, creationDate, recipeName, preparationTime, inputServing, imageUpload, calorieCount) VALUES(3, "2021-04-01", "Barbequed Sour Rice Paper Tart", 111, 9, "https://dummyimage.com/319x336", 942);INSERT INTO Recipe(recipeID, creationDate, recipeName, preparationTime, inputServing, imageUpload, calorieCount) VALUES(4, "2021-03-21", "Carved Baked Chilli Flake Tart", 273, 10, "https://www.lorempixel.com/601/156", 344);INSERT INTO Recipe(recipeID, creationDate, recipeName, preparationTime, inputServing, imageUpload, calorieCount) VALUES(5, "2021-03-12", "Whisked Candied Honeydew Melon Casserole", 220, 8, "https://www.lorempixel.com/492/323", 917);INSERT INTO Recipe(recipeID, creationDate, recipeName, preparationTime, inputServing, imageUpload, calorieCount) VALUES(6, "2021-03-17", "Stirred Greased Barbecue Sauce Soup", 206, 6, "https://placekitten.com/125/994", 615);INSERT INTO Recipe(recipeID, creationDate, recipeName, preparationTime, inputServing, imageUpload, calorieCount) VALUES(7, "2021-03-31", "Grilled Creamed Jalapeno Tart", 5, 10, "https://placeimg.com/402/713/any", 607);INSERT INTO Recipe(recipeID, creationDate, recipeName, preparationTime, inputServing, imageUpload, calorieCount) VALUES(8, "2021-03-16", "Melted Grilled Rice Chips", 160, 10, "https://placekitten.com/363/201", 542);INSERT INTO Recipe(recipeID, creationDate, recipeName, preparationTime, inputServing, imageUpload, calorieCount) VALUES(9, "2021-03-26", "Barbequed Sprinkled Raisin Juice", 80, 6, "https://placeimg.com/492/704/any", 575);INSERT INTO Recipe(recipeID, creationDate, recipeName, preparationTime, inputServing, imageUpload, calorieCount) VALUES(10, "2021-03-30", "Chopped Creamed Cashew Nut", 292, 5, "https://www.lorempixel.com/12/353", 334);/*======================================INSERTING Relationship: contains======================================*/INSERT INTO contains(recipeID, ingredientID, measurementID) VALUES(1, 37, 6);INSERT INTO contains(recipeID, ingredientID, measurementID) VALUES(1, 2, 57);INSERT INTO contains(recipeID, ingredientID, measurementID) VALUES(1, 1, 50);INSERT INTO contains(recipeID, ingredientID, measurementID) VALUES(2, 7, 17);INSERT INTO contains(recipeID, ingredientID, measurementID) VALUES(2, 34, 15);INSERT INTO contains(recipeID, ingredientID, measurementID) VALUES(3, 18, 9);INSERT INTO contains(recipeID, ingredientID, measurementID) VALUES(3, 33, 38);INSERT INTO contains(recipeID, ingredientID, measurementID) VALUES(4, 10, 23);INSERT INTO contains(recipeID, ingredientID, measurementID) VALUES(4, 19, 13);INSERT INTO contains(recipeID, ingredientID, measurementID) VALUES(5, 17, 40);INSERT INTO contains(recipeID, ingredientID, measurementID) VALUES(5, 15, 28);INSERT INTO contains(recipeID, ingredientID, measurementID) VALUES(5, 11, 49);INSERT INTO contains(recipeID, ingredientID, measurementID) VALUES(5, 2, 31);INSERT INTO contains(recipeID, ingredientID, measurementID) VALUES(6, 9, 53);INSERT INTO contains(recipeID, ingredientID, measurementID) VALUES(6, 24, 58);INSERT INTO contains(recipeID, ingredientID, measurementID) VALUES(6, 15, 30);INSERT INTO contains(recipeID, ingredientID, measurementID) VALUES(7, 40, 22);INSERT INTO contains(recipeID, ingredientID, measurementID) VALUES(7, 36, 1);INSERT INTO contains(recipeID, ingredientID, measurementID) VALUES(8, 23, 56);INSERT INTO contains(recipeID, ingredientID, measurementID) VALUES(8, 24, 31);INSERT INTO contains(recipeID, ingredientID, measurementID) VALUES(9, 32, 60);INSERT INTO contains(recipeID, ingredientID, measurementID) VALUES(9, 42, 17);INSERT INTO contains(recipeID, ingredientID, measurementID) VALUES(9, 1, 51);INSERT INTO contains(recipeID, ingredientID, measurementID) VALUES(9, 17, 4);INSERT INTO contains(recipeID, ingredientID, measurementID) VALUES(10, 5, 19);INSERT INTO contains(recipeID, ingredientID, measurementID) VALUES(10, 9, 1);/*======================================INSERTING Instructions======================================*/INSERT INTO Instruction(recipeID, stepNumber, direction) VALUES(1, 1, "Decide expert participant couple popular their.");INSERT INTO Instruction(recipeID, stepNumber, direction) VALUES(2, 1, "What send usually free case place soldier.");INSERT INTO Instruction(recipeID, stepNumber, direction) VALUES(3, 1, "Social character central political.");INSERT INTO Instruction(recipeID, stepNumber, direction) VALUES(3, 2, "Report end region test recently whom half. Card before one good season.");INSERT INTO Instruction(recipeID, stepNumber, direction) VALUES(4, 1, "Something serious easy natural affect world throw.");INSERT INTO Instruction(recipeID, stepNumber, direction) VALUES(4, 2, "Dog card actually big baby relate drop purpose. Pattern expert sing Democrat where general.");INSERT INTO Instruction(recipeID, stepNumber, direction) VALUES(5, 1, "Describe occur bed about.");INSERT INTO Instruction(recipeID, stepNumber, direction) VALUES(5, 2, "Star street sign imagine pick sell hundred worker. Community anything just face gas able history.");INSERT INTO Instruction(recipeID, stepNumber, direction) VALUES(5, 3, "Thought rock audience what.");INSERT INTO Instruction(recipeID, stepNumber, direction) VALUES(6, 1, "Couple guy imagine offer miss.");INSERT INTO Instruction(recipeID, stepNumber, direction) VALUES(6, 2, "Seek hold break if.");INSERT INTO Instruction(recipeID, stepNumber, direction) VALUES(6, 3, "Stuff future election across scene.");INSERT INTO Instruction(recipeID, stepNumber, direction) VALUES(7, 1, "Result number civil listen government main learn. Meeting control challenge until oil machine.");INSERT INTO Instruction(recipeID, stepNumber, direction) VALUES(7, 2, "Case miss far believe work act letter. Political card couple development local community.");INSERT INTO Instruction(recipeID, stepNumber, direction) VALUES(7, 3, "Marriage enter region poor positive small. Trip imagine standard explain there TV.");INSERT INTO Instruction(recipeID, stepNumber, direction) VALUES(8, 1, "Than military reduce great produce. Physical skin call.");INSERT INTO Instruction(recipeID, stepNumber, direction) VALUES(9, 1, "Happen personal popular role whose. Happy itself determine raise north beautiful person.");INSERT INTO Instruction(recipeID, stepNumber, direction) VALUES(9, 2, "Since dream suffer deal show.");INSERT INTO Instruction(recipeID, stepNumber, direction) VALUES(9, 3, "Pretty test cover happy international maybe point.");INSERT INTO Instruction(recipeID, stepNumber, direction) VALUES(10, 1, "Move fund audience field within. Use have leave might particular not third fund.");INSERT INTO Instruction(recipeID, stepNumber, direction) VALUES(10, 2, "Himself pull free whom character both audience describe.");/*======================================INSERTING Relationship: adds======================================*/INSERT INTO adds(recipeID, userID) VALUES(1, 8);INSERT INTO adds(recipeID, userID) VALUES(2, 8);INSERT INTO adds(recipeID, userID) VALUES(3, 18);INSERT INTO adds(recipeID, userID) VALUES(4, 19);INSERT INTO adds(recipeID, userID) VALUES(5, 12);INSERT INTO adds(recipeID, userID) VALUES(6, 3);INSERT INTO adds(recipeID, userID) VALUES(7, 7);INSERT INTO adds(recipeID, userID) VALUES(8, 16);INSERT INTO adds(recipeID, userID) VALUES(9, 4);INSERT INTO adds(recipeID, userID) VALUES(10, 19);/*======================================INSERTING Relationship: kitchen======================================*/INSERT INTO kitchen(ingredientID, userID) VALUES(33, 1);INSERT INTO kitchen(ingredientID, userID) VALUES(31, 1);INSERT INTO kitchen(ingredientID, userID) VALUES(31, 2);INSERT INTO kitchen(ingredientID, userID) VALUES(41, 2);INSERT INTO kitchen(ingredientID, userID) VALUES(25, 2);INSERT INTO kitchen(ingredientID, userID) VALUES(8, 3);INSERT INTO kitchen(ingredientID, userID) VALUES(7, 3);INSERT INTO kitchen(ingredientID, userID) VALUES(12, 3);INSERT INTO kitchen(ingredientID, userID) VALUES(13, 3);INSERT INTO kitchen(ingredientID, userID) VALUES(14, 4);INSERT INTO kitchen(ingredientID, userID) VALUES(22, 4);INSERT INTO kitchen(ingredientID, userID) VALUES(6, 5);INSERT INTO kitchen(ingredientID, userID) VALUES(12, 5);INSERT INTO kitchen(ingredientID, userID) VALUES(21, 6);INSERT INTO kitchen(ingredientID, userID) VALUES(24, 6);INSERT INTO kitchen(ingredientID, userID) VALUES(20, 6);INSERT INTO kitchen(ingredientID, userID) VALUES(9, 6);INSERT INTO kitchen(ingredientID, userID) VALUES(17, 7);INSERT INTO kitchen(ingredientID, userID) VALUES(22, 7);INSERT INTO kitchen(ingredientID, userID) VALUES(21, 8);INSERT INTO kitchen(ingredientID, userID) VALUES(24, 8);INSERT INTO kitchen(ingredientID, userID) VALUES(37, 8);INSERT INTO kitchen(ingredientID, userID) VALUES(30, 9);INSERT INTO kitchen(ingredientID, userID) VALUES(2, 9);INSERT INTO kitchen(ingredientID, userID) VALUES(3, 9);INSERT INTO kitchen(ingredientID, userID) VALUES(16, 10);INSERT INTO kitchen(ingredientID, userID) VALUES(18, 10);INSERT INTO kitchen(ingredientID, userID) VALUES(32, 10);INSERT INTO kitchen(ingredientID, userID) VALUES(19, 10);INSERT INTO kitchen(ingredientID, userID) VALUES(1, 11);INSERT INTO kitchen(ingredientID, userID) VALUES(20, 11);INSERT INTO kitchen(ingredientID, userID) VALUES(29, 11);INSERT INTO kitchen(ingredientID, userID) VALUES(13, 11);INSERT INTO kitchen(ingredientID, userID) VALUES(25, 12);INSERT INTO kitchen(ingredientID, userID) VALUES(6, 12);INSERT INTO kitchen(ingredientID, userID) VALUES(30, 12);INSERT INTO kitchen(ingredientID, userID) VALUES(16, 12);INSERT INTO kitchen(ingredientID, userID) VALUES(7, 13);INSERT INTO kitchen(ingredientID, userID) VALUES(9, 13);INSERT INTO kitchen(ingredientID, userID) VALUES(41, 14);INSERT INTO kitchen(ingredientID, userID) VALUES(8, 14);INSERT INTO kitchen(ingredientID, userID) VALUES(1, 14);INSERT INTO kitchen(ingredientID, userID) VALUES(42, 14);INSERT INTO kitchen(ingredientID, userID) VALUES(10, 15);INSERT INTO kitchen(ingredientID, userID) VALUES(14, 15);INSERT INTO kitchen(ingredientID, userID) VALUES(29, 16);INSERT INTO kitchen(ingredientID, userID) VALUES(18, 16);INSERT INTO kitchen(ingredientID, userID) VALUES(22, 16);INSERT INTO kitchen(ingredientID, userID) VALUES(6, 16);INSERT INTO kitchen(ingredientID, userID) VALUES(29, 17);INSERT INTO kitchen(ingredientID, userID) VALUES(22, 18);INSERT INTO kitchen(ingredientID, userID) VALUES(28, 18);INSERT INTO kitchen(ingredientID, userID) VALUES(29, 18);INSERT INTO kitchen(ingredientID, userID) VALUES(32, 18);INSERT INTO kitchen(ingredientID, userID) VALUES(10, 19);INSERT INTO kitchen(ingredientID, userID) VALUES(34, 19);INSERT INTO kitchen(ingredientID, userID) VALUES(27, 19);INSERT INTO kitchen(ingredientID, userID) VALUES(27, 20);
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
