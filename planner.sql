DROP TABLE IF EXISTS planner;CREATE DATABASE planner;USE planner;
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
/*======================================INSERTING 250,000 USERS======================================*/INSERT INTO User(fname,lname,password) VALUES("Amanda", "Peterson", "pbkdf2:sha256:150000$yaZTT88c$a53ae521c7dec56aec2f8cb3d75b6f263f5c911ca5247c837a5b7511650e11a4");INSERT INTO User(fname,lname,password) VALUES("Jermaine", "Anderson", "pbkdf2:sha256:150000$2CTKMQsm$565f205ed3251e3ade7adce451af15b665759515461643ed2b189a0184d06037");INSERT INTO User(fname,lname,password) VALUES("Jill", "Price", "pbkdf2:sha256:150000$f0JRcMm6$f9a6c1a26eb3906a35dcc15891191d60ae5ca8f5aa861dde3606c38498d5d02d");