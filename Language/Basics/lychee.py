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

# Operations on Dictionary

# Deleting a key 

del fruit_dessert['lemon']
print('After deleting lemon : '+str(fruit_dessert))

# Length of a dictionary 

print('The length of the fruit dictionary is '+str(len(fruit_dessert)))

# To check the existance of a key 

print('Is watermelon present in the fruit dessert dictionary - '+str('watermelon' in fruit_dessert))

# To check the absence of a key in a dictionary 

print('Is dragon fruit present in the dictionary ' + str('dragon fruit' not in fruit_dessert))

# pop() and popitem() of dictionary 

print(fruit_dessert.pop('banana'))
print(fruit_dessert.pop('dragon fruit', 'mango'))

print(fruit_dessert.popitem())

# copying a dictionary using the copy() method

fruit_dessert_copy = fruit_dessert.copy()

# merging dictionaries with update()

fruity_stuff.update(awesome_menu)

# 
# iterating over a dictionary
#

# iterating over the keys of a dictionary

for menu_item in awesome_menu:
    print(menu_item)
print()

# iterating over values of a dictionary

for menu_value in awesome_menu.values():
    print(menu_value)
print()

# 
# list and dictionary conversions
#

# list to dictionary conversion 

print('List to dictionary converion - ')
new_dictionary = dict(zip(awesome_menu, fruit_dessert))
print(new_dictionary)

# dictionary to list conversion
print('Dictionary to list conversion - ')
new_list = new_dictionary.items()
print(new_list)

new_list = new_dictionary.values()
print(new_list)

new_list = new_dictionary.keys()
print(new_list)

