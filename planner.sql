DROP TABLE IF EXISTS planner;
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
