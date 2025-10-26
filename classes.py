
"""Class
- A blueprint or template that defines properties/attributes and behaviors/methods
- Describes how something should look and function
- Doesn't create anything by itself - just provides the structure
- Like a recipe for a cake
Class definition: You created a class called Cake, which acts as a template for creating cakes.
Class variables: recipe_type, baking_temperature, baking_time —
these variables are the common standards required for all cake objects.
Constructor (__init__ method): This method initializes new Cake objects;
it sets up each cake with specific amounts of flour, sugar, milk, and eggs, which are passed as parameters when a new cake object is created. self refers to the specific instance calling the method.
self.cake_flour = flour: The amount of flour provided as an argument (flour) when creating a new cake object to the cake_flour attribute of that specific cake object. Each cake can have a different amount of flour based on what is passed at creation.
Methods: mix_ingredients(), bake(), serve() are the methods for cake preparation.
The methods utilize the self as a parameter for accessing the ingredients of the cake. Just like the variables, these methods are also all available for every cake object created from this class.
Flexibility in recipes: Each cake object may contain varying amounts of ingredients, demonstrating the Cake class's adaptability to different recipes.
"""


class Cake:
    recipe_type = "Basic Cake"
    baking_temperature = 180
    baking_time = 30


# To change the variable values at any time use this syntax: ClassName.variable_name.
# In our case, Cake.baking_time
"""
print(Cake.baking_time)/

Cake.baking_time = 25 # changes the baking time
print(Cake.baking_time)/
"""


# Constructor for Initializing Cake objects. it's used to build an object with different
# parameters. To call __init__, you need the def keyword, as seen below:
# self arguement allows you to refer to an object and assign it unique values
def __init__(self, flour, sugar, milk, eggs):
        self.cake_flour = flour
        self.cake_sugar = sugar
        self.cake_milk = milk
        self.cake_eggs = eggs


#Method Creation
def mix_ingredients(self):
    # Prints a message with the amounts of each ingredient
        print(f"Mixing {self.cake_flour} grams of flour, {self.cake_sugar} grams of sugar, {self.cake_milk} ml of milk, and {self.cake_eggs} eggs.")


def bake(self):
    # Uses the class variables for temperature and time to print the baking details
        print(f"Baking the cake at {self.baking_temperature}°C for {self.baking_time} minutes.")


def serve(self):
    # Prints a message indicating the cake is being served
        print("Serving the cake with decoration.")

#Class within a Class using objects from Parent Class1 into Parent Class 2
class Bakery:
    def __init__(self, name):
        self.bakery_name = name

    def prepare_cake(self, cake):
        print(f"Preparing a cake at {self.bakery_name}.")
        cake.mix_ingredients()
        cake.bake()
        cake.serve()

# Create an instance of a Bakery named 'TripleTen Bakery'
bakery_1 = Bakery("TripleTen Bakery")

# Use the Bakery instance to prepare the cake_1
bakery_1.prepare_cake(cake_1)

# Create an object cake_1 : flour, sugar, milk, eggs in order
cake_1 = Cake(200, 200, 240, 2)
cake_2 = Cake( 200, 150, 220, 2)
cake_3 = Cake( 170, 170, 200, 2)
# Call the methods for this object/ creating instances
cake_1.mix_ingredients()  # Output: Mixing 200 grams of flour, 200 grams of sugar, 240 ml of milk, and 2 eggs.
cake_1.bake()  # Output: Baking the cake at 180°C for 30 minutes.
cake_1.serve()  # Output: Serving the cake with decoration.

"""
# Object parameter verification using print() function and dot notation
print(cake_1.cake_flour)  # Output: 200 -> It means cake_1 uses 200g of flour.
print(cake_2.baking_time)  # Output: 30  -> It means cake_2 baking time is 30 minutes.
print(cake_3.recipe_type)
"""
"""
class Car:
    color = "red"
    registration = 123456
    roof_up = True
"""
