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