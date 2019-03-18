# This code snippet contains some examples on the python language

# element of operator
fruits = ["watermelon", "mango", "lychee", "mango", "cherry"]

for fruit in fruits:
    print(fruit)

print("Is dragon-fruit present in our fruit basket? " + str("dragon-fruit" in fruits))

# Slicing 

watermelon = "Watermelon is an awesome fruit!"

print(watermelon[::2])

# Concatenation of sequences 

desserts = ["Icecream", "Jalebi", "Waffle"]
heaven = fruits + desserts
print(heaven)

heart = "watermelon"
red_heart = "heart"

red_watermelon = heart + red_heart
print(red_watermelon)

# Accessing nested lists 

fruit_list = [["watermelon", "mango", "pine-apple"]]

print(fruit_list[0][1])

# More on lists 
# List operations (append, pop)

print("My awesome list")

awesome_list = []
awesome_list.append("watermelon")
awesome_list.append("watermelon")
awesome_list.append("lychee")
awesome_list.append("lime")
awesome_list.append("mango")
print(awesome_list)

fruit = awesome_list.pop()
print(awesome_list)

# alternative to peek function
print(awesome_list[-1])

# append vs extend in lists
# 
# Both of them produce different results

print()

awesome_fruits = ['watermelon', 'guava', 'kiwi', 'mango', 'lychee', "watermelon", "banana", "kiwi"]
good_fruits = ['dragon-fruit', 'sapote', 'tamarind']

# append will create a sub-list
awesome_fruits.append(good_fruits)

# extend keyword will add the element
good_fruits.extend(awesome_fruits)

print(awesome_fruits)
print(good_fruits)

# Index of an element in a list
print(awesome_fruits.index("watermelon", 1, len(awesome_fruits)))

# Shallow and Deep copying of lists in Python

print("Shallow and Deep copying")

vegetables = ["tomato", "chilli", "potato", "cauliflower"]
awful_stuff = vegetables

print(id(vegetables), id(awful_stuff))
print(vegetables, awful_stuff)

awful_stuff[3] = "Aubergine"

print(id(vegetables), id(awful_stuff))
print(vegetables, awful_stuff)

some_other_awful_stuff = vegetables[:]  
some_other_awful_stuff[2] = "Carolina Reaper"

print(id(vegetables), id(some_other_awful_stuff))
print(vegetables, some_other_awful_stuff)  