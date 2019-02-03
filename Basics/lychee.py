# This file will contain code snippets on 
# python dictionaries

# Dictionaries ane NOT ordered, they are unordered.
# Items added to dictionaries don't get stored in the order 
# in which they are added.

# Creating a dictionary 

fruit_dessert = {
    "watermelon" : "watermelon mochi",
    "banana" : "banana ice-cream sundae",
    "lychee" : "lychee ice cream",
    "lemon" : "lemonade"
}

# Accessing values from a dictionary

print('watermelon dessert :' + fruit_dessert["watermelon"])

# Populating dictionaries

fruit_dessert["mango"] = "mango ice-cream sundae"

# Creating an empty dictionary

fruit_dessert_popularity = {}

fruit_dessert_popularity["watermelon mochi"] = "super popular"
fruit_dessert_popularity["lemonade"] = "okayish popular"
fruit_dessert_popularity["lychee ice cream"] = "super popular"

# Accessing values of a dictionary from another dictionary

print("Popularity of "+fruit_dessert["watermelon"]+" : "+fruit_dessert_popularity[fruit_dessert["watermelon"]])

# Modifying previously stored values

fruit_dessert["lemon"] = "lemon maringue pie"

# Only IMMUTABLE values can be used as keys in dictionaries, if mutable values are used in dictionaries, python will raise an error

god_level_fruits = ("watermelon", "lychee", "apple", "mango", "grapes")
hellish_fruits = ("banana", "dragon fruit", "sapote")

fruity_stuff = {
    god_level_fruits : "fruity awesomeness",
    hellish_fruits : "why don't you taste good?!"
}

# Dictionaries as values
# Dictionaries can be stored as values. 

awesome_menu = {
    "fruit_desserts" : fruit_dessert,
    "popularity" : fruit_dessert_popularity
}